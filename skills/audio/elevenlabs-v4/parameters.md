# Eleven v4 — Parameters

Base URL `https://api.elevenlabs.io` · header `xi-api-key: <API key>` · `Content-Type: application/json`. Limits are measured in **characters**, not tokens.

*Verified against the ElevenLabs API reference (Create speech, Create dialogue, TTD WebSocket), Models overview, "What is Eleven v4?", Prompting best practices, TTS-vs-TTD WebSocket guide, changelog and API pricing page, October 2026.*

## Models

| | `eleven_v4` | `eleven_v4_turbo` |
|---|---|---|
| Purpose | Highest-quality produced speech: audiobooks, character VO, dialogue, localization | Expressive real-time: agents, assistants, NPCs |
| Recommended transport | Text to Dialogue API (batch / HTTP stream); Create speech also accepts it | Text to Dialogue WebSocket |
| Character limit / request | 10,000 (~10 min) | Not published — send turn-sized chunks |
| Languages | 90+ (FAQ lists 87 by name) | Same list as v4 |
| Latency | Quality-oriented | ~100 ms median inference, excl. app + network latency |
| Voice settings | Stability, Similarity | Stability, Similarity |
| Style / Speed sliders · SSML | Not available | Not available |
| Voices per TTD WebSocket | Up to 10 | **1** |
| API price (per 1K chars) | $0.08 | $0.04 |

App/ElevenCreative: v4 uses the same credit pricing as other TTS models. ElevenAgents default TTS model is now `eleven_v4_turbo` (changed 5 Oct 2026).

## Create Speech — `POST /v1/text-to-speech/{voice_id}` (stream: `…/{voice_id}/stream`)

| Field | Where | Type | Values | Default | Notes |
|---|---|---|---|---|---|
| `voice_id` | path | string | Library / IVC / PVC / Voice Design ID | — | Required. The character's identity. |
| `text` | body | string | script + tags + IPA | — | Required. ≤10,000 chars on v4. |
| `model_id` | body | string | `eleven_v4`, `eleven_v4_turbo` | `eleven_multilingual_v2` | **Always set it.** |
| `language_code` | body | string | ISO 639-1 | null | Forces language + normalization. |
| `voice_settings` | body | object | see below | voice's stored settings | Per-request override. |
| `pronunciation_dictionary_locators` | body | `[{id, version_id}]` | max 3 | null | Applied in order. |
| `seed` | body | int | 0–4,294,967,295 | null | Best-effort; determinism not guaranteed. |
| `previous_text` / `next_text` | body | string | — | null | Ignored if matching request IDs are sent. |
| `previous_request_ids` / `next_request_ids` | body | string[] | max 3 each | null | Stitching; best with the same model. |
| `apply_text_normalization` | body | enum | `auto` `on` `off` | `auto` | Number/date/symbol expansion. |
| `apply_language_text_normalization` | body | bool | — | `false` | Japanese only; adds latency. |
| `use_pvc_as_ivc` | body | bool | — | `false` | Use a PVC's IVC version: lower latency, more expressive. No longer deprecated. |
| `audio_effects` | body | object | see below | null | Added 12 Oct 2026. |
| `output_format` | query | enum | see below | `mp3_44100_128` | |
| `enable_logging` | query | bool | — | `true` | `false` = zero retention (enterprise) and **disables request stitching**. |
| `optimize_streaming_latency` | query | int 0–4 | — | — | **Deprecated.** Don't use for v4. |

### `voice_settings` (TTS)

| Field | Default | v4 behaviour |
|---|---|---|
| `stability` | 0.5 | Lower = more expressive/varied; higher = closer to a fixed baseline, can flatten. |
| `similarity_boost` | 0.75 | Higher = closer to reference voice; can cost naturalness and reproduce source artifacts. |
| `use_speaker_boost` | `true` | Generic field; adds latency. v4 docs don't mention it. |
| `style`, `speed` | 0, 1 | Present in the generic schema, but **v4 does not expose Style or Speed** — don't build on them. |

Treat both as 0–1 (UI sliders and long-standing voice-settings convention; the current API schema lists defaults but no range — unverified, confirm on your platform).

## Create Dialogue — `POST /v1/text-to-dialogue` (stream: `/v1/text-to-dialogue/stream`)

| Field | Type | Values | Default | Notes |
|---|---|---|---|---|
| `inputs` | `[{text, voice_id}]` | ≤10 unique `voice_id`s | — | Required. Keep combined `text` ≤ **2,000 chars**. |
| `model_id` | string | `eleven_v4`, `eleven_v3` | `eleven_v3` | **Always set `eleven_v4`.** |
| `settings` | object | `stability` (default 0.5), `similarity` (default 0.75) | null | Note: **`similarity`**, not `similarity_boost`, in dialogue. |
| `language_code` | string | ISO 639-1 | null | |
| `pronunciation_dictionary_locators` | array | max 3 | null | |
| `seed` | int | 0–4,294,967,295 | null | Best-effort. |
| `previous_text` / `future_text` | string | **≤100 chars each** | null | Short prosodic context only. |
| `previous_request_ids` | string[] | max 3, **closest clip last** | null | |
| `next_request_ids` | string[] | max 3, **closest clip first** | null | |
| `apply_text_normalization` | enum | `auto` `on` `off` | `auto` | |
| `use_pvc_as_ivc` | bool | — | `false` | |
| `audio_effects` | object | see below | null | |
| `output_format`, `enable_logging` | query | as TTS | | |

Dashboard dialogue allows up to 2 free regenerations with identical content/parameters. Dialogue effects are API-only.

## Text to Dialogue WebSocket — `wss://api.elevenlabs.io/v1/text-to-dialogue/stream-input`

Query: `model_id` (must start with `eleven_v3` or `eleven_v4`; the reference page still shows `eleven_v3_conversational` as default — set it), `output_format`, `sync_alignment` (default `false`; attaches character timing), `language_code`, `apply_text_normalization`, `seed`, `enable_logging`.

| Message | Shape | Notes |
|---|---|---|
| First (required) | `{"voices": ["VOICE_ID"], "xi_api_key": "…"}` | `voice_settings` and `pronunciation_dictionary_locators` accepted **only here**. Turbo: exactly 1 voice. v4: ≤10. |
| Input | `{"inputs": [{"text": "…", "voice_id": "…", "new_turn": false}]}` | `new_turn: true` (or switching `voice_id`) closes the prosody segment. |
| Flush | `{"flush": true}` | Force buffered text out without closing. |
| Keep-alive | `{"keep_alive": true}` | Resets the **20 s** receive timeout. |
| Close | `{"close_socket": true}` | Flushes, sends final frame, closes. |

Server buffers ~**40 characters / 8 words** before emitting audio — batch very short lines or flush. Responses: base64 `audio`, optional `alignment`, `is_final_audio_for_turn`. MP3/Opus may interleave a few bytes across turns; use **PCM** for exact turn boundaries.

The standard TTS WebSocket (`/v1/text-to-speech/{voice_id}/stream-input`) does **not** support v3 or v4.

## `audio_effects` (TTS + Dialogue)

| Field | Type | Range | Default | Notes |
|---|---|---|---|---|
| `filter_preset_id` | string | e.g. `phone`, `old_radio` | null | |
| `distance` | number | 0 (close) – 1 (far) | 0 | Perceived mic distance. |
| `environment_id` | string | e.g. `small_room`, `hall` | null | Reverb; stereo; tail of up to several seconds. |
| `send_level` | number | 0–1 | 1 | Reverb amount; only with `environment_id`. |
| `background_noise_id` | string | e.g. `cafe`, `keyboard` | null | Looped bed. |
| `pan` | number | −1 (L) – 1 (R) | 0 | Non-zero = stereo. |

Valid IDs: `GET /v1/audio-effects/catalog`. Unknown ID → 404. Stereo effects with `pcm_*` / `ulaw_*` / `alaw_*` → 400. Effects don't change cost. For final mixes, render dry and add effects in post.

## Output Formats

`mp3_22050_32` `mp3_24000_48` `mp3_44100_32` `mp3_44100_64` `mp3_44100_96` `mp3_44100_128` `mp3_44100_192`†
`opus_48000_32` `opus_48000_64` `opus_48000_96` `opus_48000_128` `opus_48000_192`
`pcm_8000` `pcm_16000` `pcm_22050` `pcm_24000` `pcm_32000` `pcm_44100`‡ `pcm_48000`‡
`wav_8000` `wav_16000` `wav_22050` `wav_24000` `wav_32000` `wav_44100`‡ `wav_48000`‡
`ulaw_8000` (Twilio) `alaw_8000`

† Creator tier+ · ‡ 44.1 kHz+ PCM/WAV = Pro tier+

## Recommended Presets (starting points, tune per voice)

| Use case | Model / transport | Stability | Similarity | Format |
|---|---|---|---|---|
| Film / game character acting | `eleven_v4`, dialogue | 0.35–0.50 | 0.70–0.80 | `wav_48000` |
| Audiobook narration | `eleven_v4`, segmented + stitched | 0.50–0.65 | 0.70–0.80 | `wav_44100` / `mp3_44100_192` |
| Branded voiceover | `eleven_v4` | 0.55–0.70 | 0.75–0.85 | `mp3_44100_192` / WAV |
| NPC / live agent | `eleven_v4_turbo`, TTD WebSocket | 0.50–0.70 | 0.70–0.80 | Opus, or `ulaw_8000` for telephony |
| Localization | `eleven_v4` + `language_code` | 0.50–0.65 | 0.75–0.85 | WAV/PCM |
| Maximum repeatability | `eleven_v4` | 0.70–0.85 | 0.75–0.85 | fixed |

Bands are working practice, not official presets; ElevenLabs cites ~50 / ~75 as the common baseline.

## v3 / Multilingual v2 → v4 Migration

| Old habit | Eleven v4 |
|---|---|
| `style`, `speed` sliders | Gone — use wording, punctuation, tags, voice choice, editing |
| SSML `<break time="1.5s"/>` | `…`, `—`, paragraph breaks, `[short pause]` / `[long pause]` |
| `<phoneme>` tags (Flash v2 only) | Slash-delimited IPA `"/…/"` or pronunciation dictionary |
| 5,000-char v3 limit | 10,000 on `eleven_v4` (still segment for QA) |
| Source accent carried into other languages | v4 speaks the target language with a native accent; identity kept |
| PVC not optimized (v3) | PVC fully supported — fine-tune it for v4 in My Voices |
| `optimize_streaming_latency`, TTS WebSocket | `eleven_v4_turbo` on TTD WebSocket |
| `eleven_v3_conversational` (~280 ms) | `eleven_v4_turbo` (~100 ms) |

v4 is a new architecture: same voice + same script can sound materially different. Re-render representative scenes before migrating a series.
