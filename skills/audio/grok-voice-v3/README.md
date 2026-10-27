# grok-voice-v3 — build notes

Human-facing build notes. Not loaded as part of the skill.

**Built:** 2026-10-19 · **Skill version:** 1.0 · **Model:** Grok Voice 3.0 (xAI)

---

## Research verification

Corrections / additions vs research:
- Release timing "no exact day" → released 14 Oct 2026; agents on `grok-voice-latest` switched automatically — https://x.ai/news/grok-voice-3
- "Exact current rate needs verification" → $0.08/min ($4.80/hr) for both 3.0 and 2.0; pricing table also shows "$0.004 / text input" (unit unclear) — https://docs.x.ai/developers/pricing
- Instructions "fixed section order" (unverified in research) → Role & Persona · Objective · Conversation Flow · Guardrails & Escalation · Voice & Communication Style, optional CRITICAL INSTRUCTIONS; plus core rules (sample phrases, ALWAYS/NEVER, only attached tools, don't script greeting in Flow, numbers hyphen-spelled, confirm state-changing tools) — https://docs.x.ai/developers/model-capabilities/audio/speech-to-speech/prompting-guide
- `language_hint`: Spanish/Portuguese require regional variants (`es-MX`, `es-ES`, `pt-BR`, `pt-PT`); bare `es`/`pt` not accepted; unknown codes ignored — https://docs.x.ai/developers/model-capabilities/audio/speech-to-speech
- Research example included no default voice claim; docs state none for S2S (all examples set `eve`; TTS default is `eve`) — told users to always set `voice` — same page + text-to-speech page
- Added: `force_message` (verbatim line, `interruptible` default true, no `response.create` after), per-response `instructions` override under `response`, function-call flow (all outputs before `response.create`), `audio.input.transcription.model: "grok-transcribe"`, resumption via `?conversation_id=` with 30-min inactivity expiry, tool sub-fields (web_search ≤5 domains exclusive; x_search ≤20 handles; mcp Streamable HTTP/SSE only), invalid tool config keeps previous config — speech-to-speech page
- Added: full client/server event list incl. `conversation.item.truncate`, `response.cancel`, MCP lifecycle, SIP DTMF event — https://docs.x.ai/developers/rest-api-reference/inference/voice
- Added: ephemeral token `POST /v1/realtime/client_secrets` with `expires_after.seconds`, browser subprotocol `xai-client-secret.<token>` — https://docs.x.ai/developers/model-capabilities/audio/ephemeral-tokens
- Added: SIP flow (BYO trunk, `realtime.call.incoming` webhook, `?call_id=`, `/refer` and `/hangup` REST, DTMF as text) — https://docs.x.ai/developers/model-capabilities/audio/speech-to-speech/sip
- Custom voice requirements (research: unresolved) → ≤120 s clip (90–120 s recommended), WAV 16-bit mono 24 kHz preferred, 30 voices/team, console free, API Enterprise-only, US-only excluding Illinois, 8-char IDs — https://docs.x.ai/developers/model-capabilities/audio/custom-voices
- Voices list (research: one example) → 28 built-in voices with tone/use descriptions; 20 language codes — https://docs.x.ai/developers/model-capabilities/audio/text-to-speech
- Emotion-tag syntax (research: unresolved) → documented for TTS only: closed list of inline `[tag]` and wrapping `<tag>` speech tags; S2S support not documented — text-to-speech page
- TTS covered briefly: `/v1/tts` unary + WebSocket, `language` required, 60,000-char limit, `replace` ≤200 entries, $15/1M chars — text-to-speech + pricing pages
- Vendor benchmarks for migration notes (3.0 vs 2.0): Full Duplex Bench 97.0% vs 95.1%, τ-Voice 71.6% vs 56.5% — https://x.ai/news/grok-voice-3
- Confirmed (no change): model IDs/alias, 2.0 deprecated, API unchanged on migration, `reasoning.effort` high/none default high, speed 0.7–1.5 default 1.0, `server_vad`/null, `idle_timeout_ms` re-arms, `resumption.enabled` default false, keyterms 100×50, `replace` matching rules, codecs/rates, Opus raw packets at 24 kHz, JSON/binary transport rules, tool types.

Unverified / caveats:
- Max `instructions` length, context window, session duration, S2S concurrency, latency figures (only "under one second" marketing), ephemeral-token max TTL — not published; skill says so.
- Whether TTS speech tags work in S2S replies — not documented; skill advises against relying on them.
- "Opening greeting configured as a separate field" (prompting guide) — field not documented for the raw API; skill uses `response.create` for the opener.
- `end_call` / `transfer_call` / `api_request` named in the prompting guide as built-in tools, but not in the S2S tools list — skill tells API users to define them as functions.
- Opus "mono" in research — docs say 24 kHz raw packets; mono not stated.
- Unsupported VAD tuning fields (threshold, silence duration etc.) — absent from docs; skill says don't send.
- Voice API reference page's model enum appeared inconsistent with the guide (guide: 3.0 is flagship); used the guide + release notes.
- Same-voice consistency between S2S and TTS output not documented.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
