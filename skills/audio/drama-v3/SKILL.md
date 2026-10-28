---
name: drama-3-prompts
description: Write directed scripts and request payloads for Fish Audio Drama 3 (hosted model header drama-3, open checkpoint fishaudio/drama-3, Fish Speech / SGLang-Omni / vLLM-Omni runtimes, ComfyUI Fish Audio node, OpenRouter fish-audio/drama-3). Use for multi-character scenes with up to 16 speaker IDs, <|speaker:N|> scripts, ComfyUI @Voice1 scripts, acting-objective bracket direction, point events like [shaky breath], paired word tags (<whisper>, <emphasis>, <slow>, <forceful>), experimental language tags (<french>), phoneme tags, voice cloning with reference transcripts, long-form scene chunking, take revision from director notes, and infill-style line corrections. Use when a user mentions Drama 3, Fish Drama 3, drama-3, fishaudio/drama-3, or wants acted audio drama, game, animation or film dialogue from Fish Audio. Do not guess Drama 3 syntax from S1/S2 habits, general TTS knowledge or ComfyUI wrapper syntax.
---

# Fish Audio Drama 3 — Script & Prompt Generation Skill

Drama 3 is Fish Audio's 35B-A3B mixture-of-experts speech model (3B active per token), built for directed, multi-character performance: one script carries every speaker, plain-language direction, timed vocal events and word-level tags. It is served hosted (`model: drama-3` header on `POST https://api.fish.audio/v1/tts`) and as open weights (`fishaudio/drama-3`) through Fish Speech, SGLang-Omni and vLLM-Omni. Fish labels it a **preview**: takes vary, so render a few and keep the best.

**Scope:** speech only — dialogue, narration, vocal events baked into the voice. No music, ambience beds, spatial mixing or duration control; those happen in post. For general Fish Audio TTS (S2.1-Pro, Voice Design, S1 migration) use a general Fish Audio skill.

## The Three Rules That Override Everything

1. **Direct the acting objective, not a tag pile.** One coherent bracket per beat — `[angry with himself, talking too fast to hide the fear]` — beats `[angry] [sad] [afraid] [fast]`. A bracket applies from where it appears until the next direction. Anything un-bracketed is spoken aloud.
2. **The speaker number is the role.** Assign one fixed ID (0–15) per character for the whole project and never reuse it. Voice identity binds to that ID through the payload (`reference_id` array order, or reference-to-speaker mapping on open runtimes) — never through words like `[deep male voice]`.
3. **Write the syntax of the surface you are sending to.** Native `<|speaker:N|>` for the Fish API and open runtimes; `@Voice1…@Voice5` only for the ComfyUI node. Revision and infilling need prior-take history in context — a stateless request with the old text is just a new take. Say which you are producing.

When the user's interface or API rejects or contradicts a value here, the interface wins — adjust and say so.

## Pick the Surface First

| Surface | Selects Drama 3 by | Speakers in text | Revision / infill |
|---|---|---|---|
| Fish API `/v1/tts` | header `model: drama-3` (missing/misspelled → silent `s2.1-pro`) | `<|speaker:N|>`, index = `reference_id[N]` | Not exposed — no history fields |
| Fish Speech server / CLI | checkpoint loaded at startup (no per-request model) | `<|speaker:N|>`; reference mapped per speaker (`--reference_speaker`) | Not documented |
| SGLang-Omni `/v1/tts` | `--model-path fishaudio/drama-3` | `<|speaker:N|>` | Editing as continuation via `previous_takes` |
| vLLM-Omni `/v1/audio/speech` | `model: fishaudio/drama-3` | `<|speaker:N|>`; untagged text = speaker 0 | Not exposed yet |
| ComfyUI Fish Audio TTS node | `model: drama-3` | `@Voice1`…`@Voice5` (≤5 voices; every connected voice must appear) | Not covered |
| OpenRouter | `fish-audio/drama-3` | inline tags in `input`; one `voice` | None |

## Script Structure (priority order)

| # | Layer | Example |
|---|---|---|
| 1 | Speaker | `<|speaker:1|>` |
| 2 | Acting objective — intention, emotion, listener, pace | `[trying to reassure him without revealing the danger]` |
| 3 | Spoken text, punctuation as timing | `It's nothing. Go back to sleep.` |
| 4 | Point events exactly where they land | `[shaky breath]` `[a short, disbelieving laugh]` `[long pause]` |
| 5 | Word-scoped exceptions | `<slow>do not open the door</slow>` |
| 6 | Language / pronunciation spans | `<french>…</french>` · `<|phoneme_start|>…<|phoneme_end|>` |

```
<|speaker:N|> [intention + emotion + listener + pace]
Spoken line with <emphasis>one controlled phrase</emphasis>. [point event] Continuation.

<|speaker:M|> [new direction]
Response.
```

## Decide the Operation

| User wants | Write |
|---|---|
| One voice, directed read | Brackets + text; single `reference_id` / reference |
| Scene with 2–16 characters | One script, `<|speaker:N|>` per turn, fixed cast map |
| Same line, different performance (any surface) | New take: rewrite the bracket, keep words identical |
| Revision of an accepted take (history-capable surface) | Note **relative to the previous take** + same line: `[softer and warmer than the previous take, keep the timing]` |
| Fix one word/phrase inside an accepted take | Full corrected line + "change only X" note, sent with the prior take(s) as history — or re-render with a sentence of context either side and cut |
| Long scene / chapter | One request; let the runtime chunk (~300 bytes, ≤3 speakers per chunk) |
| Exact pronunciation | Phoneme tags or a pronunciation dictionary |

## Quick Syntax Reference

- **Direction:** `[free-form, any language]` — persists until the next bracket. Short, one clause.
- **Point events:** `[sighs]` `[laughs]` `[gasps]` `[swallows]` `[voice breaks]` `[brief pause]` — open vocabulary; concrete physical description wins.
- **Paired tags (7 documented):** `<whisper>` `<emphasis>` `<soft>` `<fast>` `<slow>` `<stress>` `<forceful>` — wrap only the affected words.
- **Language tags (experimental):** `<french>` `<spanish>` `<german>` `<japanese>` `<chinese>` `<korean>` `<italian>`.
- **Phonemes:** `<|phoneme_start|>EH1 N JH AH0 N IH1 R<|phoneme_end|>` — Arpabet (English), pinyin, romaji.
- **Speakers:** `<|speaker:0|>`…`<|speaker:15|>` (native) · `@Voice1`… (ComfyUI only).

Craft, failure fixes → [best-practices.md](best-practices.md). Cast maps, references, revision chains → [continuity-and-references.md](continuity-and-references.md).

## Output Format (always two parts)

1. **Script** — in a code block: the `text` / `input` value only (speaker tags, brackets, paired tags, spoken words). Drama 3's inline tags are its native syntax and belong here; settings never do.
2. **Suggested settings** — one line, e.g. `surface: Fish API · model: drama-3 · reference_id: [<mara>, <sol>] · temperature: 0.7 · top_p: 0.7 · format: wav 44.1k · takes: 3`

For an API call, also give the body with documented fields only; on the Fish API the model is a **header**, not a body field.

## Things That Will Break the Request (or Quietly Ruin It)

- `@Voice1` sent to the Fish API or an open runtime → spoken or ignored. `<|speaker:N|>` in the ComfyUI node → use `@VoiceN`.
- Speaker numbers reshuffled between scenes, or a number reused for a new character → voices swap.
- Inline `references` as JSON on the Fish API → must be MessagePack, each item with `audio` **and** exact `text`.
- Unclosed brackets or paragraph-long directions → rhythm breaks; direction may be read aloud.
- Opening a line with a point event or filler (`[laughs] Um…`) → some serving stacks report trailing silence to `max_new_tokens`; lead with a direction or a word.
- Promising revision/infill on a stateless endpoint → it is a fresh take; say so.
- Manually splitting a scene into unrelated calls → loses the pinned first chunk and generated history that keep voices stable.
- Inventing fields: no `seed`, `duration`, `emotion`, `top_k` or `voice_id` on the Fish API; `repetition_penalty` is ignored by Drama 3; `chunk_length` does not drive Drama 3's chunker on Fish Speech.

## Iteration Workflow

1. Freeze the cast map (ID → character → voice) and the voice references first.
2. Render 2–3 candidates of a representative exchange at `temperature`/`top_p` 0.7/0.7.
3. Fix acting with bracket wording, event placement and punctuation before touching sampling.
4. Drift or instability → lower `temperature` (0.5–0.6). Flat → add intention, listener and physical state; then 0.8.
5. On a history-capable surface, revise from the accepted take with relative notes; elsewhere re-take and pick.
6. Keep lossless masters plus the exact script, settings, cast map and surface for every approved take.

## Reference Files

- **[parameters.md](parameters.md)** — Fish API header/body fields for `drama-3`, Fish Speech server and CLI fields, sampling defaults and ranges, frame-budget arithmetic, chunking constants, SGLang-Omni / vLLM-Omni / ComfyUI / OpenRouter field maps, hardware, pricing status, licence.
- **[best-practices.md](best-practices.md)** — acting-objective direction, point events, paired tags, language and phoneme tags, punctuation, scene blocking, revision-note phrasing, failure-mode fixes table.
- **[continuity-and-references.md](continuity-and-references.md)** — cast maps and speaker IDs, reference recording and transcripts, multi-clip references, long-form chunk history, revision chains and infill, take records, handoff to edit.
- **[examples.md](examples.md)** — 11 annotated scripts: monologue, emotional turn, confrontation, action, narration, multilingual, ComfyUI scene, five-character scene, revision note, infill correction, phoneme lock.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
