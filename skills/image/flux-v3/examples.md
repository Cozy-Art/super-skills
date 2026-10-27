# FLUX 3 Image — Annotated Examples

Every example is two-part: **prompt** + **suggested settings**. Settings never appear in prompt text.

---

## 1. Character Portrait (identity master)

```
A medium-close editorial portrait of Mara Venn, a woman in her early thirties
with a sharp oval face, dark brown eyes, a short black bob cut level with her
jaw, and a thin silver scar through her left eyebrow. She wears a charcoal
flight jacket with a small circular orange mission patch. She stands inside a
quiet orbital greenhouse, looking directly into the lens with calm resolve.
Soft green light reflects upward from the plants while a narrow warm rim light
outlines the right side of her face. Eye-level framing with an 85mm lens,
shallow depth of field, natural skin texture, restrained charcoal, moss green,
and amber palette.
```
**Settings:** `aspect_ratio: 4:5 · resolution: 2k · grounding: false`

**Technique:** shot size first → identity traits specific enough to repeat → light described by source and where it lands → palette as three named colours. This becomes the identity master for examples 6 and 7.

---

## 2. Environment

```
An ultra-wide landscape photograph of an abandoned coastal observatory at dawn.
Dark basalt cliffs occupy the left side, a pale concrete telescope dome sits
near the center, and the steel-blue ocean extends across the right half of the
frame. A narrow service road curves from the lower foreground toward the dome.
Low fog moves through three receding layers of terrain. Cold overcast ambient
light is interrupted by one warm beam from the rising sun, catching the dome
and wet road. Deep focus, restrained slate, rust, and pale gold palette.
```
**Settings:** `aspect_ratio: 21:9 · resolution: 2k · grounding: false`

**Technique:** left / center / right all assigned so the wide frame has no dead space; the road is the leading line; fog gives three depth layers.

---

## 3. Frozen Action

```
A low-angle sports photograph capturing the exact instant a motocross rider
clears a rain-soaked dirt jump. The motorcycle is tilted sideways in the upper
right, the rider's red jacket twists in the wind, and a fan of mud hangs frozen
behind the rear wheel. Two track marshals watch from the distant lower-left
background. Hard stadium lights cut through heavy rain, producing bright
droplets and silver rim light. Wide 28mm lens, sharp rider and motorcycle,
subtle directional motion blur in the crowd and track barriers.
```
**Settings:** `aspect_ratio: 16:9 · resolution: 2k · grounding: false`

**Technique:** "exact instant" + frozen debris = peak action; blur assigned to background only so the subject stays sharp.

---

## 4. Camera-Motion Aesthetic

```
A lateral panning photograph of a cyclist racing through a neon-lit intersection
at night. The cyclist and chrome bicycle remain sharply resolved at the center
while storefronts, traffic lights, and reflections stretch into horizontal
magenta and cyan streaks. The camera feels as though it is tracking beside the
rider at street level. Wet pavement mirrors the lights; the rider's coat streams
backward. 35mm lens, slow-shutter panning aesthetic, strong directional motion,
high contrast with controlled highlights.
```
**Settings:** `aspect_ratio: 3:2 · resolution: 1.5k · grounding: false`

**Technique:** camera movement expressed as its photographic evidence (streak direction, what's sharp).

---

## 5. Poster / Typography

```
A surreal theatrical poster rendered as a two-color lithograph on fibrous cream
paper. The exact title "THE TIDE ABOVE" appears in tall, weathered navy serif
lettering across the upper third, following the curve of a wave. A tiny
lighthouse keeper stands at the bottom of an enormous spiral staircase made
from curling ocean waves, rising toward a black moon at the top of the frame.
Limited navy #1F2A44 and vermilion #E34234 ink, imperfect registration, rough
printed edges, melancholy but adventurous mood, strong upward visual rhythm.
```
**Settings:** `aspect_ratio: 2:3 · resolution: 2k · grounding: false`

**Technique:** medium first, then the text instruction front-loaded with quote + placement + type character; hex locks the two inks.

---

## 6. Character Continuity (multi-reference)

**Inputs:** image 1 = identity master (ex. 1) · image 2 = wardrobe ref · image 3 = location ref

```
Create a new cinematic still featuring the same woman from image 1. Preserve
her exact facial structure, dark brown eyes, jaw-length black bob, left-eyebrow
scar, age, and body proportions. She now wears the charcoal technical coat from
image 2 and stands in the underground transit hall from image 3. Show her in a
three-quarter full-body view, walking toward frame left while glancing over her
right shoulder. Match the cool overhead lighting and green tiled reflections
of image 3. Keep the restrained charcoal, moss green, and amber art direction
of image 1, and keep her identity and hairstyle exactly as in image 1.
```
**Settings:** `aspect_ratio: 16:9 · resolution: 2k · grounding: false · images: [identity, coat, transit hall]`

**Technique:** every image gets a role; preserve list explicit; one new variable set (wardrobe + location) with identity locked.

---

## 7. Precise Boxed Layout

```
A cinematic science-fiction still showing pilot Mara Venn <character_1> inside
a damaged observation chamber <room_1>. A fractured planet <planet_1> fills the
window behind her. A small warning display <display_1> glows on the right.
[
  {"id": "room_1", "bbox": [0, 0, 1000, 1000],
   "desc": "A dark orbital observation chamber with brushed metal walls, suspended dust, broken ceiling panels, and cold cyan emergency light."},
  {"id": "planet_1", "bbox": [50, 80, 720, 680],
   "desc": "A huge fractured blue-white planet visible through a curved window, crossed by glowing amber fault lines."},
  {"id": "character_1", "bbox": [270, 80, 1000, 480],
   "desc": "Mara Venn, jaw-length black bob, scar through her left eyebrow, charcoal flight jacket, knees-up, three-quarter profile."},
  {"id": "display_1", "bbox": [350, 740, 700, 950],
   "desc": "A compact amber warning display reading \"ORBIT DECAY\" in precise condensed sans-serif lettering."}
]
```
**Settings:** `aspect_ratio: 16:9 · resolution: 2k · grounding: false · images: [identity master]` (optional)

**Technique:** background box covers the full frame; `[top, left, bottom, right]`; display box sized generously so the text renders.

---

## 8. Local Edit with Rows

**Input:** image 1 = approved frame from example 7

```
In <ref_image_0>, move <display_1> to the lower-left corner and change its text
to "OXYGEN 12%". Keep <character_1> and <planet_1> exactly as they are. Keep the
rest of the image completely unchanged.
[
  {"id": "character_1", "kind": "anchor", "from": "ref_image_0",
   "src_bbox": [270, 80, 1000, 480], "tgt_bbox": [270, 80, 1000, 480],
   "desc": "Mara Venn, unchanged."},
  {"id": "planet_1", "kind": "anchor", "from": "ref_image_0",
   "src_bbox": [50, 80, 720, 680], "tgt_bbox": [50, 80, 720, 680],
   "desc": "The fractured planet, unchanged."},
  {"id": "display_1", "kind": "new", "from": null, "src_bbox": null,
   "tgt_bbox": [700, 520, 960, 760],
   "desc": "A compact amber warning display reading \"OXYGEN 12%\" in condensed sans-serif."}
]
```
**Settings:** `aspect_ratio: auto · resolution: 2k · grounding: false · images: [example 7 result]`

**Technique:** anchors protect what matters; changed element re-described as `new` because its content changes.

---

## 9. Natural-Language Edit

**Input:** image 1 = portrait from example 1

```
Change only the lighting: make it late golden hour with low warm sun entering
from frame left and long soft shadows across the greenhouse plants. Preserve
her face, scar, hairstyle, jacket, pose, expression and the framing exactly.
Her identity and composition stay exactly as in image 1.
```
**Settings:** `aspect_ratio: auto · resolution: 2k · grounding: false · images: [portrait]`

---

## 10. Product Shot with Grounding

```
A clean studio product photograph of a matte black over-ear headphone resting
on a slab of pale travertine. Soft key light from upper left, a thin white rim
light along the headband, a gentle shadow falling to the right. Seamless warm
gray backdrop #D9D4CC. 100mm macro lens, f/8, every stitch on the leather
cushion visible.
```
**Settings:** `aspect_ratio: 4:5 · resolution: 2k · grounding: true` (if naming a real product) / `false` (generic)

---

## 11. FLUX.2 → FLUX 3 Payload Migration

```json
// FLUX.2 (will 422 on FLUX 3)
{"prompt": "Put the person in the red jacket", "input_image": "<scene>",
 "input_image_2": "<person>", "width": 1536, "height": 1024, "seed": 42,
 "guidance": 5, "output_format": "png"}
```
```json
// FLUX 3 Image
{"prompt": "Place the person from image 2 into image 1. Preserve the person's face, hairstyle, body proportions, and red jacket from image 2. Match the perspective, shadows, and warm afternoon lighting of image 1.",
 "images": ["<scene>", "<person>"], "aspect_ratio": "3:2", "resolution": "2k", "grounding": false}
```
**Technique:** instruction made explicit about roles; dimensions → ratio + tier; seed/guidance/format dropped.
