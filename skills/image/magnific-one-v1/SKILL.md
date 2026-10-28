---
name: magnific-one-prompts
description: Generate optimized prompts and API payloads for Magnific One, Magnific's art-direction image model (launched October 2026; endpoint POST /v1/ai/magnific-one). Use whenever a user mentions Magnific One, Magnific's new image model, Draft/Final mode, contact-sheet exploration (8 or 16 tiles), Magnific Brand Kit generations, Magnific Style references, or wants posters, campaign key visuals, editorial photos, branded social assets or exact-copy typography from Magnific — in the web/desktop app, via MCP, or via the API. Also use when migrating prompts from Magnific's legacy text-to-image endpoints or other models, since negative_prompt, seed, guidance_scale, num_images and styling are not part of the Magnific One schema and will be rejected. Do not guess Magnific One syntax from general knowledge or older Magnific endpoints.
---

# Magnific One — Prompt Generation Skill

Magnific One is a still-image model with a built-in **art-direction layer**: it interprets the brief, decides composition, style, lighting and treatment, then renders. Work happens in two stages — **Draft** (a contact sheet of directions) then **Final** (one delivery image). In the API, Final is called `mode: "quality"`.

**Scope:** stills only. No duration, motion, camera paths or image-to-video. Animate an approved still downstream in a separate video model.

## The Three Rules That Override Everything

1. **Medium first, one sharp idea, stop early.** Start with the medium and a subject + moment. Every extra sentence takes control away from the art director — add viewpoint, light and palette only where you need control.
2. **Say each thing once.** Magnific's own guide: repeating an idea in different words makes the model drop details. One light setup, one composition, one mood word.
3. **Describe causes, not effects.** "Brushed steel, one window light, charcoal palette" — not "premium". No quality tags ("8K", "masterpiece", "cinematic" stacks).

## Prompt Order

Global → local. Only layers 1–2 are usually needed.

| # | Layer | Example |
|---|---|---|
| 1 | Medium / deliverable | "Editorial photograph", "Gouache illustration", "Minimal bold poster" |
| 2 | Subject + one defining moment | "a pit mechanic carrying a tire through smoke" |
| 3 | Story detail | wardrobe, one telling prop or gesture |
| 4 | Environment + spatial relationship | foreground / middle / background |
| 5 | Viewpoint / framing | "side view at bench height", "subject on the right third" |
| 6 | Light source + time | a source already in the scene, direction, temperature |
| 7 | Material / technique | knitted, glazed, risograph grain |
| 8 | Palette + mood | 2–4 colours with spatial roles |
| 9 | Quoted copy + exclusions | `"OPEN LATE"` + "Reproduce the text exactly as written. No other logos or text." |

**The control dial (official progression):** one word (`gossip`) → subject → story → full direction. Short = more art direction from the model; long = more control for you.

**Length:** hard limit **1–2,000 characters** (API). Practical: 5–40 words to explore, 50–120 for a directed Final, up to ~250 for posters with copy.

## Decide the Operation First

| User wants | Surface / mode | Notes |
|---|---|---|
| Explore concepts | Draft · `tiles: 16` | Whole sheet billed once. Use 16 when ratio must be exact |
| Quick comparison, square/portrait | Draft · `tiles: 8` | Exact only for `1:1` `2:3` `3:2` `3:4` |
| Delivery image, known direction | Final · `quality: high` · `2k` | API default |
| Large display / print / crop room | Final · `4k` (UI: High or Max) | Max is app-only |
| Consistent look across a set | Same `reference_images` (style) | API 1–10 URLs; app Style tab 1–5 |
| On-brand output | Final + Brand Kit (Image Generator, Spaces, Designer, agent) | Not a documented API field; Final only |
| Fix one flaw | Add **one** corrective line | See `best-practices.md` §6 |
| Exact type / colours | Keep image, finish in Auto Layers / Designer | Don't reroll for typos |

## Special Syntax (Quick Reference)

- **Plain natural language only.** No weights, brackets, `--flags`, or camera tokens.
- **Exact copy in quotes:** `headline "LA CAÑA" across the top`. Follow with `Reproduce the text exactly as written. No other logos or text.`
- **Short exclusions are fine** — Magnific's own corrective line is `No people, no vehicles, no text.` There is no negative-prompt field, so put them at the end of the prompt.
- **Style vs content:** reference images in the API are *style* guidance. In the app, only the Style tab treats images as a look; normal references are read as content.

## Output Format (always two parts)

1. **Prompt** — in a code block, prompt text only. Never put mode, tiles, quality, resolution or aspect ratio in the prompt text.
2. **Suggested settings** — one line, e.g. `mode: draft · tiles: 16 · aspect_ratio: 3:4` or `Final · High · 2K · 3:4 · Brand Kit: <client>`

For API work, also give the JSON payload with valid fields only: `prompt`, `mode`, `quality`, `resolution`, `aspect_ratio`, `tiles`, `reference_images`, `webhook_url`.

## Things That Will Break the Request

- **Unknown fields are rejected** (`additionalProperties: false`). Never send `negative_prompt`, `seed`, `guidance_scale`, `num_images`, `styling`, `image`, `width`, `height`, `brand_kit`, `style`.
- `mode: "final"` — invalid. API values are `quality` and `draft`.
- `quality: "max"` — invalid. API values are `medium` and `high`; Max is a UI tier.
- `tiles: 4` — app only; the API accepts `8` or `16`.
- (API) `aspect_ratio` outside `1:1 2:1 3:1 2:3 3:2 3:4 4:3 16:9 9:16 21:9` (no `4:5`, `5:4`, `1:2`, `auto`).
- `reference_images` that aren't publicly reachable URLs, or more than 10.
- Prompts over 2,000 characters.
- `quality`/`resolution` in Draft won't error but are **ignored** (Draft is always medium, 2K sheet).

## Iteration Workflow

1. Write medium + subject + moment. Set the **final aspect ratio now** — composition is explored at that shape.
2. Draft at 16 tiles. Pick one direction and write down *why*: placement, viewpoint, light, palette, negative space.
3. Final: there is no tile ID to promote. Restate the chosen traits explicitly in the prompt, keep the same references.
4. Render High 2K first; 4K or Max only when display, print or crop latitude justifies the cost.
5. One corrective line per iteration. Never stack all of them.
6. Finish copy and exact colours in Auto Layers / Designer, not by rerolling.
7. Motion: hand the approved still to a video model as a start frame; prompt movement only.

## Reference Files

- **[parameters.md](parameters.md)** — every API field, aspect ratios, Draft sheet caveats, UI vs API differences, response/polling, credit costs, recommended combinations, migration table.
- **[best-practices.md](best-practices.md)** — medium vocabulary, cause-not-effect rewrites, control-dial levels, composition by shot type, implied camera motion, typography, the eight corrective lines, common mistakes table.
- **[continuity-and-references.md](continuity-and-references.md)** — Draft→Final handoff, Style references, Brand Kit, character identity blocks, series bible, multi-image sets, still→video handoff.
- **[examples.md](examples.md)** — 11 annotated prompts: control dial, portrait, landscape, action, implied tracking, style-reference scene, 3D material study, poster with copy, branded series, Draft→Final handoff, API payloads.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
