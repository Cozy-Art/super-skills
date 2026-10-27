# World Labs Atlas — Annotated Examples

Every example is **prompt** (appearance text only) + a separate **settings** line, plus a **camera plan** for posed tasks. Settings and camera numbers never appear in prompt text.

---

## 1. World concept seed

```
A quiet stone courtyard enclosed by two-story arcades. In the foreground a worn
limestone path curves around a shallow fountain; ivy-covered arches lead to a
warm workshop doorway in the background. Damp stone, oxidized bronze and dark
oak. Blue hour with warm window light and a thin ground mist. Wide eye-level
view with clear foreground, midground and distant sightlines. Photorealistic
cinematic naturalism, the courtyard empty and still.
```
**Settings:** `task: atlasTextToImage · aspectRatio: 16:9 · enhancePrompt: true · numSamples: 4 · returnDepth: false`

**Technique:** place → three named depth layers → materials → light/time → viewpoint → style. "Empty and still" states the absence positively. Pick the sample with the clearest ground plane to pose next.

---

## 2. Landscape at scale

```
A wind-carved basalt valley three kilometers wide, crossed by a pale glacial
river. Black hexagonal cliffs rise on both sides; sparse red tundra plants fill
the foreground and low fog follows the river into distant snow fields. Overcast
arctic noon with soft directional light and deep atmospheric perspective. Wide
elevated viewpoint over an uninterrupted horizon, physically grounded
photorealism.
```
**Settings:** `task: atlasTextToImage · aspectRatio: 16:9 · enhancePrompt: true · numSamples: 3`

**Technique:** a real dimension ("three kilometers") prevents room-scale ambiguity; fog and a river give receding depth cues.

---

## 3. Character as scale anchor

```
A vast abandoned orbital greenhouse with a collapsed glass dome at the far end.
A lone salvage engineer in an orange pressure suit stands small on the left
third, facing away toward the dome. Foreground tools and wet soil, a central
aisle receding into the distance between dense silver-green plants,
condensation on fractured glass. Cold dawn light through the dome with warm
helmet lamps. Wide environmental view; the architecture is the subject.
```
**Settings:** `task: atlasTextToImage · aspectRatio: 16:9 · enhancePrompt: true · numSamples: 4`

**Technique:** the person is small, turned away and static — story without asking the model's weakest skill (faces, articulated motion) to carry the frame.

---

## 4. Action implied by state

```
A rain-soaked maglev maintenance depot seconds after an emergency stop. The
train sits stationary while steam vents diagonally across the platform; warning
beacons reflect in shallow puddles and loose paper lies along the airflow path.
Long platform perspective under exposed service gantries, heavy cables in the
near foreground. Amber emergency light against cool storm daylight. The platform
is deserted, with clear walkable space and stable architecture.
```
**Settings:** `task: atlasTextToImage · aspectRatio: 16:9 · enhancePrompt: true · numSamples: 4`

**Technique:** steam direction, debris and reflections read as motion without moving actors; foreground cables give parallax for later camera work.

---

## 5. Single-image push-in

```
The same quiet stone courtyard at blue hour, seen from slightly closer to the
fountain.
```
**Settings:** `task: images2PosedRGBD → atlasGenerate · context: 1 posed RGBD · targets: 6 · enhancePrompt: true · returnDepth: true`

**Camera plan:** copy the posed source camera; targets 1–6 each translate +0.05 along the camera's forward axis (≈0.3 total, scene units ≈ metres); orientation and intrinsics unchanged; `coordinateSystem` as returned by posing.

**Technique:** text only restates *what* the scene is; the move is entirely in the targets. Short first move inside observed space; depth requested because these views will become context.

---

## 6. Orbit around a hero prop

```
The same ceramic service robot in the same sunlit courtyard, preserving its
white crackle glaze, blue shoulder markings, weathering and scale, and the
courtyard's warm afternoon light.
```
**Settings:** `task: atlasGenerate · context: 3 posed RGBD (front, three-quarter, rear) · targets: 13 · prompt: previous promptUsed · enhancePrompt: false · seed: fixed · returnDepth: true`

**Camera plan:** 13 targets on a constant-radius arc from 0° to 180° in 15° steps, all aimed at one robot-centred look-at point; constant height and intrinsics.

**Technique:** three-sided reference evidence carries identity; reusing `promptUsed` with enhancement off locks appearance across the arc.

---

## 7. Reveal from behind occlusion

```
A monumental underground archive carved from dark volcanic stone. Tall shelves
of sealed brass cylinders ring a circular reading chamber; dust hangs in narrow
shafts of warm light from ceiling apertures. A tight, shadowed corridor in the
near foreground opens into the bright chamber beyond. Restrained black, bronze
and amber palette, cinematic realism.
```
**Settings:** `task: atlasGenerate · context: posed seed + accepted views · targets: 10 · enhancePrompt: false (reuse promptUsed after first pass) · returnDepth: true`

**Camera plan:** A = behind a near stone pier; B = 0.3–0.6 lateral translation clearing the pier; C = clear sightline, yawing toward the chamber centre. Fill A→C with intermediate targets for smoothness.

**Technique:** the prompt builds the occluder and the reward; the geometry performs the reveal.

---

## 8. Multishot continuity

Master appearance prompt:
```
A compact 1970s coastal research station built into a foggy concrete
breakwater. Pale mint laboratory walls, orange fiberglass chairs, brushed
aluminum instruments, wet terrazzo floors and large salt-streaked windows facing
the sea. Soft overcast daylight, cyan-gray exterior fog, restrained warm
practical lights, subtle 35 mm film grain and muted period colour.
```
**Settings:** `A: atlasTextToImage → pose · B–D: atlasGenerate · prompt: A's promptUsed · enhancePrompt: false · seed: fixed`

**Camera plan:** A wide exterior from the breakwater → B medium through the main window → C low path down the instrument corridor → D close on a tide recorder with the room behind. Each shot is its own target set, generated from the nearest accepted keyframes.

**Technique:** one master prompt, many camera sets. Never paste the shot list as one prompt — that asks for a collage.

---

## 9. Blockout to environment

```
A rain-darkened brutalist transit hall with board-formed concrete walls, a
polished wet granite floor and amber wayfinding light strips along the soffits.
Cool overcast daylight falls through a long clerestory; a faint haze hangs
under the ceiling.
```
**Settings:** `task: atlasChisel · contextFrames: 1 depth per target · sourceFrames: 4 posed photos · targets: 30 · voxelSize: 0.1 · voxelGridOrientation: world · enhancePrompt: true`

**Camera plan:** 30 targets rendered from the blockout scene's camera path; depth rasters at 1280 × 720 from the same cameras.

**Technique:** layout is already fixed by depth, so the prompt spends its words on materials and light. 4 sources + 30 depth + 30 targets = 64, the rollout cap.

---

## 10. Multiview object replacement

```
Replace the yellow utility cart beside the west arch with a low oxidized-bronze
fountain.
```
**Settings:** `task: atlasMasked (account access required) · contextFrames: 8 · targets: 8, paired by index · enhancePrompt: true`

**Masks:** frame 0 = the hand-edited anchor, all-white; frames 1–7 = black over the whole cart plus a small margin, white elsewhere; 8-bit grayscale PNG on each image's grid.

**Technique:** the enhancer can't see masks, so the instruction locates the edit by a visible landmark ("beside the west arch"). With `enhancePrompt: false`, write the finished caption instead: "A low oxidized-bronze fountain stands beside the west arch in the quiet stone courtyard at blue hour."
