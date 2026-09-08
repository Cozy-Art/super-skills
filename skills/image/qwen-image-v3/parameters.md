# Qwen-Image-3.0 — Parameters

All values from Alibaba Cloud Model Studio's **Qwen Image Generation and Editing 3.0 API Reference**
(last updated 20 July 2026).

> ⚠️ **Most published parameter tables for this model are wrong** — they describe a third-party
> aggregator's API surface, not Alibaba's. Field names in particular are completely different. See the
> comparison at the end of this file.

**Model:** `qwen-image-3.0-pro` — *"The currently available model is `qwen-image-3.0-pro`."* **One
variant, not two.** A base/pro split circulates, sourced to a domain that is not Alibaba's.

**Endpoint:** `POST .../api/v1/services/aigc/multimodal-generation/generation`

**Status: limited preview.** Access requires application via the Model Gallery.

---

## Request shape

The prompt is **not** a top-level field. It is a `text` object inside the message content array:

```
input.messages[0].content = [ {"text": "…"} ]                    ← text-to-image
input.messages[0].content = [ {"text": "…"}, {"image": "…"} ]    ← editing / fusion
```

### ⚠️ Exactly one text object

> *"Contains only one `{"text": "..."}` object. … **Only one text object is allowed. Omitting it or
> providing multiple text objects will result in an error.**"*

There is **no field called `prompt`.** Everything goes in one string.

### Reference images

1–3 `{"image": "…"}` objects. **Binding is positional:** *"When multiple images are provided, the order
is defined by the array sequence."*

---

## The complete `parameters` object

This is all of it. Six fields.

| Parameter | Type | Range / values | Default | Notes |
|---|---|---|---|---|
| `prompt_extend` | boolean | — | **`true`** | Rewrites and expands the prompt before generation. **Breaks seed reproducibility** |
| `negative_prompt` | string | — | — | **A real, working negative prompt** |
| `n` | integer | 1–6 | `1` | Output count |
| `size` | string | `"width*height"` | **none** | e.g. `"1024*1024"`. Not integers |
| `seed` | integer | 0 – 2,147,483,647 | — | Only meaningful with `prompt_extend: false` |
| `watermark` | boolean | — | `false` | |

**Nothing else exists.** See "Parameters that do not exist" below.

### `size` — a string, and there is no default

`"1024*1024"` — a `width*height` **string**, not separate integer fields.

**Total pixels must be between 512×512 and 2048×2048.** The same range applies to **both** text-to-image
and image editing — there is no reduced budget when references are supplied.

**No fixed default.** *"If not specified, the model automatically recommends a resolution based on the
prompt."*

### `prompt_extend` — the most consequential default

**Defaults to `true`, and Alibaba recommends it.**

The prompt is rewritten and expanded by a language model before generation. Two consequences worth
stating plainly:

1. **Seed reproducibility does not work with it on.** A fixed seed only reproduces if the prompt
   reaching the model is identical, and expansion regenerates it each run.
2. **Anything unstated is decided by the expander.** Specificity constrains the rewrite.

---

## Input and output specifications

**Input images:** JPG, JPEG, PNG, BMP, TIFF, WEBP, GIF. **384–2048 px per side, ≤10 MB.**

**Output:** **PNG.** Download URL valid **24 hours**.

---

## Parameters that do not exist

Frequently attributed to this model and **absent from Alibaba's API**:

- **`guidance_scale` / CFG** — does not exist
- **`steps` / inference steps** — does not exist
- **`width` and `height` as integers** — it is a single `size` string
- **`positivePrompt` / `negativePrompt` / `promptExtend` (camelCase)** — these are a third-party
  aggregator's field names
- **`inputs.referenceImages`** — same
- **`@Image1` / `<IMAGE_1>`-style tokens** — those belong to other models. Qwen uses bare numbers
  (`image 1`) or square brackets (`[image 1]`), documented in the editing guide

The CFG and step values that circulate (guidance 4.0–5.0, 40–50 steps) come from **open-weight
Qwen-Image v1 / 2512 guides** — different, earlier, open models. Sending them here produces errors or
is silently ignored.

---

## Prompt length — the headline number is unconfirmed

A **~4,500 token** prompt limit is very widely quoted for this model, usually alongside "up from ~1,000
in Qwen-Image-2.0."

**It does not appear anywhere in Alibaba Cloud Model Studio's API reference** — the only first-party
document that could be retrieved. Every instance traces back to Qwen's launch post *as relayed by third
parties*.

No length ceiling is asserted here for that reason.

The **capability** — long, brief-style prompts with dense layout instructions — is real and consistent
with how the model is positioned. The **number** should not be encoded as spec.

---

## Unverified capability claims

All from launch materials relayed through third parties. Real capabilities, unconfirmed specifics:

- **12-language text rendering**
- **20+ fonts**
- **100+ styles**
- **~10 px minimum legible text size**

**The status caveat still holds as of August 2026:** no open weights, no technical report, no model
card, no independent benchmarks. A search of the Qwen Hugging Face org returns no 3.0 repository — only
`Qwen/Qwen-Image` and `Qwen-Image-Edit-2511` plus community forks.

Do not quote these figures as specification. Say the model does multilingual text rendering well; do not
say it does twelve languages at ten pixels.

---

## Text rendering convention

Wrapping exact on-image copy in double quotes is the standard technique and it works.

**But for 3.0 specifically it is documented by a third-party platform, not by Alibaba.** Alibaba's API
reference says nothing about quoting.

Contrast Krea 2, where the same convention **is** vendor-documented. Worth keeping the
distinction straight when advising.

---

## What the widely published field names got wrong

Recorded because the error is systematic rather than incidental: an entire parameter table was taken
from **Runware**, an aggregator, and presented as Alibaba's.

| Widely published (Runware) | Actual (Alibaba) |
|---|---|
| `positivePrompt` | `{"text": "…"}` in `input.messages[0].content` — **no field named `prompt`** |
| `negativePrompt` | `parameters.negative_prompt` |
| `promptExtend` | `parameters.prompt_extend` |
| `inputs.referenceImages` | `{"image": "…"}` objects in the same content array |
| `width` + `height` integers | `parameters.size` as a `"width*height"` string |
| Pixel budget to 6,553,600 | **512×512 to 2048×2048** |
| Budget drops to 2,250,000 with references | **No drop.** Same range for T2I and I2I |
| Default 1024×1024 | **No default** — model recommends from the prompt |
| — *(omitted)* | `parameters.watermark`, boolean, default `false` |

The 6,553,600 / 2,250,000 figures and the "Invalid image pixels" error string are **Runware platform
limits**, not the model's.
