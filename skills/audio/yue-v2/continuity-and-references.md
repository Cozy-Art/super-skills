# YuE2 — Continuity & References

In music, continuity means the **same song identity across takes and edits** (melody, harmony, form, lyrics), **the same voice and sonic world across tracks** (vocal timbre, ensemble, mix space), and **recurring motifs across a project**. YuE2's unique tool for this is the ABC score: the composition is a text file you can keep, diff and edit.

There is no voice clone, singer ID, audio-reference or "previous generation" parameter. Continuity = saved score + identical text + fixed seed + pinned revisions.

## 1. Housekeeping That Makes Continuity Possible

- Native: always `song.save_artifacts("outputs/<name>")` — writes `audio.flac`, `score.abc` (when `cot` ≠ `off`), plan, semantic tokens, latents, effective settings.
- ComfyUI: save the Generate ABC output text to a file; record seed, mode, sampling values and checkpoint.
- MachGen: no score is returned — save the exact request JSON (prompt, lyrics, seed) and the downloaded FLAC.
- Pin model + VAE revisions. A fixed seed is only reproducible on the same runtime, GPU class, settings and revisions.
- One output folder per version (`v01-full-seed831001/`, `v02-chorus-edit/`) — never overwrite.

## 2. Song Identity Across Takes

| Want to keep | Hold fixed | Free to change |
|---|---|---|
| Melody + harmony + form | ABC (with chords), `cot="full"` | seed, style, sampling |
| Melody only | ABC melody, `cot="melody"` | style (genre/instrumentation), harmony |
| A specific performance | ABC, seed, style, lyrics, sampling, revisions | — (re-render still varies slightly) |
| Genre/sound, new song | style line, seed range | lyrics, score |

## 3. Editing a Score

1. Generate with `cot="full"` and save artifacts (or `pipe.plan(...)` → `plan.save(dir)`).
2. Copy `score.abc` → `edited.abc`. Edit only what you mean to change: a note run, a chord, `K:` key, `M:` meter, `Q:` tempo, a repeated section.
3. Re-render with `abc=edited.abc`, same `cot`, seed, style, lyrics.
4. For reharmonisation, keep melody pitches and rhythm intact and change chord symbols only.
5. If lyrics change, preserve section order and approximate syllable counts per line so words still fit the notes.

The exact voice labels and header layout of YuE2's ABC dialect (often described as separate vocal and instrumental voices) are best read from your own generated `score.abc` — edit in the same dialect the model wrote. *(Voice naming unverified — confirm on your platform.)*

## 4. Covers via SheetSage2 (official workflow)

1. Separate environment: install `m-a-p/SheetSage2` (Python 3.10/3.11, FFmpeg 6.1 shared libs). Run it and YuE2 sequentially on one GPU.
2. Transcribe: `python models/SheetSage2/infer.py source.wav --output cover-score --melody-only` → `cover-score/score.abc` (vocal + instrumental melodies, **no chord symbols**).
3. Review while listening to the source: notes, meter, section order. Transcription errors carry into the cover.
4. Lyrics: source lyrics (where you hold rights) or a translation matched to melody syllables; tag sections to match the score order.
5. Render: `examples/generate.py --request cover-request.json --abc-file cover-score/score.abc --cot melody --output outputs/cover` (or `pipe(..., abc=..., cot="melody")`).
6. Want the original harmony too? Use a score **with** chord symbols and `cot="full"`. `melody` mode does not strip chords from a score that has them.

This is score-conditioned cover generation — not waveform continuation. The source's timbre and production are not copied; only the composition.

## 5. Vocal & Sonic Consistency Across Tracks

Write a **sound bible** once and paste it verbatim into every style line in the project:

```
SOUND: English, nocturnal synth-pop, intimate breathy female alto, analog
pads, pulsing mono bass, restrained electronic drums, wide reverb, tape warmth
```

Then append only the track-specific part (mood, tempo, arc): `…, hopeful lift in final chorus, 104 BPM`.

- Keep the vocal descriptor textually identical — "breathy female alto" ≠ "soft female voice".
- Keep ensemble, mix perspective and BPM range consistent.
- Use a small seed pool that has produced the right voice; reuse those seeds for new songs.
- Vocal timbre is still probabilistic. Audition multiple seeds and keep the ones that match.

## 6. Album / Game Score / Film-Suite Continuity

Treat a multi-track project like multi-shot coverage:

- **Leitmotif library:** an ABC file per character, place or faction (`motif-hero.abc`). Paste a motif into a track's score and change key/tempo/register/orchestration around it.
- **Section vocabulary:** same tag names and lyric point-of-view across the album.
- **Transitions:** end track A on a sustained note/chord that opens track B; encode both ends in ABC for an exact segue.
- **Variation sets:** same score, different style lines → menu theme / combat / ambient versions of one cue.
- **Archive:** prompt, lyrics, score, seed, revisions and audio for every keeper.

## 7. Hosted (MachGen) Continuity

No score, `cot` or ABC is exposed. You can only fix `prompt`, `lyrics` and `seed`. For true composition continuity across edits, move the project to the native pipeline or ComfyUI.

## 8. Handoff

- **To a DAW:** output is a full stereo mix (48 kHz FLAC); no stem export is documented for YuE2. Use a separate source-separation tool if stems are needed.
- **To video:** generate the song first, then cut picture to it — YuE2 does not take timestamps or picture-sync points, and section timing is not guaranteed.
- **From v1 projects:** keep lyrics and tag vocabulary; rewrite `genre.txt` tags as one descriptive style line; re-baseline seeds.
