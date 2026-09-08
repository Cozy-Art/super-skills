# Krea 2 — Parameters

All values from Krea's own documentation — the user guide, developer guide, `prompting.md` in the
open-source repo, and the OpenAPI schemas on the three model endpoints.

**Endpoints:**
`POST /generate/image/krea/krea-2/medium`
`POST /generate/image/krea/krea-2/large`
`POST /generate/image/krea/krea-2/medium-turbo`

> **Two audiences.** A director needs the ceilings and the controls. The exact field names,
> required fields and conflicting defaults matter to **the integration layer**, which drives the
> API directly — and this model has more than one trap for it.

---

## ⚠️ Three fields are required, with no defaults

All three OpenAPI schemas declare:

```
required: [prompt, aspect_ratio, resolution]
```

**Omitting `aspect_ratio` or `resolution` returns 400.** There are no server-side defaults for them.

This is worth stating plainly because most image APIs default both, and third-party summaries of Krea
describe them as optional. They are not.

---

## Core parameters

| Parameter | Type | Values | Default | Notes |
|---|---|---|---|---|
| `prompt` | string | — | **required** | Unconstrained length in the schema |
| `aspect_ratio` | string | 8 options — see below | **required** | |
| `resolution` | string | **`1K` only** | **required** | Hosted API enum is literally `[1K]` |
| `creativity` | string | `raw`, `low`, `medium`, `high` | **disputed** — see below | |
| `intensity` | integer | −100 … 100 | `0` | Lowercase field name |
| `complexity` | integer | −100 … 100 | `0` | |
| `movement` | integer | −100 … 100 | `0` | |
| `image_url` | string | — | — | **Image-to-image. Medium and Large only** |
| `strength` | number | 0 – 1 | `0.99` | Image-to-image. 0 keeps input, 1 fully replaces |
| `image_style_references` | array | `[{url, strength}]` | — | **maxItems: 10** |
| `moodboards` | array | `[{id, strength}]` | — | **maxItems: 1** |
| `styles` | array | `[{id, strength}]` | — | Trained LoRAs |

`additionalProperties: false` — unknown fields are rejected rather than ignored.

---

## Where Krea's own pages conflict

Two genuine first-party contradictions. Recorded rather than silently resolved.

### 1. `creativity` default — `medium` or `low`?

| Source | Says |
|---|---|
| User guide | `medium (default)` |
| Developer overview table | `medium (default)` |
| **OpenAPI schema, all three endpoints** | **`default: low`** |

**Do not ship "medium" as the API default without testing.** Set `creativity` explicitly and the
question doesn't arise.

### 2. Style-reference `strength` range — 0–1 or −2 to 2?

| Source | Says |
|---|---|
| **OpenAPI schema** | **`minimum: 0, maximum: 1, default: 0.5`** |
| Style-transfer prose page | *"Set `strength` between -2 and 2 per reference"* |

The −2…2 range is what the schema actually assigns to **`styles`** (LoRAs), not to
`image_style_references`. The prose page appears to have copied the wrong range.

**Trust the schema: 0–1, default 0.5.**

### Moodboard strength — same shape of conflict

| Source | Says |
|---|---|
| **OpenAPI schema** | **`minimum: 0, maximum: 1, default: 0.23`** |
| Moodboards prose page | *"a `strength` between -0.5 and 1.5 … Start around 0.35"* |

**Use 0–1, default 0.23.**

---

## Aspect ratios

Eight options, each with fixed pixel dimensions at 1K. Notable inclusion: **`2.35:1` → 1568×672**, a
genuine anamorphic ratio.

---

## Resolution

**Hosted API: `1K` only.** The enum contains one value.

**Open-source Turbo checkpoint: up to 2K.** From `prompting.md`: *"The turbo model can generate up to
2k resolution images."* That applies to the downloadable weights, not the hosted endpoints.

If output above 1K is needed from the hosted API, it isn't available — that is a routing decision.

---

## Tiers and pricing

| Tier | Pricing | Image-to-image | Speed |
|---|---|---|---|
| **Medium Turbo** | $0.015 / $0.0175 / $0.02 | ✗ | **~4 seconds** |
| **Medium** | $0.030 / $0.035 / $0.040 | ✓ | Standard |
| **Large** | $0.060 / $0.065 / $0.070 | ✓ | Slower |

The three prices per tier correspond to increasing option use. **Moodboard and style-reference costs do
not stack** — using both does not compound the price.

**Turbo is ~4 seconds per generation**, first-party. A "~2 seconds" figure circulates and is not Krea's.

---

## Reference attachments

| Attachment | Max | Strength | Bound by |
|---|---|---|---|
| `image_style_references` | **10** (API) — the UI shows **4** | 0–1, default 0.5 | URL |
| `moodboards` | **1** | 0–1, default 0.23 | UUID |
| `styles` | — | −2 … 2 | UUID (trained LoRA) |

The **4-image limit is a UI constraint**, not an API one. A figure of 5 circulates with no basis.

---

## What has no parameter

- **`negative_prompt`** — does not exist. Confirmed by absence plus `additionalProperties: false`
- **Batch size / `n`** — does not exist. The "up to 4 images per generation" figure is UI-only
- **`seed`** — not present in the reviewed schema
- **Guidance scale / inference steps** — not exposed on the hosted API. Step and CFG values that
  circulate (28 steps @ 4.5, 8 steps @ 0.0) come from the **diffusers** documentation for the
  open-source checkpoints and are irrelevant to the hosted endpoints
- **In-prompt reference syntax** — see `SKILL.md`. There is none

---

## Prompt length

**Krea publishes no character or token limit.** The `prompt` field is an unconstrained string in the
OpenAPI schema, and no cap appears in the user guide, developer guide or `prompting.md`.

No length ceiling is asserted here for that reason.

Krea's own guidance on length: *"long detailed prompts yield best results, but the model is capable of
generating high quality images with minimal prompt engineering."* Both ends of the range work.

---

## Deprecated field aliases — already expired

| Old | New | Accepted until |
|---|---|---|
| `presetStyles` | `styles` | **2026-06-19** |
| `imageStyleRefs` | `image_style_references` | **2026-06-19** |

Both windows closed before this skill was written. **Any legacy tooling still sending camelCase will
now receive a 400.** Worth checking if an integration was written against older Krea documentation.

---

## Open weights

Two checkpoints published on Hugging Face (`krea/Krea-2-Raw`) and GitHub (`krea-ai/krea-2`):

- **RAW** — the undistilled base checkpoint
- **Turbo** — an 8-step distilled checkpoint, up to 2K resolution

The hosted tiers and the open checkpoints are not the same thing; parameters exposed by diffusers on
the open weights (steps, CFG) have no hosted-API equivalent.

---

## Architecture

Single-stream DiT with GQA and gated sigmoid attention, SwiGLU, zero-centre RMSNorm, 3D axial RoPE.
Text encoder is **Qwen 3 VL**; VAE from **Qwen Image**, autoencoder from **FLUX 2**.

Confirmed by Krea's own technical report ablation table. A "12-billion-parameter" figure circulates
from a third-party source and was not confirmed — it is not stated in the report sections reviewed.
