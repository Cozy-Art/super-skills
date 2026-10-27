# Kling 4.0 — Annotated Examples

Every example is two-part: **prompt** + **suggested settings**. Settings never appear in prompt text. Token numbers follow the upload order listed in the settings line.

---

## 1. Character Performance (Omni Reference)

```
@Image1 defines the archivist's face, hairstyle, and rust-colored cardigan; preserve them exactly.
@Image2 defines the archive room; preserve its shelving layout and window position.

Scene and texture: dust in the air, paper fibres, worn oak desk. Visual style: quiet naturalism, soft contrast. Camera tone: one continuous medium close-up, no cuts.

0–4s: The archivist opens a water-damaged envelope and unfolds a single page.
4–8s: She recognizes the handwriting and becomes still; the camera makes a slow, restrained push-in.
8s–end: Her eyes return to the first line before she quietly smiles. Cool window light from frame-left, a warm desk lamp on the page.

Audio: she whispers in English, in a dry, unsteady voice, "You kept it." Close paper movement, quiet room tone, distant rain on the window. No background music. No subtitles.
```
**Settings:** `mode: Omni Reference · model: Kling 4.0 · duration: 12 s · aspect ratio: 16:9 · resolution: 1080p · uploads: @Image1 archivist, @Image2 archive room`

**Technique:** four-part order; role lines say what to preserve; "one continuous… no cuts" overrides default multi-shot; emotion is physical; the line lands last.

---

## 2. Landscape / Ultrawide Environment (text only)

```
A deserted coastal observatory stands on a cliff above a dark ocean before sunrise. Visual style: naturalistic, cold blue-grey with a single amber accent. Camera tone: one continuous aerial approach with no cuts.

0–5s: Begin beyond the cliff edge over the water and advance toward the building.
5–10s: Descend until the telescope dome fills the upper third of the frame; keep the observatory's geometry and the horizon line stable.
10s–end: A narrow strip of amber sunlight appears beneath the cloud layer and touches the dome.

Wind bends the grass toward the sea throughout.

Audio: waves breaking below, wind crossing from left to right, one distant gull. No dialogue. No background music. No subtitles.
```
**Settings:** `mode: Omni Reference (no assets) · model: Kling 4.0 · duration: 14 s · aspect ratio: 21:9 · resolution: 1080p (4K if your plan/interface offers it)`

**Technique:** 21:9 rewards stable geometry and horizon anchors; stereo placement in the audio; a visible change gives the clip an arc.

---

## 3. Action with a Motion Reference

```
@Image1 defines the runner's identity and clothing.
@Image2 defines the rooftop.
@Video1 supplies only the running rhythm, obstacle timing, and landing mechanics. Do not inherit its actor or location.

Maintain left-to-right travel and believable foot contact. Overcast daylight, hard edges, slight motion blur.

0–4s: Side tracking shot as the runner approaches a low ventilation duct.
4–8s: She plants her right foot, vaults the duct, and lands on both feet.
8s–end: The camera follows as she slows beside the rooftop door and looks back.

Audio: synchronized footsteps, fabric movement, the landing impact, rooftop wind. No background music. No subtitles.
```
**Settings:** `mode: Omni Reference · model: Kling 4.0 · duration: 12 s · aspect ratio: 16:9 · resolution: 1080p · uploads: @Image1 runner, @Image2 rooftop, @Video1 parkour clip (trimmed to the vault)`

**Technique:** the video reference is fenced to motion only; action written as approach → contact → landing → follow-through.

---

## 4. Camera Transfer — Product Spot

```
@Image1 defines the ceramic lamp's exact shape, glaze, and proportions; preserve the handle opening and base diameter throughout.
@Image2 defines the workshop.
Use @Video1 as the reference for camera movements and shot pacing only.

Replace the reference video's subject with the lamp and its setting with the workshop. The lamp stays stationary on the bench.

0–5s: Begin at tabletop height on the lamp's left side.
5–10s: Move in a slow half-orbit to its front; window light rakes across the glaze texture.
10s–end: Settle into a symmetrical product composition and hold.

Audio: quiet workshop ambience, a faint clock. No speech. No background music. No subtitles.
```
**Settings:** `mode: Omni Reference · model: Kling 4.0 · duration: 15 s · aspect ratio: 1:1 · resolution: 1080p · uploads: @Image1 lamp, @Image2 workshop, @Video1 orbit reference`

**Technique:** product invariants named explicitly; camera authority given to the video, identity to the image — they no longer compete.

---

## 5. Style Transition with Keyframes

```
@Image1 is the first frame: a realistic orange cat beside a rain-covered window.
@Image2 is the middle frame: the same cat and room rendered as stitched felt.
@Image3 is the last frame: the original realistic appearance.

One continuous locked-camera composition.
0–4s: The cat turns toward a passing light outside.
4–8s: As the light crosses the room, the materials transform into felt.
8s–end: A second light passes and restores the photographic materials.

Keep the cat's markings, body position, window geometry, and direction of gaze consistent. The transformation changes materials, not identity.
```
**Settings:** `mode: Keyframes · model: Kling 4.0 · duration: 12 s · keyframes: @Image1 at 0 s, @Image2 at ~6 s, @Image3 at end · aspect ratio: follows first keyframe · resolution: 1080p`

**Technique:** Keyframes takes no other references, so identity lives in the frames; beats are timed to keyframe positions; "materials, not identity".

---

## 6. First and Last Frame — Craft Process

```
Use @Image1 as the first frame and @Image2 as the last frame, then show the process in between: a potter's hands center a lump of wet clay on the wheel, open it, and pull the walls upward into the finished tall vase.

Close, slightly high angle, locked-off. Soft north-facing window light, clay slip glistening on the knuckles.

Audio: the wheel's steady hum, wet clay squelching, water dripping into the tray. No background music. No subtitles.
```
**Settings:** `mode: Keyframes · model: Kling 4.0 · duration: 10 s · keyframes: @Image1 first, @Image2 last · resolution: 1080p`

**Technique:** Kling's own first/last-frame formula; the prompt spends its words on the physical path between the two frames.

---

## 7. Thirty-Second Multi-Shot Narrative

```
@Image1 defines the courier. @Image2 defines the station. @Image3 defines the small blue parcel.

Continuity: the courier carries the parcel in her left hand until she places it on the bench. The station entrance stays behind her. Cool morning light throughout.

Shot 1 (0–6s): Wide shot. She enters from frame-left and approaches the bench.
Shot 2 (6–12s): Side-tracking medium shot. She notices a matching blue ribbon tied to the bench.
Shot 3 (12–18s): Insert. Her left hand places the parcel beside the ribbon.
Shot 4 (18–24s): Close-up. She hears a familiar whistle and looks frame-right.
Shot 5 (24–30s): Hard cut to a wider two-shot as an older man enters from frame-right. She smiles; hold the final composition.

Audio: station room tone, footsteps on tile, the parcel touching wood, one human whistle from the right. No dialogue. No background music. No subtitles.
```
**Settings:** `mode: Omni Reference · model: Kling 4.0 · duration: 30 s · aspect ratio: 16:9 · resolution: 1080p · uploads: @Image1 courier, @Image2 station, @Image3 parcel`

**Technique:** continuity invariants stated once up front; labelled shots override automatic shot splitting; every shot advances the story.

---

## 8. Bilingual Dialogue Two-Hander

```
@Image1 defines the café owner, a woman in her sixties with a grey bun and a navy apron.
@Image2 defines the young traveller with a red backpack.

A small Lisbon café at closing time, tiled walls, a single pendant lamp. Over-the-shoulder coverage, cutting between them on each line.

0–5s: The traveller, out of breath, sets a crumpled map on the counter.
5–11s: The owner studies it, then taps one street with her finger.
11s–end: The traveller nods, relieved, and shoulders the backpack.

Audio: the traveller, in English, fast and apologetic: "Sorry — is this street close?" The owner, in Portuguese, warm and unhurried: "Fica já ali, ao virar da esquina." Espresso machine cooling, street noise through the open door. No background music. No subtitles.
```
**Settings:** `mode: Omni Reference · model: Kling 4.0 · duration: 14 s · aspect ratio: 16:9 · resolution: 1080p · uploads: @Image1 owner, @Image2 traveller (+ voice profiles if you have them)`

**Technique:** each line written in the language to be spoken; speakers attributed by visible description; voice described by age, tone and speed.

---

## 9. Edit — Remove and Replace

```
Edit @Video1. Remove the person crossing in the foreground between 3s and 6s, and replace the plain grey sky with a low orange sunset. Keep the camera move, the cyclist's performance, and all other elements unchanged.
```
**Settings:** `mode: Omni Reference (edit) · model: Kling 4.0 · duration: match source · uploads: @Video1 approved take`

**Technique:** opens with "Edit @Video1" so it isn't read as reference generation; timing window; explicit preservation list. If the sky change disturbs the rest, split into two edit passes.

---

## 10. Edit — Add an Element

```
Edit @Video1. When the box is opened again at the end, add @Element1 lying inside, asleep and curled up. Match the box's interior lighting and shadow. Preserve the original composition, shots, and actions.
```
**Settings:** `mode: Omni Reference (edit) · model: Kling 4.0 · duration: match source · uploads: @Video1 unboxing take, @Element1 kitten element`

**Technique:** Kling's add-element pattern; the change is anchored to a moment, not a timestamp you'd have to measure; lighting match prevents a pasted-on look.
