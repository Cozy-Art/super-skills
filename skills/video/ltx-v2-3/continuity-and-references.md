# LTX-2.3 — Continuity & References

The native API has no seed, no reference-ID syntax and no multi-character reference slots. **Continuity is carried by media you feed back in**: first frames, last frames, source clips for extend/retake — plus identical text anchors and, locally, LoRAs.

## 1. Housekeeping

- Download every approved output immediately; keep the file, not the result URL.
- Library: `characters/`, `locations/`, `style/`, `continuity-frames/`, `approved-shots/`, `audio/`.
- Archive per shot: full request body, model ID, endpoint, source media, and (locally) seed, checkpoint, CFG/STG.
- Extract continuity frames losslessly (PNG) from the final frame or a clean late frame of each approved shot.

## 2. Tool Choice by Continuity Need

| Need | Tool | Model |
|---|---|---|
| Same character/set in a new shot | I2V from an approved frame (`image_uri`) | Fast or Pro |
| Exact end pose or composition | `image_uri` + `last_frame_uri` | Fast or Pro |
| Uninterrupted continuation of a take | `extend`, `mode: end` | Pro |
| Lead-in before an existing take | `extend`, `mode: start` | Pro |
| Fix a flawed section, keep the rest | `retake` with `start_time` + `duration` | Pro |
| Fix only the sound (or only the picture) | `retake`, `mode: replace_audio` / `replace_video` | Pro |
| Picture locked to a track/VO | `audio-to-video` + `image_uri` | Pro |
| Recurring protagonist across a series | character LoRA (open weights) | local |
| Structure from existing footage | IC-LoRA (union control: depth/pose/edges), video-to-video | local |

## 3. Character Consistency Protocol

1. Generate or shoot a **character master still**: clear face, signature wardrobe, neutral even light, in the delivery orientation (16:9 or 9:16).
2. Write an **identity anchor** and paste it identically into every prompt:
   ```
   a woman in her early forties with short black hair tucked behind one ear,
   a charcoal wool coat, and a small brass bird pin on the collar
   ```
3. Start every shot of that character from an approved frame via `image_uri`. In I2V, keep the anchor short — the image carries the face.
4. Change one variable at a time: angle, action, location, or light. Wardrobe and lighting changes come after identity is stable.
5. Dialogue and emotional beats in close-ups/mediums; large body motion in wides, where identity drift is less visible.
6. For a recurring lead, train a character LoRA on LTX-2.3 (LTX-2 LoRAs do not transfer).

## 4. First and Last Frames

- `image_uri` anchors identity, wardrobe, set and composition at t = 0; `last_frame_uri` anchors the landing.
- Make the two frames compatible: same identity, set geometry, light direction, orientation. Big differences force a morph instead of a move.
- Design the end frame first (in a still model or from a prior shot), then write the prompt as the physical path between them, including camera path and audio.
- Not combinable with `duration: null` — always set a duration.

## 5. Multi-Shot Sequencing

LTX-2.3 is most reliable at **one continuous shot per generation**. Build sequences in the edit.

1. **Shot bible:** identity anchors, style lock, lens family, palette, light direction, time of day, soundscape.
2. One primary action per clip.
3. Design shot A's last frame to motivate shot B's first frame.
4. Use A's continuity frame as B's `image_uri` for matched-action cuts; use the character master for new angles.
5. Preserve **screen direction**: exits frame right → enters next shot frame left. Match eyelines, prop hand, wardrobe state, weather, light direction.
6. Continuous camera/subject movement → `extend`. Editorial cut → new clip.

**Shot template:**
```
[Action continuing from the previous shot, screen direction]. [IDENTITY anchor].
[Setting]. [Shot size + camera move + landing]. [STYLE LOCK]. [SOUND LOCK + this shot's effects/dialogue].
```

## 6. Extend Strategy

- Prompt the **next beat**, not the whole scene: "She reaches the end of the corridor, turns, and pushes the door open; the hum grows louder."
- Keep camera behaviour consistent with the source's last seconds unless you state the change.
- `context + duration` ≤ 505 frames at the input fps. At 24 fps, e.g. 5 s context + 16 s new. At 48/50 fps the budget in seconds halves.
- Input must be ≥ 73 frames (~3 s at 24 fps), 16:9 or 9:16, ≤ 100 MB. Output matches input resolution.
- Chain extensions sparingly; review each for drift and branch from the last clean version.

## 7. Retake Strategy

- Pick the smallest window covering the defect (≥ 2 s) with a little margin on each side.
- The prompt describes **only that window**, in the same style and identity language as the original.
- `replace_audio` to redo a flubbed line or wrong music cue while keeping picture; `replace_video` to fix a gesture while keeping the sound; default replaces both.
- Output is 1080p (`1920x1080` / `1080x1920`). For 4K masters, retake then re-match in finishing, or regenerate the shot.

## 8. Audio Continuity

- Write a **sound lock** alongside the style lock and paste it verbatim: room tone, ambience bed, music palette.
  ```
  Steady rain on glass and a low carriage rumble; no music.
  ```
- Keep voice descriptions consistent across shots (age, accent, timbre words) — voice identity isn't locked by any field.
- For music-driven sequences, cut the track into sections and drive each shot with `audio-to-video` (≤ 20 s at 720p/1080p, ≤ 10 s at 1440p/4K).
- When a line is wrong but the picture is right, `retake` with `replace_audio`.
- For long-form, plan to mix/replace audio in post; generated room tone is useful as a guide track.

## 9. Style Lock

```
Restrained 1970s political thriller, 40mm spherical lens, deep focus,
cool fluorescent key with warm practicals, olive and tobacco palette, low
saturation, fine 35mm grain, measured camera movement.
```

Paste it as plain prose (labels like "STYLE:" belong in your notes, not the prompt). Keep it identical across shots and place it **after** the shot-specific action and blocking, so the event gets priority. Keep model, resolution tier, fps and (locally) checkpoint/LoRA constant across a sequence.

## 10. Seeds (local and wrappers only)

A seed reproduces output only with the same checkpoint, settings, prompt, resolution, frame count and input media. It is not an identity lock and doesn't survive version changes or prompt-enhancer changes. Use it for A/B testing wording, not for continuity.
