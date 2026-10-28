# Suno v6 — Best Practices

## 1. Producer Brief Over Tag Cloud

v6 understands musical language — vocals, instrumentation, structure, mood, references, feel. Short sentences describing **who does what, and when** outperform stacked adjectives.

| Weak | Stronger |
|---|---|
| `electric guitars` | `Palm-muted guitar drives the verses; octave leads answer the vocal in choruses.` |
| `aggressive drums` | `Dry kick and snare hold a relentless straight-eighth drive; fills only at section transitions.` |
| `emotional vocal` | `Husky alto holds back in verses, opens into sustained chest voice on the chorus, cracks slightly on the last line.` |
| `cinematic` | `Low strings start as a narrow ostinato, brass enters at the midpoint, final chorus widens into choir and percussion.` |
| `professional mastering` | `Vocal dry and forward; bass centred and warm under a distinct kick.` |
| `chill` | `72 BPM lazy swung pocket, Rhodes chords on the off-beat, brushed snare, lots of space between phrases.` |

## 2. One Dominant Identity

- One primary genre world + one or two influences: "post-punk with dub bass techniques", not six genres.
- Replace broad cultural labels ("African", "Latin") with region, tradition, rhythm and instruments: "Ghanaian highlife guitar lines over a 12/8 bell pattern".
- Describe artists by properties, not names: era, register, harmony, instrumentation, rhythm, production texture, emotional behaviour. Transfers more predictably and stays original.

## 3. Describe Groove, Not Just BPM

BPM is a target; groove is what's heard. Pair them: "94 BPM, behind-the-beat hip-hop pocket, swung sixteenth hats". Name the meter if unusual (6/8, 7/8). Key is optional — "minor key, unresolved" often works better than "C# minor".

## 4. Give Each Player a Job

Name 3–5 parts and what each does: rhythm foundation, bass role, hook carrier, texture, counter-line. Then say which stay **subordinate**. Foregrounding everything produces a crowded mix.

## 5. Define the Energy Arc

A song is temporal — write how it changes:

```
Begin with voice and one instrument. Bass joins in verse two. Drums enter only at
the pre-chorus. First chorus contained; final chorus doubles the vocal, widens the
guitars and adds a counter-melody. End on a resolved chord, no fade.
```

Tools for "cuts" and "reveals": density, register, stereo width, rhythm, harmony, vocal proximity.

**Visual → musical translation** (no camera exists):

| Visual idea | Musical equivalent |
|---|---|
| Wide establishing shot | Distant, filtered, narrow mono, long reverb |
| Slow push-in | Gradually drier, closer vocal; frequency range opens |
| Reveal | Full band enters on a downbeat; stereo widens |
| Fast cutting / action | Driving ostinato, dense percussion, risers at transitions |
| Pull-back / end card | Strip to one instrument, distant, final sustained chord |
| Landscape | Ambience, acoustic space, regional instruments, field-recording texture |

## 6. Mix Relationships — Pick Two or Three

- Vocal dry and forward; short plate only on phrase endings.
- Bass centred and warm; kick distinct beneath it.
- Guitars wide but under the lead vocal.
- Drums close and punchy; room opens only in the final chorus.
- Intro narrow and filtered; full bandwidth at the first downbeat.

More than three engineering demands start to conflict.

## 7. Endings

Without an ending instruction, outros loop or fade arbitrarily. State it in Style **and** tag it: `[Outro]` / `[End]` + "four-bar resolved ending, no fade" or "hard final hit".

## 8. Lyrics Craft

- Match syllable density to tempo: short lines for fast songs, longer vowels and space for slow ones.
- Hold one speaker, tense and image system. Make the chorus repeat — the hook is repetition, not new information.
- Leave room in the ~5,000-character Lyrics field and the 8-minute ceiling for intros, solos, held notes.
- Write words to be sung; no stage directions in plain lines.

## 9. Section Tags

Own line, square brackets:

```
[Intro]  [Verse 1]  [Pre-Chorus]  [Chorus]  [Verse 2]  [Bridge]
[Instrumental Break]  [Guitar Solo]  [Final Chorus]  [Outro]  [End]
```

Composite cues — v6 uses these as performance direction:

```
[Verse 1 - intimate alto, muted guitar pulse, restrained drums]
[Chorus - full-band lift, stacked harmonies, wider stereo]
[Bridge - drums drop out, exposed vocal, rising strings]
```

Rules:
- Section level, not per line. Per-line tags cause lyric bleed and instructions being sung.
- Keep each cue under ~10 words.
- Cues must agree with Style.
- There is no official tag specification — tags are soft guidance.

## 10. Parentheses, Duets, Instrumentals

- **Parentheses** = backing vocals / responses / ad-libs: `We run toward the morning / (toward the morning)`. Community convention, not formal syntax; use sparingly.
- **Duets:** describe contrasting singers once in Style (`Singer A: smoky contralto, guarded. Singer B: warm tenor, urgent.`), label short sections `[Verse 2 - Singer B]`, reserve `[Final Chorus - duet, close harmony]` for specific moments. If labels get sung, remove them from lyric lines and keep them only in headers. Named roles beat `[male vocals]`/`[female vocals]` for clarity.
- **Instrumentals:** toggle Instrumental; carry the full arc in Style. Optional bare section tags in Lyrics can shape structure.

## 11. Exclude

- Concise nouns / noun phrases, comma-separated: `trap hi-hats, saxophone solo, spoken intro, crowd noise, abrupt ending`.
- Never repeat the excluded thing positively in Style.
- Exclude terms display after your style with a minus prefix; your stored style text is unchanged.

## 12. Simple-Mode Brief Pattern

```
Create [musical identity] for [purpose/scene].
Feature [vocal / instrument priorities].
The arrangement should [energy arc + structure].
Use [references] in these specific roles; preserve [locked elements].
```

State the intended operation explicitly ("cover", "extend from 1:40", "replace only the bridge") — v6 can infer it, but saying it removes ambiguity.

## 13. Common Mistakes

| Problem | Cause | Fix |
|---|---|---|
| Generic result | Only genre + mood | Add groove, player roles, vocal behaviour, arc, two mix priorities |
| Prompt ignored | Variety > 0, contradictions, too many genres | Variety 0, one identity, remove conflicts |
| Unwanted instrument | "no X" in Style | Move X to Exclude |
| Instructions sung | Long or per-line bracket cues | Short section-level cues on own lines |
| Flat hook | Every section equally dense | Sparse verse, transitional pre, wider repetitive chorus |
| Singer changes mid-song | Vague vocal description, long generation | One stable vocal brief, Voice/Custom Model, Audio Influence up, Max Mode |
| BPM / bars drift | Probabilistic generation | Treat as targets; fix in Studio/DAW |
| Outro loops | No ending instruction | `[Outro]`/`[End]` + "resolved ending, no fade" |
| Duet roles blur | Long unlabelled passages, similar voices | Contrasting singers, short labelled sections |
| Good song lost in revision | Full regeneration for one defect | Replace Section, lyric edit, Extend, Remaster |
| References averaged | Many refs competing | One role per reference; drop redundant ones |
| Overcrowded mix | Every part foregrounded | One hook, one foundation, one texture; name subordinates |
| Ambiguous artist imitation | "in the style of X" | Describe properties |
| Style vs tags clash | `[EDM drop]` in a ballad | Align local cues with global Style |
