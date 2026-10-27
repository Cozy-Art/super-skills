# Suno v6 — Continuity & References

Suno has no seed and no deterministic recall. Every run is a new performance. **Continuity of sound and voice is carried by source audio, Voices, Custom Models, verbatim-repeated briefs, and local editing** — not by re-describing a song you liked.

## 1. Housekeeping That Makes Continuity Possible

- Keep every keeper in the library; download WAV (Pro/Premier) and stems for anything you'll build on.
- Log a recipe per keeper: model, Style, Lyrics version, Exclude, Variety/Weirdness/Style Influence/Audio Influence, Max Mode, reference sources (+ timestamps), chosen take.
- Reuse Prompt repopulates Lyrics, Style and Title for a controlled branch — it does **not** reproduce the audio. To keep a performance, edit the song itself.

## 2. The Music Bible (project-level lock)

Write once, paste verbatim into every Style field in the project:

```
SOUND LOCK: nocturnal synthwave, 104–110 BPM, A-minor centre. Gated drums,
pulsing octave bass, glassy arpeggio motif (rising minor third). Low detached
baritone, dry and close. Narrow verses, wide choruses. Vintage analog warmth,
light tape hiss. Resolved endings, no fades.
```

Also fix: model, Exclude list, Variety (0), Style Influence, recurring motif description, emotional arc per song. Change **one** dimension per song (tempo, orchestration, intensity, perspective) and keep the rest identical.

## 3. Singer Identity

| Method | Strength | Notes |
|---|---|---|
| Identical vocal block in every Style | Weak–medium | Same words every time: register, texture, phrasing, dynamics |
| Song reference in Simple mode ("vocal texture from Song A") | Medium | Assign it *only* the vocal role |
| Voices (your own verified voice) | Strong | Replaced Personas in the Create menu; Style Personas still live inside Voices. Raise Audio Influence if it doesn't resemble you. Voices FAQ currently says to select v5.5 — **v6 compatibility unverified; check the model dropdown**. Not available under 18 or in all regions. |
| Custom Model | Strongest for a catalog | See §4 |

**Vocal block template** (repeat verbatim):
```
VOCAL: husky low alto, close-mic and dry, conversational verses, sustained chest
voice on choruses, slight rasp on held notes, no vibrato.
```

## 4. Custom Models

- Pro/Premier; train from **as few as six** tracks you own; up to **three** private models; ready in ~2–5 minutes; select from the model dropdown.
- Existing custom models were auto-upgraded to v6 — re-validate their identity; old songs are unchanged.
- Train on tracks sharing singer, genre family, production quality and intent. A mixed set teaches an average, not an identity.

## 5. Reference Role Assignment

v6 Simple mode takes Suno songs, playlists, uploads, images and video in one prompt. Give each **one** job so references don't average:

```
Use Song A for lead vocal identity only. Use Song B for drum groove only.
Use the uploaded clip at 0:45 for the guitar melody — keep it unchanged.
Use the image only for mood: cold, empty, blue. Do not copy Song B's harmony.
```

| Source | Typical role |
|---|---|
| Suno song | Vocal identity, groove, arrangement template |
| Audio upload | Melody, riff, sample, demo to cover/extend |
| Playlist | Broad taste / palette |
| Image | Mood, scale, colour temperature → harmony, space, density |
| Video | Pacing and section changes from cuts; mood. Say "do not imitate its existing soundtrack." |

Upload limits: free up to 60 s; Pro/Premier up to 8 min (verify in the dialog). Raise Audio Influence when the source melody or voice drifts. Many images/videos increase credit cost.

## 6. Extend Continuity

Extend keeps the song up to a chosen point and generates a continuation; **Get Whole Song** stitches it.

- Extend from a clean boundary (end of a bar/phrase, stable tempo and harmony).
- Restate the active groove, instrumentation, singer and destination in Style — use the same words as the original.
- Add a transition cue in Lyrics: `[Chorus - continue current groove 4 bars]` then `[Bridge - reduce to piano]`.
- Generate options, pick the cleanest seam, then stitch.

## 7. Replace Section & Plain-Language Edits

Pro/Premier. Highlight only the region that's wrong; state the change **and** the preserve list:

```
Replace only the second chorus. Keep the lead vocal, key, tempo, drum pattern and
surrounding transitions unchanged. Add stacked gospel backing harmonies on the
final two lines and sustain the last chord for two bars.
```

Two options are generated; choosing one creates a new whole-song version. v6 also accepts single-lyric changes ("change 'midnight' to 'morning' in verse two only") without regenerating.

## 8. Cover vs Remaster

| Need | Tool |
|---|---|
| Same composition and performance, cleaner/balanced | Remaster — Subtle (polish) · Normal (default, refresh) · High (may change musical elements and vocals) |
| New singer, genre, tempo, arrangement | Cover — new Style, same lyrics; Max Mode for close covers |
| Old pre-v6 song brought forward | Cover or Remaster — the old model can't be recreated from text |

## 9. Album / Multi-Cue Scoring

1. Write the music bible (§2) and a recurring motif description.
2. Generate a master theme on v6 with Max Mode; pick the take with the clearest motif.
3. For each new cue: reference the master song for motif/sound, apply **one** transformation (orchestration, intensity, harmony, rhythm or perspective).
4. Continuous sequences → Extend. Non-contiguous scenes → new cue referencing the master.
5. Keep tempo range and key centre in the bible so cues crossfade.
6. Align to picture in Studio or a DAW — Suno timing is not frame-accurate.

**Cue template:**
```
[SOUND LOCK]. Cue: [scene purpose]. Transformation: [one change].
Target [m:ss]. [Arc]. [Ending].
```

## 10. Stems for Downstream Continuity

- Get Stems (Pro/Premier): Auto Split up to 12 stems (50 credits) · Split from Mix 1 stem + complement (10/stem) · Advanced Split ~100 instruments, Premier (10/stem).
- Stems are separated from a mix — expect some bleed. Write arrangements with clear frequency separation (one bass, one hook, defined drums) when you know you'll split.
- Reuse a clean stem (e.g. a vocal or riff) as an upload reference to carry it into new songs.
