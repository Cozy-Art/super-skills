# Grok Imagine Video 1.5 Lite — Parameters

*Verified against docs.x.ai (Video Overview, Video Generation, Image-to-Video, model page, Pricing, REST API
reference for `/v1/videos/generations`) and docs.comfy.org (GrokVideoNode), October 2026.*

**Model ID:** `grok-imagine-video-1.5-lite`
**Endpoint:** `POST https://api.x.ai/v1/videos/generations` — the same endpoint as full 1.5 and classic Grok
Video; the `model` field selects Lite.
**Pattern:** asynchronous — the POST returns a `request_id`; poll `GET /v1/videos/{request_id}` until the job
finishes, then download the video from the returned temporary URL promptly.
**Status:** tagged "New" in xAI's Video Overview (page last updated 8 October 2026). xAI has published no
separate launch announcement; partner changelogs report availability around 8 October 2026.

---

## Native request fields used by Lite

| Field | Type | Values | Default | Notes |
|---|---|---|---|---|
| `model` | string | `grok-imagine-video-1.5-lite` | — | Exact ID |
| `prompt` | string | free text | — | **Required for text-to-video.** Optional for image-to-video |
| `image` | object | `{ "url": "…" }` (public URL or base64 data URL; JPEG, PNG, WebP) or `{ "file_id": "…" }` (Files API) | none | One starting image = frame 1 |
| `duration` | integer | 1–15 | **8** | REST schema: *"Range: [1, 15]. Default: 8."* |
| `resolution` | enum | `480p`, `720p`, `1080p` | **`480p`** | Lite 1080p *"by upscaling 720p"* |
| `aspect_ratio` | enum | `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `3:2`, `2:3`, `21:9`, `5:2` | `16:9` (per the generation guide; the REST schema lists no default) | **Ignored for image-to-video** — the source image sets the ratio |
| audio off | boolean | — | audio **on** | The guide documents `generate_audio=False` (SDK) for a silent video. The field does not appear in the REST schema listing reviewed — confirm the REST name on your platform (unverified) |
| `output`, `storage_options`, `user` | objects/strings | — | — | Delivery and bookkeeping; no effect on the prompt |

### Fields Lite does not support

Present in the shared REST schema, documented only for full `grok-imagine-video-1.5`:

| Field | What it does on full 1.5 |
|---|---|
| `reference_images` | Reference-to-video: up to 14 images, 15 s, 720p |
| `reference_audios` | Up to 3 voices — a preset `voice_id` or an uploaded clip `url` (≤ 15 s) |
| `last_frame` | Pins the exact last frame (with `image`, interpolates first→last) |
| `keyframes` | Up to 4 mid-clip anchors, `timestamp_s` strictly inside the clip, 1/3-s grid |

Video **editing** and **extension** are classic `grok-imagine-video` operations, not available on either 1.5
model.

---

## Capability matrix (xAI Video Overview)

| Capability | 1.5 Lite | Full 1.5 | Classic `grok-imagine-video` |
|---|---|---|---|
| Text-to-video | Yes — 1080p upscaled from 720p | Yes — native 1080p | Yes — up to 720p |
| Image-to-video | Yes — 1080p upscaled from 720p | Yes — native 1080p | Yes — up to 720p |
| Reference images | No | Up to 14, 15 s, 720p | Up to 7, 10 s, 720p |
| Voice references | No | Up to 3 | No |
| First + last frame | No | Yes | No |
| Keyframes | No | Up to 4 | No |
| Video edit | No | No | Source up to 8.7 s |
| Video extension | No | No | Adds 2–10 s |
| Duration | 1–15 s | 1–15 s | 1–15 s |
| Audio | Native, lip-synced speech | Native, lip-synced speech | Generated audio |

---

## Pricing (docs.x.ai/developers/pricing)

| Resolution | Lite per second | 8 s clip | 15 s clip | Full 1.5 per second |
|---|---|---|---|---|
| 480p | $0.02 | $0.16 | $0.30 | $0.08 |
| 720p | $0.03 | $0.24 | $0.45 | $0.14 |
| 1080p | $0.14 | $1.12 | $2.10 | $0.25 |

Image input: **$0.01 per image**. Batch API is supported for video but billed at standard rates (no batch
discount). Lite 1080p costs ~4.7× Lite 720p and is an upscale — the cost argument for drafting low is real.

## Limits and regions

- Rate limit on the model page: **10 requests per second**.
- Regions: `us-east-1`, `us-west-2`.

## Errors (shared video error table)

| Code | Typical cause |
|---|---|
| `invalid_argument` | Unsupported duration, bad image, **prompt too long**, conflicting modes, moderated content |
| `permission_denied` | Key/team lacks access |
| `failed_precondition` | Operation not available for the selected model or settings (e.g. editing, extension, unsupported resolution) |
| `service_unavailable` | Video generation temporarily overloaded — retry |
| `internal_error` | Retry; contact support with the `request_id` if it persists |

Authentication, unknown-model and rate-limit errors return synchronously as standard API errors.

---

## The upsampler

The GET result's usage block documents a **prompt-rewriting (upsampler) LLM**:
`input_tokens_details.text_tokens` — *"Prompt text tokens consumed by the prompt-rewriting (upsampler) LLM"* —
plus rewritten-prompt and reasoning output tokens. Your prompt is expanded before generation; anything left
unspecified is decided by the rewrite. Whether it can be bypassed is not documented.

## Text-to-video internals

xAI: on 1.5 and 1.5 Lite, *"text-to-video uses text-to-image then image-to-video under the hood: the model
generates a first frame from your prompt"* and then animates it. Practical consequence: describe the opening
composition clearly.

---

## Wrapper differences

| Platform | ID / notes |
|---|---|
| xAI native | `grok-imagine-video-1.5-lite` |
| ComfyUI `GrokVideoNode` | Default model is Lite; duration 1–15, **default 6**; aspect options `auto`, 16:9, 4:3, 3:2, 1:1, 2:3, 3:4, 9:16 (no 21:9 / 5:2); `seed` exists but *"actual results are nondeterministic regardless of seed"* — it only forces a re-run |
| Vercel AI Gateway | `spacexai/grok-imagine-video-1.5-lite` (unverified — confirm on your platform) |
| OpenRouter | `x-ai/grok-imagine-video-1.5-lite` (unverified — confirm on your platform) |
| Runware | `xai:grok-imagine@video-1.5-lite`; default 6 s; 64,000-character wrapper prompt cap — not an xAI limit (unverified — confirm on your platform) |

Always set `duration` explicitly when moving between platforms.

---

## What has no parameter

- **`seed`** — none natively; results are nondeterministic
- **`negative_prompt`** — none
- **Frame rate, codec, CFG, motion intensity, camera-control object** — none documented
- **Prompt length ceiling** — exists (error table) but no figure is published
