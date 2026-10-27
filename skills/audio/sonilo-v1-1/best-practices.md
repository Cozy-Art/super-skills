# Sonilo — Best Practices

## 1. Detail Level: Musical Evidence Over Adjectives

A prompt should name things a mixer could point to: instruments, register, density, tempo, arc, space.

| Weak | Better |
|---|---|
| `background music` | `Instrumental underscore, sparse felt piano and soft sub pulse, steady mid-tempo, leaves room for narration` |
| `epic` | `Hybrid orchestral swell: low strings ostinato, taiko hits on downbeats, brass enters only at the climax` |
| `happy` | `Bright, playful, major-key; plucked ukulele, hand claps, light glockenspiel, bouncy 110 BPM` |
| `sad` | `Slow, aching; solo cello over sustained pad, wide silences, unresolved final chord` |
| `cinematic` | `Restrained cinematic pulse, gradual build, one big harmonic lift at the reveal, clean cadence` |
| `cool sound` | `Short metallic latch click, close perspective, dry room, 0.3-second tail` |

Precise mood beats strong mood: "confident, not triumphant", "tense but controlled", "nostalgic without sentimentality".

## 2. Detail Level by Endpoint

| Endpoint | Words | What to write |
|---|---|---|
| text-to-music | 25–80 (≤1,000 chars portable) | Full brief: purpose, mood, genre, 2–4 instruments, tempo, arc, mix space, exclusions |
| video-to-music | 0–35 | Only what pixels can't say: tone, instrument family, emotional reading, follow vs. contrast the edit |
| text-to-SFX | 10–50 | Cause, material, space, distance, intensity, envelope, realism |
| video-to-SFX | 0–20 global | A policy line; targeted detail goes in segments |
| video-to-sound | 15–40 each | Two separate briefs; music never asks for Foley, SFX never asks for music |

Start video jobs with **no prompt** once — it shows what the footage already implies, so your prompt only fixes the gap.

## 3. Exclusions Are Fine (in Words)

There's no negative field, but plain-language exclusions work and are encouraged: `no vocals`, `no choir`, `no festival drop`, `no trailer booms`, `no music` (in SFX prompts), `no voices`. Keep to 2–3 targeted exclusions — a long "no" list dilutes the brief.

**Vocals:** Sonilo documents instrumental output only. Always state `instrumental` / `no vocals` for narration beds; don't promise lyrics or sung lines.

## 4. Contradictions to Avoid

- `minimal but huge`, `slow 70 BPM high-speed`, `quiet explosive impact` — pick one, or explain the contrast ("quiet verses, one explosive hit at 0:22").
- Stacking genres: `lo-fi trap orchestral jazz metal` → muddy. One genre + one flavour ("cinematic with a lo-fi texture").
- Global prompt that lists every scene change — move scene changes into `segments`.
- Asking video-to-music for whooshes, UI blips or impacts — that's SFX.

## 5. Music Vocabulary That Steers Well

```
Energy:     sparse · restrained · steady · driving · propulsive · building · explosive · resolving
Texture:    intimate · wide · airy · dense · dry · lush · gritty · glassy · warm analog
Tempo:      slow ~70 BPM · mid-tempo ~95 · upbeat ~120 · half-time feel · rubato / free time
Arc:        slow build · hold back then open · drop out before the hit · natural final cadence · button ending
Mix space:  leave room for narration · sparse midrange · low-end only under dialogue · instrumental
Structure:  intro · verse · chorus · bridge · breakdown · drop · outro · sting (inside segment prompts)
```

## 6. SFX Vocabulary That Steers Well

Name the **cause**, then the **material**, then the **space**:

```
Cause:      footstep · latch · swing · scrape · impact · pour · rustle · flutter · ignition · servo
Material:   wet gravel · hollow wood · sheet steel · leather · glass · ceramic · cloth · rubber
Space:      dry studio · tiled bathroom · concrete garage · open field · dense forest · car interior
Distance:   close-mic · arm's length · across the room · distant · off-screen
Envelope:   sharp transient · short tail · 1-second decay · slow swell · sustained loop
Treatment:  realistic Foley · hyper-real · stylized cartoon · sci-fi designed · UI minimal
```

Video-to-SFX baseline policy (official): `realistic Foley, ambience, and action sound effects synced to visible events`.

## 7. Camera & Edit → Auditory Interpretation

No camera field exists — the footage carries the move. Tell Sonilo how to **hear** it:

| On screen | Write |
|---|---|
| Slow push-in | "narrow the texture and let tension rise as we close in" |
| Aerial / crane reveal | "widen the harmony and stereo field, add high air at the reveal" |
| Handheld chase | "dense rhythmic motion, tight percussion, no long sustains" |
| Locked-off still frame | "hold a single sustained chord; let silence breathe" |
| Smash cut | "hard stop, a beat of silence, then re-enter" (put it in a segment ending at the cut) |
| Slow motion | "half-time feel, stretched reverb tails" |
| Montage of quick cuts | "steady pulse that carries across cuts rather than hitting each one" |

## 8. Segment Design

- **2–5 segments** for a 30–90 s piece. Segment structural turns, not every cut.
- **Repeat identity terms** across neighbours (`same felt-piano motif`, `warm analog pulse`) and change **one** dimension per boundary: density, percussion, register, harmony or intensity.
- **Boundaries on real events:** place a segment edge a few frames before a reveal so the change lands on it; check the alignment by ear — v1.1 is tight but not a cue-sheet engine.
- **Cover the whole timeline** or accept that uncovered stretches follow the global prompt.
- **Section words go in the prompt:** `"chorus: full theme, add strings"`.
- **SFX segments** are for exceptions: a missed latch, a quiet stretch (`"room tone only, no action sounds"`), a stylized moment, an ambience change.

## 9. `prompt_influence` Tuning (video-to-music only)

| Value | Behaviour | Use |
|---|---|---|
| 0.2–0.4 | Footage dominates; prompt is a hint | Sync is everything; trust the cut |
| 0.5 (default) | Balanced | First pass |
| 0.6–0.8 | Prompt dominates genre/instruments | Brand sound, specific instrumentation |
| 0.9–1.0 | Literal prompt adherence | Rarely — sync and natural ending can weaken |

Move in 0.1–0.15 steps and change nothing else between tests.

## 10. Dialogue & Mix Hygiene

- Narration bed: `instrumental`, `sparse midrange`, `leave room for narration` **and** `preserve_speech` + `ducking` (async).
- Need the full original soundtrack (ambience + speech)? `keep_original_sound` on video-to-video-* endpoints.
- Already have music and VO? `audio-ducking` — no prompt, no tuning knobs.
- Don't set `preserve_speech` and `keep_original_sound` together without intent — `keep_original_sound` wins.

## 11. Common Mistakes

| Symptom | Likely cause | Fix |
|---|---|---|
| Generic, forgettable score | Prompt says "background music" | Mood + 2–4 instruments + tempo + arc + exclusions |
| Right genre, loose sync | Prompt dominates footage | Lower `prompt_influence`; shorten prompt; lock the cut |
| Good sync, wrong brand tone | Footage carries no brand intent | Add a short sonic identity phrase; influence 0.65–0.8 |
| Lurching scene changes | Segments change too much at once | Keep instrument family; change energy first |
| Vocals/choir appear | No exclusion | State `instrumental, no vocals, no choir` |
| Dialogue buried | No speech workflow | `mode=async` + `preserve_speech` + `ducking` |
| SFX off-picture | Used text-to-SFX for a visible event | video-to-SFX + a segment around the event |
| Music endpoint gave no Foley | Wrong endpoint | video-to-sfx or video-to-sound |
| 400/422 on WAV or variants | `mode=stream` default | `mode=async` |
| 422 on video | Audio-only file / renamed mp3 / GIF / VP8 | Real video stream, MP4/H.264 |
| Re-run doesn't match | No seed exists | Archive the chosen output; don't re-roll for a fix |
| Score drifts after re-edit | Cut changed after generation | Regenerate against the new cut |
| `segments` ignored/rejected | Sent as nested array or bad times | JSON string; numeric `start < end` |
