---
name: ai-agent-readiness
description: Audit and fix how a website is read by AI agents and answer engines — llms.txt, per-bot robots.txt policy, CDN/WAF bot gates, markdown mirrors, JSON-LD, SSR verification, and content extractability. Use this skill whenever the user mentions llms.txt, robots.txt, GPTBot/ClaudeBot/PerplexityBot or any AI crawler, GEO, AEO, "AI SEO", answer engines, getting cited by ChatGPT/Claude/Perplexity/Gemini, agent-readable or machine-readable content, schema.org/structured data for AI, or asks why their site isn't showing up in AI answers — and also when shipping or reviewing a marketing site, docs site, or landing page where AI discoverability should be checked before launch, even if they don't name any of these terms.
---

# AI Agent Readiness

Make a site legible to two very different machine audiences, and stop confusing them for one.

## The two audiences (this framing drives every decision)

**Answer engines** — ChatGPT Search, Perplexity, Google AI Overviews, Claude's search. They crawl your HTML, chunk it, and cite passages. Measured evidence says they **almost never fetch `/llms.txt`**; they read rendered HTML. What moves them: being reachable at all, server-rendered content, and self-contained quotable passages.

**Working agents** — Cursor, Claude Code, Copilot, MCP clients, browsing agents. These **do** fetch `/llms.txt` and `.md` mirrors routinely when pointed at a site. What moves them: a curated map and clean markdown.

Optimizing for one and claiming credit with the other is the most common failure in this space. Say which audience each recommendation serves.

## Three layers, in this order

Work the layers in order. A perfect `llms.txt` behind a CDN that blocks the bot is worth nothing.

1. **The Gate** — can the agent get the bytes? CDN/WAF bot rules, robots.txt, `Content-Usage`, auth walls, rate limits.
2. **The Map** — can it find what matters? llms.txt, `.md` mirrors, sitemap, link relations, internal linking.
3. **The Meal** — is there anything extractable once it arrives? SSR HTML, chunkable passages, JSON-LD, freshness.

## Workflow

### 1. Establish mode and posture

Two things must be settled before writing any file. Ask if not already clear.

**Mode** — auditing a live site, implementing from scratch, or both.

**Posture** — training vs. retrieval are separate decisions and most people have never made them explicitly:

| Posture | Training crawlers | Search/answer crawlers | Fits |
|---|---|---|---|
| **Open** | allow | allow | Marketing sites, OSS docs, personal brand — you want to be in the model's weights |
| **Cited, not trained** | block | allow | Most SaaS and publishers — stay citable, opt out of training |
| **Closed** | block | block | Paid/proprietary content — accepts invisibility in AI answers |

State the trade-off plainly: blocking search/answer crawlers means the brand disappears from AI answers with no warning signal. Blocking training crawlers costs long-term model familiarity but not citations. Never pick for the user; present the three and let them choose.

### 2. Audit

Run the bundled script before forming any opinion — it checks all three layers and costs one command:

```bash
python3 scripts/audit.py --url https://example.com
```

Add `--repo /path/to/project` to also inspect source (Next.js `robots.ts`, `app/` routes, client-only pages, JSON-LD in components). `--json` emits machine-readable output for CI. If the environment has no network access, run repo mode and say plainly which live checks were skipped.

Read the script's findings, then read the relevant reference file before recommending fixes — the references carry the current bot tables, spec details, and evidence rankings that keep advice from drifting into folklore.

### 3. Fix in impact order

Do not present findings as a flat list. Order them:

1. **Blocking issues** — CDN/WAF blocking retrieval bots, `noindex`, client-only rendering of key content, auth walls. These make everything else moot.
2. **Policy correctness** — robots.txt matching the chosen posture, per-bot rather than blanket rules.
3. **Extractability** — answer-first structure, self-contained passages, tables, freshness metadata.
4. **Map files** — llms.txt, `.md` mirrors, link relations.
5. **Nice-to-have** — JSON-LD beyond `Organization`/`Article`, directory listings.

That order is deliberately the reverse of how most GEO advice is written. llms.txt and schema get the attention; the gate and the render are what actually break.

### 4. Verify, don't assume

Every change gets a verification command, not a claim. `curl -A "PerplexityBot" -I <url>`, a JS-disabled fetch to confirm content is in the raw HTML, a re-run of `audit.py`. robots.txt changes take roughly 24–48 hours to propagate at major operators, so same-day toggling proves nothing.

## Reference files

Read the one that matches the layer being worked on. Do not load all four.

- `references/crawlers.md` — the Gate. Bot-by-bot table with purpose and whether it affects citations, the CDN/WAF trap, `Content-Usage`/AIPREF and Cloudflare Content Signals, crawler verification, robots.txt patterns per posture.
- `references/llms-txt.md` — the Map. The v2 spec format, what it's actually good for, `.md` mirrors, link relations, and honest expectation-setting.
- `references/extractability.md` — the Meal. Evidence-ranked tactics for being cited, chunking for RAG, and a schema.org reality check.
- `references/nextjs-vercel.md` — implementation recipes for Next.js App Router, middleware, and Vercel. Read when writing code rather than advising.

## Assets

- `assets/robots.txt.template` — annotated, three postures, uncomment the one you want.
- `assets/llms.txt.template` — spec-correct skeleton with inline notes.

## Do

- Separate the two audiences in every recommendation, and name which one a change serves.
- Check the CDN/WAF layer before the robots.txt layer. It sits upstream and overrides it.
- Treat `Google-Extended` and `Applebot-Extended` as usage-control tokens, not crawlers — blocking them changes how content may be used, not whether it's fetched.
- Give every finding a verification command.
- Say when evidence is weak. "Schema is parsing hygiene, not a citation lever" is more useful than a confident number.
- Write llms.txt by hand for small sites. A curated 20-link file beats a generated 400-link dump; the whole point is fitting in context.

## Don't

- Don't sell llms.txt as an answer-engine visibility play. Adoption sits around 10% and the largest study to date found it added noise rather than signal to citation prediction. Recommend it for agent-routing and docs, honestly framed.
- Don't block `ChatGPT-User`, `Claude-User`, or `Perplexity-User` expecting privacy — these are user-triggered fetches that generally bypass robots.txt because a human asked for that specific page.
- Don't write a blanket `User-agent: * Disallow: /` for AI concerns. It's indiscriminate and usually costs search visibility the user wanted to keep.
- Don't recommend `FAQPage` schema for rich results — Google removed FAQ rich results in May 2026. It still helps chunking; that's the reason to use it, not SERP appearance.
- Don't trust a user-agent string for access control. They're trivially spoofed; verify by published IP range, reverse DNS, or Web Bot Auth signature.
- Don't generate `.md` mirrors for every route on a large site. Do the docs and the pages agents actually need.
- Don't stack `llms.txt`, `llms-full.txt`, `ai.txt`, and `.well-known/` variants without a reason. Each unmaintained file is a stale-content liability.

## Checklist

Ship-blocking:
- [ ] CDN/WAF bot rules reviewed — retrieval bots reach a 200, not a challenge page
- [ ] Key content present in raw HTML with JS disabled (SSR/SSG, not client-only)
- [ ] No stray `noindex` / `X-Robots-Tag` on pages meant to be discoverable
- [ ] robots.txt distinguishes training from retrieval bots and matches the chosen posture

Should-have:
- [ ] Answer-first structure: each section opens with a standalone claim in 40–60 words
- [ ] Facts carry dates, figures, and named sources; `dateModified` is accurate
- [ ] `Organization` + `Article`/`Product` JSON-LD, visible content only, validated
- [ ] Comparison content rendered as real HTML tables, not prose or images
- [ ] `/llms.txt` present, spec-ordered, hand-curated, links resolve

Worth doing:
- [ ] `.md` mirrors for docs routes, exposed via `Link:` header or `<link rel="alternate">`
- [ ] `Content-Usage` directive set if expressing training preference beyond robots.txt
- [ ] Bot traffic monitored in logs so new agents get caught
- [ ] Re-verified 24–48h after robots.txt changes

## Timely note

Cloudflare's defaults change on **15 September 2026**: for new domains, new sites, and existing free-plan customers who haven't adjusted settings, Training and Agent crawlers are blocked by default on pages that display ads, while Search stays allowed. Mixed-purpose crawlers get evaluated under both policies. If the site is behind Cloudflare, check the dashboard rather than assuming robots.txt is in charge. Verify current state — this is a moving target and the date may now be past.
