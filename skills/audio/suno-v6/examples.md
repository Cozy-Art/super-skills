# Suno v6 — Annotated Examples

Every example is two-part: **prompt fields** (Brief, or Style / Lyrics / Exclude / Title) + **suggested settings**. UI settings never appear in prompt text; BPM, groove, structure and target length do, because Suno has no fields for them.

---

## 1. Simple-Mode Character Song

**Brief**
```
A vulnerable indie-folk confession from a night-shift paramedic driving home at
dawn. Intimate husky alto, fingerpicked acoustic guitar, soft brushed drums.
Restrained verses, a quietly uplifting final chorus. Keep the storytelling
specific and conversational; end cleanly without a fade.
```
**Settings:** `model: v6 · Simple mode · Variety: 0–low · Weirdness: 30% · Max Mode: off`

**Technique:** identity → character/purpose → voice + two players → arc → ending. Four sentences is enough in Simple mode.

---

## 2. Full Custom Song (Style + Lyrics)

**Style**
```
Nocturnal 1980s synthwave, 108 BPM, steady four-on-the-floor. Low detached
baritone, dry and close, opens into fuller chest voice on choruses. Gated
snare, pulsing octave bass, glassy arpeggio carries the hook; warm pad stays
underneath. Sparse first verse, bass and drums lock in at the pre-chorus, final
chorus widens with a counter-melody synth. Vocal forward; synths wide but under
the voice. Four-bar resolved ending, no fade.
```
**Lyrics**
```
[Intro]

[Verse 1 - sparse, vocal and pad only]
Streetlights count the minutes
Down the empty boulevard
I keep your number written
On the back of a parking card

[Pre-Chorus - drums enter, building]
And the radio keeps saying
That the night is almost through

[Chorus - full band, wide]
Drive until the morning
Drive until it's true
(until it's true)
Every mile is a warning
Every mile is you

[Verse 2]
...

[Final Chorus - counter-melody, bigger]
...

[Outro - pad and arpeggio, resolve]
[End]
```
**Exclude**
```
saxophone, guitar solo, spoken intro, crowd noise, fade out
```
**Title:** `Drive Until the Morning`

**Settings:** `model: v6 · Instrumental: off · Variety: 0 · Weirdness: 30% · Style Influence: high · Max Mode: on`

**Technique:** Style follows identity → pulse → performance → players → arc → mix → ending (~560 chars). Section cues echo the Style arc; parentheses carry a backing echo.

---

## 3. Instrumental Landscape Cue

**Style**
```
Nordic ambient chamber folk, 68 BPM, slow breathing pulse. Bowed cello carries
the main motif; sparse felt piano answers it. Distant wordless contralto enters
only after the midpoint. Wind-like granular texture, long cold reverb, wide
stereo field, deep silence between phrases. Begin nearly empty, grow into a
luminous string swell, return to solo piano. Resolved final chord.
```
**Exclude**
```
drum kit, handclaps, bright synth leads, spoken narration, abrupt ending
```
**Settings:** `model: v6 · Instrumental: on · Variety: 0 · Weirdness: 35% · Style Influence: high · Max Mode: on if > 2 min`

**Technique:** landscape composed with space and timbre, not visuals. "No percussion" became `drum kit, handclaps` in Exclude.

---

## 4. Action Chase Cue

**Style**
```
Industrial electronic chase cue, 142 BPM, straight sixteenth-note drive.
Distorted kick and metallic snare stay relentless; sub bass pulses in short
syncopated bursts. A two-note synth ostinato is the only melodic hook. Rising
noise and denser percussion at each transition. Start immediately. Midpoint
half-time fake-out, then return at full intensity with wider synths and heavier
drums. Target 2:00. Hard final hit.
```
**Exclude**
```
vocals, guitar solo, choir, jazz harmony, atmospheric intro, long breakdown, fade out
```
**Settings:** `model: v6 · Instrumental: on · Variety: 0 · Weirdness: 40% · Style Influence: high · Max Mode: off`

**Technique:** motion intensity = tempo, density and transitions. Target length stated as a goal, not a setting.

---

## 5. Musical "Camera Move"

**Style**
```
Dream-pop slow dance, 82 BPM. Open as if heard through a wall: mono, filtered
piano and distant room vocal. Over sixteen bars bring the singer closer, restore
full frequency range and widen the stereo image. At the chorus reveal warm bass,
brushed drums and shimmering guitars around a dry centred vocal. Pull everything
back to distant mono for the last line, then stop on a soft unresolved chord.
```
**Settings:** `model: v6 · Instrumental: off · Variety: 0 · Weirdness: 40% · Style Influence: high`

**Technique:** wide shot → push-in → reveal → pull-back, translated into mix perspective. It will not produce visuals.

---

## 6. Duet

**Style**
```
Cinematic soul duet, 76 BPM. Singer A: smoky contralto, guarded, precise
phrasing. Singer B: warm tenor, earnest, slightly breathless. Upright bass and
dry piano lead the verses; restrained drums enter at the pre-chorus. Voices stay
distinct and alternate short sections, first overlap in the bridge, close
harmony only in the final chorus. Intimate analog production, vocals forward,
resolved ending.
```
**Lyrics**
```
[Verse 1 - Singer A, restrained]
You left the porch light burning
Like a question in the rain

[Verse 2 - Singer B, tender]
I followed every back road
Just to hear you say my name

[Bridge - Singer A then Singer B, tension rising]
I learned to live without you
I never learned to leave

[Final Chorus - duet, close harmony]
We were two sides of the doorway
Both afraid to turn the key

[Outro - Singer A alone]
The porch light is still burning
[End]
```
**Settings:** `model: v6 · Variety: 0 · Weirdness: 25% · Style Influence: high · Max Mode: on`

**Technique:** identities defined once in Style; roles live only in section headers so names aren't sung.

---

## 7. Controlled Style A/B (same song, two productions)

**Style — Variant A (warm)**
```
1970s-inspired soft soul, 84 BPM relaxed pocket. Intimate chest-voice lead.
Rounded bass, dry close drums, gentle string countermelody. Warm tape
saturation, hopeful restraint, resolved ending.
```
**Style — Variant B (cold)**
```
Minimal nocturnal synth-pop, 84 BPM. Detached low vocal. Gated electronic
drums, glassy digital pads. Narrow verses opening into a wide chorus, anxious
unresolved harmony, abrupt stop.
```
**Settings (both):** `model: v6 · Variety: 0 · Weirdness: 30% · Style Influence: high · same Lyrics, same Title`

**Technique:** only the Style changes; lyrics, model, tempo and sliders fixed so the comparison is clean.

---

## 8. Multimodal Mashup (Simple mode)

**Brief**
```
Build a new 3:20 song from these references. Take the lead vocal and lyric
phrasing from Song A, the drum groove from Song B, and the clean guitar figure
from the uploaded audio at 0:45. Use the attached rooftop image only for mood:
lonely, reflective, neon-lit. Reharmonise everything as restrained 1980s
synthwave at 108 BPM. Preserve the vocal identity and guitar melody, add a
larger final chorus, finish with an eight-bar instrumental outro.
```
**Exclude:** `saxophone, spoken dialogue`

**Settings:** `model: v6 · Simple mode · refs: Song A, Song B, upload, image · Variety: 0 · Audio Influence: raise if guitar drifts · Max Mode: on`

**Technique:** each reference gets exactly one role; locked elements named; negatives moved to Exclude.

---

## 9. Replace Section Repair

**Instruction (highlight 1:42–2:05)**
```
Replace only the second chorus. Keep the lead vocal, key, tempo, drum pattern
and surrounding transitions unchanged. Add stacked gospel backing harmonies on
the final two lines and sustain the last chord for two bars.
```
**Settings:** `tool: Replace Section · model: v6 · choose 1 of 2 options`

**Technique:** change + preserve list, smallest possible region. Never regenerate a mostly-good song.

---

## 10. Extend With a Transition

**Style** (same words as the original, plus destination)
```
Nocturnal 1980s synthwave, 108 BPM, steady four-on-the-floor. Low detached
baritone, dry and close. Gated snare, pulsing octave bass, glassy arpeggio hook.
Continue the chorus groove, drop to pad and voice for a bridge, then a final
chorus with counter-melody. Four-bar resolved ending, no fade.
```
**Lyrics**
```
[Chorus - continue current groove, 4 bars]
[Bridge - pad and voice only]
Somewhere past the overpass
The dark begins to thin
[Final Chorus - full band, counter-melody]
Drive until the morning...
[End]
```
**Settings:** `tool: Extend from 2:48 (end of chorus bar) · model: v6 · Variety: 0 · then Get Whole Song`

**Technique:** the original's Style restated verbatim keeps the singer and sound; the extension point sits on a clean bar boundary.

---

## 11. Score Cue From a Music Bible

**Style**
```
SOUND LOCK: nocturnal synthwave, 104–110 BPM, A-minor centre. Gated drums,
pulsing octave bass, glassy arpeggio motif (rising minor third). Vintage analog
warmth. Cue: rooftop confrontation. Transformation: half-time, motif moved to
low distorted synth. Target 1:30. Builds from pulse to full drums at 0:45.
Hard stop.
```
**Settings:** `model: v6 · Instrumental: on · refs: master theme song (motif only) · Variety: 0 · Style Influence: high · Max Mode: off`

**Technique:** pasted sound lock + one transformation + the master theme as motif-only reference keeps a project's cues related.
