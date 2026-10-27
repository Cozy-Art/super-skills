# Recraft V4 — Parameters

Native base URL: `https://external.api.recraft.ai/v1` · header `Authorization: Bearer <RECRAFT_API_TOKEN>`.
Endpoints: `POST /images/generations` · `POST /images/generations/vector` (enforces `_vector` models) · `POST /images/imageToImage` · `POST /styles` · `POST /prompts/enhance`.

*Verified against the Recraft API reference (endpoints, models overview, appendix, pricing, image-to-image, llms-full.txt) and the Recraft changelog, October 2026.*

## Model IDs

| Tier | Raster id | Vector id | Native size | Notes |
|---|---|---|---|---|
| V4 | `recraftv4` | `recraftv4_vector` | 1K | Design taste, prompt accuracy, production vectors |
| V4 Pro | `recraftv4_pro` | `recraftv4_pro_vector` | 2K | Same prompt language, finer detail |
| V4 Styles | `recraftv4_styles` | `recraftv4_styles_vector` *(unverified id)* | 1K (`_pro` = 2K) | Always requires a style; default when refs attached and no `model` |
| V4.1 | `recraftv4_1` | `recraftv4_1_vector` | 1K (`recraftv4_1_pro` = 2K) | **API default model** |
| V4.1 Utility | `recraftv4_1_utility` | — | 1K (`_pro` = 2K) | Flat lighting, simple predictable composition |
| V4.1 Flash | `recraftv4_1_flash` | none | 1K only | ~1.3 s; no styles, no vector, no image-to-image |

Raster ids also accept a `_raster` alias (e.g. `recraftv4_1_raster`). Vector ids are every id ending `_vector`. Previous gen: `recraftv3`, `recraftv3_vector`, `recraftv2`.

## Generation Fields (`/images/generations`)

| Field | Type | Values | Default | V4 notes |
|---|---|---|---|---|
| `prompt` | string | 1–10,000 chars | — | Required. V3/V2 cap at 1,000. |
| `model` | string | ids above | `recraftv4_1` (`recraftv4_styles` if style refs) | Always set it. |
| `size` | string | 14 ratios (`"4:5"`) or exact sizes from table | auto from prompt | Ratio form works everywhere; vector accepts **only** ratio form. |
| `n` | integer | 1–6 | 1 | 4–6 to explore, 1 for locked finals. |
| `random_seed` | integer | no published range | random | Reproducible only when every other input matches. |
| `style_id` | UUID | from `/styles` or a prior ref-generation | — | Not on Flash. Cannot combine with references. |
| `style_reference_urls` (JSON) / `style_references` (multipart) | URL[] / files | 1–10 images, ≤64 MB total | — | Creates a private style for the request; response returns its `style_id`. +$0.005. |
| `style_match` | string | `flexible` · `precise` | `flexible` | `regular` is V2/V3 only. |
| `style` | string | `any` (V4 base style) | — | V3 curated names (`realistic_image`, …) do not apply. Docs are inconsistent here — omit unless required. |
| `controls.colors` | object[] | ≤10 × `{"rgb":[r,g,b],"weight":0–1}` | — | Weights all-or-none, sum ≤1.0. Preference, not exact colour match. |
| `controls.background_color` | object | `{"rgb":[r,g,b]}` | — | Flat / catalog grounds. |
| `response_format` | string | `url` · `b64_json` · `multipart` | `url` | URLs expire ~24 h. `multipart` saves a round-trip. |
| `image_format` | string | `webp` (lossless) · `png` | `webp` | Raster only. |

V3-only (reject or ignore on V4): `negative_prompt`, `text_layout`, `controls.artistic_level`, `controls.no_text`, `style_match: regular`, curated `style` names.

## Sizes (ratio → pixels)

| Ratio | 1K (V4 / V4.1 / Flash) | 2K (Pro) | Typical use |
|---|---:|---:|---|
| `1:1` | 1024×1024 | 2048×2048 | Icons, tiles, product hero |
| `2:1` | 1536×768 | 3072×1536 | Banner, panorama |
| `1:2` | 768×1536 | 1536×3072 | Tall poster |
| `3:2` | 1280×832 | 2560×1664 | Landscape photo |
| `2:3` | 832×1280 | 1664×2560 | Portrait print, poster |
| `4:3` | 1216×896 | 2432×1792 | Editorial landscape |
| `3:4` | 896×1216 | 1792×2432 | Editorial portrait |
| `5:4` | 1152×896 | 2304×1792 | Product / editorial |
| `4:5` | 896×1152 | 1792×2304 | Social portrait |
| `6:10` | 832×1344 | 1664×2688 | Mobile / poster |
| `14:10` | 1280×896 | 2560×1792 | Wide editorial |
| `10:14` | 896×1280 | 1792×2560 | Portrait editorial |
| `16:9` | 1344×768 | 2688×1536 | Presentation, thumbnail |
| `9:16` | 768×1344 | 1536×2688 | Stories / reels cover |

Wrappers (older ComfyUI nodes, partner UIs) may show fewer presets — the native table wins.

## Image-to-Image (`/images/imageToImage`)

| Field | Values | Notes |
|---|---|---|
| `image` (multipart) / `image_url` (JSON, URL or data URL) | PNG, JPG, WEBP, SVG · <20 MB · ≤16 MP · sides 256–4096 px | Required. |
| `prompt` | ≤ model limit | Describe the change. |
| `strength` | float 0–1 | **Required, no default.** 0 ≈ identical, 1 = least similar. |
| `model` | V3, V4, V4.1 raster or vector | Default `recraftv4_1`. **Flash not supported.** |
| `n`, `random_seed`, `controls`, `response_format`, `image_format` | as above | |
| `style`, `style_id`, `style_match`, `negative_prompt`, `text_layout` | — | **V3 only** on this endpoint. |

Starting strengths (heuristics, not presets): colour/light fix 0.10–0.25 · wardrobe/season/surface 0.25–0.45 · restyle keeping layout 0.45–0.65 · major reinterpretation 0.65–0.85.

## Other Endpoints

- `POST /styles` — create a reusable style from references ($0.005). A style created against `recraftv4_styles` only works with that model (docs elsewhere say "all models except Flash" — test your pairing).
- `POST /prompts/enhance` — `{"prompt": "..."}` (≤2,000 chars) → `enhanced_prompt`; $0.01.
- Tools priced separately: vectorize $0.01 · remove background $0.01 · crisp upscale $0.004 · creative upscale $0.25 · enhance details (re-render with V4.1 Pro) $0.21.

## Pricing (per image, API)

| Tier | Raster | Vector | Pro raster (2K) | Pro vector |
|---|---:|---:|---:|---:|
| V4 | $0.04 | $0.08 | $0.25 | $0.30 |
| V4.1 | $0.035 | $0.08 | $0.21 | $0.30 |
| V4.1 Utility | $0.035 | $0.08 | $0.21 | $0.30 |
| V4 Styles | $0.035 | $0.05 | $0.10 | $0.12 |
| V4.1 Flash | $0.007 | — | — | — |

Style references add $0.005 per request. Image-to-image is billed per model (pricing page lists only V3 under editing — confirm V4 i2i cost on your account). Latency: Flash ~1.3 s (official); V4 ~10 s and Pro ~30 s *(unverified — confirm on your platform)*.

## Recommended Combinations

| Workflow | `model` | `size` | `n` | Extras |
|---|---|---|---|---|
| Concept screening | `recraftv4_1_flash` | target | 6 | `multipart`, `webp` |
| Art-directed web asset | `recraftv4` | target | 2–4 | seed stored |
| Brand series | `recraftv4` / `recraftv4_styles` | fixed | 1–4 | `style_id`, `precise`, `controls.colors` |
| Poster / print | `recraftv4_pro` | `2:3` `3:4` `1:2` | 1 | `png` |
| Logo / icon set | `recraftv4_vector` → `recraftv4_pro_vector` | `1:1` | 4 → 1 | 2–3 colour controls |
| Revision of a keeper | `recraftv4` | (from source) | 2 | `/imageToImage`, `strength` 0.15–0.35 |

## Migration

**V3 → V4:** prompt cap 1,000 → 10,000 · curated `style` → describe medium in prose or use a V4 style/refs · `negative_prompt` → short positive-prompt exclusion · `text_layout` → prose hierarchy/placement · `artistic_level` → describe static vs dynamic composition · `no_text` → "no text or logos" · inpaint/outpaint/background ops stay on V3. Start with a shorter baseline; V4 supplies more design defaults.

**V4 → V4 Pro:** change `model` only; syntax identical. Pro is a detail tier, not a new prompt language.

**V4 → V4.1:** same syntax; test the prompt unchanged, then trim boilerplate V4.1's stronger defaults already supply.

**V4 / Pro → Flash:** `model: recraftv4_1_flash`; drop every style field, source image, `_pro`/`_vector`; keep `size` (1K), `n`, `random_seed`, `controls`, formats.

**Wrappers:** Runware (`positivePrompt`, up to 20 results, JPG default), fal, Replicate, OpenRouter, ComfyUI expose their own names and defaults. Map native fields deliberately; a visible `negative_prompt` widget does not mean V4 uses it.
