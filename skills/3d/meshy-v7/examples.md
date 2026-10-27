# Meshy 7.1 — Annotated Examples

Every example is two-part: **prompt(s)** + **suggested settings**. Settings never appear in prompt text. Geometry and texture prompts are separate blocks.

---

## 1. Simple Prop

```
A medieval wooden treasure chest, compact rectangular silhouette with a domed
lid, thick oak planks with raised forged-iron bands and a large padlock on the
front, grounded fantasy realism, single unified object.
```
**Settings:** `text-to-3d preview → refine · ai_model: meshy-7.1 · geometry_resolution: standard · texture_resolution: 2k · target_formats: [glb]`

**Technique:** subject → silhouette → countable features → construction that affects shape → one style → technical intent. No scene, no lighting.

---

## 2. Hero Prop with Separate Texture Prompt

Geometry prompt:
```
A deep-sea research drone, flattened oval hull, four short protected thrusters,
a front panoramic sensor dome and two folded manipulator arms, robust
industrial proportions, hard-surface science-fiction design, single watertight
vehicle asset.
```
Texture prompt:
```
Matte safety-yellow marine paint over aluminium, dark navy rubber seals, white
serial markings on the hull sides, salt deposits around seams, chipped edges
exposing bare metal, moderate roughness.
```
**Settings:** `preview: geometry_resolution: 4k · should_remesh: false → refine: enable_pbr: true · texture_resolution: 4k · target_formats: [glb, fbx]`

**Technique:** shape and surface split so paint and weathering don't eat the geometry budget. 4K geometry because panel seams and thruster grilles must be real geometry for close-ups.

---

## 3. Rig-Ready Character

```
A full-body desert courier android, slim humanoid proportions, rounded helmet
with one horizontal amber visor, compact backpack integrated into the torso,
sand-worn painted aluminium plates over dark rubber joints, clean retro-futurist
game art, symmetrical A-pose, separated arms and legs, rig-ready.
```
**Settings:** `text-to-3d preview → refine · ai_model: meshy-7.1 · pose_mode: a-pose · geometry_resolution: 2k · texture_resolution: 2k · then remesh ≤300k → rigging height_meters: 1.8`

**Technique:** pose set by field **and** echoed in text; backpack "integrated" so it doesn't float; no handheld items to fuse with fingers.

---

## 4. Stylized Character

```
A cheerful red-panda alchemist, oversized round head, short sturdy limbs, large
striped tail, round brass goggles pushed up on the forehead, soft carved-wood
appearance, whimsical stylized game character, T-pose, clean readable
silhouette.
```
**Settings:** `text-to-3d preview → refine · pose_mode: t-pose · geometry_resolution: standard · texture_resolution: 2k`

**Technique:** shape language ("oversized", "sturdy") carries the style. The potion-bottle belt was removed — loose small accessories float. Make them separate props.

---

## 5. Environment Module

```
A single ancient jungle temple gateway, broad stepped basalt arch on two thick
square pillars, shallow carved sun symbols across the lintel, cracked stone
edges softened by thick moss pads, weathered archaeological realism, modular
environment asset, solid unified construction.
```
**Settings:** `text-to-3d preview → refine · geometry_resolution: 2k · enable_pbr: true · texture_resolution: 4k · target_formats: [glb]`

**Technique:** one module, not "a jungle temple scene". Moss as thick pads (volume), not hanging roots or vines (thin strands fail).

---

## 6. Display Sculpture (static pose)

```
A cybernetic samurai captured at the end of a downward sword strike, wide
grounded stance, torso twisted slightly left, both armoured hands gripping a
thick katana angled toward the base, layered ceramic armour over black
mechanical joints, dynamic collectible-statue composition, sturdy connected
forms on an integrated round base.
```
**Settings:** `text-to-3d preview → refine · geometry_resolution: 4k · pose_mode: "" · texture_resolution: 4k · target_formats: [glb, stl]`

**Technique:** display mesh, so dynamic pose is fine — but connected forms and a base keep it printable. For an animatable version, make an A-pose master and animate the strike instead.

---

## 7. Multi-View Rebuild (exact asymmetric prop)

No geometry prompt — the views carry shape. Optional texture prompt:
```
Worn olive-green canvas, tan leather straps with brass buckles, faded white
stencil number on the front flap, frayed edges, matte finish.
```
```json
{
  "image_urls": ["https://example.com/front.png", "https://example.com/left.png", "https://example.com/back.png", "https://example.com/right.png"],
  "ai_model": "meshy-7.1",
  "geometry_resolution": "2k",
  "should_texture": true,
  "texture_prompt": "Worn olive-green canvas, tan leather straps with brass buckles, faded white stencil number on the front flap, frayed edges, matte finish.",
  "enable_pbr": true,
  "texture_resolution": "4k",
  "image_enhancement": false,
  "target_formats": ["glb", "fbx"]
}
```
**Settings:** `multi-image-to-3d · front view first · geometry_resolution: 2k (4k not available) · image_enhancement: false (clean renders)`

**Technique:** same pose, scale and light in every view; front first. `4k` would error here.

---

## 8. Retexture Variant Set (one mesh, three factions)

```
Faction skin: polished royal-blue enamel armour plates, gold filigree trim on
plate edges, white leather straps, light scuffs on raised edges, satin finish.
```
```
Faction skin: blackened iron armour plates, dull red cloth wraps, bone-white
rivets, heavy rust in crevices and soot on lower plates, rough matte finish.
```
```
Faction skin: verdigris bronze armour plates, mossy green cloth wraps, pale
stone inlays, patina pooled in recesses, worn bright highlights, semi-matte.
```
**Settings:** `retexture · input_task_id: <master refine task> · enable_original_uv: true · enable_pbr: true · texture_resolution: 2k · ai_model: meshy-7`

**Technique:** identical sentence structure, only material/palette nouns swapped → variants read as one family. Original UVs keep texel density consistent. Retexture runs on Meshy 7 (`latest` there = 7).

---

## 9. Game-Ready Prop Kit Item (Smart Topology)

```
A wooden market crate stacked with three cabbages, chunky slatted box with
corner posts, cabbages resting securely inside, chunky hand-sculpted stylized
fantasy, soft bevelled edges, slightly exaggerated proportions, single unified
object, game-ready.
```
**Settings:** `text-to-3d preview → refine · model_type: smart-topology · ai_model: meshy-t2.5 · target_polycount: 4000 · topology: triangle · texture_resolution: 2k`

**Technique:** the last sentence is the kit's verbatim style lock block. Smart Topology gives clean low-poly triangles from the start; `quad` would error here.

---

## 10. Motion Pipeline (character → rig → custom clip)

Geometry prompt:
```
A full-body armoured parkour courier, athletic human proportions, flexible
segmented chest armour, reinforced knee pads, compact helmet and lightweight
boots, practical near-future design, neutral A-pose, separated arms and legs,
rig-ready.
```
Text to Motion prompt:
```
The character sprints forward for two steps, plants the left foot, vaults over
a waist-high obstacle with both hands, lands softly on bent knees, and regains a
balanced running stance.
```
```json
{ "prompt": "The character sprints forward for two steps, plants the left foot, vaults over a waist-high obstacle with both hands, lands softly on bent knees, and regains a balanced running stance.", "mode": "prime", "duration": 4.5 }
```
Then:
```json
{ "rig_task_id": "<rigging task id>", "motion_task_id": "<text-to-motion task id>", "post_process": { "operation_type": "change_fps", "fps": 24 } }
```
**Settings:** `text-to-3d preview (pose_mode: a-pose) → refine → remesh ≤300k → rigging → text-to-motion prime 4.5 s → animations change_fps 24`

**Technique:** motion prompt = sequence + mechanics + end state, no camera. Camera moves ("low side-tracking, 35mm") are authored in the renderer. Apply the clip within 3 days of the motion task.
