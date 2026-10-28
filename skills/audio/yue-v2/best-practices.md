# YuE2 — Best Practices

## 1. The Style Line: Audible Evidence Over Adjectives

One compact comma-separated line. Every term should name something a listener could point to.

| Weak | Better |
|---|---|
| `cinematic` | `wide stereo strings, low brass swells, taiko hits, slow crescendo` |
| `sad song` | `minor-key piano ballad, restrained tempo, sparse arrangement, fragile close vocal` |
| `good vocals` | `clear tenor, intimate dry close-mic delivery, light vibrato on held notes` |
| `vintage` | `1970s soul, tape saturation, room-mic drums, Wurlitzer, plate reverb` |
| `epic EDM` | `progressive house, side-chained supersaw chords, four-on-the-floor kick, riser into a big drop, 126 BPM` |
| `chill` | `lo-fi hip hop, dusty swung drums, muted Rhodes, vinyl crackle, 78 BPM` |

Name **roles**, not just instruments: "muted trumpet lead", "Rhodes comping", "syncopated electric bass", "cello ostinato".

## 2. Genre Discipline

- **One primary genre + at most one compatible influence.** "Dream pop with shoegaze guitars" is a sound; "jazz, metal, reggaeton, ambient" is noise.
- **Fusions as progressions.** Write contrast as a deliberate arc: "acoustic folk verses building into a controlled future-bass chorus" — not "sparse folk maximalist EDM".
- **Language first.** Start with `English`, `Mandarin`, etc. It steers pronunciation more reliably than leaving it implicit. English and Chinese are confirmed; other languages are unverified.

## 3. Vocal Identity

Without a vocal descriptor the singer varies widely between seeds. Give register + texture + delivery:

```
breathy female alto · gritty baritone · bright clear tenor · smoky contralto
mezzo-soprano with wide vibrato · soft male falsetto · gospel choir backing
duet: low male tenor and bright female alto · Instrumental, no vocals
```

There is **no voice-ID, voice-clone or singer-reference parameter**. Text description + a saved score + fixed seed is the whole toolkit (see continuity file).

## 4. Lyrics: Density and Form

- Section tag on its **own line**; **blank line** between sections.
- 2–4 lines per verse, 2–4 per chorus; lines of ~5–9 syllables sing cleanly. Dense prose rushes phrasing and blurs diction.
- Repeat the chorus text exactly when you want a recognisable hook.
- End with `[Outro]` (or a short `[Final Chorus]` + `[Outro]`) so the song resolves before the duration ceiling.
- Keep everything inside lyrics singable. Stage directions ("guitar gets louder here") will be sung — put them in style, or use a standalone tag like `[Guitar Solo]`.
- Too many words for the budget → truncated ending. Fewer, shorter sections fix it; on MachGen also watch the 400-char minimum for vocal songs (pad with real sections, not filler).

Useful tags: `[Intro] [Verse] [Pre-Chorus] [Chorus] [Post-Chorus] [Bridge] [Final Chorus] [Outro]` and instrumental cues `[Build] [Drop] [Breakdown] [Guitar Solo] [Interlude]`. YuE v1 found `[Intro]` less stable as a first section — if openings wobble, start on `[Verse]` and describe the intro in style instead (v1-era evidence; re-test on YuE2).

## 5. Instrumentals

- State it twice: style begins `Instrumental …` and ends `… no singing`.
- Lyrics = bare section tags (blank-line separated) or empty.
- MachGen: add `force_instrumental: true`. Vocals/humming can still appear — regenerate with a new seed if so.
- Give the arc a structure: `[Intro] [Build] [Climax] [Outro]` maps an energy curve the model can follow.

## 6. Tempo, Meter, Key

- `102 BPM` in style is **steering**, not a click track. Pair it with groove words (half-time, swung, breakbeat, rubato).
- Odd meters (`7/8`), exact key, tempo changes, modulations: prose gets you close sometimes; the **ABC score** gets you there reliably. Generate a plan, then edit `K:`, `M:`, `Q:` and the notes in the ABC.
- Don't stack tempo cues ("slow ballad, 160 BPM, energetic").

## 7. Visual Concepts → Musical Language

YuE2 has no camera. When briefs arrive in film language, translate:

| Visual idea | Musical analogue | Style wording |
|---|---|---|
| Close-up | Intimate vocal foreground | `dry close-mic alto, sparse accompaniment, breath detail` |
| Wide landscape | Broad soundstage, slow harmony | `wide stereo strings, distant horn, slow harmonic rhythm, long reverb tail` |
| Action sequence | Rhythmic density, rising dynamics | `driving ostinato, accelerating percussion layers, impact accents` |
| Tracking shot | Continuous handoff | `motif passes from cello to synth to guitar without stopping` |
| Crane reveal | Register + orchestration expansion | `begins mono and low, opens into full stereo choir and high strings` |
| Montage | Short contrasting sections, one motif | Reuse one hook across brief verse/chorus blocks |
| Match cut | Shared tone across a section break | `each section ends on a sustained note that becomes the next lead` |

## 8. Controls: When to Touch What

- **`cot`:** stay on `full` unless you have a reason. `melody` for covers/heavy restyle; `off` for quick, loose sketches (no editable score).
- **`cfg_scale`:** leave at 1.0. Try 1.2 only if style or lyrics are being ignored.
- **Sampling (ComfyUI):** defaults first. Lower temperature for steadier takes; higher for variety. Raising `repetition_penalty` well above 1.2 discourages loops but can break chorus repetition.
- **Seeds:** vary seed to explore performances; fix seed to compare edits.
- **Best-of-N:** render several seeds and choose — selection measurably beats a single sample.

## 9. Common Mistakes

| Mistake | Symptom | Fix |
|---|---|---|
| Production notes inside lyrics | Instructions sung aloud | Move to style; use standalone `[Solo]`-type tags |
| Too many words per section | Rushed phrasing, slurred diction, cut ending | Shorter lines, fewer sections, add `[Outro]` |
| Genre salad | Generic, unstable identity | One genre + one influence, or a written progression |
| No vocal descriptor | Singer changes every take | Register + texture + delivery |
| Section label on same line as lyrics | Tag sung or ignored | Tag alone on its line, blank line between sections |
| Re-describing a melody in prose | New melody each time | Reuse/edit saved ABC |
| `abc` with `cot="off"` | Error / score ignored | `cot="full"` or `"melody"` |
| Empty ABC in ComfyUI expecting `full` | Silently runs `off` | Wire Generate ABC output or paste a score |
| Instrumental still sings | Humming/vocals | Instrumental in style + bare tags + `force_instrumental` + reroll |
| MachGen lyrics < 400 chars | Rejected | Add real sections, or go instrumental |
| `duration_secs` on MachGen | Not supported for YuE2 | Omit; control length with lyric amount |
| "Sounds exactly like [living artist]" | Policy/quality issues | Describe timbre, era, instrumentation |
| Changing seed + style + lyrics at once | Can't tell what helped | One variable per run |
| v1 flags (`--run_n_segments` …) | Unknown args | Use YuE2 fields only |
