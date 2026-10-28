---
name: grok-voice-3-prompts
description: Write system instructions, personas and session configuration for xAI Grok Voice 3.0 (model ID grok-voice-3.0, alias grok-voice-latest), the real-time speech-to-speech model behind xAI's Voice Agent API (wss://api.x.ai/v1/realtime). Use whenever a user mentions Grok Voice, Grok Voice 3, grok-voice-latest, xAI realtime / voice agent / speech-to-speech, or wants to build a phone agent, support or sales line, receptionist, in-car or hands-free assistant, tutor, rehearsal partner or NPC that talks live — persona, speaking style, turn-taking, tool-use phrasing, guardrails, escalation, voice choice, pronunciation maps, keyterms, turn detection, idle re-engagement, session resumption, SIP calls, or migrating from grok-voice-2.0. Also covers short scripted lines via xAI Text to Speech (/v1/tts) speech tags. Do not guess Grok Voice fields or prompt structure from general knowledge or other vendors' realtime APIs.
---

# Grok Voice 3.0 — Voice-Agent Instructions Skill

Grok Voice 3.0 (`grok-voice-3.0`, released 14 Oct 2026) is xAI's real-time speech-to-speech model: bidirectional audio over a WebSocket, server-side turn detection, function/web/X/file/MCP tools. `grok-voice-latest` points to it; `grok-voice-2.0` is deprecated. There is no per-utterance text prompt — **the "prompt" is the session's `instructions` (system prompt) plus voice and session config**, sent in `session.update`.

**Scope:** live conversation. For fixed, pre-written lines (disclaimers, IVR prompts, trailers) use `force_message` inside a session or the separate Text to Speech API — see [parameters.md](parameters.md).

## The Three Rules That Override Everything

1. **Instructions describe behaviour; they are never read aloud.** Write in second person ("You are…"), Markdown, short bullets, in xAI's section order. The model will speak whatever its turns contain — so require spoken words only: no markdown, lists, emojis or stage directions *in its replies*.
2. **Sound is set by config, not prose.** Voice timbre = `voice` ID. Pace = `audio.output.speed` (0.7–1.5). Pronunciation = `replace` map. Recognition of names = `keyterms`. Instructions can't change how a voice sounds — only what it says and how it phrases it.
3. **Only reference tools that exist, and confirm before anything that changes state.** Tool names in the prompt must match the schema exactly. Read-only lookups: call without asking. Bookings, refunds, cancellations, transfers: confirm first, and say a short line before the call.

When the user's console, SDK or API rejects or contradicts a value here, the interface wins — adjust and say so.

## Instruction Structure (xAI's recommended order)

| # | Section | What goes in it |
|---|---|---|
| 1 | `## Role & Persona` | Identity, brand, disposition, that it's an AI |
| 2 | `## Objective` | Desired outcome + fallback, 1–2 sentences |
| 3 | `## Conversation Flow` | How the call goes, using only attached tools. Prose for simple agents; phases (Goal / How to respond / Exit when) for complex ones. Don't script the opening greeting here |
| 4 | `## Guardrails & Escalation` | Scope limits, no medical/legal/financial advice, escalation triggers, safety path, transfer line |
| 5 | `## Voice & Communication Style` | Spoken-only output, turn length, sample phrases, numbers, language lock, unclear-input handling |
| + | `## CRITICAL INSTRUCTIONS` (optional) | Only hard rules, kept short, ALWAYS / NEVER |

Also bake in key facts (business name, hours, prices, policies, full URL) and tell the agent to answer only from them or its knowledge base, and to admit when it doesn't know.

## Decide the Setup First

| User wants | Config | Notes |
|---|---|---|
| Browser / mobile voice agent | `server_vad`, ephemeral token, PCM 24 kHz | Token via `POST /v1/realtime/client_secrets`; key never on client |
| Phone line (SIP) | `?call_id=…`, `audio/pcmu` or `audio/pcma` 8 kHz | Transfer/hangup are REST calls; DTMF arrives as text |
| Push-to-talk / walkie-talkie | `turn_detection: null` | Client sends `input_audio_buffer.commit` |
| Agent should nudge a silent user | `turn_detection.idle_timeout_ms` | Re-arms after each reply; repeats until user speaks |
| Survive dropped connections | `resumption.enabled: true` (both sessions) | Reconnect with `?conversation_id=`; history expires after 30 min idle |
| Lowest latency, simple tasks | `reasoning.effort: "none"` | Default `"high"` |
| Exact legal / compliance line | `force_message` item | Spoken verbatim; no `response.create` after it |
| One-turn behaviour change | `response.create` with `instructions` | Overrides session prompt for that response only |
| Pre-rendered narration or IVR audio | Text to Speech `/v1/tts` | Supports speech tags; not a live agent |

## Quick Syntax Reference

- **Session prompt:** `session.update` → `session.instructions` (string). Updateable mid-session.
- **Voice:** lowercase ID, always set explicitly, e.g. `eve`, `ara`, `rex`, `leo`, `sal`, `orion`, `carina`… 28 built-in, plus custom 8-char IDs.
- **Pronunciation:** `"replace": {"Elara": "eh-LAHR-ah"}` — case-insensitive, whole-word, longest key wins; audio only, transcript keeps the original.
- **Recognition:** `audio.input.transcription.keyterms` ≤100 terms × ≤50 chars; `language_hint` BCP-47 (`es-MX`/`es-ES`, `pt-BR`/`pt-PT` — bare `es`/`pt` rejected).
- **Numbers/codes in replies:** instruct the agent to speak each character separately, hyphen-joined, read back and confirm.
- **Tool preambles:** one short line before any tool call ("One moment while I check that."), or a sample phrase in each tool's `description`.
- **Speech tags** (`[laugh]`, `<whisper>`) are documented for TTS only; their effect in speech-to-speech replies is unverified — don't rely on them in instructions.

Field-by-field detail → [parameters.md](parameters.md). Writing craft → [best-practices.md](best-practices.md).

## Output Format (always two parts)

1. **Instructions** — in a code block: the Markdown system prompt only (sections above). Never put voice, speed, VAD, formats, tools JSON or model ID inside it.
2. **Suggested settings** — one line, e.g. `model: grok-voice-3.0 · voice: ara · speed: 1.0 · turn_detection: server_vad · reasoning: high · audio: pcm 24000 · tools: lookup_order, transfer_call`

If the user is wiring the API, also give the `session.update` JSON (valid fields only) and tool schemas. Add `replace` / `keyterms` when names, brands or jargon appear.

## Things That Will Break the Request

- Instructions that mention tools not in `tools`, or with different names — the agent will promise actions it can't take.
- Asking for markdown, lists, tables, emojis or `*actions*` in replies — they get spoken or garbled.
- Scripting the greeting inside Conversation Flow — xAI's guide says the opener is configured separately; over the raw API, trigger it with `response.create` (optionally with a one-turn `instructions` override).
- `turn_detection: null` without sending `input_audio_buffer.commit` — the model never replies.
- Sending `response.create` after a `force_message`, or before every `function_call_output` of the turn is submitted.
- Bare `es` / `pt` in `language_hint`; >100 keyterms or terms >50 chars.
- `audio.output.speed` outside 0.7–1.5; non-24 kHz Opus; Ogg files chunked as Opus; G.711 at anything but 8 kHz.
- Resumption enabled on only one side, or reconnecting after 30 min idle.
- `web_search` with both `allowed_domains` and `excluded_domains` (mutually exclusive; max 5) — invalid tool config returns `error`, the session keeps its old config.
- Putting an API key in browser code — use an ephemeral token.

## Iteration Workflow

1. Pick 2–3 candidate voices and audition the same short exchange in the xAI console voice playground.
2. Draft instructions in the five sections; keep Objective to 1–2 sentences and turns to 1–2 sentences.
3. Run real calls: interruptions, silence, garbled audio, off-topic asks, a wrong spelling to read back.
4. Change **one** thing per pass — a bullet, a sample phrase, a guardrail. Small wording changes cause big behaviour shifts.
5. Fix mispronunciations with `replace`, misheard names with `keyterms` — not with more prose.
6. Use a stronger text model to critique the prompt for ambiguity and conflicts, then re-test.
7. Lock voice + instructions + config per agent version; log them with transcripts.

## Reference Files

- **[parameters.md](parameters.md)** — endpoint, auth, every `session.update` field, audio codecs/transports, tools, events, function-calling flow, force_message, resumption, idle timeout, SIP, voices table, custom voices, TTS endpoint + speech tags, pricing, limits.
- **[best-practices.md](best-practices.md)** — writing each section, persona and speaking style, turn length, sample phrases, numbers and codes, unclear input, language lock, tool phrasing and confirmation, escalation and safety paths, common mistakes table.
- **[continuity-and-references.md](continuity-and-references.md)** — agent manifests, persona bibles, keeping voice and behaviour consistent across sessions and versions, resumption, per-turn overrides, custom voices for brand identity, migrating from grok-voice-2.0.
- **[examples.md](examples.md)** — annotated instruction sets: receptionist, support with tools, sales qualifier, in-car assistant, tutor, dialogue rehearsal partner, game NPC, bilingual line, crisis-aware wellness line, supervisor pattern, SIP after-hours, TTS scripted line.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
