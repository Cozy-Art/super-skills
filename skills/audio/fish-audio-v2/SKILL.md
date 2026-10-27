---
name: fish-audio-prompts
description: Generate optimized scripts and API payloads for Fish Audio text-to-speech — S2.1-Pro (s2.1-pro, s2.1-pro-free), Drama 3 (drama-3), S2-Pro and legacy S1 — plus voice cloning, Voice Design and multi-speaker dialogue. Use whenever a user mentions Fish Audio, fish.audio, OpenAudio, Fish Speech, S2.1-Pro, S2-Pro, Drama 3, or wants expressive TTS, voiceover, audiobook narration, voice-agent speech, cloned or designed voices, bracketed emotion cues like [whispering], <|speaker:N|> dialogue, pronunciation/phoneme control, or POST /v1/tts payloads — including via OpenRouter, ComfyUI or other wrappers. Also use when migrating S1 (parenthesis) scripts before the December 31, 2026 retirement. Do not guess Fish Audio syntax from general knowledge or older S1 / Fish Speech habits.
---

# Fish Audio TTS — Prompt Generation Skill

Fish Audio turns a **script** (spoken text + inline performance cues) into speech in a chosen voice. One endpoint, `POST https://api.fish.audio/v1/tts`; the `model` **header** picks the engine. Voice identity comes from a voice model ID (`reference_id`), never from the script.

**Scope:** speech only. No music, no ambience beds, no spatial mixing, no duration control. Sound design and room acoustics happen in post.

## The Three Rules That Override Everything

1. **The script is the prompt — direction goes in brackets, everything else is spoken.** S2-family and Drama 3 read `[free-form direction]` as performance; any un-bracketed stage direction will be read aloud. Describe *sound and delivery*, never visuals.
2. **Voice lives in `reference_id`, not in words.** `[deep male voice]` won't replace the timbre of the reference. Create a voice model once, reuse its ID for every take. Same ID + same model + same settings = continuity.
3. **Always set the `model` header explicitly.** A missing or misspelled header silently falls back to `s2.1-pro` (no error); the Python SDK defaults to `s2-pro`, the JS SDK to deprecated `s1`. S1 uses `(parentheses)` — those are not converted on S2/Drama 3.

## Pick the Model First

| Need | `model` header | Why |
|---|---|---|
| Production default: apps, agents, narration | `s2.1-pro` | Best all-round; TTFA + DPA guarantees; 83 languages |
| Free testing / prototypes | `s2.1-pro-free` | Same model, $0, no TTFA/DPA guarantees |
| Acted, directed, scripted performance (drama, trailers, games) | `drama-3` | Closest adherence to direction; adds scoped `<whisper>…</whisper>`-style tags. Not positioned for live conversation |
| Existing S2 integration | `s2-pro` | Previous gen; same bracket syntax |
| Legacy only | `s1` | Deprecated, retires Dec 31, 2026 → migrate |

## Script Structure (order within a line)

| # | Layer | Example |
|---|---|---|
| 1 | Speaker tag (dialogue only) | `<|speaker:0|>` |
| 2 | Sentence-level direction | `[quietly reassuring, speaking to a frightened child]` |
| 3 | Spoken text with deliberate punctuation | `You're safe now. Take one slow breath with me.` |
| 4 | Inline sounds / pauses where they happen | `[sighing]` `[break]` `[long-break]` `[shaky breath]` |
| 5 | Word-level stress | `[emphasis] Friday` (S2) · `<emphasis>Friday</emphasis>` (Drama 3) |

```
<|speaker:N|>[emotion + energy + relationship to listener] Spoken sentence. [sound] Next sentence.
```

- One primary emotion per sentence; never more than three combined. Put the cue at the **start** of the sentence it controls; put a new cue exactly where delivery changes.
- Cues are short, actor-brief style: `[deadpan, mildly inconvenienced]`, not a paragraph.
- Punctuation is the timing engine: periods = boundaries, commas = light breaths, ellipses = hesitation (sparingly), paragraph breaks = stronger separation.

## Decide the Operation

| User wants | Request shape |
|---|---|
| One voice, one line/paragraph | `text` + `reference_id: "<id>"` |
| Dialogue in one render | `text` with `<|speaker:0|>…<|speaker:1|>…` + `reference_id: ["id0","id1"]` (S2 family / Drama 3 only) |
| Reusable cloned voice | `POST /model` with clean audio → use returned `_id` as `reference_id` |
| One-off clone, no stored model | `references: [{audio, text}]` — **MessagePack only**, transcript required |
| Invent a voice from a description | `POST /v1/voice-design` (`model: voice-design-1`, `instruction`) → audition candidates → create model |
| Pin a name/term's pronunciation | `pronunciation_dictionary` or phoneme tags `<|phoneme_start|>…<|phoneme_end|>` |
| Long-form (chapters) | Split by scene/paragraph; `latency: normal`, `chunk_length` 250–300, `condition_on_previous_chunks: true` |
| Live agent | WebSocket / streaming; `latency: balanced`, smaller chunks, buffer 5–10 words |

## Quick Syntax Reference

- **Brackets (S2.1-Pro, S2-Pro, Drama 3):** `[happy]` `[whispering]` `[in a hurry tone]` `[laughing]` `[clear throat]` `[break]` `[long-break]` — or any free-form description. Cues don't count toward token limits.
- **Scoped tags (Drama 3 only):** `<whisper>` `<emphasis>` `<soft>` `<fast>` `<slow>` `<stress>` `<forceful>` — wrap only the affected words.
- **Language switch (Drama 3, experimental):** `<french>Un café, s'il vous plaît.</french>`
- **Speakers:** `<|speaker:0|>` = `reference_id[0]`, 0-based, in array order.
- **S1 legacy:** `(happy)` parentheses, fixed tag set. Never mix with brackets.

Full cue vocabulary, punctuation and pronunciation → [best-practices.md](best-practices.md).

## Output Format (always two parts)

1. **Script** — in a code block: the `text` value only (spoken words + bracket cues + speaker/scoped tags). Inline cues *are* Fish's native syntax, so they belong in the script; API settings never do.
2. **Suggested settings** — one line, e.g. `model: s2.1-pro · reference_id: <narrator> · temperature: 0.6 · top_p: 0.7 · speed: 0.95 · latency: normal · format: wav 44.1k`

For an API call, also give the JSON body with only documented fields, and the `model` header separately (it is a header, not a body field).

## Things That Will Break the Request (or Quietly Ruin It)

- `model` in the JSON body instead of the header → ignored; falls back to `s2.1-pro`.
- `references` sent as JSON → must be `application/msgpack`; each item needs `audio` **and** `text`.
- Stage directions without brackets → spoken aloud. `(happy)` on S2/Drama 3 → spoken or ignored.
- `<|speaker:N|>` with a single-string `reference_id`, or on `s1` → no multi-voice.
- Scoped `<whisper>` tags on `s2.1-pro` → not documented there; treat as Drama-3-only.
- Inventing fields: there is no `seed`, `duration`, `emotion`, `voice_id`, `speed` (top level), `pitch` or `style` on `/v1/tts`. Speed lives in `prosody.speed` (0.5–2.0).
- `sample_rate` not valid for the format (e.g. 48000 with mp3) → use the format table in `parameters.md`.

## Iteration Workflow

1. Lock voice first: create/approve the voice model; note its ID.
2. Test 2–3 representative lines at `temperature/top_p 0.7/0.7`, `s2.1-pro-free` if budget matters.
3. Fix delivery with cue wording and punctuation before touching sampling.
4. Identity or pronunciation drifting → lower `temperature`, then `top_p`. Too flat → raise slightly or switch the line to `drama-3`.
5. Render 2–4 takes only for high-emotion lines; pick the best (no seed — takes are not reproducible).
6. Save the exact request JSON + model header with every approved file.

## Drama 3 Has Its Own Skill

This skill covers Drama 3 as one hosted `model` option inside a general Fish Audio workflow. For Drama 3-specific work — long multi-character scenes (up to 16 speaker IDs), acting-objective direction, point events, the open `fishaudio/drama-3` checkpoint on Fish Speech / SGLang-Omni, take revision and infilling, or ComfyUI `@VoiceN` labels — use the dedicated **drama-3-prompts** skill (`audio/drama-v3`).

## Reference Files

- **[parameters.md](parameters.md)** — every `/v1/tts` header/body field, formats and sample rates, latency/chunking, prosody, presets, voice-model and Voice Design endpoints, pricing, concurrency, S1 migration table.
- **[best-practices.md](best-practices.md)** — cue vocabulary, placement, intensity, punctuation, pronunciation/phonemes, Drama 3 scoped tags, dialogue blocking, common-mistakes table.
- **[continuity-and-references.md](continuity-and-references.md)** — cloning references, voice bibles, cross-take consistency, long-form chunking, pickups, multi-speaker casting, handoff to video/edit.
- **[examples.md](examples.md)** — annotated scripts: narration, agent, documentary, action, dialogue, Drama 3 scoped tags, pronunciation, Voice Design, S1 migration, MessagePack zero-shot.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
