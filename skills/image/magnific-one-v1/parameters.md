# Magnific One — Parameters

Native endpoint: `POST https://api.magnific.com/v1/ai/magnific-one` · header `x-magnific-api-key: <API key>` · `Content-Type: application/json`.
Schema has `additionalProperties: false` — any unlisted field is rejected.

*Verified against the Magnific API reference (Magnific One overview + generate pages), the Magnific API changelog (Oct 8 2026 entry), the Magnific One prompting guide, the Brand Kit docs, and VentureBeat's launch coverage, October 2026.*

## Request Fields

| Field | Type | Required | Values | Default | Notes |
|---|---|---|---|---|---|
| `prompt` | string | ✅ | 1–2,000 chars | — | Plain natural language. No token count published — the character limit is the only hard max. |
| `mode` | string | — | `quality` · `draft` | `quality` | `quality` = one finished image (the app's **Final**). `draft` = contact sheet of variations. `final` is not a valid value. |
| `quality` | string | — | `medium` · `high` | `high` | `quality` mode only. Draft always renders at `medium`. |
| `resolution` | string | — | `1k` · `2k` · `4k` | `2k` | `quality` mode only. Draft sheet is always `2k`. |
| `aspect_ratio` | string | — | `1:1` `2:1` `3:1` `2:3` `3:2` `3:4` `4:3` `16:9` `9:16` `21:9` | `1:1` | In Draft, applies to **each tile**. No `auto`, no `4:5`. |
| `tiles` | integer | — | `8` · `16` | `8` | Draft only; ignored in `quality` mode. |
| `reference_images` | string[] | — | 1–10 publicly accessible image URLs | — | Style guidance, both modes. No extra charge. File formats / size limits not published. |
| `webhook_url` | string (uri) | — | callback URL | — | Notified on status change; alternative to polling. |

There is no seed, negative prompt, guidance, step count, width/height, source-image (edit) field, Brand Kit field or style-preset field in the API.

## Draft Sheet Geometry

| `tiles` | Sheet | Ratios returned exactly |
|---|---|---|
| `8` | 2×4 | `1:1` `2:3` `3:2` `3:4` only — others approximated to the closest supported ratio |
| `16` | 4×4 | All ten |

Rule: if the shape matters (banner, 21:9 hero, 9:16 story), Draft at **16**.

The completed Draft task returns 8 or 16 separate image URLs, already cut from the sheet.

## Resolution & Pixels

- Tiers are `1k` / `2k` / `4k`; exact pixels vary with ratio. Magnific's guide shows **2K High at 3:4 = 1536×2048**. A full pixel table is not published — don't assume 4K means 3840×2160.
- Output format, alpha/transparency and colour profile are not documented. Result is an image URL.

## App (UI) vs API

| Control | Web / desktop app | API |
|---|---|---|
| Exploration | **Draft**: 4, 8 or 16 directions (fewer = more detail each) | `mode: "draft"`, `tiles` 8 or 16 |
| Delivery | **Final**: default 2K High; options up to 4K and **Max** | `mode: "quality"`, `quality` medium/high, `resolution` 1k/2k/4k |
| Style | Style tab: 1–5 images, or a built-in Magnific style | `reference_images` 1–10 URLs |
| Brand Kit | Final only; Image Generator, Spaces, Designer, agent | Not a documented field |
| Finishing | Auto Layers (editable layers), Designer (vector) | — |

State which surface a prompt targets. `quality: "max"` does not exist in the API.

## Response & Polling

- Submit returns immediately: `data.task_id` (uuid), `data.status`, `data.generated` (empty until done).
- Status enum: `CREATED` · `IN_PROGRESS` · `COMPLETED` · `FAILED`.
- Poll `GET /v1/ai/magnific-one/{task-id}`; list tasks with `GET /v1/ai/magnific-one`.
- `COMPLETED` → `generated` holds 1 URL (`quality`) or 8/16 URLs (`draft`).
- Retry 503s with exponential backoff. Rate limits depend on subscription tier.
- Download keepers promptly; URL lifetime is not documented.

## Cost

| Request | Billing |
|---|---|
| API `quality` | Once, at the price for the chosen `quality` + `resolution` (current rates on Magnific's API pricing page) |
| API `draft` | Once for the whole sheet at the `medium` / `2k` price — 8 or 16 tiles cost the same |
| `reference_images` | No effect on price |

App launch credit prices (per Final image, from launch coverage — confirm in the interface, which always shows the exact cost):

| Final tier | Credits |
|---|---|
| High · 2K | 180 |
| High · 4K | 250 |
| Max · 2K | 600 |
| Max · 4K | 1,000 |

Draft in the app costs the same as one image for the whole sheet.

## Recommended Combinations

| Goal | Settings | Why |
|---|---|---|
| Broad concept exploration | `draft` · `tiles: 16` · target ratio | Max variety, exact ratio, one charge |
| Fast square/portrait comparison | `draft` · `tiles: 8` · `1:1`/`2:3`/`3:2`/`3:4` | These stay exact at 8 |
| Social feed final | `quality` · `high` · `2k` · `3:4` or `1:1` | Delivery quality without 4K cost |
| Story / reel cover | `quality` · `high` · `2k`–`4k` · `9:16` | Native vertical |
| Wide campaign hero | Draft 16 @ `21:9` → `quality` `4k` `21:9` | Composition explored at final shape |
| Web banner | `quality` · `2k`–`4k` · `3:1` | Native banner ratio |
| Cheap wording test | `quality` · `medium` · `1k` | Lowest-cost single render |
| Branded series (app) | Final · same Brand Kit · same Style set · same ratio · same prompt skeleton | Separates brand, look and scene |

## Migration (legacy Magnific endpoints / other models)

| Habit | Magnific One |
|---|---|
| Quality-tag-heavy prompt | Strip tags; medium + subject + moment |
| `negative_prompt` | Not in schema — one short exclusion sentence at the end of the prompt |
| `seed` for reproducibility | Not in schema — fixed prompt skeleton + same references (+ Brand Kit in app) |
| `num_images` / 4-up grids | `mode: "draft"` with `tiles: 8`/`16` |
| `guidance_scale`, `styling` | Not in schema — style comes from `reference_images` |
| `width`/`height` | `aspect_ratio` + `resolution` |
| `mode: "final"` | `mode: "quality"` |
| Brand boilerplate in every prompt | Move to a Brand Kit (app); keep scene content in prompt |
| Reroll to fix a typo | Auto Layers / Designer |

There is no earlier Magnific One version; no Magnific One syntax is deprecated.
