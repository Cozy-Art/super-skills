# LTX-2.3 — Parameters

Native API base: `https://api.ltx.io` (legacy `https://api.ltx.video` still works) · header `Authorization: Bearer <API key>` · `Content-Type: application/json`.

*Verified against docs.ltx.io (API reference, Supported Models / LTX-2.3 page, Pricing, Input Formats, API changelog), the Lightricks/LTX-2.3 Hugging Face model card and the LTX PyTorch API docs, October 2026.*

## V1 vs V2

| | V1 (`/v1/...`) | V2 (`/v2/...`) |
|---|---|---|
| Behaviour | Synchronous — response body is the MP4 | Async — `202` returns `{id, created_at}` |
| Status | Deprecated; **stops working after 26 Oct 2026, 23:59 UTC** | Current |
| Result | Saved from response | Poll `GET /v2/<endpoint>/{id}` until `completed`, download `result.video_url` |

Same auth, parameters and pricing on both. Build everything new on V2. Download results immediately rather than relying on the URL lasting (expiry not documented).

## Models

| Model ID | T2V | I2V | Audio-to-video | Retake | Extend |
|---|---|---|---|---|---|
| `ltx-2-3-pro` | ✅ | ✅ | ✅ | ✅ | ✅ |
| `ltx-2-3-fast` | ✅ | ✅ | — | — | — |
| `ltx-2-5-pro` / `ltx-2-5-fast` (newer family) | ✅ | ✅ | ✅ | — | — |

LTX-2 IDs `ltx-2-pro` / `ltx-2-fast` were removed 16 Aug 2026 and now return errors.

## Resolution / FPS / Duration Matrix (T2V and I2V)

Resolution is a `WIDTHxHEIGHT` string. Only 16:9 and 9:16 — orientation comes from the string; there is no `aspect_ratio` field.

| Tier | Landscape | Portrait |
|---|---|---|
| 720p | `1280x720` | `720x1280` |
| 1080p | `1920x1080` | `1080x1920` |
| 1440p | `2560x1440` | `1440x2560` |
| 4K | `3840x2160` | `2160x3840` |

| Model | Resolution | FPS | Durations (s) |
|---|---|---|---|
| `ltx-2-3-pro` | all tiers | 24, 25, 48, 50 | 6, 8, 10 |
| `ltx-2-3-fast` | 720p, 1080p | 24, 25 | 6, 8, 10, 12, 14, 16, 18, 20 |
| `ltx-2-3-fast` | 720p, 1080p | 48, 50 | 6, 8, 10 |
| `ltx-2-3-fast` | 1440p, 4K | 24, 25, 48, 50 | 6, 8, 10 |

## Text-to-Video — `POST /v2/text-to-video`

| Field | Type | Req | Default | Values / notes |
|---|---|---|---|---|
| `prompt` | string | ✅ | — | ≤ 5,000 chars |
| `model` | enum | ✅ | — | `ltx-2-3-pro`, `ltx-2-3-fast` (also `ltx-2-5-*`) |
| `duration` | integer | ✅ | — | from matrix. (`null` = auto length, LTX-2.5 only) |
| `resolution` | string | ✅ | — | from matrix |
| `fps` | integer | — | `24` | from matrix |
| `generate_audio` | boolean | — | `true` | `false` = silent video |
| `camera_motion` | enum | — | none | `dolly_in` `dolly_out` `dolly_left` `dolly_right` `jib_up` `jib_down` `static` `focus_shift` |

## Image-to-Video — `POST /v2/image-to-video`

All T2V fields, plus:

| Field | Type | Req | Notes |
|---|---|---|---|
| `image_uri` | string | ✅ | First frame. HTTPS URL, data URI, or LTX cloud-storage URI |
| `last_frame_uri` | string | — | Last frame; video interpolates between the two. Not combinable with `duration: null` |

## Audio-to-Video — `POST /v2/audio-to-video` (Pro only on 2.3)

| Field | Type | Req | Default | Notes |
|---|---|---|---|---|
| `audio_uri` | string | ✅ | — | Its length sets the video length |
| `image_uri` | string | one of | — | First frame. Required if no `prompt` |
| `prompt` | string | one of | — | ≤ 5,000 chars. Required if no `image_uri`; may be `""` with an image |
| `resolution` | string | — | auto | Omitted: follows image orientation (1920x1080 / 1080x1920), else 1920x1080 |
| `model` | enum | — | `ltx-2-3-pro` | |
| `fps` | integer | — | `24` | |
| `last_frame_uri` | string | — | — | Requires `image_uri` |
| `camera_motion` | enum | — | — | same 8 values |

Max input audio on `ltx-2-3-pro`: **20 s at 720p/1080p, 10 s at 1440p/4K**. No `duration` or `generate_audio` field.

## Retake — `POST /v2/retake` (Pro only)

| Field | Type | Req | Default | Values / notes |
|---|---|---|---|---|
| `video_uri` | string | ✅ | — | ≤ 3840x2160, ≥ 73 frames (~3 s at 24 fps) |
| `start_time` | number | ✅ | — | ≥ 0 seconds |
| `duration` | number | ✅ | — | ≥ 2 seconds; clamped to clip end |
| `prompt` | string | — | — | ≤ 5,000 chars — describe the replacement section |
| `mode` | enum | — | `replace_audio_and_video` | `replace_audio`, `replace_video`, `replace_audio_and_video` |
| `resolution` | enum | — | from orientation | `1920x1080` or `1080x1920` only |
| `model` | enum | — | `ltx-2-3-pro` | |

## Extend — `POST /v2/extend` (Pro only)

| Field | Type | Req | Default | Values / notes |
|---|---|---|---|---|
| `video_uri` | string | ✅ | — | 16:9 or 9:16, ≤ 4K, ≥ 73 frames; ≤ 100 MB |
| `duration` | number | ✅ | — | 2–20 s of new material |
| `prompt` | string | — | — | ≤ 5,000 chars — describe what happens next |
| `mode` | enum | — | `end` | `end` (continue forward) or `start` (generate a lead-in) |
| `context` | number | — | auto (max) | 1–20 s of source used as context |
| `model` | enum | — | `ltx-2-3-pro` | |

`context + duration` ≤ **505 frames** at the input's fps (~21 s at 24 fps; less at 48/50). Output keeps the input resolution; audio continues with the video (no audio field).

## Input Formats & Limits

| | Formats |
|---|---|
| Images | PNG, JPEG, WebP |
| Video | MP4, MOV, MKV — H.264 / H.265 |
| Audio | WAV (AAC-LC/MP3/Vorbis/FLAC inside), MP3, M4A (AAC-LC), OGG (Opus/Vorbis). **No PCM, no HE-AAC** — a plain PCM .wav is rejected |

| Method | Images | Video | Audio |
|---|---|---|---|
| HTTPS URL | 15 MB (10 s timeout) | 32 MB (30 s) | 32 MB (30 s) |
| Data URI (encoded size) | 7 MB | 15 MB | 15 MB |
| LTX cloud storage upload | 200 MB | 200 MB (extend: 100 MB) | 200 MB |

## Pricing (USD per second of output, Oct 2026)

| Resolution | Fast T2V/I2V | Pro T2V/I2V | Pro audio-to-video* |
|---|---|---|---|
| 720p | $0.03 | $0.04 | $0.06 |
| 1080p | $0.06 | $0.08 | $0.10 |
| 1440p | $0.12 | $0.16 | $0.18 |
| 4K | $0.24 | $0.32 | $0.34 |

\*Billed on input audio length. Retake $0.10/s (billed on input video length) and extend $0.10/s (capped at 505 billed frames), both at 1080p. Example: 8 s Pro 4K = $2.56; 8 s Fast 1080p draft = $0.48.

## Recommended Combinations

| Workflow | Model | Resolution | FPS | Duration | Notes |
|---|---|---|---|---|---|
| Storyboard / blocking test | Fast | 720p or 1080p | 24 | 6 | cheapest validation |
| Final cinematic shot | Pro | 1440p / 4K | 24 | 8–10 | I2V from approved frame if identity matters |
| Sports / fast action | Pro | 1080p / 1440p | 48 or 50 | 6–8 | smoother sampling, not more action |
| Vertical social | Pro or Fast | 1080x1920 | 24/25 | 6–10 | native portrait — don't crop landscape |
| Long single take | Fast | 1080p | 24/25 | 12–20 | one continuous action only |
| Product reveal | Pro | 4K | 24 | 6–8 | I2V + optional `last_frame_uri` |
| Music video beat | Pro A2V | 1080p | 24 | = audio (≤ 20 s) | image_uri for identity |
| PAL / broadcast | either | target | 25 / 50 | — | |

## Wrapper Field Maps (platform-specific, not native)

| Platform | Notable differences |
|---|---|
| Replicate `lightricks/ltx-2.3-pro` / `-fast` | `task` (`text_to_video`, `image_to_video`, `audio_to_video`, `retake`, `extend`), `image`, `last_frame_image`, `audio`, `video`; `resolution` = `1080p`/`2k`/`4k` (A2V/retake/extend 1080p only); separate `aspect_ratio` `16:9`/`9:16`; **fps default 25**; `camera_motion` adds `none` (default); `retake_start_time`, `retake_duration`, `retake_mode`, `extend_mode` |
| Leonardo | `ltxv-2.3-pro` / `ltxv-2.3-fast`, `prompt_enhance`, start/end frames under `guidances` (unverified — confirm on your platform) |
| Runware | `positivePrompt`, optional `negativePrompt`, `CFGScale`, steps (unverified — confirm on your platform) |
| MachGen | seed + prompt enhancement exposed; reported 16:9 / 24 fps grid (unverified — check its model list) |

Seeds, negative prompts and prompt enhancers on wrappers are **provider features**. The native API has none of them, and the official guide says the prompt enhancer applies only to local open-source paths.

## Open Weights (local / ComfyUI)

Checkpoints: `ltx-2.3-22b-dev` (full, trainable, bf16) · `ltx-2.3-22b-distilled` and `-distilled-1.1` (8 steps, CFG 1; 1.1 = different aesthetic, better audio) · distilled LoRAs (`-distilled-lora-384`, `-1.1`) · spatial upscalers x2 (1.1) and x1.5 · temporal upscaler x2. License: LTX-2 Community License.

| Control | Full (dev) | Distilled | Notes |
|---|---|---|---|
| Steps | 20–50 | 4–8 (designed for 8) | |
| `cfg_scale` | 2.0–5.0 (start 3.0–3.5) | **1.0** | raising distilled CFG → oversaturation/distortion |
| `stg_scale` | 0.5–1.5 (0 = off) | workflow-baked | temporal coherence |
| `stg_blocks` | e.g. `[28]` (`[]` = off) | — | |
| `rescale_scale` | ~0.7 | — | tames CFG oversaturation |
| `modality_scale` | 1.0–3.0 | — | >1 when audio sync matters |
| Width / height | divisible by 32 | same | defaults like 768×512, 512×768, 640×640 |
| Frames | `8n + 1` | same | 65 ≈ 2.7 s, 97 ≈ 4.0 s, 121 ≈ 5.0 s, 161 ≈ 6.7 s, 257 ≈ 10.7 s @ 24 fps |
| Seed | integer | integer | reproducible only on the same checkpoint/settings |

HQ pipeline: two-stage — base checkpoint + distilled LoRA at ~0.8 + spatial upscaler. The official ComfyUI two-stage distilled template: 960×544 base → x2 → ~1920×1088, 121 frames @ 24 fps, 8 + 3 steps, CFG 1. Negative prompt (local only) ships as `pc game, console game, video game, cartoon, childish, ugly` — edit it for observed failures, don't pile on.

## Migration

| From | To |
|---|---|
| `ltx-2-pro` / `ltx-2-fast` | `ltx-2-3-pro` / `ltx-2-3-fast` |
| `/v1/<endpoint>` sync | `/v2/<endpoint>` async + poll |
| `api.ltx.video` | `api.ltx.io` (old host still works) |
| LTX-2 LoRAs | retrain on the 2.3 latent space — they don't transfer |
| LTX-2 seed baselines | re-establish; seeds don't carry across versions |
| 25/50-only habits | 24/48 now available alongside 25/50 |
