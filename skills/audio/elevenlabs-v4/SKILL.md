---
name: eleven-v4-prompts
description: Write performance-ready scripts and API payloads for ElevenLabs Eleven v4 and Eleven v4 Turbo text-to-speech (model IDs eleven_v4, eleven_v4_turbo). Use whenever a user mentions Eleven v4, ElevenLabs v4, v4 Turbo, eleven_v4, or wants expressive voiceover, audiobook or long-form narration, character acting, multi-speaker dialogue (Text to Dialogue), voice-agent or game NPC lines, multilingual localization, IPA pronunciation fixes, audio tags like [whispers] or [sighs], audio effects (reverb, distance, pan), or voice consistency across lines, scenes and sessions — in the ElevenLabs app, ElevenCreative/Studio, the API, or ElevenAgents. Also use when migrating Eleven v3 / Multilingual v2 scripts, since SSML breaks, style and speed sliders do not apply to v4. Do not guess Eleven v4 syntax from general knowledge or older ElevenLabs model habits.
---

# Eleven v4 — Script & Prompt Generation Skill

Eleven v4 is ElevenLabs' newest speech model family (launched 28 Sep 2026). `eleven_v4` is the quality model for produced and long-form audio; `eleven_v4_turbo` is the same family tuned for real-time (~100 ms median inference). The "prompt" is the **spoken script** with inline natural-language **audio tags** in square brackets — there is no separate description field.

**Scope:** speech only. Voice is chosen by `voice_id`, not described into existence. Precise sound design, music and spatial mixing belong in separate generation or a DAW.

## The Three Rules That Override Everything

1. **Write for the ear.** Only words that should be spoken, plus directions that have an audible consequence. No visual language ("wide shot", "16:9", "cinematic"), no stage directions that can't be heard ([pacing], [grinning]).
2. **Direct with tags, punctuation and context — not sliders or SSML.** v4 exposes only Stability and Similarity. `style`, `speed`, `<break>`, `<prosody>` and `<phoneme>` do not apply. Pace and emotion come from the writing.
3. **Continuity lives in the voice ID and request stitching, not in description.** Lock `voice_id` + model + settings for a character; chain adjacent clips with `previous_request_ids` / `next_request_ids`. Don't re-describe the voice's age or timbre in every line.

## Script Order

| # | Layer | Example |
|---|---|---|
| 1 | Baseline delivery tag (once, at the top) | `[calm, intimate narration]` |
| 2 | The spoken line(s) | natural sentences, contractions, fragments |
| 3 | Local turn tags — only where performance changes | `[voice tightening]`, `[restrained alarm, pace quickening]` |
| 4 | Non-verbal reactions beside their moment | `[sighs]`, `[soft laugh]`, `[clears throat]` |
| 5 | Punctuation for rhythm | `…` hesitation · `—` interruption · CAPS for one stressed word |
| 6 | Pronunciation fixes | `"/æˈstɪəriən/"` slash-delimited IPA, or a dictionary |

```
[BASELINE: register, emotion, energy, pace] Spoken line. Spoken line…

[LOCAL CHANGE] Next phrase — interrupted. [REACTION] Final phrase.
```

**Length (characters, not tokens):** single TTS request ≤ 10,000 chars (~10 min) for `eleven_v4` · Text to Dialogue ≤ 2,000 combined chars per request · quality sweet spot 300–800 chars per generation; drop under 800 if artifacts appear.

## Decide the Operation First

| User wants | Model | Endpoint / transport | Notes |
|---|---|---|---|
| One voice, produced read | `eleven_v4` | Create/Stream speech `POST /v1/text-to-speech/{voice_id}` | Up to 10,000 chars; segment for QA |
| Multi-character scene | `eleven_v4` | Text to Dialogue `POST /v1/text-to-dialogue` (or `/stream`) | One `voice_id` per turn; ≤10 unique voices; ≤2,000 chars |
| Long-form narration / audiobook | `eleven_v4` | TTS or TTD, segmented + stitched | Request IDs between segments |
| Voice agent / NPC / live app | `eleven_v4_turbo` | TTD WebSocket `wss://…/v1/text-to-dialogue/stream-input` | **One registered voice per connection** on Turbo |
| Low-latency multi-voice | `eleven_v4` on TTD WebSocket (≤10 voices) or one Turbo socket per voice | TTD WebSocket | Trade latency vs voice count |
| Re-voice an existing performance | — | Speech-to-Speech / Voice Changer | Text prompts can't carry exact timing |
| Phone / radio / room colour | either | `audio_effects` field | Not in the script text |

Never use the ordinary TTS WebSocket (`/v1/text-to-speech/{voice_id}/stream-input`) for v4 — it does not accept v3/v4.

## Special Syntax (Quick Reference)

- **Audio tags:** `[natural language]` immediately before or after the words they modify. Open vocabulary, not an enum. Prefer explicitly vocal wording: `[low, gravelly voice]` beats `[gravel]` (could become a sound effect).
- **Combine compatible properties** in one tag: `[quiet, tired, slightly amused]`. Never stack contradictions.
- **Sound-event tags** (`[applause]`, `[door slams]`, `[explosion]`) work but are probabilistic — fine for drafts, render separately for timed production.
- **Pauses:** `…`, `—`, paragraph breaks, `[short pause]`, `[long pause]`. No SSML `<break>`.
- **IPA:** wrap in slashes, quote it, include stress marks: `"/ˌbaɪoʊˈkemɪstri/"`. Only on words that need it.
- **Dialogue:** one API turn per speaker change; tags go inside each turn's `text`. `Speaker 1:` labels are for drafting/UI only.

Full tag vocabulary, punctuation and normalization rules → [best-practices.md](best-practices.md).

## Output Format (always two parts)

Audio tags and IPA **are** inline syntax — they belong in the script. Everything else does not.

1. **Script** — in a code block: spoken words + inline tags + IPA only. Never put model, stability, similarity, output format, seed or effects in the text.
2. **Suggested settings** — one line, e.g. `model: eleven_v4 · stability: 0.45 · similarity: 0.75 · output: wav_48000 · voice: <character voice_id>`

For multi-speaker scenes, give the script as labelled turns (`NAME: [tag] line`) plus the `inputs` JSON. If the user is building an API call, give the payload with only valid fields (see [parameters.md](parameters.md)).

## Things That Will Break the Request

- SSML (`<break>`, `<prosody>`, `<phoneme>`) — unsupported on v4; may be spoken or ignored.
- Relying on `style` / `speed` in `voice_settings` — v4 exposes only Stability and Similarity; v3-era slider recipes won't transfer.
- Omitting `model_id` — Create speech defaults to `eleven_multilingual_v2`, Text to Dialogue to `eleven_v3`. Always send it.
- Dialogue over ~2,000 combined chars — may end early or fail validation. More than 10 unique `voice_id`s per dialogue request.
- Registering >1 voice on an `eleven_v4_turbo` TTD WebSocket.
- `previous_text` / `future_text` over 100 chars on dialogue.
- Stereo effects (reverb with `send_level` > 0, non-zero `pan`) with `pcm_*`, `ulaw_*` or `alaw_*` output → HTTP 400.
- `optimize_streaming_latency` — deprecated; use Turbo + TTD WebSocket.

## Iteration Workflow

1. Pick the voice first; audition 2–3 candidates on one representative line. The voice is the biggest variable.
2. Draft with one baseline tag, Stability ~0.5, Similarity ~0.75, `mp3_44100_128`.
3. Render 2–4 takes of important lines (generation is nondeterministic; `seed` is best-effort only).
4. Change **one** variable per pass: wording/punctuation → tag → Stability → voice.
5. Fix names with IPA or a pronunciation dictionary before the final pass.
6. Final at production format (WAV/PCM 44.1–48 kHz), keeping model + settings identical; log request IDs and stitch neighbours.
7. Loudness, EQ, spatialization, music and timed SFX in post.

## Reference Files

- **[parameters.md](parameters.md)** — every TTS / Text to Dialogue / WebSocket field, voice settings, continuity fields, audio effects, output formats + tier gates, limits, pricing, recommended presets, v3 → v4 migration.
- **[best-practices.md](best-practices.md)** — writing for ears, tag vocabulary by category, phrase-level direction, intensity gradients, punctuation, IPA, text normalization, voice selection, common mistakes table.
- **[continuity-and-references.md](continuity-and-references.md)** — production manifests, character voice bibles, request stitching, repairing middle clips, multi-scene beat sheets, cloning for consistency, cross-language accent behaviour, real-time session continuity.
- **[examples.md](examples.md)** — annotated scripts: character line, intimate beat, narration, action escalation, audio "camera move", two-hander dialogue, interruption, multilingual brand read with IPA, agent turn, audiobook segment stitch, regenerated middle clip, effects payload.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
