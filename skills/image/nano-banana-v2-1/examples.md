# Nano Banana 2.1 — Annotated Examples

Every example is two-part: **prompt** + **suggested settings**. Settings never appear in prompt text.

---

## 1. Product Shot

```
A premium studio product photograph of a matte-black ceramic travel mug centred
on pale limestone. A softbox above-left lays a long diffused highlight along the
rim and a soft contact shadow falls to the lower right. Slightly elevated
three-quarter view, product-photography lens look, crisp ceramic texture, warm
neutral palette, clean unmarked surfaces.
```
**Settings:** `aspect_ratio: 1:1 · image_size: 1K (draft) / 2K (final) · thinking_level: medium`

**Technique:** light described by source and where it lands; "clean unmarked surfaces" instead of "no logo".

---

## 2. Character Portrait (from a reference)

**Inputs:** casting portrait of the actor

```
A close cinematic portrait of the woman in the attached portrait, seated by a
train window at blue hour, looking out with quiet determination. Cool window
light shapes the right side of her face; a dim amber carriage lamp rims her
hair. Keep her oval face, dark curls, the small scar through her left eyebrow
and her gold stud earrings identical to the portrait. Photoreal, 85mm lens look,
shallow depth of field, subtle film grain.
```
**Settings:** `aspect_ratio: 4:5 · image_size: 2K · thinking_level: medium · references: [casting portrait]`

**Technique:** reference bound by content; identity anchors listed as the keep-list; two light sources, one dominant.

---

## 3. Environment Landscape

```
A vast establishing photograph of a windswept coastal research station on black
volcanic cliffs. Foreground: wet basalt and orange lichen. Middle ground: three
low white modular buildings joined by covered walkways. Background: a steel-gray
ocean under an approaching squall, with a thin break of sunlight on the horizon.
Chest-height 24mm wide perspective; horizon on the upper third; the station sits
in the lower-left third and the right half is open sea and weather. Cold
desaturated palette, wind-driven rain, documentary realism.
```
**Settings:** `aspect_ratio: 21:9 · image_size: 2K · thinking_level: medium`

**Technique:** explicit layers and thirds so the wide frame has no dead space.

---

## 4. Frozen Action

```
A decisive action photograph of a downhill mountain biker launching from a wet
rock ledge toward frame left. The rider is fully airborne, knees bent, front
wheel slightly high; a sheet of muddy water explodes from the rear tyre. Camera
low beside the trail, 28mm look, rider sharp, directional blur only in the trees
and spinning wheels, overcast forest light with one cool backlight through mist.
Keep the rider's red full-face helmet and the turquoise frame clearly readable.
Exactly one rider and one bicycle.
```
**Settings:** `aspect_ratio: 3:2 · image_size: 2K · thinking_level: high`

**Technique:** body mechanics + direction of travel; blur assigned to background; count stated positively; `high` thinking for spatial relationships.

---

## 5. Camera-Motion Aesthetic

```
A single photographic frame with the energy of a fast handheld tracking shot: a
courier sprints toward camera through a crowded night market while the camera
retreats at waist height. Her face and torso stay sharp; lanterns and stalls
stretch into soft directional streaks behind her; foreground shoppers cross the
frame as partial occlusions. 35mm perspective, slight dutch angle, wet pavement
reflecting cyan and amber signs.
```
**Settings:** `aspect_ratio: 16:9 · image_size: 2K · thinking_level: high`

**Technique:** the camera move expressed as its still-frame evidence; "a single photographic frame" prevents storyboard panels.

---

## 6. Multi-Reference Campaign Composite

**Inputs:** model portrait · bicycle · helmet · waterfront location (4 references: 1 character, 3 object)

```
Create a premium outdoor campaign photograph. The woman from the portrait
reference rides the forest-green bicycle along the empty waterfront path from
the location photo, wearing the cream helmet with its straps fastened. She
approaches at a slight angle in the left third; the harbour stays visible across
the right half for campaign copy.

Use the golden-hour direction and long shadows of the location photo for every
element. Preserve her face, gray hair streak and mustard jacket. Preserve the
bicycle's step-through frame, tan saddle, front basket and cream tyres. Preserve
the helmet's shape, cream shell and tan straps. Photoreal 35mm lifestyle
advertising, natural wheel blur, clean unmarked surfaces.
```
**Settings:** `aspect_ratio: 16:9 · image_size: 2K · thinking_level: high · references: [portrait, bicycle, helmet, waterfront]`

**Technique:** Google's `[References] + [Relationship] + [New scenario]` order; one final light model; per-reference preservation list; negative space named.

---

## 7. Infographic with Exact Copy

```
A horizontal four-panel infographic titled "HOW RETURNS WORK" in large dark-navy
capitals at the top, on an off-white background. Below it, four equal panels in
one row, read left to right, joined by thin coral arrows. Each panel holds a
coral numbered circle, one navy line icon, a bold heading and one smaller gray
caption.

Panel 1: number "1", laptop icon, heading "Start online", caption "Request a return in your account".
Panel 2: number "2", printer icon, heading "Print label", caption "We email a prepaid shipping label".
Panel 3: number "3", parcel icon, heading "Drop off", caption "Leave it at any pickup point".
Panel 4: number "4", wallet icon, heading "Get refunded", caption "Money back within 5 days".

Flat vector style, generous spacing, identical panel structure, consistent line
weight, crisp legible typography.
```
**Settings:** `aspect_ratio: 16:9 · image_size: 2K · thinking_level: high`

**Technique:** grid before content; parallel sentences per panel; every string quoted with a role.

---

## 8. Conversational Edit (thread)

**Input:** the previous turn's image (sent with `previous_interaction_id`)

```
Change only the jacket, from navy wool to rust suede with the same cut and
collar. Keep her face, pose, hands, the train window, the camera position and
the blue-hour lighting unchanged.
```
**Settings:** `aspect_ratio: (unchanged) · image_size: 2K · thinking_level: medium · previous_interaction_id: <prior turn>`

**Technique:** one change, before → after, concrete keep-list drawn from the actual frame.

---

## 9. Panorama

```
A seamless panoramic illustration of a coastal city at dusk, read left to right:
harbour cranes and container ships at the far left, the old town climbing a hill
of terracotta roofs in the centre, a lit cathedral spire and a lighthouse on the
headland at the right edge. A continuous band of warm windows runs along the
waterline; the sky shifts from apricot on the left to deep indigo on the right.
Gouache on textured paper, soft dry-brush edges, limited warm-cool palette.
```
**Settings:** `aspect_ratio: 4:1 · image_size: 2K (4K if your plan offers it) · thinking_level: medium`

**Technique:** the frame described as bands so no section repeats; extreme ratio rendered at 2K+.

---

## 10. Thumbnail from a Video

**Input:** the product demo video

```
From the attached product video, design a bold video thumbnail. Use the moment
the lid lifts and steam rises: the cooker large on the right, slightly
low-angle, crisp and bright. On the left, the headline "10-MINUTE RAMEN" in
heavy white condensed sans with a thin black outline, stacked on two lines.
Saturated warm kitchen background softly blurred.
```
**Settings:** `aspect_ratio: 16:9 · image_size: 1K · thinking_level: high · references: [demo video]`

**Technique:** video as context only — names the moment to extract and the still to design; headline quoted with style and placement.
