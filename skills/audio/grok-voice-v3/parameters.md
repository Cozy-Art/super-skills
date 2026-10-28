# Grok Voice 3.0 — Parameters

*Verified against xAI docs (Speech to Speech, Speech to Speech Prompting Guide, SIP, Voice overview, Text to Speech, Custom Voices, Ephemeral Tokens, Voice API reference, Pricing, Release notes) and the xAI Grok Voice 3.0 announcement, October 2026.*

## Models

| ID | Status | Notes |
|---|---|---|
| `grok-voice-latest` | Alias → `grok-voice-3.0` | Default of the `model` query param. Agents on the alias were switched automatically. |
| `grok-voice-3.0` | Current flagship (released 14 Oct 2026) | Same API, events and price as 2.0. |
| `grok-voice-2.0` | Deprecated | Migrate by changing the `model` param only. |

Pin `grok-voice-3.0` for reproducible behaviour; use the alias only if you want silent upgrades.

## Connection & Auth

| Item | Value |
|---|---|
| Endpoint | `wss://api.x.ai/v1/realtime?model=grok-voice-3.0` |
| Server auth | `Authorization: Bearer <XAI_API_KEY>` — server-side only |
| Client auth | Ephemeral token: server calls `POST https://api.x.ai/v1/realtime/client_secrets` with `{"expires_after": {"seconds": 300}}` → `{value, expires_at}`. Browser: `new WebSocket("wss://api.x.ai/v1/realtime", ["xai-client-secret.<value>"])`. No `session` or `expires_after.anchor` fields. Default/max expiry not published. |
| SIP | `?call_id=<id>` from the `realtime.call.incoming` webhook; requires API key (not client secret); `model` ignored when `call_id` set. |
| Resume | `?conversation_id=<id>` (see Resumption) |

## `session.update` → `session` fields

| Field | Type | Values / range | Default | Notes |
|---|---|---|---|---|
| `instructions` | string | Markdown system prompt | — | Max length not published. Updateable mid-session. |
| `voice` | string | built-in ID (lowercase) or custom voice ID | not stated for S2S (TTS default is `eve`) — always set it | |
| `reasoning.effort` | enum | `"high"`, `"none"` | `"high"` | `none` = faster, less deliberate. Also settable as connection param. |
| `turn_detection.type` | string \| null | `"server_vad"`, `null` | — | `null` = manual turns via `input_audio_buffer.commit`. |
| `turn_detection.idle_timeout_ms` | number \| null | ms | `null` | Re-engages user after silence following a reply; re-arms after each response; repeats until user speaks. |
| `resumption.enabled` | bool | | `false` | Must be true on original and resumed session. |
| `audio.input.format.type` / `audio.output.format.type` | string | `audio/pcm`, `audio/pcmu`, `audio/pcma`, `audio/opus` | `audio/pcm` | Input and output can differ. |
| `audio.input.format.rate` / `audio.output.format.rate` | number | PCM only: 8000, 16000, 22050, 24000, 32000, 44100, 48000 | 24000 | |
| `audio.input.transport` / `audio.output.transport` | enum | `"json"`, `"binary"` | `"json"` | See Audio. |
| `audio.output.speed` | number | 0.7–1.5 | 1.0 | The only pace control. |
| `audio.input.transcription.language_hint` | BCP-47 | e.g. `en`, `fr`, `es-MX`, `pt-BR` | unset (auto-detect) | Bare `es`/`pt` not accepted; unknown codes ignored; updateable mid-session. |
| `audio.input.transcription.keyterms` | string[] | ≤100 terms, ≤50 chars each | — | Biases recognition of names/jargon; updateable mid-session. |
| `audio.input.transcription.model` | string | `"grok-transcribe"` | — | Enables `conversation.item.input_audio_transcription.updated` (cumulative user transcript). |
| `replace` | object | `{"phrase": "spoken form"}` | — | Pronunciation map; see below. |
| `tools` | array | `function`, `web_search`, `x_search`, `file_search`, `mcp` | — | See Tools. |

Not documented for Grok Voice (don't send): `temperature`, `modalities`, `max_response_output_tokens`, VAD `threshold` / `silence_duration_ms` / `prefix_padding_ms` / `eagerness`. (Unverified — confirm on your platform before assuming support.)

### `replace` rules

- Case-insensitive match; replacement spoken with the casing you give.
- Whole words only: `"Acme Mobile"` won't match `Acme-Mobile` or `Acme Mobiles` — add those variants as keys.
- Longest key wins when keys share a prefix.
- Changes audio only; transcript keeps the original. Applied map echoed on `session.updated`. Updateable mid-session.
- S2S size limits not published (TTS: ≤200 entries, keys ≤100 chars, values ≤128 chars — a safe ceiling).

## Audio

| Codec | Spec |
|---|---|
| `audio/pcm` | Linear16 little-endian, any listed rate (default 24 kHz) |
| `audio/pcmu` | G.711 μ-law, 8 kHz (telephony) |
| `audio/pcma` | G.711 A-law, 8 kHz (telephony) |
| `audio/opus` | 24 kHz, one raw Opus packet per payload — not an Ogg file cut into chunks |

Transport: `json` = base64 audio inside JSON events (default); `binary` = raw codec bytes as WebSocket binary frames, while lifecycle events and transcripts stay JSON. Input accepts either transport for the configured codec; output uses only the configured one; output-transport changes apply at the next response boundary.

## Tools

| Type | Config | Runs |
|---|---|---|
| `function` | `name`, `description`, `parameters` (JSON Schema) | Client: you execute and return output |
| `web_search` | `allowed_domains` **or** `excluded_domains` (≤5, exclusive), `enable_image_understanding`, `location` {country, city, region, timezone} | Server |
| `x_search` | `allowed_x_handles` **or** `excluded_x_handles` (≤20, exclusive), `from_date`/`to_date` (YYYY-MM-DD), `enable_image_understanding`, `enable_video_understanding` | Server |
| `file_search` | `vector_store_ids`, `max_num_results` | Server |
| `mcp` | `server_url`, `server_label` (required); `server_description`, `allowed_tools`, `authorization`, `headers` | Server; Streamable HTTP or SSE only |

Invalid tool config → `error` event; session stays connected with its previous config.

**Function-calling flow:** receive `response.function_call_arguments.done` → run function → `conversation.item.create` with `{"type": "function_call_output", "call_id": <from the event>, "output": "<JSON string>"}` → after **all** outputs for the turn are in, send `response.create`.

Prompting-guide tool names (`end_call`, `transfer_call`, `api_request`) are examples of tools an agent platform may attach — over the raw API you must define them yourself as `function` tools (on SIP, back them with the `/refer` and `/hangup` REST calls).

## Events

**Client → server:** `session.update`, `input_audio_buffer.append`, `input_audio_buffer.commit` (manual turns only), `input_audio_buffer.clear`, `conversation.item.create` (`function_call_output`, `force_message`), `conversation.item.delete`, `conversation.item.truncate`, `response.create` (optional one-turn `instructions`), `response.cancel`.

**Server → client (main):** `session.created`, `session.updated`, `conversation.created` (holds `conversation.id`), `input_audio_buffer.speech_started` / `speech_stopped` / `committed` / `timeout_triggered`, `conversation.item.added`, `response.created`, `response.output_audio.delta` (alias `response.audio.delta`), `response.output_audio_transcript.delta` / `.done`, `response.function_call_arguments.done`, MCP lifecycle events, `response.done`, `error`. SIP only: `input_audio_buffer.dtmf_event_received`.

**Not supported:** `conversation.item.retrieve`, `output_audio_buffer.*`, `rate_limits.updated`, `conversation.item.input_audio_transcription.failed`.

### `force_message` (verbatim line, no model)

```json
{"type": "conversation.item.create",
 "item": {"type": "force_message", "role": "assistant",
          "interruptible": false,
          "content": [{"type": "output_text", "text": "This call is being recorded."}]}}
```
`interruptible` defaults to `true`. The item **is** the turn — don't follow with `response.create`. 

### Per-response override

```json
{"type": "response.create", "response": {"instructions": "Respond in Spanish for this turn only."}}
```
Later responses revert to the session `instructions`.

## Resumption

Enable on both sessions → save `conversation.created.conversation.id` → reconnect with `?conversation_id=<id>`. Replays user/assistant transcripts, tool calls and function outputs. History expires after **30 min** of inactivity. Re-send `session.update` (instructions, voice, tools) on the resumed socket — config replay is not documented.

## SIP (phone)

Register a BYO-trunk number (`POST /v2/phone-numbers`, `origin: "byo_trunk"`), point the carrier at `sip:{number}@sip.voice.x.ai;transport=tls`, receive signed `realtime.call.incoming` webhooks, join with `?call_id=`. Transfer: `POST /v1/realtime/calls/{call_id}/refer` (to `tel:` / `sip:`; blocks until resolved; on failure the caller stays connected). Hang up: `/v1/realtime/calls/{call_id}/hangup`. DTMF reaches the model as text, flushed on `#`, 2.5 s idle, or speech. Use `audio/pcmu` or `audio/pcma`.

## Voices (28 built-in)

| ID | Character | Suited to |
|---|---|---|
| `eve` | Energetic, upbeat, British | General (default) |
| `ara` | Warm, friendly | General |
| `leo` | Authoritative, strong, British | General |
| `rex` | Confident, clear | General |
| `sal` | Smooth, balanced | General |
| `carina` | Soft, empathetic, soothing | Wellness, support |
| `celeste` | Compassionate, reassuring | Support, assistant |
| `aurora` | Serene, steady | Support, assistant |
| `liora` | Calm, grounded | Wellness, assistant |
| `luna` | Gentle, patient, nurturing | Education, assistants |
| `lux` | Grounded, calm, wise | Wellness, narration |
| `ursa` | Friendly, warm, steadfast | Assistant, podcasts |
| `naksh` | Warm, thoughtful, Indian accent | Assistant, support |
| `rigel` | Precise, professional, Australian accent | Assistant, support |
| `castor` | Charismatic, easygoing | Sales, support |
| `atlas` | Confident, commanding | Sales, assistant |
| `zenith` | Sharp, focused | Sales, advertising |
| `iris` | Friendly, upbeat, charming | Sales support |
| `helios` | Upbeat, versatile | Assistant, wellness |
| `cosmo` | Bright, curious | Education, podcasts |
| `lumen` | Warm, articulate | Education, advertising |
| `helix` | Bold, high-energy | Commentary, podcasts |
| `sirius` | Quick-witted, playful | Commentary, characters |
| `kepler` | Inventive, charismatic | Advertising, podcasts |
| `zagan` | Powerful, dramatic | Characters, narration |
| `orion` | Rich, cinematic, resonant | Narration, audiobooks |
| `altair` | Elegant, premium | Advertising, narration |
| `perseus` | Strong, trustworthy | Advertising, narration |

List live: `GET https://api.x.ai/v1/tts/voices`. Any voice can speak any supported language. Descriptions are xAI's TTS table — S2S rendering may differ; audition.

**Languages:** 20 documented codes — `en`, `ar-EG`, `ar-SA`, `ar-AE`, `bn`, `zh`, `fr`, `de`, `hi`, `id`, `it`, `ja`, `ko`, `pt-BR`, `pt-PT`, `ru`, `es-MX`, `es-ES`, `tr`, `vi`; input language auto-detected.

## Custom Voices

- Clone from one reference clip, **max 120 s** (400 if longer); 90–120 s recommended, <30 s may lack detail. WAV 16-bit mono 24 kHz preferred; lossy formats' artifacts get cloned; background noise gets cloned; delivery style gets cloned — record in the register the agent will use.
- Console: up to 30 voices per team, free. API (`POST /v1/custom-voices`, multipart) requires Enterprise. Voice IDs: 8 lowercase alphanumerics. Re-recording = delete + recreate (new ID).
- Availability: United States only, excluding Illinois. Use only voices you have rights and consent to clone (xAI's page states no consent process — your responsibility).
- Works anywhere a built-in voice does: `voice` in `session.update`, `voice_id` in TTS.

## Text to Speech (scripted lines, not live)

`POST https://api.x.ai/v1/tts` (unary) · `wss://api.x.ai/v1/tts` (streaming). Model ID not named in docs.

| Field | Values | Default |
|---|---|---|
| `text` | ≤60,000 chars, supports speech tags | required |
| `language` | BCP-47 or `auto` | **required** |
| `voice_id` | built-in or custom | `eve` |
| `output_format` | `{codec: mp3\|wav\|pcm\|mulaw\|alaw, sample_rate: 8000–48000, bit_rate (mp3): 32k–192k}` | mp3 24 kHz 128 kbps |
| `speed` | 0.7–1.5 | 1.0 |
| `optimize_streaming_latency` | 0, 1, 2 | 0 |
| `text_normalization` | bool | false |
| `with_timestamps` | bool | false |
| `replace` | ≤200 entries; respellings or IPA | — |

**Speech tags (TTS):** inline `[pause]` `[long-pause]` `[hum-tune]` `[laugh]` `[chuckle]` `[giggle]` `[cry]` `[tsk]` `[tongue-click]` `[lip-smack]` `[breath]` `[inhale]` `[exhale]` `[sigh]`; wrapping `<soft>` `<whisper>` `<loud>` `<build-intensity>` `<decrease-intensity>` `<higher-pitch>` `<lower-pitch>` `<slow>` `<fast>` `<sing-song>` `<singing>` `<emphasis>`. Closed list — don't invent tags. Whether S2S honours them: unverified.

Streaming TTS: ≤50 concurrent sessions per team; `text.delta` / `text.done` / `text.clear` (barge-in).

## Pricing (October 2026)

| | Price |
|---|---|
| Speech to Speech (`grok-voice-3.0`, same as 2.0) | $0.08 / min ($4.80 / hr); pricing page also lists "$0.004 / text input" (unit wording unclear — confirm) |
| Text to Speech | $15.00 / 1M chars (billed on input text, not `replace` output) |
| Speech to Text | $0.10 / hr REST · $0.20 / hr streaming |
| Custom voices | No separate price listed |

## Unpublished limits

Max `instructions` length, context window, max session duration, S2S concurrency, latency SLA (marketing: "under one second"), ephemeral-token max TTL. Don't state numbers for these.
