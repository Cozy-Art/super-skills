# Sonilo — Parameters

Native API: `https://api.sonilo.com/v1/<endpoint>` · header `Authorization: Bearer <SONILO_API_KEY>` (keys look like `sk_...`; keep server-side) · body `multipart/form-data` (`curl -F`).
Current music model: **Sonilo v1.1** (June 2026; v1.0 March 2026). SFX: **Sound Effects 1.0** (July 2026). No `model`/`version` field — the endpoint selects the model.

*Verified against sonilo.com/openapi.json, platform.sonilo.com/openapi.json, platform.sonilo.com/docs (text-to-sfx, video-to-sfx), sonilo.com/pricing, sonilo.com/news/sonilo-v1-1, github.com/sonilo-ai/sonilo-mcp, ComfyUI nodes_sonilo.py and fal.ai sonilo/v1.1 docs, October 2026.*

## Endpoints

| Method + path | Returns | Sync? |
|---|---|---|
| `POST /v1/text-to-music` | audio | stream (default) or async |
| `POST /v1/video-to-music` | audio | stream (default) or async |
| `POST /v1/video-to-video-music` | MP4 with score muxed | async only |
| `POST /v1/text-to-sfx` | audio | async only |
| `POST /v1/video-to-sfx` | audio | async only |
| `POST /v1/video-to-video-sfx` | MP4 with SFX muxed | async only |
| `POST /v1/video-to-sound` | combined music+SFX audio (+ components) | async |
| `POST /v1/video-to-video-sound` | MP4 with combined mix | async |
| `POST /v1/video-analysis` | music / sound-design brief | async |
| `POST /v1/audio-ducking` | voice-over-music mix | async only (202) |
| `POST /v1/proofread`, `/v1/dubbing` | .srt / dubbed media | not prompt work |
| `GET /v1/tasks/{task_id}` | task status + result | poll every 2–5 s |
| `GET /v1/account/services`, `/v1/account/usage?days=1–365` | limits, usage | — |

There is **no** `/v1/vocal-isolation` route — use `preserve_speech` or `audio-ducking`.

## Music Fields

### `text-to-music`

| Field | Type | Values | Default | Notes |
|---|---|---|---|---|
| `prompt` | string | 1–2,000 chars (ComfyUI enforces 1–1,000) | — | **Required.** Stay ≤1,000 for portability. |
| `duration` | integer | 5–360 s | — | Required in core spec; MCP/ComfyUI accept from 1 s. Always send it. Billing minimum is 15 s. |
| `segments` | string (JSON) | array of `{start, end, prompt?}` | none | Timeline structure inside one track. |
| `mode` | enum | `stream` · `async` | `stream` | Stream returns M4A as it generates. |
| `output_format` | enum | `m4a` · `wav` · `mp3` | `m4a` | `wav`/`mp3` require `async`. |
| `variants_num` | integer | 1–10 | 1 | >1 requires `async`; billed linearly. |
| `stems` | boolean | — | false | Requires `async`. (unverified — listed in platform OpenAPI, but sonilo.com/docs says stems are not offered; confirm on your account.) |

### `video-to-music` / `video-to-video-music`

| Field | Type | Values | Default | Notes |
|---|---|---|---|---|
| `video` / `video_url` | file / URI | exactly one | — | Real video stream required. |
| `prompt` | string | ≤2,000 chars | auto from video | Optional; keep short. |
| `segments` | string (JSON) | see below | none | Per-scene direction. |
| `prompt_influence` | number | 0–1 | 0.5 | Low = footage leads; high = literal prompt. **Only these two endpoints.** |
| `mode` | enum | `stream` · `async` | `stream` | video-to-music only; video-to-video is always async. |
| `output_format` | enum | `m4a` · `wav` · `mp3` | `m4a` | video-to-music only; wav/mp3 need async. |
| `variants_num` | integer | 1–10 | 1 | >1 needs async. video-to-video returns a `videos` array. |
| `preserve_speech` | boolean | — | false | Isolates source speech and keeps it over the score. Needs async. |
| `ducking` | boolean | — | false | Adds a dialogue-safe `ducked` track. Needs async. Best-effort; no effect without a voice source. |
| `keep_original_sound` | boolean | — | false | **video-to-video-music only.** Keeps the entire source soundtrack (not just speech); supersedes `preserve_speech`. |
| `isolate_vocals` | boolean | — | — | Legacy alias ORed with `preserve_speech`. Don't use in new work. |
| `stems` | boolean | — | false | video-to-music; async. (unverified — see above.) |

Video limits: 300 MB default upload; **360 s** max for video-to-music and video-to-video-music. Containers mp4 / mov / m4v / webm with H.264, H.265/HEVC, VP9 or AV1 (no GIF, no VP8). MP4/H.264 is safest. (v1.1 announcement says "up to 600 s" platform-wide — endpoint caps are lower; trust the endpoint.)

## SFX Fields

### `text-to-sfx` (always async)

| Field | Type | Values | Default | Notes |
|---|---|---|---|---|
| `prompt` | string | 1–2,000 chars | — | **Required.** |
| `duration` | integer | 1–180 s | — | Integer seconds — no sub-second. Required in core spec; send it. |
| `audio_format` | enum | `wav` · `mp3` · `aac` · `flac` | service default (AAC/.m4a in MCP) | snake_case — never `audioFormat`. |

### `video-to-sfx` / `video-to-video-sfx` (always async)

| Field | Type | Values | Notes |
|---|---|---|---|
| `video` / `video_url` | file / URI | exactly one | 300 MB default, **480 s** max. |
| `prompt` | string | ≤2,000 chars | Optional global SFX policy. |
| `segments` | string (JSON) | `{start, end, prompt?}` | Direct impacts, quiet stretches, ambience changes. |
| `audio_format` | enum | `wav` · `mp3` · `aac` · `flac` | video-to-sfx only. |

## Combined Sound Fields (`video-to-sound` / `video-to-video-sound`)

| Field | Type | Values | Default | Notes |
|---|---|---|---|---|
| `video` / `video_url` | file / URI | exactly one | — | 300 MB, 480 s. |
| `music_prompt` | string | text | — | Score brief. |
| `sfx_prompt` | string | text | — | Foley/ambience policy. |
| `segments` | string (JSON) | `{start, end, prompt?}` | none | Shared timeline. |
| `preserve_speech` | boolean | — | false | |
| `ducking` | boolean | — | false (API) | Ignored when `preserve_speech` is used. sonilo-mcp defaults it to true. |
| `keep_original_sound` | boolean | — | false | video-to-video-sound only. |
| `output_format` | enum | `wav` · `m4a` · `mp3` | `wav` | video-to-sound only. |
| `variants_num` | integer | 1–10 | 1 | Results in `outputs` array. |

## Segment Object

```json
[{"start": 0, "end": 8, "prompt": "intro: sparse felt piano, low pulse"},
 {"start": 8, "end": 20, "prompt": "verse: add brushed percussion, same piano motif"}]
```
`start` (number, required) · `end` (number, required, > start) · `prompt` (string, optional). Serialize the array to a **string** for the form field: `-F 'segments=[{"start":0,...}]'`. No `label`, `intensity` or `bpm` keys.

## Audio Ducking

`voice_file` or `voice_url` (exactly one; a video file is OK — its audio is used and output re-muxed) + `music_file` or `music_url` (exactly one). **No tuning fields** — no ratio, attack or release.

## Task Response & Polling

- Async submit → **202** `{task_id, status: "processing"}`. Poll `GET /v1/tasks/{task_id}` every 2–5 s with a timeout.
- Terminal: `succeeded` / `completed`, `failed`, `canceled`. Result fields may include `audio`, `video`, `music`, `sfx`, `music_processed`, `output_url`, `output_type`, `duration_seconds`, `cost`, `error`, `refunded`, plus `outputs` / `videos` / `ducked` arrays where requested.
- Download only from a real succeeded asset; check `content_type` and size.
- Errors: 401 auth · 402 insufficient balance · 403 service not enabled · 404 bad path/host · 413 oversize URL download · 422 invalid input (e.g. audio-only video) · 429 honor `Retry-After`.
- All output carries an inaudible provenance watermark.

## Output Formats

| Endpoint family | Options | Use |
|---|---|---|
| Music | `m4a` (AAC, default) · `wav` (16-bit PCM) · `mp3` (320 kbps CBR) | M4A previews; WAV for post |
| SFX | `wav` · `mp3` · `aac` · `flac` | WAV/FLAC for post |
| video-to-sound | `wav` (default) · `m4a` · `mp3` | WAV mix + components |
| video-to-video-* | MP4 with source picture/dimensions retained | Review / social delivery |

No sample-rate or bit-depth selector is documented — don't invent one.

## Recommended Combinations

| Workflow | Endpoint | Settings |
|---|---|---|
| Fast concept pass | video-to-music | no/short prompt · `prompt_influence 0.4–0.5` · `mode async` · `variants_num 2` · m4a |
| Brand-constrained score | video-to-music | identity brief · `prompt_influence 0.65–0.8` · 2–4 segments · `variants_num 2–3` |
| Narrated content | video-to-music | `mode async` · `preserve_speech true` · `ducking true` · wav |
| Social MP4 deliverable | video-to-video-music | `keep_original_sound` or `preserve_speech` · `variants_num 2` |
| Library cue | text-to-music | `duration` exact · async · wav · `variants_num 3` |
| Foley pass | video-to-sfx | one-line policy + segments · `audio_format wav` |
| One-call finished mix | video-to-sound | both prompts · `preserve_speech` as needed · wav |
| Final master | any | async · wav · `variants_num 1` (re-run of a chosen prompt) |

Influence ranges are working recommendations, not official presets. Start at 0.5 and move one step at a time.

## Pricing (credits, per output second)

| Model | Credits / s |
|---|---|
| Video-to-Music | 18 |
| Video-to-Sound-Effects | 18 |
| Text-to-Music | 5 |
| Text-to-Sound-Effects | 4 |

Minimum 15 s billed and 200 credits per generation; `variants_num` multiplies cost; `prompt_influence`, `ducking`, `stems` are free add-ons. Plans: Free (2,000 credits / 2 weeks, non-commercial, "Music by Sonilo" credit) · Pro $11.99/mo (40,000) commercial · Premium $23.99/mo (100,000) adds film/TV/broadcast · Enterprise custom. API is pay-as-you-go prepaid credits with a few free trial calls. Rates change — check sonilo.com/pricing.

## Wrapper Platforms

| Platform | Differences |
|---|---|
| fal.ai `sonilo/v1.1/video-to-music` | `video_url` only · `num_samples` (not `variants_num`) · `prompt_influence` 0.5 · `start_offset` + `duration` to score a sub-range · output AAC/m4a `audios` array · no segments listed |
| ComfyUI (Sonilo API nodes) | Text to Music (prompt 1–1,000 chars, duration 1–360, default 30) and Video to Music (≤360 s). `seed` widget is **ignored** by Sonilo. |
| sonilo-mcp (official MCP) | tools `text_to_music`, `video_to_music`, `text_to_sfx`, `video_to_sfx`, `video_to_sound`, `video_to_video_*`, `audio_ducking`; MCP caps SFX/sound video at 180 s and defaults `ducking` true on video_to_sound |

## v1.0 → v1.1

| Area | v1.0 | v1.1 |
|---|---|---|
| Sync | footage-driven score | tighter beats/builds/transitions; resolves to a musical ending |
| Speech | none | `preserve_speech` |
| Structure | automatic only | `segments` + section words (intro/verse/chorus/bridge) |
| Prompt adherence | baseline | preferred 50% vs 30% in Sonilo's internal eval |

No syntax break. Re-test `prompt_influence` — v1.1 follows prompts more strongly.

## Not Available (do not send)

`seed` · `negative_prompt` · `lyrics` · `vocals` · `bpm` · `key` · `genre` · `label` · `ducking_ratio` · `attack_ms` · `release_ms` · `audioFormat` · `aspect_ratio` · `resolution` · `sample_rate` · `image` · `audio_reference` · `/v1/vocal-isolation`
