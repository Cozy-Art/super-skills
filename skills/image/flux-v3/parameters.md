# FLUX 3 Image — Parameters

Native endpoint: `POST https://api.bfl.ai/v1/flux-3-image` · header `x-key: <API key>` · `Content-Type: application/json`.
Schema has `additionalProperties: false` — any unlisted field returns **422**.

*Verified against the BFL API reference, October 2026.*

## Request Fields

| Field | Type | Required | Values | Default | Notes |
|---|---|---|---|---|---|
| `prompt` | string | ✅ | free text | — | Generation description or edit instruction. No documented maximum length. |
| `images` | string \| string[] \| null | — | 1–10 http(s) URLs or base64 | null | Order matters: image 1 drives `auto` framing and is the strongest anchor. BFL guides cite ≥256×256 and ≤16 MP per reference. |
| `aspect_ratio` | string | — | `21:9` `2:1` `16:9` `3:2` `7:5` `4:3` `5:4` `1:1` `4:5` `3:4` `5:7` `2:3` `9:16` `1:2` `9:21` `auto` | `auto` | Under `auto`: a ratio requested in the prompt wins → else follows image 1 → else prompt decides, fallback `1:1`. Prefer setting it explicitly. |
| `resolution` | string | — | `768sq` `1k` `1.5k` `2k` `4k` | `1k` | Equal-pixel-area tiers; exact dimensions vary with ratio. |
| `safety_tolerance` | integer | — | `0`–`7` | `2` | 0 = strictest. Your route/org sets the approved maximum; unapproved levels return 422 listing allowed values. |
| `grounding` | boolean | — | `true` / `false` | `true` | Allows web + image search before generating. |
| `version` | string | — | `latest` | `latest` | Dated pinned releases are planned, not yet published. |

## Resolution Tiers

| Tier | Approx. area | Use |
|---|---|---|
| `768sq` | 768×768 (~0.6 MP) | Fast wording / layout tests |
| `1k` | ~1 MP | Default; web, app, concept passes |
| `1.5k` | ~2.25 MP | When 1k is short but 2k is overkill |
| `2k` | ~4 MP | Hero images, typography, cropping headroom |
| `4k` | ~16 MP | Approved finals only — can take minutes |

Changing resolution is a new generation. Pass the approved draft as image 1 if composition must survive.

## Grounding Guidance

| Situation | `grounding` |
|---|---|
| Fictional worlds, controlled art direction, repeatable style | `false` — search can inject unwanted visual concepts |
| Real places, current products, events, factual likeness of objects | `true` |
| Edits of your own images | usually `false` |

## Recommended Combinations

| Workflow | Ratio | Resolution | Grounding | References |
|---|---|---|---|---|
| Prompt iteration | target | `768sq` | `false` | 0–1 |
| Web / app asset | target | `1k`–`1.5k` | as needed | 0–3 |
| Editorial hero | `16:9` `3:2` `4:3` | `2k` | `false` | character/style refs |
| Poster / cover | `2:3` `3:4` `4:5` | `2k` | `false` | type/style refs |
| Cinematic widescreen | `21:9` `2:1` | `2k` | `false` | location ref |
| Vertical social | `9:16` `4:5` | `1k`–`2k` | as needed | 0–3 |
| Final print | target | `4k` | as needed | approved master first |
| Local edit | `auto` | match delivery | `false` | previous result first |

## Response & Polling

- Submit returns `id`, `polling_url` (+ optional `cost`, `input_mp`, `output_mp`).
- Poll until ready; result contains `result.sample` (signed URL, **expires ~1 hour — download immediately**), `result.prompt` (the model's expanded prompt — read it to debug), and generation duration.
- One image per task. No native output-format selector — inspect `Content-Type`.

## Not Available (do not send)

`negative_prompt` · `seed` · `guidance` · `steps` · `width` · `height` · `input_image` / `input_image_N` · `mode` · `output_format` · `output_quality` · `prompt_upsampling`

Wrapper platforms (fal.ai `blackforestlabs/flux-3/text-to-image`, Replicate `black-forest-labs/flux-3-image`) may expose `output_format`, prompt expansion, etc. Document those as platform features, not BFL syntax.

## FLUX.2 → FLUX 3 Migration

| FLUX.2 habit | FLUX 3 Image |
|---|---|
| Separate model endpoints | One `/v1/flux-3-image` for generate + edit |
| `input_image`, `input_image_2`… | One ordered `images` array (max 10) |
| `width`/`height` | `aspect_ratio` + `resolution` |
| `seed` for reproducibility | Removed — reuse approved outputs as references |
| `guidance`, `steps` | Removed |
| `negative_prompt` | Rewrite as positive descriptions |
| `output_format` | Not native |
| ~4 MP ceiling | ~16 MP at `4k` |
| Natural-language placement only | Prompt-embedded 0–1000 bounding boxes |
| Whole-image regeneration on edit | Keep / move / new / remove box rows |

FLUX.2 is not deprecated. Stay on FLUX.2 if a workflow depends on seeds, LoRAs, open weights or inference controls.
