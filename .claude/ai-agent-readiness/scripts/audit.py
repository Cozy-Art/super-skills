#!/usr/bin/env python3
"""
AI agent readiness audit.

Checks three layers:
  Gate  - can an agent get the bytes (robots.txt policy, per-bot reachability, CDN gates)
  Map   - can it navigate (llms.txt, markdown mirrors, link relations, sitemap)
  Meal  - is anything extractable (SSR content, JSON-LD, headings, tables, dates)

Usage:
    python3 audit.py --url https://example.com
    python3 audit.py --repo /path/to/project
    python3 audit.py --url https://example.com --repo . --json

Standard library only. No install step.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

TIMEOUT = 15
UA = "ai-agent-readiness-audit/1.0 (+site-owner self-audit)"

# Bots whose blocking removes the site from AI answers.
RETRIEVAL_BOTS = [
    "OAI-SearchBot",
    "Claude-SearchBot",
    "PerplexityBot",
    "Googlebot",
    "bingbot",
    "Applebot",
]
# Bots that feed model training. Blocking these is a legitimate choice.
TRAINING_BOTS = [
    "GPTBot",
    "ClaudeBot",
    "CCBot",
    "Google-Extended",
    "Applebot-Extended",
    "Bytespider",
    "Meta-ExternalAgent",
    "Amazonbot",
]
# User-triggered fetchers. Generally ignore robots.txt by design.
USER_BOTS = ["ChatGPT-User", "Claude-User", "Perplexity-User", "Meta-ExternalFetcher"]

# Bots actually probed over the network (kept small to stay polite).
PROBE_BOTS = ["OAI-SearchBot", "Claude-SearchBot", "PerplexityBot", "GPTBot"]


# --------------------------------------------------------------------------
# tiny helpers
# --------------------------------------------------------------------------

def fetch(url: str, ua: str = UA, method: str = "GET"):
    """Return (status, headers_dict, body_text). Never raises."""
    req = urllib.request.Request(url, headers={"User-Agent": ua}, method=method)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            raw = resp.read(2_000_000) if method == "GET" else b""
            charset = resp.headers.get_content_charset() or "utf-8"
            return resp.status, dict(resp.headers), raw.decode(charset, "replace")
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers or {}), ""
    except Exception as e:  # noqa: BLE001 - network conditions are the point
        return None, {"_error": str(e)}, ""


class Extract(HTMLParser):
    """Pull the few HTML facts the audit needs."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.jsonld: list[str] = []
        self.md_links: list[str] = []
        self.describedby: list[str] = []
        self.headings = 0
        self.tables = 0
        self.time_tags = 0
        self.text_len = 0
        self._in_ld = False
        self._in_skip = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "script" and a.get("type") == "application/ld+json":
            self._in_ld = True
            self.jsonld.append("")
        elif tag in ("script", "style"):
            self._in_skip += 1
        elif tag == "link":
            rel = (a.get("rel") or "").lower()
            if "alternate" in rel and "markdown" in (a.get("type") or "").lower():
                self.md_links.append(a.get("href", ""))
            if "describedby" in rel:
                self.describedby.append(a.get("href", ""))
        elif tag in ("h1", "h2", "h3"):
            self.headings += 1
        elif tag == "table":
            self.tables += 1
        elif tag == "time":
            self.time_tags += 1

    def handle_endtag(self, tag):
        if tag == "script" and self._in_ld:
            self._in_ld = False
        elif tag in ("script", "style") and self._in_skip:
            self._in_skip -= 1

    def handle_data(self, data):
        if self._in_ld:
            self.jsonld[-1] += data
        elif not self._in_skip:
            self.text_len += len(data.strip())


def parse_robots(text: str) -> dict[str, dict]:
    """Map lowercased user-agent -> {'allow': [...], 'disallow': [...]}.

    Handles stacked User-agent lines, which is how AI policies are usually written.
    """
    groups: dict[str, dict] = {}
    pending: list[str] = []
    started = False
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line or ":" not in line:
            continue
        field, _, value = line.partition(":")
        field, value = field.strip().lower(), value.strip()
        if field == "user-agent":
            if started:
                pending, started = [], False
            pending.append(value.lower())
            groups.setdefault(value.lower(), {"allow": [], "disallow": [], "other": []})
        elif field in ("allow", "disallow") and pending:
            started = True
            for ua in pending:
                groups[ua][field].append(value)
        elif pending:
            for ua in pending:
                groups[ua]["other"].append(f"{field}: {value}")
    return groups


def verdict_for(bot: str, groups: dict[str, dict]) -> str:
    g = groups.get(bot.lower())
    if g is None:
        g = groups.get("*")
        if g is None:
            return "no rule (allowed by default)"
        prefix = "via * : "
    else:
        prefix = ""
    if any(d == "/" for d in g["disallow"]):
        return prefix + "BLOCKED"
    if g["disallow"]:
        return prefix + f"allowed except {len(g['disallow'])} path(s)"
    return prefix + "allowed"


def validate_llms_txt(text: str) -> list[str]:
    """Return spec violations, per llmstxt.org v2 ordering rules."""
    problems = []
    lines = [ln.rstrip() for ln in text.splitlines()]
    body = [ln for ln in lines if ln.strip()]
    if not body:
        return ["file is empty"]
    if not body[0].startswith("# "):
        problems.append("must open with an H1 (the only required section)")
    if not any(ln.startswith(">") for ln in body[:6]):
        problems.append("no blockquote summary near the top (recommended)")
    # After the first H2, only list items / blank lines / further H2s are in-spec.
    seen_h2 = False
    for ln in lines:
        if ln.startswith("## "):
            seen_h2 = True
            continue
        if seen_h2 and ln.strip() and not ln.lstrip().startswith(("-", "*")):
            problems.append(f"prose after first H2 breaks parsers: {ln.strip()[:60]!r}")
            break
    if seen_h2:
        links = re.findall(r"^\s*[-*]\s*\[([^\]]+)\]\(([^)]+)\)(.*)$", text, re.M)
        if not links:
            problems.append("H2 sections present but no markdown links found")
        else:
            undesc = [t for t, _u, rest in links if not rest.strip().startswith(":")]
            if len(undesc) > len(links) / 2:
                problems.append(
                    f"{len(undesc)}/{len(links)} links lack a ': description' note"
                )
            if len(links) > 60:
                problems.append(
                    f"{len(links)} links — likely auto-generated; curate for context fit"
                )
    return problems


# --------------------------------------------------------------------------
# live-site audit
# --------------------------------------------------------------------------

def audit_url(base: str) -> dict:
    if not base.startswith(("http://", "https://")):
        base = "https://" + base
    base = base.rstrip("/") + "/"
    out: dict = {"target": base, "gate": {}, "map": {}, "meal": {}, "findings": []}
    add = lambda sev, layer, msg: out["findings"].append(  # noqa: E731
        {"severity": sev, "layer": layer, "message": msg}
    )

    # ---- Gate: robots.txt --------------------------------------------------
    status, _hdrs, robots_txt = fetch(urljoin(base, "/robots.txt"))
    out["gate"]["robots_status"] = status
    if status != 200 or not robots_txt.strip():
        add("high", "gate", "No robots.txt — every crawler is allowed by default and "
                            "training vs. retrieval cannot be distinguished.")
        groups = {}
    else:
        groups = parse_robots(robots_txt)
        out["gate"]["retrieval"] = {b: verdict_for(b, groups) for b in RETRIEVAL_BOTS}
        out["gate"]["training"] = {b: verdict_for(b, groups) for b in TRAINING_BOTS}
        out["gate"]["user_triggered"] = {b: verdict_for(b, groups) for b in USER_BOTS}

        blocked = [b for b, v in out["gate"]["retrieval"].items() if "BLOCKED" in v]
        if blocked:
            add("high", "gate", "Retrieval bots blocked in robots.txt — removes the site "
                                f"from AI answers: {', '.join(blocked)}")
        named = [b for b in RETRIEVAL_BOTS + TRAINING_BOTS if b.lower() in groups]
        if not named:
            add("medium", "gate", "robots.txt names no AI user agents — training and "
                                  "retrieval are governed by the same blanket rule.")
        if any("BLOCKED" in v for v in out["gate"]["user_triggered"].values()):
            add("low", "gate", "User-triggered fetchers are blocked; these generally "
                               "ignore robots.txt, so the rule mostly has no effect.")

        cu = re.findall(r"^\s*(content-usage|content-signal)\s*:(.*)$",
                        robots_txt, re.I | re.M)
        out["gate"]["content_usage"] = [f"{k}:{v.strip()}" for k, v in cu]
        out["gate"]["crawl_delay"] = bool(re.search(r"^\s*crawl-delay", robots_txt,
                                                    re.I | re.M))
        out["gate"]["sitemap_declared"] = bool(re.search(r"^\s*sitemap\s*:", robots_txt,
                                                         re.I | re.M))
        if not out["gate"]["sitemap_declared"]:
            add("low", "gate", "robots.txt declares no Sitemap:")

    # ---- Gate: per-bot reachability (the CDN check) ------------------------
    probes = {}
    for bot in PROBE_BOTS:
        st, hdrs, _ = fetch(base, ua=bot, method="GET")
        probes[bot] = {
            "status": st,
            "server": hdrs.get("Server", ""),
            "x_robots_tag": hdrs.get("X-Robots-Tag", ""),
        }
        if st is None:
            add("high", "gate", f"{bot}: request failed ({hdrs.get('_error','')[:60]})")
        elif st in (401, 402, 403, 429, 503):
            add("high", "gate", f"{bot} receives HTTP {st} — an edge/WAF rule is "
                                "blocking it upstream of robots.txt.")
        elif st != 200:
            add("medium", "gate", f"{bot} receives HTTP {st}")
        if hdrs.get("X-Robots-Tag", "").lower().find("noindex") >= 0:
            add("high", "gate", f"X-Robots-Tag: noindex served to {bot}")
    out["gate"]["probes"] = probes
    cf = any("cloudflare" in (p["server"] or "").lower() for p in probes.values())
    out["gate"]["behind_cloudflare"] = cf
    if cf:
        add("medium", "gate", "Cloudflare detected. Bot policy is set in the dashboard "
                              "and overrides robots.txt; defaults changed 15 Sep 2026 to "
                              "block Training/Agent crawlers on ad-bearing pages.")

    # ---- Map: llms.txt -----------------------------------------------------
    st, _h, llms = fetch(urljoin(base, "/llms.txt"))
    out["map"]["llms_txt_status"] = st
    if st == 200 and llms.strip() and not llms.lstrip().startswith("<"):
        out["map"]["llms_txt_bytes"] = len(llms)
        problems = validate_llms_txt(llms)
        out["map"]["llms_txt_problems"] = problems
        for p in problems:
            add("low", "map", f"llms.txt: {p}")
    else:
        out["map"]["llms_txt_problems"] = ["absent"]
        add("low", "map", "No /llms.txt. Worth adding for coding/IDE agents and MCP "
                          "clients; not expected to affect answer-engine citations.")

    st_full, _h, _b = fetch(urljoin(base, "/llms-full.txt"), method="HEAD")
    out["map"]["llms_full_txt_status"] = st_full

    st_sm, _h, _b = fetch(urljoin(base, "/sitemap.xml"), method="HEAD")
    out["map"]["sitemap_status"] = st_sm
    if st_sm != 200 and not out["gate"].get("sitemap_declared"):
        add("medium", "map", "No sitemap.xml found at the conventional path.")

    # ---- Meal: homepage HTML ----------------------------------------------
    st, hdrs, html = fetch(base)
    out["meal"]["status"] = st
    if st == 200 and html:
        ex = Extract()
        try:
            ex.feed(html)
        except Exception:  # noqa: BLE001 - malformed HTML shouldn't kill the audit
            pass
        out["meal"]["visible_text_chars"] = ex.text_len
        out["meal"]["headings"] = ex.headings
        out["meal"]["tables"] = ex.tables
        out["meal"]["time_tags"] = ex.time_tags
        out["meal"]["markdown_alternate_links"] = ex.md_links
        out["meal"]["describedby_links"] = ex.describedby
        link_hdr = hdrs.get("Link", "")
        out["map"]["link_header"] = link_hdr
        if "text/markdown" in link_hdr:
            out["map"]["markdown_via_header"] = True

        types = []
        bad = 0
        for blob in ex.jsonld:
            try:
                data = json.loads(blob)
            except json.JSONDecodeError:
                bad += 1
                continue
            for node in data if isinstance(data, list) else [data]:
                if isinstance(node, dict):
                    t = node.get("@type")
                    types.extend(t if isinstance(t, list) else [t])
                    for g in node.get("@graph", []) or []:
                        if isinstance(g, dict) and g.get("@type"):
                            gt = g["@type"]
                            types.extend(gt if isinstance(gt, list) else [gt])
        out["meal"]["jsonld_types"] = [t for t in types if t]
        out["meal"]["jsonld_invalid_blocks"] = bad
        if bad:
            add("medium", "meal", f"{bad} JSON-LD block(s) failed to parse.")
        if not types:
            add("low", "meal", "No JSON-LD on the homepage. Add Organization with "
                               "sameAs links — parsing/entity hygiene, not a citation lever.")
        elif "Organization" not in types and "Corporation" not in types:
            add("low", "meal", f"JSON-LD present ({', '.join(sorted(set(types))[:5])}) "
                               "but no Organization node.")

        if ex.text_len < 800:
            add("high", "meal", f"Only ~{ex.text_len} chars of text in the raw HTML — "
                                "content is likely client-rendered and invisible to AI "
                                "crawlers. Verify with JS disabled.")
        elif ex.text_len < 2000:
            add("medium", "meal", f"Sparse raw HTML (~{ex.text_len} chars). Confirm the "
                                  "substantive content is server-rendered.")
        if ex.headings < 3:
            add("low", "meal", "Few headings — weak chunk boundaries for RAG retrieval.")
        if re.search(r'<div id="(root|__next)"></div>', html):
            add("high", "meal", "Empty React root in the served HTML: client-only render.")
    else:
        add("high", "meal", f"Homepage returned {st} to a normal request.")

    out["score"] = score(out["findings"])
    return out


# --------------------------------------------------------------------------
# repo audit
# --------------------------------------------------------------------------

SKIP_DIRS = {"node_modules", ".git", ".next", "dist", "build", ".vercel", "out",
             "coverage", ".turbo", "vendor", "__pycache__"}


def walk(root: str, limit: int = 6000):
    seen = 0
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith(".")]
        for f in filenames:
            seen += 1
            if seen > limit:
                return
            yield os.path.join(dirpath, f)


def audit_repo(root: str) -> dict:
    out: dict = {"target": root, "repo": {}, "findings": []}
    add = lambda sev, layer, msg: out["findings"].append(  # noqa: E731
        {"severity": sev, "layer": layer, "message": msg}
    )
    files = list(walk(root))
    rel = [os.path.relpath(p, root) for p in files]

    def has(*names):
        return [r for r in rel if os.path.basename(r) in names]

    out["repo"]["robots_files"] = has("robots.txt", "robots.ts", "robots.js")
    out["repo"]["llms_files"] = has("llms.txt", "llms-full.txt")
    out["repo"]["sitemap_files"] = has("sitemap.xml", "sitemap.ts", "sitemap.js")
    out["repo"]["framework"] = (
        "next" if has("next.config.js", "next.config.ts", "next.config.mjs") else
        "astro" if has("astro.config.mjs", "astro.config.ts") else
        "unknown"
    )

    if not out["repo"]["robots_files"]:
        add("high", "gate", "No robots.txt or robots.ts in the repo.")
    if not out["repo"]["llms_files"]:
        add("low", "map", "No llms.txt in the repo.")
    if not out["repo"]["sitemap_files"]:
        add("medium", "map", "No sitemap source found.")

    client_pages, jsonld_files, use_effect_fetch = [], [], []
    for path, r in zip(files, rel):
        if not r.endswith((".tsx", ".jsx", ".ts", ".js", ".astro", ".mdx")):
            continue
        try:
            with open(path, "r", encoding="utf-8", errors="replace") as fh:
                head = fh.read(120_000)
        except OSError:
            continue
        base = os.path.basename(r)
        if base.startswith(("page.", "layout.")) and re.match(
            r'^\s*[\'"]use client[\'"]', head
        ):
            client_pages.append(r)
        if "application/ld+json" in head:
            jsonld_files.append(r)
        if re.search(r"useEffect\([^)]*\)\s*=>\s*\{[^}]*fetch\(", head, re.S):
            use_effect_fetch.append(r)

    out["repo"]["client_rendered_pages"] = client_pages[:20]
    out["repo"]["jsonld_files"] = jsonld_files[:20]
    out["repo"]["useeffect_fetch_files"] = use_effect_fetch[:20]

    if client_pages:
        add("high", "meal", f'{len(client_pages)} page/layout file(s) marked "use client" '
                            "— their content will not be in the server-rendered HTML: "
                            + ", ".join(client_pages[:5]))
    if not jsonld_files:
        add("low", "meal", "No JSON-LD found anywhere in the source.")
    if use_effect_fetch:
        add("medium", "meal", f"{len(use_effect_fetch)} file(s) fetch content in "
                              "useEffect — that content is invisible to AI crawlers.")

    out["score"] = score(out["findings"])
    return out


# --------------------------------------------------------------------------
# reporting
# --------------------------------------------------------------------------

WEIGHT = {"high": 25, "medium": 8, "low": 2}


def score(findings: list[dict]) -> int:
    return max(0, 100 - sum(WEIGHT.get(f["severity"], 0) for f in findings))


ICON = {"high": "!!", "medium": "! ", "low": "· "}


def render(result: dict) -> str:
    L = [f"\nAI agent readiness — {result['target']}", "=" * 62]
    for layer, title in (("gate", "GATE  (can agents get the bytes)"),
                         ("map", "MAP   (can they navigate)"),
                         ("meal", "MEAL  (is anything extractable)"),
                         ("repo", "REPO  (source inspection)")):
        d = result.get(layer)
        if not d:
            continue
        L.append(f"\n{title}\n" + "-" * 62)
        for k, v in d.items():
            if isinstance(v, dict):
                L.append(f"  {k}:")
                for kk, vv in v.items():
                    L.append(f"    {kk:<22} {vv}")
            elif isinstance(v, list):
                L.append(f"  {k:<24} {', '.join(map(str, v))[:200] or '(none)'}")
            else:
                L.append(f"  {k:<24} {v}")

    L.append("\nFINDINGS\n" + "-" * 62)
    order = {"high": 0, "medium": 1, "low": 2}
    fs = sorted(result["findings"], key=lambda f: order.get(f["severity"], 3))
    if not fs:
        L.append("  none")
    for f in fs:
        L.append(f"  {ICON.get(f['severity'],'  ')} [{f['layer']}] {f['message']}")
    L.append(f"\nScore: {result['score']}/100  "
             f"({sum(1 for f in fs if f['severity']=='high')} blocking, "
             f"{sum(1 for f in fs if f['severity']=='medium')} medium, "
             f"{sum(1 for f in fs if f['severity']=='low')} minor)")
    L.append("\nScore is a triage aid, not a grade. Fix blocking findings first —\n"
             "a perfect llms.txt behind a WAF that blocks the bot is worth nothing.\n")
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser(description="Audit a site's readiness for AI agents.")
    ap.add_argument("--url", help="live site to audit, e.g. https://example.com")
    ap.add_argument("--repo", help="path to project source for static inspection")
    ap.add_argument("--json", action="store_true", help="emit JSON instead of a report")
    args = ap.parse_args()

    if not args.url and not args.repo:
        ap.error("give --url, --repo, or both")

    results = []
    if args.url:
        results.append(audit_url(args.url))
    if args.repo:
        results.append(audit_repo(args.repo))

    if args.json:
        print(json.dumps(results if len(results) > 1 else results[0], indent=2))
    else:
        for r in results:
            print(render(r))

    return 1 if any(
        f["severity"] == "high" for r in results for f in r["findings"]
    ) else 0


if __name__ == "__main__":
    sys.exit(main())
