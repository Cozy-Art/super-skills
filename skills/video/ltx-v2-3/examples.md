# LTX-2.3 — Annotated Examples

Every example is two-part: **prompt** + **suggested settings**. Settings never appear in prompt text. All target one continuous 6–10 s shot unless noted.

---

## 1. Character Close-Up with Dialogue

```
A tired woman in her early forties sits beside a rain-streaked train window and
slowly lifts her eyes toward the passing lights. Her short black hair is tucked
behind one ear, and she wears a charcoal wool coat with a small brass bird pin on
the collar. The shot begins in a tight profile close-up as the camera makes a very
slow dolly in, amber streetlight reflections sliding across her face. Her lower lip
tightens, she exhales against the glass, and the fog briefly hides her eyes before
clearing. Cool blue carriage light contrasts with the warm reflections, shallow depth
of field, fine 35mm grain. Soft rail noise and rain fill the carriage; she whispers
in English, "Not this time." No music.
```
**Settings:** `model: ltx-2-3-pro · resolution: 2560x1440 · fps: 24 · duration: 8 · generate_audio: true · camera_motion: dolly_in`

**Technique:** preset and prose agree (slow dolly in); emotion is physical; one short quoted line placed last so it lands after the action; "No music" closes the audio brief. The identity sentence becomes the anchor for later shots.

---

## 2. Landscape / Environment

```
Wind moves through a vast field of silver grass on a high plateau as a storm rolls
in from distant mountains. The shot opens as an ultra-wide aerial view with a lone
stone observatory in the lower-left foreground and dark blue ridges layered across
the horizon. The camera glides forward slowly above the grass, keeping the
observatory anchored while low clouds swallow the peaks one by one. A narrow shaft
of late-afternoon sun travels across the valley and vanishes as the first drops of
rain streak past. The palette shifts from pale gold and sage to slate blue, with
natural haze and restrained contrast. Deep wind, rolling thunder, and the dry hiss
of grass make up the soundtrack; no music or voices.
```
**Settings:** `model: ltx-2-3-pro · resolution: 3840x2160 · fps: 24 · duration: 10 · generate_audio: true` (no `camera_motion` — an aerial glide isn't a preset)

**Technique:** wide shot carries geography and environmental motion; a visible change (light shaft disappears, palette shifts) gives the clip an arc.

---

## 3. Action

```
A courier in a red motorcycle jacket sprints across a wet rooftop while a compact
security drone races behind her at shoulder height. She clears one narrow gap, lands
hard, and slides beneath a half-closed metal gate as sparks scatter where the drone
clips the frame. The camera tracks backward at waist height in front of her, matching
her speed and keeping her centered while neon signs streak behind her. As she slides,
the camera drops with her and ends low on the far side of the gate as she rises and
runs on. Cold rain, cyan and magenta reflections, sharp rim light, controlled motion
blur. Footfalls, strained breathing, rain on metal, the drone rotor, and the gate
impact are synchronized; no dialogue, no music.
```
**Settings:** `model: ltx-2-3-pro · resolution: 1920x1080 · fps: 48 · duration: 6 · generate_audio: true`

**Technique:** exactly one jump + one slide; camera path stated with height, direction and landing; effects tied to visible events. 48 fps for smoother sampling.

---

## 4. Camera Reveal

```
A botanist kneels beside a tiny luminous flower in a dark volcanic cave and gently
brushes ash from its petals. The shot begins as a macro close-up of her gloved
fingers and the blue-white flower, the cave reduced to black bokeh. The camera
slowly pulls back, revealing hundreds of identical lights spreading across the
cavern floor and a vast stone arch overhead. She stays still near the center as the
widening frame turns the discovery from intimate to monumental. The flowers cast
cool underlight while a warm beam from her headlamp traces rock texture and drifting
dust. Water drips echo through the cave, her suit fabric creaks, and a low musical
tone blooms only when the full cavern is revealed.
```
**Settings:** `model: ltx-2-3-pro · resolution: 2560x1440 · fps: 24 · duration: 10 · generate_audio: true · camera_motion: dolly_out`

**Technique:** one dominant preset instead of stacking dolly_out + jib_up; music cue timed to the reveal.

---

## 5. Product (I2V)

**Input:** `image_uri` = approved 4K product still

```
The watch rotates exactly one quarter turn clockwise over the full shot, revealing
the engraved crown and the fine radial texture of the dial without changing shape.
A thin ribbon of water keeps circling the basalt base. The camera stays locked in a
medium product frame while focus shifts once from the wet basalt foreground to the
watch face and holds there. A narrow white strip light travels slowly across the
metal; the background stays deep black. A quiet mechanical tick and a soft water
ripple; no music or speech.
```
**Settings:** `model: ltx-2-3-pro · resolution: 3840x2160 · fps: 24 · duration: 6 · generate_audio: true · camera_motion: focus_shift · image_uri: [product still]`

**Technique:** I2V prompt describes only the change — rotation amount, light travel, focus handoff — not the watch's appearance. Logos and fine type stay in the source image; add any new text in post.

---

## 6. Stylized Mood (style lock in use)

```
A solitary detective crosses an empty 1940s hotel lobby as ceiling fans turn slowly
above him. He wears a rumpled cream suit and carries a closed black umbrella; his
reflection moves across the polished floor a few steps behind. The shot opens as a
symmetrical wide from the reception desk, then the camera dollies right while he
crosses left. He stops beneath the last lamp and looks toward an unseen elevator.
Monochrome film noir with crushed blacks, hard venetian-blind shadows through
cigarette haze, bright practical lamps, and subtle film weave. Distant thunder, fan
motors, wet shoes on marble, and a muted upright-bass phrase.
```
**Settings:** `model: ltx-2-3-pro · resolution: 2560x1440 · fps: 24 · duration: 10 · generate_audio: true · camera_motion: dolly_right`

**Technique:** action and blocking first, then the reusable style-lock and sound-lock sentences, pasted verbatim into every shot of the sequence (as plain prose — no labels). Opposing motion (camera right, subject left) is stated explicitly.

---

## 7. First-to-Last-Frame

**Inputs:** `image_uri` = behind-the-shoulder opening frame · `last_frame_uri` = frontal medium close-up

```
A young violinist in a forest-green coat stands alone at the center of an empty
concert hall stage and raises her bow. She plays one sustained note while warm aisle
lights come up row by row from the stage to the balcony. The camera moves in a smooth
clockwise half-circle at a constant distance, ending directly in front of her in a
medium close-up. Her coat, hairstyle, violin and the stage geometry stay unchanged
throughout. The note is clear and dry at first, then the hall reverberation grows
as the lights reach the balcony; no applause or speech.
```
**Settings:** `model: ltx-2-3-pro · resolution: 1920x1080 · fps: 24 · duration: 8 · generate_audio: true · image_uri: [start] · last_frame_uri: [end]`

**Technique:** prompt is the physical path between two compatible frames; orbit described in prose (no preset). Duration must be set — interpolation can't use `null`.

---

## 8. Audio-to-Video (music beat)

**Inputs:** `audio_uri` = 12 s song section (MP3) · `image_uri` = singer master frame

```
The singer stands under a single bare bulb in a narrow brick alley and sings toward
the camera, her shoulders rising on each breath. On the first downbeat she steps
forward into the light; on the chorus she tilts her head back and closes her eyes.
The camera pushes in slowly from a medium shot to a close-up, the bulb swinging
gently and throwing moving shadows across the wet bricks. Warm tungsten key, deep
teal shadows, light haze, fine grain.
```
**Settings:** `endpoint: /v2/audio-to-video · model: ltx-2-3-pro · resolution: 1920x1080 · fps: 24 · camera_motion: dolly_in · audio_uri: [12 s section] · image_uri: [singer master]` (length = audio; no `duration`/`generate_audio`)

**Technique:** describe performance beats against the music, not the sound itself — the track is supplied. Audio ≤ 20 s at 1080p (≤ 10 s at 1440p/4K); encode as MP3/M4A, not PCM WAV.

---

## 9. Retake (fix one gesture, keep the sound)

**Input:** `video_uri` = approved 10 s 1080p dialogue shot; the hand gesture at 4–6 s is malformed

```
She sets the coffee cup down on the table with her right hand, fingers releasing
the handle cleanly, then rests both hands flat on the table and looks up at him.
Same warm kitchen window light and medium shot framing, the camera holding still.
```
**Settings:** `endpoint: /v2/retake · model: ltx-2-3-pro · start_time: 3.5 · duration: 3 · mode: replace_video · resolution: 1920x1080`

**Technique:** window padded half a second each side; prompt covers only the window and restates framing/light; `replace_video` keeps the original dialogue take.

---

## 10. Extend (continue the take)

**Input:** `video_uri` = approved 8 s 24 fps corridor walk (from I2V)

```
She keeps walking to the end of the flickering corridor, stops at the steel door,
and pushes it open with her shoulder. Cold white light floods in from the room
beyond and washes over her face as the camera continues tracking backward in front
of her at the same pace. The fluorescent buzz fades under a rising low hum from the
open room; her footsteps echo, then stop.
```
**Settings:** `endpoint: /v2/extend · model: ltx-2-3-pro · mode: end · duration: 8 · context: 5` (5 s context + 8 s new = 312 frames ≤ 505)

**Technique:** prompt is the next beat only; camera behaviour carried over from the source's final seconds; audio transition written as part of the continuation. Resolution is inherited from the input.

---

## API Body (T2V, from example 3)

```json
{
  "prompt": "A courier in a red motorcycle jacket sprints across a wet rooftop…",
  "model": "ltx-2-3-pro",
  "duration": 6,
  "resolution": "1920x1080",
  "fps": 48,
  "generate_audio": true
}
```
`POST https://api.ltx.io/v2/text-to-video` → `202 {id}` → poll `GET /v2/text-to-video/{id}` → download `result.video_url`.
