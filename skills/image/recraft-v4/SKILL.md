---
name: recraft-v4-prompts
description: Generate optimized prompts and API payloads for Recraft's V4 image family — Recraft V4 (recraftv4), V4 Pro (recraftv4_pro, 2K), V4 Vector / Pro Vector (native SVG), plus sibling tiers V4.1, V4.1 Pro, V4.1 Utility, V4.1 Flash (recraftv4_1_flash) and V4 Styles (recraftv4_styles). Use whenever a user mentions Recraft, Recraft V4, V4 Pro, V4.1 Flash, Recraft Studio, external.api.recraft.ai, or wants design-led raster images, editable SVG logos/icons/illustrations, brand-palette control, poster typography, style-reference series, or image-to-image from Recraft — including via Runware, fal, Replicate, OpenRouter or ComfyUI nodes. Also use when migrating Recraft V3 prompts, since negative_prompt, text_layout, artistic_level, no_text and curated style names do not work on V4. Do not guess Recraft V4 syntax from general knowledge or V3 habits.
---

# Recraft V4 — Prompt Generation Skill

Recraft V4 is a design-taste still-image family: one prompt language, many tiers (1K raster, 2K Pro raster, SVG vector, fast Flash, style-locked Styles). The `model` id chooses the tier; the prompt never does.

**Scope:** stills only (raster WebP/PNG or SVG). No duration, motion, audio or camera paths — motion words describe the *look* of one frame.

## The Three Rules That Override Everything

1. **Always set `model` explicitly.** Omitted, the API defaults to `recraftv4_1` (or `recraftv4_styles` when style references are attached) — not V4. Reproducibility depends on it.
2. **Everything you want lives in the positive prompt.** V4 has no `negative_prompt`, no `text_layout`, no `artistic_level`, no `no_text`, no curated style names. Exclusions are a short plain clause ("no text or logos"), typography is described in prose.
3. **Match language to output type.** Raster: medium, light, material, lens. Vector: silhouette, geometry, fill/stroke rules, palette count, scalability — not texture or photographic light.

## Prompt Order (global → local)

| # | Layer | Example |
|---|---|---|
| 1 | Medium / deliverable | "Editorial photograph", "Flat vector icon set", "Large-format poster" |
| 2 | Subject + action (+ count) | "exactly three bottles", "one cyclist leaning into a turn" |
| 3 | Environment + spatial relations | foreground / midground / background, thirds, negative space |
| 4 | Framing + pose | "chest-up, subject in right third, facing left" |
| 5 | Identity / material details | wardrobe, surfaces, geometry |
| 6 | Light | direction, quality, colour temperature |
| 7 | Camera look | angle, focal-length look, depth of field, motion treatment |
| 8 | Palette, mood, constraints | 2–4 named colours, finish, short exclusions |
| 9 | Literal text | quoted copy + hierarchy + placement |

```
[MEDIUM]. [SUBJECT + COUNT + ACTION]. [ENVIRONMENT + RELATIONSHIPS].
[FRAMING]. [DETAILS]. [LIGHT]. [CAMERA LOOK]. [PALETTE + CONSTRAINTS].
[QUOTED TEXT + HIERARCHY + PLACEMENT].
```

**Two modes:** *Interpretive* (≈3–15 words) to let V4 / V4.1 make design decisions while exploring; *Architectural* (short labelled sentences) when counts, placement, text or brand matter. Limit: 10,000 characters (no token limit published). Length targets are practical, not official.

## Decide the Tier and Operation First

| User wants | `model` | Endpoint / extras |
|---|---|---|
| Fast ideation, bulk screening | `recraftv4_1_flash` | generations only; no styles, no vector, no image-to-image |
| Everyday art-directed 1K raster | `recraftv4` (or `recraftv4_1`) | `/images/generations` |
| Print / dense detail / typography edges | `recraftv4_pro` (2K) | same prompt, Pro size |
| Editable logo, icon, illustration | `recraftv4_vector` / `recraftv4_pro_vector` | ratio `size` only; `/images/generations/vector` enforces SVG |
| Series in one look from refs | `recraftv4` + `style_reference_urls` or `style_id`, or `recraftv4_styles` | `style_match: flexible | precise` |
| Change an existing image | `recraftv4` / `recraftv4_pro` | `/images/imageToImage` + required `strength` 0–1 |
| Flat, predictable product/UI imagery | `recraftv4_1_utility` | V4.1 sibling tier (flat light, simple composition) |

## Special Syntax (Quick Reference)

- **Visible text:** quote it — `headline reads "NIGHT SIGNAL" in condensed cream sans-serif across the top`. State hierarchy (largest / secondary), alignment, crop, overlap. Keep copy short.
- **No weighting syntax:** `(word:1.4)`, `::`, `--ar` are not Recraft syntax. Emphasis = position + repetition + specificity.
- **Palette:** name colours in prose *and* pass `controls.colors` (≤10 RGB, optional weights summing ≤1.0) when brand matters. `controls.background_color` for flat/catalog grounds.
- **Size:** use ratio form (`"4:5"`) — works on every model and is the only form vector accepts.

Full parameter table → [parameters.md](parameters.md).

## Output Format (always two parts)

1. **Prompt** — in a code block, prompt text only. Never put model, size, seed, palette RGB or format inside the prompt text.
2. **Suggested settings** — one line, e.g. `model: recraftv4_pro · size: 2:3 · n: 1 · image_format: png · controls.colors: navy/cream`

If the user is building an API call, give the JSON body with only valid native fields (`prompt`, `model`, `size`, `n`, `random_seed`, `controls`, `style_id` or `style_reference_urls`, `style_match`, `response_format`, `image_format`; plus `image_url`/`strength` for image-to-image).

## Things That Will Break the Request

- On V4/V4.1: `negative_prompt`, `text_layout`, `controls.artistic_level`, `controls.no_text`, curated `style` names (V4 only knows base style `any`).
- On Flash: any style field, any source image, any `_vector`/`_pro` variant.
- `style_id` **together with** style references — rejected.
- On `/imageToImage`: `style`, `style_id`, `style_match` are V3-only; missing `strength` (required, no default).
- Exact pixel sizes on vector models, or sizes outside the 14-ratio table.
- Wrapper field names (Runware `positivePrompt`, ComfyUI widgets) in native JSON — map deliberately.

## Iteration Workflow

1. Explore with Flash or V4, short prompt, `n: 4–6`.
2. Rewrite the winner as an architectural prompt; lock model, size, palette controls, `random_seed`.
3. Revise with image-to-image at the lowest `strength` that works; one change per pass.
4. Render the approved direction on `recraftv4_pro` (or Pro Vector) only where 2K/print detail pays.
5. Download results promptly (URLs are temporary, ~24 h); store full request bodies with each file.

## Reference Files

- **[parameters.md](parameters.md)** — model ids, endpoints, every field with valid values, sizes table, pricing, image-to-image, V3 → V4 and V4 → Flash migration.
- **[best-practices.md](best-practices.md)** — detail level, emphasis, composition and camera language for stills, typography, vector discipline, exclusions, common mistakes table.
- **[continuity-and-references.md](continuity-and-references.md)** — seeds, identity blocks, style references/`style_id`/V4 Styles, image-to-image continuity, storyboard series bibles, brand systems.
- **[examples.md](examples.md)** — annotated prompts: Flash exploration, character, landscape, action, depth study, poster, vector icons, logo, brand-palette product, style-reference series, image-to-image, V3 migration.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
