# The Map — llms.txt and markdown mirrors

Contents: [What it's for](#what-its-actually-for) · [Format](#format-v2-spec) · [Example](#example) · [Markdown mirrors](#markdown-mirrors) · [Failure modes](#failure-modes) · [llms-full.txt](#llms-fulltxt)

## What it's actually for

Set expectations before writing a line of it.

**Where it works.** IDE and coding agents — Cursor, Windsurf, Claude Code, Copilot, Cline, Aider — routinely fetch `/llms.txt` and `/llms-full.txt` when pointed at a documentation site. The pattern is: identify which library owns a feature, fetch its llms.txt, pull only the linked pages needed. MCP servers are built around this (LangChain's `mcpdoc` exposes llms.txt files as a `fetch_docs` tool). Chrome's Lighthouse audits for one under its agentic-browsing checks. OpenAI, Anthropic, and Google publish them for their own developer docs.

**Where it doesn't.** Log analysis across large monitored estates finds AI *search* crawlers — GPTBot, ClaudeBot, PerplexityBot, OAI-SearchBot, Google-Extended — overwhelmingly skip the file and crawl HTML directly. A 300,000-domain study found roughly 10% adoption and, when llms.txt presence was tested as a predictor of AI citation frequency, removing the variable *improved* the model's accuracy. It added noise, not signal. Google's own search advocates have said no AI crawler has claimed to use it.

**The honest position.** Ship it — it's cheap, it's the first standardized machine-readable surface for agents, and the cost of being wrong is one small file. But sell it as agent-routing infrastructure, not as an answer-engine visibility play. If someone is choosing between writing llms.txt and fixing client-side rendering, the rendering wins every time.

The proposal is a community convention maintained at llmstxt.org (v2, revised August 2026). It is not a W3C or IETF standard and has no enforcement mechanism.

## Format (v2 spec)

Markdown, at `/llms.txt` or any subpath (`/docs/llms.txt` covers everything under `/docs/`). Where several apply, agents use the most specific. Sections in this exact order:

1. Optional byte-order mark
2. **An H1** with the project or site name — the only required section
3. A **blockquote** with a short summary containing the key context needed to understand the rest
4. Zero or more markdown sections of any type **except headings** — paragraphs, lists, caveats
5. Zero or more **H2-delimited "file list" sections**, each a markdown list of `- [Link title](url): optional notes`
6. By convention, a final `## Optional` section for links an agent can skip when context is tight

Because the format is precise, it's parseable by regex and classical tooling — don't improvise the structure.

## Example

```markdown
# Director's Studio

> An AI filmmaking platform for turning a script into shot-planned,
> model-ready sequences. This file covers the product docs and API.

Important notes:

- The API is versioned; `/v2` is current and `/v1` is frozen.
- Model adapters are documented per-provider, not in one combined page.

## Docs

- [Quickstart](https://example.com/docs/quickstart.md): End-to-end first render in ten minutes
- [Shot schema](https://example.com/docs/schema.md): The JSON structure every adapter consumes

## API

- [REST reference](https://example.com/docs/api/rest.md): Endpoints, auth, rate limits

## Optional

- [Changelog](https://example.com/changelog.md): Release history since 2025
```

Authoring guidelines from the spec: concise, jargon-free language; a short informative note on every link; no unexplained terms. **Test it the way the spec suggests** — hand an agent only the llms.txt and ask it real questions about the site. If it can't answer, the file is decorative.

## Markdown mirrors

The half of the proposal people skip, and the more useful half. Publish a clean markdown version of any page an agent might need, at the same URL with `.md` appended (`page.html.md`) or substituted (`page.md`). Directory URLs get `index.md` or `index.html.md`.

Discovery uses standard link relations:
- `rel="alternate" type="text/markdown"` → the markdown version of this page
- `rel="describedby"` → the llms.txt covering it

Either as HTML `<link>` elements or an HTTP `Link:` response header. The header form also works for non-HTML resources and can be set at the CDN or server layer without touching a single page:

```
Link: </docs/page.html.md>; rel="alternate"; type="text/markdown", </docs/llms.txt>; rel="describedby"
```

Links inside llms.txt should point at these markdown versions, not the HTML. The file stays small; detail lives behind the links and is fetched only when needed.

Platforms that generate all of this automatically: Mintlify, GitBook, Wix, Yoast and AIOSEO for WordPress, plus plugins for VitePress, Docusaurus, Drupal, and nbdev. Check whether the stack already emits one before hand-rolling.

## Failure modes

These make an llms.txt actively worse than none:

- **Generated dumps.** A 400-link auto-generated index defeats the purpose — the file exists to fit in context. Curate.
- **Stale links.** Agents follow them literally; a 404 rate above a few percent teaches the agent the file is unreliable.
- **Links to blocked content.** Cross-file conflicts are documented in the wild: llms.txt pointing at URLs that robots.txt or the WAF blocks. Audit the two together.
- **Wrong section order.** Headings before the blockquote, or prose after the first H2, breaks parsers that follow the spec.
- **Treating it as an access-control file.** It isn't robots.txt. It grants and denies nothing. Some third-party writeups get this backwards.

## llms-full.txt

An informal companion holding full page content inline rather than links. No spec status. It's useful for small docs sites an agent can swallow whole, and counterproductive for anything large — the size defeats the context-window rationale. Publish one only when the whole corpus genuinely fits in a context window, and keep it generated rather than hand-maintained.
