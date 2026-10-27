# Qwen-Image-2.1 — Annotated Examples

Every example is two-part: **prompt** + **suggested settings**. Settings never appear in prompt text. Defaults unless stated: 40 steps · `true_cfg_scale` 1.0 · `use_kv_cache` on · fixed seed · save PNG.

---

## 1. Character Portrait (identity master)

```
A vertical cinematic portrait photograph of a middle-aged lunar cartographer standing
against a dark observatory wall. She occupies the right two-thirds of the frame,
looking just past the camera with a calm, analytical expression. Her short
silver-streaked hair is softly backlit, and she wears a practical charcoal flight
jacket with a small orange mission patch on the left shoulder. Along the left side,
the wall falls away into soft shadow, leaving generous negative space. The camera
sits at eye level with an 85 mm portrait perspective and shallow depth of field
focused on her eyes. Cool diffused light falls from the upper left, while a dim
amber instrument panel adds a warm edge along her jaw. The overall composition is
quiet and asymmetrical, with a restrained blue-grey and amber palette and a
thoughtful near-future mood.
```
**Settings:** `2:3 · 1696 × 2528 · steps 40 · cfg 1.0 · seed 42`

**Technique:** observational voice; opening sentence names medium + subject + background; spatial walk; one lighting sentence; one "overall composition" close. Save as the identity master for examples 9 and 11.

---

## 2. Environment

```
A wide photorealistic landscape photograph of a wind-carved coastal research station
on a black volcanic cliff at dawn. In the lower-left foreground, wet basalt rocks
reflect the pale sky, and a narrow metal walkway leads diagonally toward three low
weathered modules in the middle distance. On the right, waves break far below in
white ribbons, and the horizon stays unobstructed across the upper third. The camera
stands at shoulder height with a natural wide perspective and deep focus. Soft blue
morning light arrives from the left, while warm interior windows punctuate the
modules. The overall composition emphasises isolation and scale through a cool
slate, teal and charcoal palette.
```
**Settings:** `16:9 · 2752 × 1536 · steps 40 · cfg 1.0`

**Technique:** both sides of the wide frame are occupied; walkway is the leading line; three depth layers.

---

## 3. Action Still (decisive instant)

```
A low-angle editorial action photograph captures a parkour courier at the decisive
instant of clearing a narrow rooftop gap. The runner is suspended across the
centre-right of the frame, front knee raised, rear leg extended, one hand reaching
toward the landing ledge. The charcoal jacket and loose straps stream backward, fine
rain streaks diagonally through the frame, and water bursts from the takeoff edge.
Blurred rooftop vents fill the lower foreground and a dense neon city recedes behind.
The camera uses a wide 28 mm perspective; the face stays sharp while the hands,
trailing fabric and distant lights carry restrained directional motion blur. Cold
cyan signage contrasts with warm orange windows. The overall composition carries
urgent nocturnal energy along a strong left-to-right diagonal.
```
**Settings:** `3:2 · 2528 × 1696 · steps 40 · cfg 1.0`

**Technique:** motion as evidence (fabric, water, blur location) — one frame, not an animation.

---

## 4. Camera-Movement Keyframe

```
A cinematic film still viewed from a camera twenty centimetres above wet pavement,
tracking parallel to a vintage electric motorcycle racing from left to right through
a narrow night market. The motorcycle fills the lower-right half of the frame, its
rider leaning forward with focused eyes and both hands on the controls. Foreground
lantern poles sweep into elongated horizontal blur while the rider and motorcycle
remain crisp; market stalls and pedestrians recede in layered parallax behind them,
with open space ahead of the motorcycle on the right. Warm red lantern light reflects
across the pavement, balanced by cool blue rain light from the open street. The
overall composition feels like the midpoint of a fast lateral tracking shot.
```
**Settings:** `16:9 · 2752 × 1536 · steps 40 · cfg 1.0`

**Technique:** camera move expressed as a single viewpoint + parallax/blur evidence. Animate the move downstream in a video model using this as the keyframe.

---

## 5. Poster With Typography

```
A vertical modernist science-fiction poster printed on deep navy paper with a fine
fibrous texture. In the upper-left corner, a small pale-cyan monospaced label reads
"ORBITAL ARCHIVE 07". Across the upper third, a large condensed off-white headline
reads "MEMORY HAS" on the first line and "MASS" on a second line, with wide letter
spacing and strict left alignment. In the middle of the frame, an enormous
translucent amber sphere glows above a solitary small astronaut standing in the lower
centre. Thin cyan orbital diagrams arc behind the sphere and stop short of the
headline. Along the bottom edge, a compact off-white caption reads "A FILM BY LENA
VOSS". The lighting is flat and even, like a printed surface. The overall composition
is precise and archival-futurist, in navy, amber, cyan and off-white.
```
**Settings:** `2:3 · 1696 × 2528 · steps 40 · cfg 1.0 (A/B at 2.0 if letters soften)`

**Technique:** every string quoted, positioned, sized and styled; line break described in words; reading-order walk (corner → top → middle → bottom).

---

## 6. Infographic / Chart

```
A clean flat-design infographic on a warm off-white background. Across the top, a bold
charcoal sans-serif title reads "WATER USE PER KILOGRAM". Below it, a horizontal bar
chart fills the middle of the frame with three teal bars labelled on the left
"Beef", "Rice" and "Potatoes", and value labels at the end of each bar reading
"15,400 L", "2,500 L" and "290 L". The bars decrease in length from top to bottom.
A thin grey axis runs along the bottom with tick labels "0", "5,000", "10,000" and
"15,000". In the lower-right corner, a small grey caption reads "Source: sample data".
The lighting is shadowless and even. The overall composition is airy and legible,
with generous margins and a teal, charcoal and off-white palette.
```
**Settings:** `4:3 · 2400 × 1792 · steps 40 · cfg 1.0`

**Technique:** chart labels, values and ticks are all quoted text; bar order and relative length stated.

---

## 7. Transparent Game Asset (RGBA)

```
This is an RGBA image with transparency. A polished isometric game icon of a compact
brass astrolabe, with concentric engraved rings, a small sapphire pointer, crisp
bevelled edges, subtle oxidation in the recessed grooves and soft studio highlights,
centred with even margins and a contact shadow contained within its base. The image
has alpha channel and the background is transparent.
```
**Settings:** `1:1 · 2048 × 2048 · steps 40 · cfg 1.0 · save PNG (keep alpha)`

**Technique:** official wrapper verbatim; object-only description; shadow kept inside the silhouette.

---

## 8. Single-Image Edit (background replace)

**Input:** `image` = approved portrait (ex. 1)

```
Replace only the background with a quiet observatory interior at night, a large
brass telescope softly out of focus behind her and a starfield visible through an
open dome slit. Preserve the person, pose, expression, clothing, framing and
foreground lighting exactly as in the image, and match the new background's
perspective and depth of field to the original.
```
**Settings:** `2:3 · 1696 × 2528 (same as source) · steps 40 · cfg 1.0 · same seed · image: portrait`

**Technique:** imperative; change described concretely; one broad preserve clause; "the image" (no tag) for a single input.

---

## 9. Multi-Reference Composite

**Inputs:** `image=[identity, outfit, scene]`

```
Use <image3> as the scene canvas and preserve its composition, perspective, street
layout, weather and lighting. Place the person from <image1> on the right side of the
crosswalk, preserving the exact facial identity, hairstyle, skin tone and body
proportions from <image1>. Dress the person in the complete jacket, trousers, shoes
and shoulder bag from <image2>, preserving the garments' construction, colours and
materials. Pose the person walking toward the left while glancing over the right
shoulder. Match the cool rainy street illumination and ground reflections of <image3>.
```
**Settings:** `3:2 · 2528 × 1696 (canvas ratio) · steps 40 · cfg 1.0 · KV cache on · image: [identity, outfit, scene]`

**Technique:** one auditable role per tag; canvas named first in the prompt even though it's third in the list; identity pointed to, not described.

---

## 10. Marked Local Edit

**Input:** `image` = desk photo with a red circle drawn around a coffee mug

```
Replace only the object inside the red circle with a closed black leather notebook
lying flat and aligned to the desk's perspective, with a soft contact shadow matching
the window light. Remove the red circle in the result. Preserve every element outside
the marked region, including the camera angle, lighting, colours and composition.
```
**Settings:** `match source size · steps 40 (simple local edits tolerate fewer in ComfyUI) · cfg 1.0 · image: marked photo`

**Technique:** mark named by colour + shape; annotation removal requested; new object gets perspective and shadow behaviour.

---

## 11. Diffusers Call (identity-preserving new shot)

```python
import torch
from PIL import Image
from diffusers import QwenImage21Pipeline

pipe = QwenImage21Pipeline.from_pretrained("Qwen/Qwen-Image-2.1", torch_dtype=torch.bfloat16).to("cuda")
identity = Image.open("identity/cartographer_master.png")
location = Image.open("locations/greenhouse.png")

prompt = (
    "Use <image2> as the scene canvas and preserve its layout and lighting. Place the woman "
    "from <image1> kneeling beside the central planter, preserving her exact facial identity, "
    "silver-streaked hair and charcoal flight jacket from <image1>. She inspects a seedling "
    "with a small handheld lamp, her face in three-quarter profile toward frame left. "
    "Match the soft green bounce light and warm rim light of <image2>."
)

image = pipe(
    prompt=prompt,
    image=[identity, location],
    width=2752, height=1536,
    num_inference_steps=40,
    true_cfg_scale=1.0,
    use_kv_cache=True,
    generator=torch.Generator("cuda").manual_seed(42),
).images[0]
image.save("approved-shots/shot_04_v1.png")
```
**Settings:** `16:9 · 2752 × 1536 · steps 40 · cfg 1.0 · seed 42 · KV cache on · image: [identity, location]`

**Technique:** explicit size (never rely on `output_resolution` default); full recipe pinned; identity slot 1 kept constant across shots. For hosted `qwen-image-2.1-pro`, send the same prompt with the platform's `width`/`height`, reference array, seed and `promptExtend: false`.
