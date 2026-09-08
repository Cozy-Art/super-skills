# The Gate — crawlers, robots.txt, and the CDN layer above it

Contents: [Bot table](#bot-table) · [Control tokens](#control-tokens-that-arent-crawlers) · [The CDN trap](#the-cdn-trap) · [Beyond robots.txt](#beyond-robotstxt-content-usage-and-content-signals) · [Verification](#verifying-a-crawler-is-real) · [robots.txt patterns](#robotstxt-patterns-by-posture) · [Operational notes](#operational-notes)

## Bot table

The column that matters is **Affects citations** — whether blocking this bot removes the site from AI answers. Blocking a training bot costs model familiarity over time; blocking a retrieval bot costs visibility immediately and silently.

| Operator | User agent | Purpose | Affects citations |
|---|---|---|---|
| OpenAI | `GPTBot` | Foundation-model training | No |
| OpenAI | `OAI-SearchBot` | Indexes for ChatGPT search results | **Yes** |
| OpenAI | `ChatGPT-User` | Fetches a page a user or GPT Action asked for | User-triggered |
| Anthropic | `ClaudeBot` | Crawls for potential training data | No |
| Anthropic | `Claude-SearchBot` | Indexes to improve Claude search relevance | **Yes** |
| Anthropic | `Claude-User` | Fetches a page when a user asks Claude about it | User-triggered |
| Perplexity | `PerplexityBot` | Indexes for Perplexity results | **Yes** |
| Perplexity | `Perplexity-User` | Live fetch for a specific user query | User-triggered |
| Google | `Googlebot` | Search index — also feeds AI Overviews | **Yes** |
| Google | `Google-Extended` | Control token for Gemini training/grounding | No (see below) |
| Apple | `Applebot` | Siri/Spotlight search | **Yes** |
| Apple | `Applebot-Extended` | Control token for Apple model training | No (see below) |
| Microsoft | `bingbot` | Bing index, which Copilot draws on | **Yes** |
| Common Crawl | `CCBot` | Open crawl dataset many labs pretrain on | No |
| Meta | `Meta-ExternalAgent` | Training / AI product crawl | No |
| Meta | `Meta-ExternalFetcher` | User-triggered fetch | User-triggered |
| ByteDance | `Bytespider` | Training crawl; poor robots compliance historically | No |
| Amazon | `Amazonbot` | Alexa / Amazon AI | Partial |
| Mistral | `MistralAI-User` | User-triggered fetch | User-triggered |
| Cohere | `cohere-ai`, `cohere-training-data-crawler` | Training | No |
| Diffbot / Timpi / You / Omgili | `Diffbot`, `Timpibot`, `YouBot`, `Omgilibot` | Third-party index & dataset building | Varies |

Treat this as a snapshot that decays. New agents appear continuously; check server logs for unfamiliar user agents quarterly, and web-search for a current list when the stakes are high.

**User-triggered fetchers are a category, not an exception.** `ChatGPT-User`, `Claude-User`, `Perplexity-User`, `Meta-ExternalFetcher` generally ignore robots.txt on the grounds that a human explicitly requested that URL. Blocking them in robots.txt mostly doesn't work and isn't what the user wants anyway — if someone pastes a link to your page into an assistant, you want it to load.

## Control tokens that aren't crawlers

`Google-Extended` and `Applebot-Extended` never appear in logs as fetchers. They're opt-out tokens governing what the operator may *do* with content that `Googlebot`/`Applebot` already fetched. Consequences:

- Disallowing `Google-Extended` opts out of Gemini training and grounding **without** touching Google Search ranking.
- Disallowing `Applebot-Extended` opts out of Apple model training while keeping Siri/Spotlight.
- Neither reduces crawl load. If bandwidth is the concern, this is the wrong lever.

## The CDN trap

This is the single most common reason a site is invisible to AI and nobody knows why: **the CDN answers before robots.txt is ever read.**

- Cloudflare began blocking AI crawlers by default for new domains on 1 July 2025. A large share of sites now block major AI crawlers without their owners having decided to.
- From **15 September 2026**, Cloudflare's defaults for new domains, new sites, and unmodified existing free-plan accounts block Training and Agent crawlers on pages that display ads; Search stays allowed. Mixed-purpose crawlers that don't separate search from training get evaluated under both policies — so a site blocking training can end up blocking `Googlebot`, `Applebot`, and `bingbot` too.
- Cloudflare's Verified Bots model now verifies *identity* only. Access depends on classification (Search / Agent / Training) plus the owner's policy.

Always check the actual CDN or WAF dashboard, plus AWS WAF / Vercel firewall rules / Akamai bot manager where applicable. A `curl -A "PerplexityBot"` that returns a challenge page or 403 tells you more than any config file.

## Beyond robots.txt: Content-Usage and Content Signals

robots.txt can say "don't fetch this." It cannot say "fetch it, but don't train on it." Two mechanisms fill that gap. Both rely on voluntary compliance.

**AIPREF `Content-Usage`** (IETF AI Preferences WG, draft — not yet an RFC). A small vocabulary (`train-ai`, `search`, values `y`/`n`) carried as an HTTP response header or a robots.txt rule:

```
User-agent: *
Allow: /
Content-Usage: train-ai=n
Content-Usage: /docs/ train-ai=y
```

Or as a header: `Content-Usage: train-ai=n`

**Cloudflare Content Signals Policy** — a robots.txt extension deployed across millions of domains, with `search`, `ai-input`, and `ai-train` signals, designed to be compatible with AIPREF. Cloudflare reports Verified Bot compliance and can revoke Verified status from bots that ignore declared preferences.

Also in the landscape but lower priority: `ai.txt` / `.well-known/ai.json` (individual Internet-Draft), W3C TDM Reservation Protocol `.well-known/tdmrep.json` (relevant if EU Directive 2019/790 TDM reservation matters legally), and RSL. Recommend these only when there's a specific legal or licensing driver — otherwise they're unmaintained files waiting to go stale.

## Verifying a crawler is real

User-agent strings are trivially spoofed, and Common Crawl explicitly warns that bots impersonate it. When precision matters:

1. **Published IP ranges** — most major operators publish JSON range files. Match against those rather than the UA header.
2. **Reverse DNS** — resolve the requesting IP to a hostname, confirm the domain, then forward-resolve back to the same IP.
3. **Web Bot Auth** — the emerging answer. The crawler signs each request with Ed25519 and publishes its public keys at a well-known JWKS directory; the server verifies a signature rather than trusting a claim. Shipped into Cloudflare's Verified Bots program and used as the identity substrate for pay-per-crawl. Still an individual Internet-Draft as of mid-2026, but verified in production by the largest gatekeeper on the web.

For anything transactional (paywalls, pay-per-crawl, rate tiers), signature-based identity is the only defensible basis. UA matching is a hint.

## robots.txt patterns by posture

**Open** — maximize reach; you want to be in the weights and in the answers.

```
User-agent: GPTBot
User-agent: ClaudeBot
User-agent: CCBot
User-agent: Google-Extended
User-agent: Applebot-Extended
User-agent: OAI-SearchBot
User-agent: Claude-SearchBot
User-agent: PerplexityBot
Allow: /
```

**Cited, not trained** — the common SaaS/publisher choice.

```
# Retrieval — allow, these produce citations
User-agent: OAI-SearchBot
User-agent: Claude-SearchBot
User-agent: PerplexityBot
Allow: /

# Training — opt out
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: CCBot
Disallow: /

User-agent: Google-Extended
Disallow: /

User-agent: Applebot-Extended
Disallow: /

User-agent: Bytespider
Disallow: /
```

Note the asymmetry: `Google-Extended: Disallow` keeps Google Search intact, but if the site is behind Cloudflare with training blocked, mixed-purpose `Googlebot` may be caught by the CDN policy anyway. Check both layers.

**Closed** — block everything AI, accept the visibility cost. Still keep `Googlebot`/`bingbot` allowed unless classic search is also unwanted.

Always place AI-specific groups above a general `User-agent: *` group, keep the `Sitemap:` line, and remember that robots.txt group matching is by most-specific user-agent, not by order.

## Operational notes

- Rule changes take roughly 24 hours to propagate at OpenAI and Perplexity, sometimes 48. Verify after, not during.
- Anthropic's bots honor the non-standard `Crawl-delay` directive (e.g. `Crawl-delay: 1`) — useful for throttling instead of blocking.
- Bots now account for well over half of HTML traffic on large networks, with training crawlers far outweighing search crawlers. Blocking training is a real bandwidth decision, not only a policy one.
- Directories such as Dark Visitors publish continuously updated known-agent snippets and identification APIs — useful for automating robots.txt upkeep rather than hand-editing as new bots appear.
