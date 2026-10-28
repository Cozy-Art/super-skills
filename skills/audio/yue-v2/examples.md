# YuE2 — Annotated Examples

Every example is two-part: **prompt** (Style block + Lyrics block) + **suggested settings**. Settings never appear in the text. All lyrics are original. On MachGen, Style → `prompt`, Lyrics → `audio_config.lyrics`; on DiffSynth-Studio, Style → `prompt`.

---

## 1. Intimate Vocal Song (default recipe)

**Style**
```
English indie folk, intimate warm baritone, fingerpicked acoustic guitar, soft upright bass, brushed snare, reflective and tender, close dry vocal, gentle room ambience, 82 BPM
```
**Lyrics**
```
[Verse]
I left the porch light burning
Though the road forgot your name
The kettle hums a little tune
It never sings the same

[Chorus]
Come home through the quiet
Come home before the rain
I kept a chair beside the fire
Come home through the quiet again

[Verse]
The orchard dropped its apples
The river took the bridge
I wrote you letters in the frost
Along the window ledge

[Chorus]
Come home through the quiet
Come home before the rain
I kept a chair beside the fire
Come home through the quiet again

[Outro]
The light is on, the light is on
```
**Settings:** `cot: full · seed: 831001 · cfg_scale: 1.0 · max_duration: 240 s · native or ComfyUI`

**Technique:** style in layer order (language → genre → voice → instruments → mood → production → BPM); short lines, exact chorus repeat for a hook; `[Outro]` so it resolves.

---

## 2. Instrumental Landscape

**Style**
```
Instrumental ambient post-rock, bowed guitar lead, felt piano, low cello drones, distant field-recording texture, slow tidal swells, foggy coastline at dawn, expansive stereo image, long reverb tails, 68 BPM, no singing
```
**Lyrics**
```
[Intro]

[Build]

[Climax]

[Outro]
```
**Settings:** `cot: full · seed: 4410 · max_duration: 300 s` — MachGen: `force_instrumental: true`, lyrics as above

**Technique:** "Instrumental" first and "no singing" last; bare tags give an energy curve without words to sing. The environment is the "subject", expressed as soundstage and texture.

---

## 3. Action Cue in an Odd Meter

**Style**
```
Instrumental hybrid electronic action score, 7/8 ostinato, distorted cello pulses, modular synth arpeggio, taiko and tight electronic drums, urgent rising intensity, sudden half-time break before final acceleration, punchy cinematic mix, 148 BPM
```
**Lyrics**
```
[Intro]

[Drive]

[Breakdown]

[Finale]

[Outro]
```
**Settings:** `cot: full · seed: 90210 · max_duration: 180 s · then inspect score.abc`

**Technique:** prose gets you near 7/8; check `M:` in the saved score and, if wrong, fix it to `M:7/8` and re-render with `abc=` (see example 8). Prose for feel, score for facts.

---

## 4. "Crane Shot" as Mix Movement

**Style**
```
English cinematic art pop, clear female mezzo-soprano, begins with mono felt piano and close vocal, soft bass enters in the pre-chorus, percussion grows through the verse, chorus opens into wide strings and high synths, continuous seamless build, luminous and awe-filled, 96 BPM
```
**Lyrics**
```
[Verse]
A single window holds the night
A silver line becomes the sky

[Pre-Chorus]
Every room begins to turn

[Chorus]
Open the walls and let in light
Carry the horizon inside

[Outro]
Hold the last chord and fade
```
**Settings:** `cot: full · seed: 2207 · max_duration: 200 s`

**Technique:** a visual reveal translated into arrangement order (mono → stereo, low → high, sparse → full). Each stage tied to a named section.

---

## 5. Dark-to-Hopeful Arc

**Style**
```
English alternative soul with trip-hop verses and a gospel-tinged final chorus, smoky contralto lead, Rhodes, sub bass, dusty breakbeat, restrained minor-key opening, gradual harmonic brightening, layered choir only in the final chorus, warm tape saturation, 88 BPM
```
**Lyrics**
```
[Verse]
The station clock forgot to move
I counted sparks beneath the rail

[Chorus]
Even in the tunnel
There is daylight in the sound

[Bridge]
Let the old walls answer
Let the new voice gather round

[Final Chorus]
Even in the tunnel
We can turn the whole train around

[Outro]
Daylight in the sound
```
**Settings:** `cot: full · seed: 5150 · cfg_scale: 1.0 (try 1.2 if the choir never arrives)`

**Technique:** fusion written as a timeline, not a tag pile; the choir is pinned to `[Final Chorus]` in both fields.

---

## 6. Call-and-Response Duet

**Style**
```
English cinematic synth-rock duet, low male tenor and bright female alto, alternating verses, unison chorus, analog arpeggiator, live toms, distorted bass, chorus guitar, tense verses, triumphant hook, bridge drops to voices and pulse before a full-band return, polished wide mix, 118 BPM
```
**Lyrics**
```
[Verse - Voice A]
I kept the map beneath my coat
The river moved the border south

[Verse - Voice B]
I kept the signal in the dark
A little fire inside my mouth

[Chorus - Together]
We are not lost if we are moving
We are not late if dawn is near

[Bridge]
We name the road and it appears

[Final Chorus - Together]
We are not lost if we are moving
Raise the lights, the way is clear
```
**Settings:** `cot: full · seed: 1188 · render 4–8 seeds and pick`

**Technique:** singer hints in tags are soft — the style line does the real work by naming both voices and the alternation. If a label gets sung, drop the ` - Voice A` suffixes. Note the bridge's "drops to voices and pulse" lives in style, not lyrics.

---

## 7. Restyle Cover (melody kept, new genre)

```bash
python models/SheetSage2/infer.py source.wav --output cover-score --melody-only
```
**Style**
```
English jazz-funk, warm lead vocal, Rhodes piano, syncopated electric bass, tight dry drums, muted trumpet fills, late-night club mood, 106 BPM
```
**Lyrics:** the source lyrics (rights cleared), sectioned to match `score.abc` order.
```python
from pathlib import Path
cover = pipe(
    style="English jazz-funk, warm lead vocal, Rhodes piano, syncopated electric bass, tight dry drums, muted trumpet fills, late-night club mood, 106 BPM",
    lyrics=Path("cover_lyrics.txt").read_text(encoding="utf-8"),
    abc=Path("cover-score/score.abc").read_text(encoding="utf-8"),
    cot="melody",
    seed=831001,
)
cover.save_artifacts("outputs/cover-jazz-funk")
```
**Settings:** `cot: melody · abc: reviewed melody-only score · seed: 831001`

**Technique:** `--melody-only` drops chords so `cot="melody"` lets the new genre reharmonise. Review the transcription by ear first. Use `cot="full"` + a chorded score to keep the original harmony.

---

## 8. Surgical Score Edit

Baseline: example 1 saved at `outputs/porch/`.
```bash
cp outputs/porch/score.abc edited.abc
# edit: change one chord symbol in the bridge (e.g. "Am" -> "F"); leave every other bar untouched
```
```python
song = pipe(style=STYLE_EX1, lyrics=LYRICS_EX1,
            abc=open("edited.abc").read(), cot="full", seed=831001)
song.save_artifacts("outputs/porch-v02-keychange")
```
**Settings:** `cot: full · seed: 831001 (unchanged) · same revisions + sampling`

**Technique:** read the dialect your own `score.abc` uses before editing. Only the score changed, so any difference is attributable to the edit. Expect the performance to vary slightly; the composition holds.

---

## 9. MachGen Hosted Payloads

**Vocal** (lyrics must be 400–10,000 characters — this block is ~520):
```json
{
  "model": "YuE2-3B",
  "task_type": "T2M",
  "prompt": "English neo-soul, intimate alto lead, Rhodes, syncopated bass, dry pocket drums, warm and reflective, 92 BPM",
  "audio_config": {
    "lyrics": "[Verse]\nMorning paints the kitchen gold\nCoffee steam and stories told\nYou hum a line I almost know\nThe radio is soft and low\n\n[Chorus]\nStay a while, stay a while\nLet the day wait at the door\nStay a while, stay a while\nI don't need anything more\n\n[Verse]\nRain is tapping on the pane\nCounting down the morning train\nYou find my hand beneath the sheet\nThe city hums a slower beat\n\n[Chorus]\nStay a while, stay a while\nLet the day wait at the door\nStay a while, stay a while\nI don't need anything more\n\n[Outro]\nStay a while",
    "force_instrumental": false
  },
  "seed": 831001
}
```
**Instrumental:**
```json
{
  "model": "YuE2-3B",
  "task_type": "T2M",
  "prompt": "Instrumental cinematic ambient, solo cello lead, granular pads, low piano, slow crescendo, spacious and cold, 64 BPM, no singing",
  "audio_config": { "lyrics": "[Intro]\n\n[Build]\n\n[Climax]\n\n[Outro]", "force_instrumental": true },
  "seed": 831001
}
```
**Settings:** `POST /api/v0/generate → poll /api/v0/tasks/{id} · FLAC · ≤ ~6 min · $0.10`

**Technique:** only documented fields — no `duration_secs`, `cot` or `abc`. On *"Score limit reached"*, shorten lyrics or simplify style and resubmit.

---

## 10. YuE v1 → YuE2 Migration

```text
# YuE v1
genre.txt:  inspiring female uplifting pop airy vocal electronic bright vocal
lyrics.txt: [verse] ... (blank line) [chorus] ...
python infer.py --stage1_model m-a-p/YuE-s1-7B-anneal-en-cot \
  --stage2_model m-a-p/YuE-s2-1B-general --run_n_segments 2 \
  --stage2_batch_size 4 --max_new_tokens 3000 --genre_txt genre.txt --lyrics_txt lyrics.txt
```
```python
# YuE2
song = pipe(
    style="English uplifting electronic pop, airy bright female vocal, glossy synth chords, punchy four-on-the-floor drums, inspiring and euphoric, 122 BPM",
    lyrics=open("lyrics.txt").read(),   # keep tags, capitalise if you like; sections are form now, not 30 s sessions
    cot="full",
    seed=831001,
)
```
**Settings:** `cot: full · seed: re-baselined (v1 seeds don't transfer)`

**Technique:** five space-separated tags become one ordered descriptive line with language and BPM; all stage/segment flags are deleted.
