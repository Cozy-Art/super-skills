# Grok Imagine Video 1.5 Lite — Annotated Examples

Every example is two-part: **prompt** + **suggested settings**. Settings never appear in prompt text. Each
targets one simple shot — Lite's sweet spot.

---

## 1. Character Portrait (text-to-video)

```
A medium close-up of a weathered lighthouse keeper in her sixties standing beside a fogged
window at dawn, grey hair pinned back, navy wool coat buttoned to the collar. She watches the
storm outside, then turns toward camera and gives a small, knowing smile. Locked off on a tripod
with an almost imperceptible push in, portrait-lens perspective, shallow depth of field. Cool blue
window light from camera-left, a warm tungsten rim from behind. Distant surf, glass rattling
softly in its frame, low wind through the tower; no music, no dialogue.
```
**Settings:** `model: grok-imagine-video-1.5-lite · mode: text-to-video · duration: 8 · resolution: 720p · aspect_ratio: 16:9 · audio: on`

**Technique:** opens with the frame (shot size, subject, setting, light) because Lite renders a first frame
before animating; one action with an end state; the audio layer is closed explicitly so nothing is invented.

---

## 2. Landscape (text-to-video)

```
A high aerial view over terraced rice fields after monsoon rain at sunrise, a narrow-gauge
train curving through the valley floor. Low mist peels away from the hills as the train's
reflection slides across the flooded terraces. Smooth forward drone glide that slowly rises to
reveal a distant mountain range. Soft amber sunlight, deep atmospheric haze, restrained natural
colour. A quiet train rhythm, birds waking, breeze through wet grass, one distant horn; no
narration, no music.
```
**Settings:** `model: grok-imagine-video-1.5-lite · mode: text-to-video · duration: 12 · resolution: 720p · aspect_ratio: 21:9 · audio: on`

**Technique:** environmental motion (mist, reflection) carries the shot; one rising move with a reveal as the
landing. 21:9 is a native-API ratio — some wrappers don't offer it.

---

## 3. Action (text-to-video)

```
A low-angle tracking shot beside a white rally car with blue decals accelerating along a wet
forest road. The rear tyres throw a fan of water, the suspension compresses over one bump, and the
car drifts slightly through a right-hand bend. The camera holds two metres off the driver-side rear
quarter on a fast stabilised track, readable motion blur in the trees. Overcast daylight, wet
reflections on the bodywork. A rising engine note, gravel spray, one sharp gear change; no music.
The car's body shape and decals stay unchanged throughout.
```
**Settings:** `model: grok-imagine-video-1.5-lite · mode: text-to-video · duration: 8 · resolution: 720p · aspect_ratio: 16:9 · audio: on`

**Technique:** one action in three ordered physical beats; synced effects tied to visible events; a stability
line for the livery.

---

## 4. Product (text-to-video)

```
A three-quarter close-up of a brushed-steel espresso machine on a dark stone counter. A hand
locks the portafilter, presses the illuminated round button, and two even streams of espresso
begin to fill a clear glass. A slow 15-degree orbit clockwise. Warm edge light traces the brushed
metal; reflections stay clean and physically plausible. A metal click, pump hum, liquid pour,
faint café room tone. The machine's geometry and front badge stay exact; no added text.
```
**Settings:** `model: grok-imagine-video-1.5-lite · mode: text-to-video · duration: 7 · resolution: 720p · aspect_ratio: 1:1 · audio: on`

**Technique:** product described as geometry + material; the action is a short mechanical sequence; Lite at
720p is $0.21 for this clip — draft here, finish at 1080p only if needed.

---

## 5. Dialogue Two-Shot (text-to-video)

```
A locked eye-level medium two-shot in a quiet late-night diner booth. Maya, on the left in a red
raincoat, leans forward and says quietly, "Tell me you didn't open it." Eli, on the right in a
grey hoodie, glances toward the door, then answers flatly, "I only looked inside." A very slow
push in. Cool fluorescent overhead light, rain streaking the window behind them. Both lines spoken
by the visible speakers with natural lip-sync, soft refrigerator hum, rain on glass, one ceramic
cup set down between the lines; no music, no subtitles or on-screen text.
```
**Settings:** `model: grok-imagine-video-1.5-lite · mode: text-to-video · duration: 10 · resolution: 720p · aspect_ratio: 16:9 · audio: on`

**Technique:** each speaker named, placed left/right and given one short line in double quotes — the
`Name … "line"` shape xAI uses; delivery in words; judge lip-sync at 720p, not 480p.

---

## 6. Single Speaker to Camera (text-to-video)

```
A medium close-up of a young market vendor in a yellow apron behind a stall of stacked oranges,
early morning street behind her. She looks straight into the lens and says brightly, in a quick
Spanish-accented voice, "First crate's half price — today only." She lifts one orange and taps
it twice. Handheld with a gentle sway at eye level. Low golden sun from camera-right, long
shadows across the stall. Street chatter, a scooter passing, crates knocking; no music.
```
**Settings:** `model: grok-imagine-video-1.5-lite · mode: text-to-video · duration: 6 · resolution: 720p · aspect_ratio: 9:16 · audio: on`

**Technique:** voice character described in words (Lite has no voice selection); the line is short enough to
leave time for the gesture.

---

## 7. Portrait (image-to-video)

```
She takes one slow breath, her eyes move toward the window, then her head turns only slightly as
warm afternoon light drifts across her face. Nearly locked camera with subtle handheld
micro-movement, no zoom or reframing. Her face, freckles, hairstyle, clothing and the original
colour grade stay unchanged. Quiet apartment room tone, distant traffic, fabric rustle; no speech,
no music.
```
**Settings:** `model: grok-imagine-video-1.5-lite · mode: image-to-video · image: [approved portrait still] · duration: 8 · resolution: 720p · audio: on` (aspect ratio follows the image)

**Technique:** describes change only; names what holds; never re-describes the image. No `aspect_ratio` — it
is ignored in image-to-video.

---

## 8. Product Label (image-to-video)

```
A single highlight travels slowly down the edge of the glass as the amber liquid catches it and the
camera drifts almost imperceptibly toward the label. Otherwise locked off. The label text and
bottle shape stay exact. A crystalline chime, then a soft low room tone.
```
**Settings:** `model: grok-imagine-video-1.5-lite · mode: image-to-video · image: [hero bottle still] · duration: 5 · resolution: 720p · audio: on`

**Technique:** minimal motion protects a precious frame; label legibility is stated as a stability rule, the
way xAI's own image-to-video examples frame it.

---

## 9. Vertical Social Clip (text-to-video)

```
An extreme close-up of glossy chilli oil bubbling in a black wok. Hand-cut noodles drop into the
oil and curl; then the camera rises with the chef's chopsticks as the noodles lift and steam
crosses the lens; finally it settles on the finished bowl, sesame and scallions falling once. Rich
red and amber palette, crisp texture, fast but physically plausible motion. Hot sizzle, chopstick
taps, kitchen extractor hum; no voice, no music, no text or logo.
```
**Settings:** `model: grok-imagine-video-1.5-lite · mode: text-to-video · duration: 9 · resolution: 720p · aspect_ratio: 9:16 · audio: on`

**Technique:** three beats sequenced with "then… finally" instead of timecodes (timecodes are undocumented on
Lite); vertical framing lives in settings only.

---

## 10. Routing Away (notes, not a prompt)

**Scenario:** a recurring heroine must match her approved character sheet in every shot, speak in the same
preset voice, and the scene ends on a specific composed frame.

```
This shot should not run on Grok Imagine Video 1.5 Lite.

- Identity bound from reference images → Lite has no reference_images.
  Full Grok Imagine Video 1.5 takes up to 14 (reference-to-video, 720p).
- Same voice every shot → Lite has no voice references. Full 1.5 takes
  up to 3 (preset voice_id or an uploaded clip).
- Exact end frame → Lite cannot pin a last frame. Full 1.5 supports
  image + last_frame interpolation.

Recommend: full Grok Imagine Video 1.5 for this shot. Keep Lite for the
cheap coverage — establishing shots, inserts, crowd reactions — where
no binding is needed.
```

**Technique:** name the missing capability, the model that has it, and what Lite should still do. Routing part
of a scene is not routing away from the model.

---

## Quick Reference

| Situation | Model / mode | Note |
|---|---|---|
| Simple imagined shot with sound | Lite T2V | Open with the frame |
| Animate an approved still | Lite I2V | Describe change; ratio from image |
| Short lip-synced line(s) | Lite T2V/I2V | `Name: "line"`, one per speaker |
| Specific voice | Full 1.5 | Voice references are 1.5-only |
| Character/product bound from images | Full 1.5 | Up to 14 references |
| Exact end frame / mid-clip pins | Full 1.5 | `last_frame`, `keyframes` |
| Native 1080p | Full 1.5 | Lite 1080p is an upscale |
| Edit or extend a clip | Classic `grok-imagine-video` | Not on either 1.5 model |
