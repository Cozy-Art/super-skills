# Tripo P1 — Annotated Examples

Every example is two-part: **prompt** (+ optional negative prompt) and **suggested settings**. Settings never appear in prompt text. All use `model: P1-20260311`.

---

## 1. Mobile Game Prop

```
A stylized low-poly wooden supply crate, squat rectangular form, thick corner planks,
separate iron bands and recessed side handles, dark oak and blackened steel, mobile game prop.
```
Negative prompt:
```
floating boards, broken corners, open lid, text, logo, thin geometry
```
**Settings:** `face_limit: 1200 · texture: true · pbr: true · texture_quality: standard · auto_size: true · export_uv: true`

**Technique:** asset → form → three parts → materials → use, 27 words. Wear and scratches are left out of geometry; ask for them in a later texture pass if needed.

---

## 2. Riggable Character (geometry pass, then texture)

```
A friendly bipedal maintenance robot in a neutral symmetrical A-pose, broad rounded torso,
short segmented arms held away from the body, separate shoulder shells, compact tool backpack,
large oval head with one recessed visor, stylized low-poly game character, white ceramic
panels with orange accents, clean silhouette for rigging.
```
Negative prompt:
```
duplicate limbs, fused arms, crossed legs, floating parts, tiny fingers, weapon, text
```
**Settings:** pass 1 `face_limit: 12000 · texture: false · pbr: false` (try 3 `model_seed`s) → pass 2 same seeds `texture: true · pbr: true · texture_quality: detailed`

**Technique:** pose and limb clearance stated up front for rigging; "separate" on shells and backpack helps segmentation. Then `rig-check` → `rig` (see example 9).

---

## 3. Quadruped Creature

```
A lean quadruped courier lizard in a neutral standing pose, long tapered torso, four clearly
separated muscular legs, broad flat feet, thick balancing tail held straight back, compact
saddle harness as a distinct part, stylized low-poly game creature, teal scales and worn
brown leather.
```
Negative prompt:
```
running pose, crossed legs, extra limbs, curled tail touching body, rider, floating straps
```
**Settings:** `face_limit: 10000 · texture: true · pbr: true · texture_quality: standard`

**Technique:** leg count + "clearly separated" + tail away from body = clean quadruped rig. Motion comes later: rig `model: v2.5-20260210 · rig_type: quadruped` → retarget `preset:quadruped:walk`.

---

## 4. Hard-Surface Vehicle

```
A compact lunar exploration buggy, low rectangular chassis, four oversized wheels in separate
wheel housings reaching halfway up the body, open two-seat cockpit, rear equipment rack and a
front sensor mast, hard-surface stylized low-poly design, matte white composite with dark grey
rubber and small blue accents.
```
Negative prompt:
```
six wheels, enclosed cabin, driver, background, floating equipment, asymmetric wheels
```
**Settings:** `face_limit: 15000 · texture: false` → lock `image_seed` + `model_seed` → `pbr: true · texture_quality: detailed`

**Technique:** wheel count and a ratio ("halfway up the body") remove the two most common vehicle failures; negative prompt pins the count.

---

## 5. Modular Environment Kit (style block)

```
A straight ruined sandstone wall module, wide rectangular slab about twice as wide as tall,
thick stepped top edge with two broken notches, flat connection faces on both sides, flat
base aligned to the ground, stylized low-poly PBR game asset, rounded bevelled edges, broad
readable shapes, matte hand-painted surfaces, warm sandstone and driftwood palette with teal accents.
```
Negative prompt:
```
surrounding terrain, plants, people, loose rubble, floating stones, arch
```
**Settings:** `face_limit: 3500 · pbr: true · texture_quality: standard · auto_size: true` · keep `export_orientation` unset

**Technique:** everything after "stylized low-poly…" is the kit's verbatim style block. Siblings swap only the first clause: "A ruined sandstone corner wall module…", "A sandstone archway gate module…".

---

## 6. Same Mesh, Material Variants

Base prompt (approved):
```
A ceremonial owl mask, symmetrical heart-shaped silhouette, deep recessed eye sockets,
layered feather plates as broad separate forms, carved dark walnut with aged-brass inlays,
stylized handcrafted fantasy prop, flat wall-mountable back surface.
```
Variant via `POST /v3/models/texture`:
```json
{
  "input": "task_<approved_mask>",
  "model": "v3.5-20260815",
  "texture_prompt": { "text": "pale bleached bone with soot-blackened recesses and verdigris copper inlays" },
  "texture_seed": 2207,
  "texture_quality": "detailed",
  "pbr": true
}
```
**Settings:** generation `face_limit: 6000 · image_seed/model_seed locked` · texture call as shown

**Technique:** retexturing the task_id guarantees identical geometry; `texture_prompt.text` carries only material language. Note `model` here is the *texture* version.

---

## 7. Multiview Product (no text prompt)

Reference brief for the image model making the four views:
```
Orthographic-style product view of a compact red water pump, cylindrical motor housing on a
flat rectangular base, round intake on the left, outlet pipe on top. Centred, full object in
frame, plain light-grey seamless background, soft shadowless studio light, identical scale
and camera height in every view, no text or watermark.
```
Request:
```json
{
  "model": "P1-20260311",
  "inputs": [
    {"front": "https://assets.example.com/pump_front.png"},
    {"left":  "https://assets.example.com/pump_left.png"},
    {"back":  "https://assets.example.com/pump_back.png"},
    {"right": "https://assets.example.com/pump_right.png"}
  ],
  "model_seed": 731902,
  "face_limit": 18000,
  "pbr": true,
  "texture_alignment": "original_image",
  "auto_size": true
}
```
**Settings:** as shown · rerun with same `model_seed` for reproducibility

**Technique:** the endpoint has no `prompt` — intent lives in consistent views. `front` is mandatory; view-key form only, never mixed with positional strings.

---

## 8. Single Concept Image, Chained

```
A chunky stylized treasure goblin standing in a neutral A-pose, full body, three-quarter
view, centred on a plain white background, soft even studio light, no shadows, clear gaps
between arms and torso and between the legs.
```
**Settings:** make the image with a Tripo `text_to_image` task → `POST /v3/generation/image-to-model` with `input: "<that task_id>" · face_limit: 14000 · texture_alignment: original_image · enable_image_autofix: false`

**Technique:** the prompt here is for the *reference image*. ¾ view exposes depth; limb gaps survive into the mesh. Chaining by task_id avoids re-upload and keeps the exact image.

---

## 9. Rig + Animation Chain

```
1. POST /v3/animations/rig-check   {"input": "task_<robot>"}                → riggable: true, rig_type: biped
2. POST /v3/animations/rig         {"input": "task_<robot>", "model": "v3.0-20260909",
                                    "rig_type": "biped", "spec": "unity", "out_format": "fbx"}
3. POST /v3/animations/retarget    {"input": "task_<rig>", "animations": ["preset:idle", "preset:walk", "preset:run"],
                                    "animate_in_place": true, "out_format": "fbx"}
4. POST /v3/models/convert         {"input": "task_<retarget>", "format": "FBX",
                                    "pivot_to_center_bottom": true, "fbx_preset": "bake_scale"}
```
**Settings:** source mesh from example 2 · same rig `model`/`spec` for every character in the project

**Technique:** P1 never animates; the neutral pose from the prompt is what makes this chain work. Short `preset:*` IDs are documented for rig v2.5; confirm the preset list for rig v3.0 on your account (unverified). If retarget rejects them, use rig v1.0 with `preset:biped:*`.

---

## 10. Blockout at Minimum Budget

```
A low-poly watchtower blockout, square stone base, tall tapering wooden shaft about four
times taller than the base width, flat square lookout platform with a pyramid roof.
```
**Settings:** `face_limit: 400 · texture: false · pbr: false · export_uv: false`

**Technique:** four big forms only — at 400 faces, railings, ladders and shingles would just collapse. Fastest, cheapest pass for layout or greyboxing.

---

## 11. Fast Look-Dev Texture

```
A stylized potion bottle, round bulbous body with a short narrow neck, chunky cork stopper,
thick glass with glowing violet liquid, leather tag tied as one solid band around the neck,
mobile game pickup item.
```
**Settings:** `face_limit: 1500 · pbr: true · texture_quality: fast · texture_version: v3.5-20260815 · delight: true`

**Technique:** `fast` costs the same as `standard` and is only valid with texture v3.5 (otherwise error `1004`). The tag is written as "one solid band" to avoid a thin floating string.

---

## 12. Migrating to P2 for Quads

Same prompt as example 2, changed fields only:
```json
{ "model": "P2-20260801", "quad": true, "face_limit": 20000 }
```
**Settings:** P2 quad range 48–25,000; triangle up to 50,000

**Technique:** prompts transfer unchanged — migration is parameter-level. Never send `quad` with P1 (400). Alternative that stays on P1: `models/convert` with `quad: true` (forces FBX output).
