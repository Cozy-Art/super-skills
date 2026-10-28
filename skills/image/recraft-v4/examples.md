# Recraft V4 — Annotated Examples

Every example is two-part: **prompt** + **suggested settings**. Settings never appear in prompt text.

---

## 1. Flash Exploration (interpretive)

```
Fashion portrait of an older woman architect, close-up, soft window light, quiet confidence.
```
**Settings:** `model: recraftv4_1_flash · size: 4:5 · n: 6 · response_format: multipart`

**Technique:** under 15 words leaves composition and styling to the model; six cheap rolls to find a direction before writing an architectural prompt.

---

## 2. Controlled Character Scene (identity master)

```
Editorial environmental portrait. Mara, a woman in her early 40s with warm
brown skin, short tightly curled black hair, a small scar through the left
eyebrow, dark green eyes, and one brass crescent earring, stands in the right
third of a quiet railway workshop. She wears a charcoal field jacket with a
rust-orange collar and holds a folded route map at waist height. Eye-level
medium shot, relaxed shoulders, direct gaze. Soft overcast daylight enters
from tall windows on camera-left; subtle warm practical lights recede behind
her. 50 mm documentary-photography look, moderate depth of field, natural skin
texture, muted charcoal, rust, brass and blue-gray palette. No text or logos.
```
**Settings:** `model: recraftv4 · size: 3:4 · n: 4 · random_seed: 271828 · image_format: png`

**Technique:** identity sentence first and reusable verbatim; placement in thirds; light by source and direction; single short exclusion at the end.

---

## 3. Landscape and Atmosphere

```
Wide cinematic landscape of a red research station on a vast black volcanic
plain at blue hour. Low clouds drag across distant ridges; a narrow warm window
glow is the only artificial light. Low viewpoint with dark basalt in the
foreground, the station small in the middle distance, mountains fading into
cold haze. 24 mm wide-angle look, restrained slate-blue, charcoal and
signal-red palette, immense negative space, quiet isolation.
```
**Settings:** `model: recraftv4 · size: 16:9 · n: 2` (screen weather/season variants on `recraftv4_1_flash` first)

**Technique:** foreground / midground / background each assigned; one warm light source as focal point against a cold palette.

---

## 4. Action Still (panning aesthetic)

```
Documentary sports photograph of one track cyclist sprinting left-to-right
through a rain-darkened city circuit. The decisive instant as the rider leans
into the turn: face and torso sharp, wheels and spectators stretched into
horizontal motion blur. Very low curb-level side angle, 35 mm panning-shot
aesthetic, wet pavement reflecting white and amber lights, spray lifting from
the rear tyre. High contrast, natural athletic posture. No signage, logos or
extra riders.
```
**Settings:** `model: recraftv4 · size: 3:2 · n: 4`

**Technique:** describes the visible result of panning — where blur is and isn't — rather than a camera move; count locked with "one" and "no extra riders".

---

## 5. Depth Study (Pro detail)

```
Cinematic interior photograph inside a vast modern observatory at dawn. A lone
astronomer stands in silhouette in the lower-left foreground while the open
dome and telescope rise through the center. Ultra-wide 20 mm perspective from a
slightly low angle; a blurred metal railing frames the near foreground, the
astronomer and telescope remain crisp, and a pale mountain horizon dissolves
into mist beyond the dome. Cool diffuse sky light with one narrow warm rim from
the east. Monumental scale, steel-blue and amber palette, deep spatial layering.
```
**Settings:** `model: recraftv4_pro · size: 2:1 · n: 1 · image_format: png`

**Technique:** Pro earns its cost on dense structure and fine edges; three explicit depth planes with focus assigned to each.

---

## 6. Typography Poster

```
Large-format contemporary museum poster on a matte black background. A
translucent cobalt glass sculpture floats slightly below center and casts a
soft refracted blue glow. Oversized uppercase condensed headline "FORM / LIGHT"
spans the top edge, tightly spaced and slightly cropped. A smaller line
"NEW MEDIA EXHIBITION" runs vertically along the right edge. The date
"18 OCT — 09 FEB" sits bottom-left in a clean geometric sans-serif. The
sculpture overlaps the lower edge of the headline without obscuring
readability. Strict black, cobalt and off-white palette, precise modernist
grid, generous negative space, premium print finish. No additional copy or logos.
```
**Settings:** `model: recraftv4_pro · size: 2:3 · n: 1 · image_format: png`

**Technique:** three quoted strings with explicit hierarchy and position; layer interaction stated; no `text_layout` exists, so placement is prose. Add body copy afterwards.

---

## 7. Vector Icon Set

```
Exactly six navigation icons for a coastal science museum, arranged in a
3 × 2 grid: lighthouse, wave sensor, research vessel, shell specimen, weather
balloon and map marker. Flat vector icons with bold geometric silhouettes,
consistent rounded corners, uniform visual weight, identical stroke logic and
generous internal negative space. Strict two-colour system: deep navy and warm
coral on white. Flat solid fills only; no gradients, shadows, texture,
lettering or perspective. Each icon remains recognizable at 24 pixels.
```
**Settings:** `model: recraftv4_vector · size: 3:2 · n: 4 · controls.colors: [{rgb:[22,38,74],weight:0.6},{rgb:[240,110,90],weight:0.4}] · controls.background_color: {rgb:[255,255,255]}`

**Technique:** geometry and stroke rules instead of material language; count + grid named; colour count fixed in prose and RGB. Ratio form only for vector.

---

## 8. Logo Mark

```
Minimal logo mark for an independent coffee roaster called "Northbound". A
single geometric compass needle merged with a coffee bean silhouette, built
from two interlocking shapes on a strict circular grid. Bold even stroke
weight, rounded terminals, balanced optical center. Wordmark "NORTHBOUND"
centered beneath in a wide geometric sans-serif, all caps, generous tracking.
Two flat colours: espresso brown and cream. Scales cleanly from favicon to
signage.
```
**Settings:** `model: recraftv4_vector · size: 1:1 · n: 4` → finalist on `recraftv4_pro_vector · n: 1`

**Technique:** shape logic and grid first, wordmark as a quoted secondary element; explore on V4 Vector ($0.08), finish on Pro Vector ($0.30).

---

## 9. Brand-Palette Product Shot (full payload)

```
Editorial product photograph of one matte cobalt perfume bottle centered on
pale limestone. Soft daylight from upper left, long gentle shadow to lower
right, 85 mm product-photo look, restrained cobalt and warm ivory palette.
No text or logos.
```
**Settings:** `model: recraftv4 · size: 4:5 · n: 4 · random_seed: 314159 · response_format: multipart · image_format: png`

```json
{
  "prompt": "Editorial product photograph of one matte cobalt perfume bottle centered on pale limestone. Soft daylight from upper left, long gentle shadow to lower right, 85 mm product-photo look, restrained cobalt and warm ivory palette. No text or logos.",
  "model": "recraftv4",
  "size": "4:5",
  "n": 4,
  "random_seed": 314159,
  "controls": {
    "colors": [{"rgb": [28, 62, 142], "weight": 0.6}, {"rgb": [239, 230, 210], "weight": 0.3}],
    "background_color": {"rgb": [239, 230, 210]}
  },
  "response_format": "multipart",
  "image_format": "png"
}
```
**Technique:** palette stated in words and reinforced with weighted RGB controls (weights sum ≤1.0).

---

## 10. Style-Reference Series

```
A fox librarian shelving books on a tall rolling ladder, seen from below, warm
lamplight pooling on the floor, a cat asleep on the lowest rung.
```
**Settings:** `model: recraftv4 · size: 4:5 · n: 2 · style_reference_urls: [one clean illustration ref] · style_match: precise` → reuse returned `style_id` for every later frame (drop the URLs)

**Technique:** the prompt carries only subject, pose and composition — the reference carries line, colour and texture. Never send `style_id` and references together.

---

## 11. Image-to-Image Continuity

**Input:** `image_url` = approved portrait from example 2

```
The same woman and wardrobe, now standing beside a train window at dawn.
Preserve her facial identity, haircut, earring, jacket and the eye-level
framing. Replace the workshop light with soft cool dawn light from the window.
```
**Settings:** `endpoint: /images/imageToImage · model: recraftv4 · strength: 0.22 · n: 2 · random_seed: 271828 · image_format: png`

**Technique:** describe only the change plus a preserve list; lowest strength that achieves it. No style fields here — they're V3-only on this endpoint.

---

## 12. V3 → V4 Migration

```json
// V3 (fields ignored or rejected on V4)
{"prompt": "cozy cabin in snow", "model": "recraftv3", "style": "realistic_image",
 "negative_prompt": "people, text", "controls": {"artistic_level": 4, "no_text": true}}
```
```json
// V4
{"prompt": "Photograph of a small timber cabin half-buried in fresh snow at dusk, warm window glow, pine forest behind, deserted clearing. Dynamic low diagonal composition. No text or logos.",
 "model": "recraftv4", "size": "3:2", "n": 2}
```
**Technique:** curated style → medium in prose; negative prompt → "deserted clearing" + one exclusion clause; `artistic_level` → composition stated explicitly; `no_text` → prose.
