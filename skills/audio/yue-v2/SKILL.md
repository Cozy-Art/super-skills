---
name: yue-2-prompts
description: Generate optimized style prompts, structured lyrics and request payloads for YuE2 (m-a-p/YuE2-3B), the open lyrics-to-song model from M-A-P/HKUST that plans melody and chords as editable ABC notation before rendering 48 kHz stereo audio. Use whenever a user mentions YuE2, YuE 2, YuE2-3B, m-a-p/YuE2, the YuE2Pipeline, ComfyUI's YuE2 Generate ABC / Generate Music nodes, DiffSynth-Studio YuE2, or MachGen's YuE2-3B T2M endpoint, or wants a full song with vocals from lyrics, an instrumental, a score-conditioned cover (SheetSage2 to ABC), an edited-score re-render, or reproducible A/B song variations with an open-weights model. Also use when migrating YuE v1 genre.txt / run_n_segments / ICL workflows to YuE2. Do not guess YuE2 syntax from YuE v1, Suno or other music models.
---

# YuE2 — Prompt Generation Skill

YuE2 is a ~3B open-weights song model: **style text + lyrics in, 48 kHz stereo song out**, with an optional human-readable ABC score in the middle that you can save, edit and re-render. It is not YuE v1 — no stages, no 30-second sessions, no `genre.txt` tag soup.

**Scope:** music only. No aspect ratio, resolution, camera, image or video controls exist. Visual ideas ("close-up", "crane reveal") only work translated into arrangement and mix language.

## The Three Rules That Override Everything

1. **Two fields, never mixed.** Style (genre, voice, instruments, mood, tempo, production) goes in `style`/`prompt`. Only singable words and bracketed section tags go in `lyrics`. Production notes in lyrics get sung.
2. **The score is the continuity, not the prose.** To keep a melody, chords or form, reuse or edit the ABC (`abc=` + `cot="full"|"melody"`). Re-describing a melody in words gives you a new song.
3. **Use only the controls your interface exposes.** Native/ComfyUI expose `cot`, `abc`, `seed`, sampling, CFG. MachGen exposes `prompt`, `lyrics`, `force_instrumental` — and nothing else YuE2-specific. Never borrow fields from other models.

## Prompt Order

**Style field** — one compact comma-separated line, 20–60 words (practical heuristic, no official max):

| # | Layer | Example |
|---|---|---|
| 1 | Language | `English` / `Mandarin` |
| 2 | Primary genre (+ one compatible influence) | `dream pop with shoegaze guitars` |
| 3 | Vocal identity or instrumental lead | `breathy female alto` · `Instrumental, solo cello lead` |
| 4 | 2–5 defining instruments, with roles | `chorus guitar, warm synth pads, melodic bass` |
| 5 | Rhythm / groove | `half-time drums`, `swung hi-hats`, `four-on-the-floor` |
| 6 | Mood + arrangement arc | `wistful, verses sparse, chorus opens wide` |
| 7 | Production texture | `dry close vocal, tape saturation, wide reverb` |
| 8 | Tempo | `102 BPM` (steering cue, not a transport lock) |

```
[LANGUAGE], [GENRE + INFLUENCE], [VOCAL / LEAD], [INSTRUMENTS], [GROOVE],
[MOOD + ARC], [PRODUCTION], [BPM]
```

**Lyrics field** — section tag on its own line, short singable lines beneath, blank line between sections:

```
[Verse]
two to four short lines

[Chorus]
the hook, repeatable
```

Default form: 4–6 sections (`[Verse]` `[Pre-Chorus]` `[Chorus]` `[Bridge]` `[Outro]`). Add `[Outro]` so the song resolves instead of being cut.

## Decide the Operation First

| User wants | Interface | `cot` | `abc` | Lyrics |
|---|---|---|---|---|
| Original song, editable result | Native / ComfyUI | `full` (default) | none (model plans) | Full sectioned lyrics |
| Fast loose ideation | Native (`off`) / ComfyUI (empty ABC) | `off` | none | Compact |
| Keep melody, change arrangement/genre (cover) | Native / ComfyUI | `melody` | reviewed SheetSage2 `--melody-only` score | Aligned to score sections & syllables |
| Keep melody **and** harmony | Native / ComfyUI | `full` | score with chord symbols | Aligned |
| Edit one note/chord/section, re-render | Native / ComfyUI | as baseline | edited copy of saved `score.abc` | Same as baseline |
| Hosted vocal song | MachGen T2M | not exposed | not exposed | 400–10,000 chars |
| Hosted instrumental | MachGen T2M | not exposed | not exposed | empty or bare tags + `force_instrumental: true` |

## Quick Syntax Reference

- **Section tags:** `[Intro] [Verse] [Pre-Chorus] [Chorus] [Bridge] [Final Chorus] [Outro]`; instrumental cues as standalone tags: `[Guitar Solo]`, `[Build]`, `[Drop]`, `[Breakdown]`. Reinforce any instrumental passage in style too.
- **Singer hints:** `[Verse - Voice A]`, `[Chorus - Together]` are soft hints, not voice routing. If the label gets sung or roles merge, simplify.
- **`cot`:** `full` = melody + chord plan · `melody` = melody-only plan (covers) · `off` = no score. Supplying `abc` requires `full` or `melody`.
- **ComfyUI:** `mode` offers only `full`/`melody`; an **empty `abc` string silently forces `off`**.
- **DiffSynth-Studio** names the style field `prompt`, not `style`.
- Full parameter tables → [parameters.md](parameters.md).

## Output Format (always two parts)

When producing a prompt for the user, return:

1. **Prompt** — code blocks containing prompt text only: a **Style** block and a **Lyrics** block (or bare section tags for instrumentals). Section tags and the BPM/language words belong in the text because YuE2 has no separate tempo, structure or language parameter — that is the model's real input syntax, not a settings leak.
2. **Suggested settings** — one line, e.g. `cot: full · seed: 831001 · cfg_scale: 1.0 · max_duration: 240 s · interface: native` or `MachGen T2M · force_instrumental: false · seed: 831001`

Never put `cot`, `seed`, CFG, sampling, duration or output format inside the style or lyrics text. If the user is building a call, also give the Python call or JSON payload using only that interface's valid fields.

## Things That Will Break the Request

- **MachGen:** vocal lyrics under 400 or over 10,000 characters are rejected before generation. Don't send `duration_secs` (docs: omit for YuE2), `cot`, `abc`, `cfg_scale` or sampling fields. A too-long score fails with `status: FAILED` and *"Score limit reached…"* — shorten lyrics or simplify style. Tracks over ~6 min are truncated but return as success.
- **Native/ComfyUI:** `abc` with `cot="off"`; long style + lyrics + ABC eat the 24,576-position shared context and shorten (or truncate) the song; `max_duration` is a ceiling, not a target.
- **YuE v1 carry-overs:** `--run_n_segments`, `--stage1_model`, `--stage2_model`, `--stage2_batch_size`, `--max_new_tokens`, `--use_audio_prompt`, `--use_dual_tracks_prompt`, `--*_track_prompt_path`, `--prompt_start_time/--prompt_end_time`, `genre.txt`/`lyrics.txt` — none exist in YuE2.
- **Other-model fields:** `aspect_ratio`, `width`/`height`, `negative_prompt`, `duration`, `voice_id`, `composition_plan`, image/audio reference URLs.
- **Content:** asking it to sound exactly like a named living artist — describe the audible traits instead. Covers need rights to the source song and lyrics.

## Iteration Workflow

1. Draft with `cot="full"`, default sampling, fixed seed, one 25–50-word style line, 4–6 short sections.
2. Save everything — native `song.save_artifacts(dir)` writes audio, `score.abc`, tokens, latents and settings.
3. Diagnose by layer: wrong genre/voice → edit style · wrong words/phrasing → edit lyrics · wrong melody/chords/form → edit the ABC · good song, wrong performance → new seed with same ABC.
4. Change **one** category per run; keep seed, revisions and sampling fixed for real A/B.
5. When quality matters, render several seeds and pick (the YuE2 report's best-of-8 beat single-sample scores).
6. Decoder check: compare `YuE2-Vae` (default, better perceptual quality) vs `YuE2-Vae-legacy` (paper benchmark) on the **same** saved latent, not a new generation.

## Reference Files

- **[parameters.md](parameters.md)** — native pipeline, ComfyUI nodes, DiffSynth-Studio, MachGen fields; ranges, defaults, hardware, output spec, pricing, licence, v1 migration table.
- **[best-practices.md](best-practices.md)** — style-line craft, lyric density and section design, instrumentals, visual-to-musical translation, BPM/meter, common mistakes table.
- **[continuity-and-references.md](continuity-and-references.md)** — artifact bundles, ABC editing, covers via SheetSage2, vocal/sonic consistency, album and score-suite continuity, leitmotif libraries.
- **[examples.md](examples.md)** — 10 annotated requests: vocal song, instrumental landscape, action cue, mix-movement build, mood arc, duet, cover, score edit, MachGen payloads, v1 migration.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
