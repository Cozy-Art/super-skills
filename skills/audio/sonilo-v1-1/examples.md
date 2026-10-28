# Sonilo — Annotated Examples

Every example is two-part: **prompt** (+ segments JSON where used) + **suggested settings**. Settings never appear in prompt text.

---

## 1. Character Theme (text-to-music)

```
Instrumental character theme for a solitary deep-sea cartographer: patient, curious,
and slightly haunted; felt piano, bowed glass, soft contrabass, and distant metallic
resonance; slow ~72 BPM pulse, restrained opening, one hopeful harmonic lift near the
end, natural final cadence, no vocals, no trailer drums.
```
**Settings:** `endpoint: text-to-music · duration: 75 · mode: async · output_format: wav · variants_num: 3`

**Technique:** purpose → precise mood → four timbres → tempo → arc → exclusions. Three variants because this becomes the hero take for the character's THEME block (continuity §3).

---

## 2. Landscape / Environment (text-to-music)

```
Expansive dawn over a high desert plateau, serene but not sentimental; airy strings,
wood flute, subtle hand percussion, and a warm low drone; very gradual build with wide
silences and a natural final cadence, instrumental, no choir, no electronic bass.
```
**Settings:** `endpoint: text-to-music · duration: 90 · mode: async · output_format: wav · variants_num: 2`

**Technique:** "serene but not sentimental" pins the emotional register; "wide silences" is an arrangement instruction, not an adjective.

---

## 3. Chase Sequence with Segments (video-to-music)

```
Tense modern orchestral-electronic chase score, precise and propulsive, low strings,
tight hybrid percussion, restrained brass, no vocals, follow the edit rather than
forcing a constant beat.
```
```json
[
  {"start": 0,  "end": 10, "prompt": "stealthy opening, sparse low pulse, hold back percussion"},
  {"start": 10, "end": 27, "prompt": "accelerate with tight percussion and repeating low-string motif"},
  {"start": 27, "end": 35, "prompt": "brief near-silence, suspended tension before impact"},
  {"start": 35, "end": 48, "prompt": "full chase energy, low-string motif returns larger, decisive final hit and short resolve"}
]
```
**Settings:** `endpoint: video-to-music · mode: async · output_format: wav · prompt_influence: 0.55 · variants_num: 2`

**Technique:** global prompt sets identity; segments only at four dramatic turns; "low-string motif" repeats across segments so boundaries don't lurch. The near-silence segment makes the impact land.

---

## 4. Camera-Move Interpretation (video-to-music)

```
Begin intimate and narrow as we track through the dark corridor; gradually widen the
harmony and stereo field during the forward move; at the exterior reveal, open into
luminous strings and a single deep impact, then resolve quietly, no vocals.
```
**Settings:** `endpoint: video-to-music · mode: async · output_format: m4a · prompt_influence: 0.5 · variants_num: 2`

**Technique:** no camera field exists — the prompt describes the *auditory consequence* of a move the footage already contains. Default influence so the footage still times the reveal.

---

## 5. Isolated Realistic SFX (text-to-sfx)

```
Close-up leather hiking boot stepping once onto wet forest gravel, small stones compress
and shift, subtle mud suction on lift-off, natural woodland reflections, realistic,
no music, no voice, no exaggerated cinematic impact.
```
**Settings:** `endpoint: text-to-sfx · duration: 3 · audio_format: wav`

**Technique:** cause → material → micro-detail → space → treatment → exclusions. Integer duration (no sub-second). Note the 15 s billing minimum — batch several library sounds into one session plan rather than many 1 s calls.

---

## 6. Video-Native Foley & Ambience (video-to-sfx)

```
Naturalistic production sound: detailed Foley, continuous location ambience, and
restrained action accents synced to visible events; no music, no voices, no trailer booms.
```
```json
[
  {"start": 0,  "end": 12, "prompt": "quiet interior room tone, cloth movement, soft footsteps on wood"},
  {"start": 12, "end": 18, "prompt": "emphasize the metal latch, door swing, and exterior wind transition"},
  {"start": 18, "end": 32, "prompt": "open-air ambience, gravel footsteps, distant birds, realistic perspective"}
]
```
**Settings:** `endpoint: video-to-sfx · audio_format: wav` (always async)

**Technique:** one policy line + segments at location changes; segment 2 rescues a key prop sound the automatic pass might underplay.

---

## 7. Narrated Product Film — One Call (video-to-sound)

`music_prompt`
```
Premium minimal electronic underscore, confident and human, warm analog bass, soft
pulse, glassy plucks, gradual build toward the product reveal, instrumental, leave
generous space for narration, no festival drop.
```
`sfx_prompt`
```
Clean realistic product Foley and subtle interface confirmations synced to visible
actions; precise mechanical clicks, soft material handling, restrained room tone,
no exaggerated impacts, no music.
```
**Settings:** `endpoint: video-to-sound · preserve_speech: true · output_format: wav · variants_num: 2`

**Technique:** two separate briefs with no overlap in vocabulary. `ducking` is ignored when `preserve_speech` is on, so it's omitted. One call keeps music and SFX synced to the same analysis.

---

## 8. Vertical Social Short with Talking Head (video-to-video-music)

```
Upbeat lo-fi pop bed, light and friendly; plucked guitar, soft kick, finger snaps,
steady ~100 BPM, small lift at the final call to action, instrumental, sparse midrange.
```
**Settings:** `endpoint: video-to-video-music · preserve_speech: true · ducking: true · prompt_influence: 0.5 · variants_num: 2`

**Technique:** MP4 back with picture and dimensions untouched — no aspect-ratio field needed. "Sparse midrange" keeps the voice band clear; `preserve_speech` + `ducking` handles level.

---

## 9. Brand Series — Identity Block (video-to-music, episode N)

```
SERIES IDENTITY: warm analog pulse, muted felt-piano four-note motif, brushed
percussion, restrained optimism, intimate mix, instrumental, no brass, no vocals.
This episode: slightly brighter, builds to a hopeful peak at the customer reveal.
```
**Settings:** `endpoint: video-to-music · mode: async · output_format: wav · prompt_influence: 0.65 · variants_num: 3`

**Technique:** identity block pasted verbatim every episode; only the last sentence changes. Influence fixed at 0.65 across the series so the identity holds equally each time.

---

## 10. Song-Structured Library Cue (text-to-music + segments)

```
Instrumental indie-electronic track for a travel montage, warm and optimistic,
analog synth arpeggio, live bass, crisp drums, ~118 BPM, no vocals.
```
```json
[
  {"start": 0,  "end": 10, "prompt": "intro: arpeggio alone, filtered, building anticipation"},
  {"start": 10, "end": 30, "prompt": "verse: add bass and drums, same arpeggio"},
  {"start": 30, "end": 50, "prompt": "chorus: full energy, open filter, add bright pad"},
  {"start": 50, "end": 60, "prompt": "outro: drums drop out, arpeggio fades to a clean ending"}
]
```
**Settings:** `endpoint: text-to-music · duration: 60 · mode: async · output_format: wav · variants_num: 2`

**Technique:** section labels live inside segment prompts (no `label` field). Segment ends match `duration` exactly.

---

## 11. UI Sound Set (text-to-sfx)

```
Minimal app interface confirmation sound: two soft rounded synth tones rising a
perfect fifth, glassy and friendly, very short attack, dry studio, 0.4-second tail,
no music, no voice.
```
**Settings:** `endpoint: text-to-sfx · duration: 1 · audio_format: wav`

**Technique:** stylized/designed treatment described as tones, interval and envelope. For a matching set (error, notification), keep "soft rounded synth tones, glassy and friendly, dry studio" verbatim and change only the gesture.

---

## 12. API Call (curl, video-to-music with segments)

```bash
curl -X POST "https://api.sonilo.com/v1/video-to-music" \
  -H "Authorization: Bearer $SONILO_API_KEY" \
  -F "video_url=https://example.com/final_cut_v3.mp4" \
  -F "prompt=Restrained cinematic pulse, felt piano and low strings, gradual build to the reveal, instrumental, no vocals" \
  -F 'segments=[{"start":0,"end":15,"prompt":"intro: sparse piano"},{"start":15,"end":40,"prompt":"build: add low strings and pulse"}]' \
  -F "prompt_influence=0.55" \
  -F "mode=async" \
  -F "output_format=wav" \
  -F "variants_num=2"
# → 202 {"task_id": "...", "status": "processing"}; poll GET /v1/tasks/{task_id} every 2–5 s
```
**Technique:** exactly one video source; `segments` is a JSON **string**; `mode=async` because WAV and `variants_num > 1` both require it.
