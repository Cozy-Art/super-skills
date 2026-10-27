# Fish Audio — Parameters

Native endpoint: `POST https://api.fish.audio/v1/tts` · headers `Authorization: Bearer <API key>`, `Content-Type: application/json` (or `application/msgpack`), `model: <model id>`.
Response: audio bytes (chunked transfer). Errors: `401` no permission · `402` no payment/credit · `429` concurrency limit (no `Retry-After`; back off exponentially) · `503` overloaded.

*Verified against the Fish Audio API reference (Text to Speech, Create Model, Voice Design), Models Overview, Emotion Control, Drama 3, Migrate from S1, Pricing & Rate Limits and Voice Cloning best-practice pages at docs.fish.audio, October 2026.*

## `model` Header

| Value | Status | Languages | Cue syntax | Price (per M UTF-8 bytes of input text) |
|---|---|---|---|---|
| `s2.1-pro` | Recommended production; TTFA + DPA guarantees | 83 | `[brackets]` | $15.00 |
| `s2.1-pro-free` | Same model, dev/prototyping, no TTFA/DPA guarantees | 83 | `[brackets]` | $0 (fair use) |
| `drama-3` | Released Oct 13, 2026 — directed/scripted performance; open weights | 83 | `[brackets]` + scoped `<tags>` | Not on official pricing page yet — third-party listings show launch discounts (unverified — confirm on your platform) |
| `s2-pro` | Previous generation, open source | 80+ | `[brackets]` | $15.00 |
| `s1` | Deprecated — retires Dec 31, 2026; afterwards served and billed as `s2.1-pro` | 13 | `(parentheses)`, fixed 64+ set | $15.00 |

Missing or unrecognized value → silently served by `s2.1-pro`. SDK defaults differ: Python SDK sends `s2-pro`; JS SDK (`fish-audio` 0.1.0) sends `s1`. Always set it.

## Request Body (`/v1/tts`)

| Field | Type | Values | Default | Notes |
|---|---|---|---|---|
| `text` | string | script | **required** | Spoken text + inline cues/tags |
| `reference_id` | string \| string[] \| null | voice model ID(s) | `null` | Array = multi-speaker, index matches `<|speaker:N|>` |
| `references` | ReferenceAudio[] \| ReferenceAudio[][] \| null | `{audio: bytes, text: transcript}` (WAV/MP3/FLAC) | `null` | Inline zero-shot clone. **MessagePack only.** 2-D array for zero-shot multi-speaker |
| `temperature` | number | 0–1 | 0.7 | Higher = more varied/expressive |
| `top_p` | number | 0–1 | 0.7 | Nucleus sampling diversity |
| `prosody` | object \| null | see below | `null` | Global speed/volume |
| `chunk_length` | integer | 100–300 | 300 (raw API) / 200 (SDK & feature docs) | Characters per internal text chunk — not a request max |
| `min_chunk_length` | integer | 0–100 | 50 | Min characters before a new chunk |
| `normalize` | boolean | | `true` | Text normalization (numbers, symbols) |
| `language` | string \| null | e.g. `en`, `es-MX`, `zh-CN`; `auto`/empty = per-chunk detection | `null` | Affects normalization and timestamp alignment only, not voice |
| `format` | string | `mp3` `wav` `pcm` `opus` | `mp3` | |
| `sample_rate` | integer \| null | see format table | `null` (44100; 48000 for opus) | |
| `mp3_bitrate` | integer | 64, 128, 192 (kbps) | 128 | mp3 only |
| `opus_bitrate` | integer | -1000 (auto), 24000, 32000, 48000, 64000 (**bps**) | -1000 (schema) | opus only; docs also say "32 kbps default" — set explicitly |
| `latency` | string | `low` `balanced` `normal` | `normal` (raw API) / `balanced` (SDK) | Quality vs time-to-first-audio |
| `max_new_tokens` | integer | | 1024 | Max generated **audio** tokens per chunk — safety ceiling, not duration |
| `condition_on_previous_chunks` | boolean | | `true` | Uses previous audio as context — keep on for long-form |
| `repetition_penalty` | number | >1.0 reduces repetition | 1.2 | **No effect on S2.1-Pro** (per migration guide) |
| `early_stop_threshold` | number | 0–1 | 1 | Leave default |
| `features` | string[] | e.g. `["quality-guard"]` | `[]` | Feature flags; behaviour not further documented |
| `pronunciation_dictionary` | array \| null | ≤3 entries: `{id, version}` refs **or** inline `{items:[{key, value, case_sensitive}]}` (≤5000 items) | `null` | Unresolvable refs are dropped silently |

### `prosody`

| Field | Values | Default | Notes |
|---|---|---|---|
| `speed` | 0.5–2.0 | 1 | Global rate |
| `volume` | dB | 0 | Gain |
| `normalize_loudness` | boolean | `true` | S2 family only; accepted but no effect on `s1` |

## Formats & Sample Rates (all mono)

| Format | Sample rates | Bitrate | Use |
|---|---|---|---|
| `wav` | 8k, 16k, 24k, 32k, 44.1k (16-bit) | — | Editing, mastering, archive |
| `pcm` | same as wav, raw 16-bit | — | Low-latency playback, telephony |
| `mp3` | 32k, 44.1k | 64 / 128 / 192 kbps | Delivery, web |
| `opus` | 48k | auto / 24–64 kbps | Streaming, bandwidth |

## Latency & Chunking

| Workload | `latency` | `chunk_length` | Format |
|---|---|---|---|
| Final narration / audiobook | `normal` | 250–300 | wav 44.1k or mp3 192 |
| Production voiceover | `normal` | 200–300 | wav / mp3 |
| Interactive assistant | `balanced` | 100–180 | opus / pcm |
| Lowest latency | `low` | 100 | pcm / opus |

`balanced` ≈ 300 ms TTFA; `normal` ≈ 500 ms, most stable. Smaller chunks start sooner; larger chunks are more efficient and steadier over long text. Chunk ranges in the table are practical guidance, not official.

## Sampling Starting Points (practical, not official)

| Goal | `temperature` | `top_p` |
|---|---:|---:|
| Max consistency (IVR, UI lines, compliance) | 0.2–0.4 | 0.4–0.6 |
| Stable natural speech | 0.5–0.7 | 0.6–0.75 |
| Expressive character | 0.7–0.85 | 0.75–0.9 |
| Exploratory | 0.85–1.0 | 0.9–1.0 |

Drift → lower `temperature` first, then `top_p`. Never max both by default.

## Presets

```json
// Stable agent (stream)
{"temperature": 0.35, "top_p": 0.55, "chunk_length": 120, "latency": "balanced",
 "format": "opus", "sample_rate": 48000, "prosody": {"speed": 1.0, "volume": 0, "normalize_loudness": true}}

// Final narration / audiobook
{"temperature": 0.5, "top_p": 0.65, "chunk_length": 300, "latency": "normal",
 "condition_on_previous_chunks": true, "format": "wav", "sample_rate": 44100,
 "prosody": {"speed": 0.93, "volume": 0, "normalize_loudness": true}}

// Expressive character (render several takes)
{"temperature": 0.8, "top_p": 0.85, "chunk_length": 200, "latency": "normal",
 "format": "wav", "sample_rate": 44100, "prosody": {"speed": 1.0, "volume": 0, "normalize_loudness": true}}
```

## Voice Model Endpoint (`POST /model`)

`multipart/form-data` recommended. Returns `_id` → use as `reference_id`.

| Field | Required | Values / default |
|---|---|---|
| `type` | ✅ | `tts` |
| `title` | ✅ | string |
| `train_mode` | ✅ | `fast` (instantly available) |
| `voices` | ✅ | 1–20 audio files |
| `texts` | — | transcripts matching `voices` (≤20); omitted → ASR runs |
| `visibility` | — | `private` (default) · `unlist` · `public` (downgraded to private via API — publish in web app) |
| `enhance_audio_quality` | — | `true` default |
| `voice_design_signatures` | — | one per voice, from Voice Design; invalid signature rejects request (how candidates expose a signature is not in the Voice Design schema — unverified, confirm on your platform) |
| `description`, `tags`, `cover_image`, `generate_sample` | — | optional metadata (`cover_image` required if public) |

Response `state`: `created` → `training` → `trained` / `failed`.

## Voice Design (`POST /v1/voice-design`, header `model: voice-design-1`, JSON only)

| Field | Required | Values | Default |
|---|---|---|---|
| `instruction` | ✅ | 1–2000 chars, natural-language voice description | — |
| `reference_text` | — | preview line (API ref max 150 chars; feature page says 300 — stay ≤150) | `null` |
| `language` | — | BCP-47 hint | `null` |
| `n` | — | 1–4 candidates | 2 |
| `speed` | — | >0, ≤3 | 1 |
| `num_step` | — | 1–128 | 32 |
| `guidance_scale` | — | ≥0 | 2 |
| `instruct_guidance_scale` | — | ≥0 | 0 |
| `seed` | — | integer | `null` |

Returns `candidates[]` with `audio_base64` (WAV), `sample_rate`, `duration_ms`, `index`, `id`. $0.01 per successful request (not per candidate). Extra fields are rejected.

## Concurrency (shared across keys and ASR)

| Prepaid total | Concurrent requests |
|---|---|
| < $100 | 5 |
| ≥ $100 | 15 |
| ≥ $1,000 | 50 |
| Enterprise | custom |

## Not Available on `/v1/tts` (do not send)

`seed` · `duration` · `voice_id` · `emotion` / `emotion_strength` · `pitch` · `style` · top-level `speed` / `volume` · `negative_prompt` · aspect ratio / resolution / image inputs. Wrappers (OpenRouter, ComfyUI partner nodes, Runware) may rename or cap fields (e.g. Runware's 3,000-char limit) — treat those as platform rules, not Fish syntax.

## S1 → S2.1-Pro Migration

| Area | S1 | S2.1-Pro / S2-Pro / Drama 3 |
|---|---|---|
| Header | `s1` | `s2.1-pro` (or `drama-3`) |
| Cue syntax | `(happy)` fixed set | `[happy]` or free-form `[whispers sweetly]` — **not auto-converted** |
| Dialogue | render per speaker, stitch | native `<|speaker:N|>` + `reference_id` array |
| Languages | 13 | 83 (S2.1-Pro, Drama 3) |
| `normalize_loudness` | no effect | default `true` — set `false` to match old masters |
| `repetition_penalty` | active | no effect on S2.1-Pro — re-listen |

Convert only genuine control tags; leave grammatical parentheses alone.
