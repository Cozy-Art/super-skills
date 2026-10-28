---
name: nano-banana-2-1-prompts
description: "Generate optimized prompts for Google's Nano Banana 2.1 (gemini-nano-banana-2.1), the October 2026 GA successor to Nano Banana 2 (gemini-3.1-flash-image) — a fast Flash-tier image generation and conversational image-editing model. Use whenever a user mentions Nano Banana 2.1, NB 2.1, gemini-nano-banana-2.1, or the newest Nano Banana / Gemini Flash image model, or wants text-to-image, multi-reference composites (up to 14 images, up to 4 characters), multi-turn edits, exact in-image text, infographics, panoramic stills (1:4 to 8:1), search-grounded images, or posters/thumbnails from a video or PDF — in AI Studio, the Gemini API, Vertex AI or wrappers like fal and Runware. Also use when migrating Nano Banana 2 jobs (512px tier and minimal-thinking default are gone). Not for Nano Banana Pro (gemini-3-pro-image). Do not guess 2.1 syntax from older Nano Banana versions or general knowledge."
---

# Nano Banana 2.1 — Prompt Generation Skill

Nano Banana 2.1 (`gemini-nano-banana-2.1`) is Google's Flash-tier native image model: it generates stills and edits them conversationally. It replaces Nano Banana 2 (`gemini-3.1-flash-image`, now deprecated) with better prompt adherence, realism, text rendering, multi-turn character consistency and panoramic output. The prompt grammar carries over — plain-language scene briefs, no tokens, no weights.

**Scope:** image (and text) output only. Video and PDF are accepted as *context* (make a poster, thumbnail or summary graphic from them) — there is no video output, duration, motion or camera-path control.

## Which Nano Banana?

| Name | Model ID | Pick it for |
|---|---|---|
| **Nano Banana 2.1** (this skill) | `gemini-nano-banana-2.1` | Default everyday model: speed + quality, 1K/2K/4K, panoramas, up to 4 characters + 10 objects |
| Nano Banana Pro | `gemini-3-pro-image` | Heaviest reasoning and studio finish; different reference split (5 characters, 6 objects, 3 style) — use its own skill |
| Nano Banana 2 Lite | `gemini-3.1-flash-lite-image` | Lowest latency/cost, 1K only, up to 14 object refs, no character refs |
| Nano Banana 2 | `gemini-3.1-flash-image` | Deprecated — migrate to 2.1 |

If the user just says "Nano Banana" and the tool is current Google AI Studio/Gemini API Flash, assume 2.1 and say so.

## The Rules That Override Everything

1. **Write a scene brief in sentences, positively.** Subject, action, setting, composition, light, medium — connected prose, not tag lists. There is no negative prompt; write "an empty street", not "no cars". Skip quality tags ("8K, masterpiece").
2. **Give every reference a job, by content.** Google's own prompts point at attachments by what they are and what they're for — "using the attached napkin sketch as the structure and the fabric sample as the texture". Add order ("the second image") only to disambiguate. Say what to take and what to leave.
3. **Edits = one change + a concrete keep-list.** "Change only X. Keep the face, pose, background, camera position and lighting unchanged." There is no seed: continuity comes from reference images and the conversation thread.

**The interface is the source of truth.** If the user's tool or API rejects or contradicts a value here (ratio, size, thinking level, reference count), the interface wins — adjust and tell the user.

## Prompt Order

| # | Layer | Example |
|---|---|---|
| 1 | Intent / deliverable | "A premium campaign key visual", "A storyboard frame", "A four-panel infographic" |
| 2 | Subject + defining traits | identity anchors, product construction, counts |
| 3 | Action / state | pose, expression, relationships between subjects |
| 4 | Setting | location, time, weather, foreground / mid / background |
| 5 | Composition | shot size, angle, placement in frame, negative space, reading order |
| 6 | Light + colour | source, direction, quality, temperature, palette, mood |
| 7 | Camera or medium | lens / depth of field, or illustration material, line, texture |
| 8 | Exact text | every literal string in quotes + position, size, weight, type class |
| 9 | Reference roles + keep-list | what each attachment supplies; what must not change |

```
Create [deliverable] of [subject + traits], [action]. Set in [setting, layers].
[Composition + placement]. [Light source + direction + palette].
[Lens or medium]. Text: "[EXACT COPY]" at [position], [type style].
Using [reference] as [role] — take only [attributes]. Keep [invariants] unchanged.
```

**Length (practical, no official target):** icon/simple object 1–2 sentences · directed scene 50–120 words · multi-reference composite or infographic: several short paragraphs. Delete synonyms and conflicting instructions before adding more.

## Decide the Operation First

| User wants | Inputs | Prompt pattern |
|---|---|---|
| New image from text | none | Full brief (layers 1–8) |
| Composite from references | 1–14 images (≤4 characters, ≤10 objects) | `[References] + [Relationship] + [New scene]`, role per image |
| Edit one image | that image | "Change only…" + keep-list; for removal, name what fills the gap |
| Refine across turns | previous turn in the thread | Narrow follow-up; replay all approved changes if drift appears |
| Exact copy / infographic / menu | optional style ref | Grid first, then each block in reading order with quoted strings |
| Panorama / banner | optional | Describe left→right (or top→bottom) bands; suggest 2K/4K |
| Current facts (weather, scores, events) | none | Ask for the data + how to visualize it; suggest search grounding |
| Poster/thumbnail from video or PDF | the file | State the frame/page/content to extract and the still to design |

## Quick Syntax Reference

- **Text:** `the headline "HOW RETURNS WORK" in large dark-navy capitals across the top`. Quote exact capitalization and punctuation; give each string a role.
- **References:** by content + role — "the woman in the portrait reference", "the forest-green bicycle". Optional ordinal for clarity: "the bicycle (second image)".
- **Style scoping:** "Use only the palette, grain and contrast of the poster reference; take nothing else from it."
- **Counts and positions:** "exactly six bottles, each once", "subject in the lower-left third", "the right half stays open for copy".
- **Camera motion:** describe its still-frame evidence ("tracking-shot aesthetic, background streaked, runner sharp").

Depth → [best-practices.md](best-practices.md) · references, threads and series → [continuity-and-references.md](continuity-and-references.md).

## Output Format (always two parts)

1. **Prompt** — in a code block, prompt text only. Never put aspect ratio, size tier, thinking level or model name inside the prompt.
2. **Suggested settings** — one line, e.g.
   `aspect_ratio: 4:5 · image_size: 2K · thinking_level: medium · search grounding: off · references: [portrait master, jacket]`
   Offer `4K` and `high` thinking as "if your plan/interface offers it"; they cost more and take longer.

If the user is building a native API call, also give an Interactions API body with only documented fields (`model`, `input`, `response_format`, `generation_config.thinking_level`, `tools`, `previous_interaction_id`) — see [parameters.md](parameters.md).

## Things That Will Break or Degrade the Request

- `image_size` in lowercase (`"2k"`) — rejected. Use `1K` `2K` `4K`.
- `512px` / `0.5K` — that was Nano Banana 2 only; use `1K` and downsample.
- The old model string `gemini-3.1-flash-image` — deprecated.
- `negative_prompt`, `seed`, `temperature`, `top_p/top_k` — not part of the documented image controls (sampling params reportedly return an error — unverified).
- More than 14 references, or more than 4 character references.
- Wrapper field names (`image_urls`, `num_images`, `positivePrompt`, `enable_web_search`, `output_format`) sent to the native API — they belong to fal/Runware, not Google.
- Asking for a video, GIF or "camera move" — it returns a still.

## Iteration Workflow

1. Draft at `1K`, `minimal` or `medium` thinking. Pin the thinking level — the default changed from `minimal` (v2) to `medium` (2.1).
2. Fix the biggest miss with one wording change at a time; don't rewrite the whole brief.
3. Typography, dense layouts, multi-reference composites, strict placement → `high` thinking, `2K`.
4. Edit in the thread with narrow "change only / keep" turns. After 3–4 turns of drift, restart from the master image and apply all approved changes in one numbered prompt.
5. Final at `2K`/`4K` (panoramas especially). A new tier is a new render — attach the approved image and ask to recreate it, preserving composition.

## Reference Files

- [parameters.md](parameters.md) — model lineup, Interactions API fields, image sizes, aspect ratios, thinking levels, grounding, limits, pricing, Nano Banana 2 migration, wrapper notes.
- [best-practices.md](best-practices.md) — brief structure, positive phrasing, composition by shot type, camera language for stills, typography/layout, editing (keep-lists, removal, inserts), grounding, thinking choice, panoramas, common-mistakes table.
- [continuity-and-references.md](continuity-and-references.md) — reference capacity, roster and role binding, multi-turn threads, character sheets and masters, style bible, storyboard sequencing, drift reset, video/PDF context, handoff to video models.
- [examples.md](examples.md) — 10 annotated prompts: product, character portrait, landscape, action, motion aesthetic, multi-reference campaign, infographic, conversational edit, panorama, video-to-thumbnail.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
