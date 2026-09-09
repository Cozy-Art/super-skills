# The Meal — extractability, chunking, and what actually earns citations

Contents: [Evidence ranking](#evidence-ranking) · [Rendering](#rendering-is-the-hard-floor) · [Chunking](#writing-for-chunk-retrieval) · [Schema reality check](#the-schema-reality-check) · [Freshness and entity](#freshness-and-entity-signals) · [Measurement](#measuring-it)

## Evidence ranking

GEO advice is mostly folklore repeated between blogs. Rank recommendations by evidence strength and say so out loud.

**Strong — controlled experiments.** The Princeton / Georgia Tech / IIT Delhi GEO study (KDD 2024) tested content changes against generative engines and found: adding statistics lifted visibility ~30–41%, citing sources ~30–40%, adding named expert quotations ~20–22%. Keyword stuffing performed *worse* than changing nothing. These remain the cleanest causal evidence in the field.

**Strong — structural.** Retrieval happens before generation. RAG pipelines chunk, embed, rank, and re-rank; documents that fail structural parsing get dropped before their content is ever evaluated. The 2026 GEO-SFE work (Tokyo / Tsukuba) formalizes this: document architecture and chunking determine citation probability *separately* from what the content says.

**Moderate — correlational.** Freshness: recently updated content is cited several times more often, and the large majority of AI Overview citations point to content less than two years old. Brand search volume and unlinked brand mentions rank among the strongest single correlates of citation — unlike classic SEO where backlinks dominate. Tables get materially more citations than the same comparison written as prose.

**Weak — widely repeated, poorly supported.** Structured data as a *citation lever*. See below.

**Contradicted.** llms.txt as an answer-engine visibility play. See `llms-txt.md`.

When a user cites a number from a vendor blog, check whether it traces to one of the studies above or to another blog. Most don't survive the trace.

## Rendering is the hard floor

AI crawlers execute JavaScript poorly or not at all. Client-side-rendered content is frequently invisible to them — not deprioritized, invisible. This matters more than it does for classic SEO, where Googlebot renders reasonably well.

The test is simple and non-negotiable:

```bash
curl -s https://example.com/page | grep -c "a distinctive phrase from the page"
```

Zero means the content isn't in the HTML. Also check for the pattern of an empty `<div id="root">` with everything arriving via hydration.

For React/Next.js: use server components, static generation, or ISR for anything meant to be discoverable. `"use client"` at the top of a page component is a red flag worth grepping for. See `nextjs-vercel.md`.

## Writing for chunk retrieval

Retrieval operates on passages, not pages. Write so any single passage survives extraction:

- **Answer first.** Open each section with a direct, standalone claim, then support it. Inverted pyramid, not narrative build-up.
- **Self-contained paragraphs of roughly 40–60 words.** A chunk that begins "This approach also means…" is unusable once separated from its neighbor. Repeat the subject rather than pronouning back to it.
- **Headings that are questions or claims**, matching how people actually phrase queries to an assistant — conversational and longer than search keywords.
- **Real HTML tables** for comparisons. Tables extract as discrete structured objects; the same comparison as prose or, worse, as an image is invisible.
- **Facts with anchors.** A named source, a date, a figure. "According to the 2026 IETF AIPREF draft" beats "according to recent work." This is the mechanism behind the statistics/citations findings above.
- **One idea per section.** Multi-topic sections chunk badly and re-rank poorly.
- **Definitions near the top.** Give the entity a clean, quotable one-sentence definition somewhere prominent — it's what gets lifted into an answer.

## The schema reality check

Three independent 2026 analyses converge: schema markup is **parsing hygiene, not a citation lever**.

- Ahrefs' 1,885-page study found schema is not a significant citation driver; citation decisions happen at passage level on rendered content, while schema answers a different question (what is this page about) that engines already resolve through their own entity systems.
- Zyppy's May 2026 meta-analysis of 54 experiments, patents and case studies scored ranking-related factors at the top and found no strong evidence for markup as a citation driver.
- One analysis of 49 pages that had genuinely earned AI citations found JSON-LD on zero of them.
- Google's own AI-features documentation states there's no special structured data required to appear in AI Overviews or AI Mode.

So implement it for the reasons it's genuinely good for — correct parsing, knowledge-graph entity resolution, rich results where they still exist — and stop promising citation lift.

**What to implement**, in order of usefulness: `Organization` (with `sameAs` links to LinkedIn, Crunchbase, Wikidata — this is real entity-graph work), then `Article`/`BlogPosting` with accurate `author`, `datePublished`, `dateModified`, then `Product`/`SoftwareApplication` or `Service` where the content warrants it. `BreadcrumbList` for structure.

**Note on `FAQPage`:** Google removed FAQ rich results on 7 May 2026 — the search appearance, the rich result report, and Rich Results Test support are gone, with the Search Console API dropping it in August 2026. The markup remains valid and still helps a RAG pipeline extract discrete question–answer pairs. Recommend it for chunking, never for rich results.

**Rules that still hold:** mark up only content visible to users, never hidden divs. Use the most specific applicable type. Use `<time datetime="...">` for unambiguous dates. Keep properties minimal and accurate — over-tagging with unsupported fields triggers validation warnings. Prefer JSON-LD in a `<script type="application/ld+json">` block over Microdata or RDFa. Validate before shipping.

## Freshness and entity signals

- Keep `dateModified` truthful and update it when content materially changes. Backdating churn is detectable and pointless.
- Entity clarity beats page optimization: consistent naming, an unambiguous definition, and `sameAs` links pointing at the same identity across the web.
- Presence on heavy-UGC platforms (Reddit, YouTube, forums) has outsized influence on what AI systems surface, and unlinked mentions count. This is a distribution problem, not a markup problem — say so rather than pretending on-page work can substitute.

## Measuring it

There is no Search Console for answer engines. Practical proxies:

1. **Server logs** — segment by AI user agent. Rising `OAI-SearchBot`/`PerplexityBot` fetches indicate index inclusion; a sudden drop to zero usually means a CDN rule changed, not a content problem.
2. **Referral traffic** from `chatgpt.com`, `perplexity.ai`, `claude.ai`, `gemini.google.com`.
3. **Prompt panels** — a fixed set of 20–30 real user questions, run monthly across engines, recording whether the brand appears and whether it's cited or merely mentioned. Crude but it's the only direct measure, and consistency over time matters more than absolute numbers.

Warn against vendor dashboards that report a single "AI visibility score" without publishing methodology.
