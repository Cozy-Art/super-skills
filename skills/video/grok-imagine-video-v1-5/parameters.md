# Grok Imagine Video 1.5 — Parameters

All values from xAI's own documentation — the model page, the video capability pages, and the REST API
reference. Where xAI publishes nothing, this file says so.

**Model ID:** `grok-imagine-video-1.5`
**Aliases:** `grok-imagine-video-1.5-preview`, `grok-imagine-video-1.5-2026-05-30`
**Endpoint:** `POST /v1/videos/generations`
**Pattern:** async — submit, receive `request_id`, poll; output is a temporary hosted URL

> **Two audiences.** A director needs the ceilings and defaults. The parameter names and mode
> exclusivity matter to **the integration layer**, which drives the API directly.

---

## Core parameters

| Parameter | Type | Values | Default | Notes |
|---|---|---|---|---|
| `prompt` | string | — | required | Plain string. Passed through an upsampler LLM before generation |
| `duration` | integer | 1–15 | **8** | Generation only — extension has its own range |
| `resolution` | string | `480p`, `720p`, `1080p` | **`480p`** | See restrictions below |
| `aspect_ratio` | string | `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `3:2`, `2:3` | `16:9` | Image-to-video inherits the source image's ratio |
| `image` | image | — | — | Image-to-video. **Mutually exclusive with `reference_images`** |
| `reference_images` | array | — | — | Reference-to-video. **Mutually exclusive with `image`** |
| `reference_audios` | array | `[{"voice_id": "…"}]` | — | Max 3. Preset voices, not uploads |

### Defaults that are commonly reported wrong

Two values circulate incorrectly in third-party guides and are worth stating plainly:

- **Default resolution is `480p`** — xAI: *"480p — Standard definition, faster processing (default)."*
  Not 720p.
- **Default duration is 8 seconds.** Not 5, not 6.

### Resolution restrictions

| Mode | Max resolution |
|---|---|
| Text-to-video | 1080p |
| Image-to-video | 1080p |
| **Reference-to-video** | **720p** |
| Edit | 720p (and inherits from source) |

**1080p is a 1.5-only capability** for text-to-video and image-to-video. Using reference images costs
you the top tier — a real trade-off to weigh when identity binding is optional.

### Aspect ratio in image-to-video

The output inherits the source image's aspect ratio. **Overriding it stretches the image** rather than
cropping or letterboxing. Match the source, or accept distortion.

---

## Mode exclusivity

The five modes run on the **same endpoint**, selected by which inputs are present. Reference-to-video is
not a separate API surface, despite claims otherwise.

**`image` and `reference_images` cannot both be present** — the request returns 400.

| Mode | Inputs |
|---|---|
| Text-to-video | `prompt` |
| Image-to-video | `prompt` + `image` |
| Reference-to-video | `prompt` + `reference_images` and/or `reference_audios` |
| Edit | source video + `prompt` |
| Extend | source video + `prompt` + `duration` |

---

## Extension

`POST /v1/videos/extensions`

| Parameter | Range | Default |
|---|---|---|
| `duration` | **2–10** | **6** |

**Narrower than the generation range**, and easy to miss.

**`duration` is the portion ADDED, not the total.** xAI: *"if your input video is 10 seconds and you
set `duration` to 5, the returned video will be 15 seconds."*

Extension continues **from the last frame** of the input. **There is no frame-selection field** — claims
that 1.5 added explicit frame selection for extensions are unsupported by any xAI text and absent from
the endpoint schema.

---

## Editing

**Runs on the non-1.5 `grok-imagine-video` model**, so 1.5's improvements do not apply.

**Inherit-then-cap, not fixed output:**

- **Duration** — *"retains the duration of the original, which is capped at 8.7 seconds."* A 4-second
  input yields a 4-second output
- **Resolution** — *"matches the input video's resolution, capped at 720p (e.g., a 1080p input will be
  downsized to 720p)"*

---

## Audio

**Native, on by default.** xAI: *"Generated videos include an audio track by default."*

### Voice tokens

`reference_audios: [{"voice_id": "eve"}]` supplies **preset voices** from xAI's TTS roster, addressed
in the prompt as `<AUDIO_0>`, `<AUDIO_1>`, `<AUDIO_2>` — **max 3**.

**Custom voice cloning is restricted to trusted partners.** These tokens select a timbre from a fixed
roster; they do not accept an uploaded voice sample.

**There is no documented way to script what a voice says.** See `SKILL.md`.

---

## What has no parameter

- **`seed`** — does not exist. Seed-locked reproducibility is unavailable on this model
- **`negative_prompt`** — does not exist. Whether in-prompt negation works is undocumented
- **Frame selection for extension** — does not exist
- **Custom voice upload** — trusted partners only

---

## What xAI does not publish

**Prompt length.** A ceiling exists — the REST error table lists `invalid_argument` as covering *"a
prompt that is too long"* — but **no character or token figure is published anywhere.**

No length ceiling is asserted here for that reason.

**Reference image count.** No numeric cap appears in the REST schema. xAI's own examples use three. A
figure of seven circulates in third-party guides with no basis.

---

## The upsampler

The usage schema documents a **prompt-rewriting (upsampler) LLM** that processes the prompt before
generation: `input_tokens_details.text_tokens` is described as *"Prompt text tokens consumed by the
prompt-rewriting (upsampler) LLM."*

**Implication for prompting:** a short prompt is not what the model sees. It is expanded first, by
something making its own choices about anything left unspecified. This is why claims of a short-prompt
sweet spot on this model are implausible — see `best-practices.md`.

---

## Pricing

**$0.08 per second** of output.

At the 8-second default, that is roughly $0.64 per generation. Iterating at 480p costs the same per
second as 1080p — the resolution tiers are not separately priced, so there is no cost argument for
drafting low. Time-to-result is the only saving.

---

## Rate limits and regions

Not covered in detail in the sources reviewed. Check current xAI documentation before planning a batch
workflow.
