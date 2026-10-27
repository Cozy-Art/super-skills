# Grok Imagine Video 1.5 — Parameters

All values from xAI's own documentation — the model page, the video capability pages, and the REST API
reference. Where xAI publishes nothing, this file says so.

*Re-verified against docs.x.ai video overview, generation, image-to-video, reference-to-video and
extension pages, the pricing page and the REST videos reference, 19 October 2026.*

**Model ID:** `grok-imagine-video-1.5`
**Aliases:** `grok-imagine-video-1.5-preview`, `grok-imagine-video-1.5-2026-05-30`
**Endpoint:** `POST /v1/videos/generations`
**Pattern:** async — submit, receive `request_id`, poll; output is a temporary hosted URL

> **Two audiences.** A director needs the ceilings and defaults. The parameter names and how inputs
> combine matter to **the integration layer**, which drives the API directly.

---

## Core parameters

| Parameter | Type | Values | Default | Notes |
|---|---|---|---|---|
| `prompt` | string | — | required for T2V / R2V | Plain string. Passed through an upsampler LLM before generation. Optional for image-to-video and whenever a frame is pinned |
| `duration` | integer | 1–15 | **8** | Generation only — extension has its own range. `seconds` accepted as an alias |
| `resolution` | string | `480p`, `720p`, `1080p` | **`480p`** | See restrictions below |
| `aspect_ratio` | string | `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `3:2`, `2:3`, `21:9`, `5:2` | `16:9` | Ignored in image-to-video |
| `image` | object (`url` or `file_id`) | JPEG, PNG, WebP | — | First frame. Alone = image-to-video; with other inputs = pinned first frame in reference-to-video |
| `last_frame` | image | — | — | Pins the exact last frame. 1.5 only |
| `keyframes` | array of `{image, timestamp_s}` | **max 4** | — | `timestamp_s` strictly between 0 and `duration`, snapped to a 1/3-second grid. 1.5 only |
| `reference_images` | array (`url` or `file_id`) | **max 14** on 1.5 | — | Reference-to-video. Tokens `<IMAGE_0>`… |
| `reference_audios` | array of `{voice_id}` or `{url}` | **max 3** | — | Preset voice, or an audio clip ≤ 15 s (access-gated — see Audio). Tokens `<AUDIO_0>`… |

### Defaults that are commonly reported wrong

- **Default resolution is `480p`** — xAI: *"480p — Standard definition, faster processing (default)."*
  Not 720p.
- **Default duration is 8 seconds.** Not 5, not 6.

### Resolution restrictions

| Mode | Max resolution |
|---|---|
| Text-to-video | 1080p (native) |
| Image-to-video | 1080p (native) |
| **Reference-to-video** (any of references, voices, last frame, keyframes) | **720p**, up to 15 s |
| Edit (classic model) | 720p (and inherits from source) |

**Native 1080p is a 1.5 capability** for text-to-video and image-to-video (1.5 Lite reaches 1080p only
by upscaling 720p). Using any reference-to-video input costs you the top tier — a real trade-off to
weigh when identity binding is optional.

### Aspect ratio in image-to-video

xAI: *"The output always matches the still's aspect ratio; `aspect_ratio` is ignored."* Crop the source
image to the delivery ratio before generating.

---

## How inputs combine into modes

The modes run on the **same endpoint**, selected by which inputs are present. On 1.5 they combine
rather than exclude each other.

| Mode | Inputs |
|---|---|
| Text-to-video | `prompt` |
| Image-to-video | `prompt` (optional) + `image` alone |
| Reference-to-video | `prompt` + any of `reference_images`, `reference_audios`, `last_frame`, `keyframes` — optionally with `image` as the pinned first frame |
| Edit (classic model) | source video + `prompt` |
| Extend (classic model) | source video + `prompt` + `duration` |

Audio references alone are enough to select reference-to-video — `reference_images` is not required.

**Token numbering with a pinned first frame:** the `image` takes `<IMAGE_0>` and reference images start
at `<IMAGE_1>`. Without a pinned first frame, the first reference image is `<IMAGE_0>`.

Earlier versions of this skill stated that `image` and `reference_images` together return 400. Current
xAI docs describe the combination as a first-frame pin on 1.5. Some hosted routes still disallow
references with a start frame — check your interface.

---

## Pinned frames

- **`image`** — first frame
- **`last_frame`** — *"pins the exact last frame of the clip"*; the video ends arriving on that image
- **`keyframes`** — *"At most 4 keyframes per request."* Each `timestamp_s` must be *"greater than 0 and
  less than `duration`"*; anchors snap to a 1/3-second grid, and two that round to the same slot are
  rejected
- **Loop** — *"To loop a clip, pass the same image as `image` and `last_frame`."*

Classic `grok-imagine-video` *"still rejects `last_frame` and `keyframes`."*

---

## Extension

`POST /v1/videos/extensions` — **runs on classic `grok-imagine-video`**, not 1.5 (xAI's capability
table marks extension "Not supported" on 1.5). A 1.5 clip can be the source.

| Parameter | Range | Default |
|---|---|---|
| `duration` | **2–10** | **6** |
| Source video length | 2–15 s | — |

**`duration` is the portion ADDED, not the total.** xAI: *"if your input video is 10 seconds and you
set `duration` to 5, the returned video will be 15 seconds."*

Extension continues **from the last frame** of the input. **There is no frame-selection field.**

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

**Native, on by default.** xAI: *"Generated videos include an audio track by default."* The xAI SDK
turns it off with `generate_audio=False`; that field does not appear in the REST request schema
reviewed *(unverified REST name — confirm on your platform)*.

### Speech

1.5 *"generates lip-synced speech."* xAI's examples write lines as speaker + quoted text —
`Sam: "I took the job in Berlin. We could leave in March."`, `She says: "Welcome to my dream living
room."` Example usage, not a documented rule.

### Voice tokens

`reference_audios` entries take **either** `voice_id` **or** `url`, not both — **max 3**, addressed as
`<AUDIO_0>`, `<AUDIO_1>`, `<AUDIO_2>`.

- **`voice_id`** — a preset voice from xAI's TTS roster (e.g. `eve`, `ara`, `ursa`), case-insensitive.
  An unknown ID returns 400 with the list of available voices
- **`url`** — base64 data URL or http(s) link to an audio clip of at most 15 seconds. xAI's guide:
  *"voice references with your own audio files are available to trusted partners"* on request. The
  field exists in the schema; access depends on your account

---

## What has no parameter

- **`seed`** — does not exist. Seed-locked reproducibility is unavailable on this model
- **`negative_prompt`** — does not exist. Whether in-prompt negation works is undocumented
- **Frame selection for extension** — does not exist

---

## What xAI does not publish

**Prompt length.** A ceiling exists — the error table lists `invalid_argument` as covering *"a prompt
that is too long"* — but **no character or token figure is published anywhere.**

No length ceiling is asserted here for that reason.

**The full preset voice roster** is not enumerated on the video pages; an invalid `voice_id` returns
the list.

---

## The upsampler

The usage schema documents a **prompt-rewriting (upsampler) LLM** that processes the prompt before
generation: `input_tokens_details.text_tokens` is described as *"Prompt text tokens consumed by the
prompt-rewriting (upsampler) LLM,"* and `output_tokens` as *"rewritten-prompt text tokens + reasoning
tokens."*

**Implication for prompting:** a short prompt is not what the model sees. It is expanded first, by
something making its own choices about anything left unspecified. This is why claims of a short-prompt
sweet spot on this model are implausible — see `best-practices.md`.

---

## Pricing

Per second of output, **by resolution** (xAI pricing page):

| Resolution | Price / second | 8 s default |
|---|---|---|
| 480p | $0.08 | $0.64 |
| 720p | $0.14 | $1.12 |
| 1080p | $0.25 | $2.00 |

Plus **$0.01 per input image** (listed as media input on the pricing page).

Drafting at 480p is now both faster *and* cheaper — 1080p costs about 3× a 480p draft.

---

## Rate limits and regions

Not covered in detail in the sources reviewed. Check current xAI documentation before planning a batch
workflow.
