# Magnific One — Annotated Examples

Every example is two-part: **prompt** + **suggested settings**. Settings never appear in prompt text. "Final" = app; `quality` = API.

---

## 1. Control Dial — Same Idea, Four Levels

```
gossip
```
```
two grandmothers in matching lilac tracksuits gossiping on a bench, one hiding a croissant behind her back
```
```
Two grandmothers in matching lilac tracksuits gossiping and laughing on a park
bench in Madrid, one hiding a croissant behind her back. Side view at bench
height, both in profile. Late afternoon sun through plane trees, dappled light
on their faces. Soft pastel palette, lilac against warm terracotta.
```
**Settings:** levels 1–2 → `mode: draft · tiles: 16 · aspect_ratio: 3:2` · level 4 → `mode: quality · quality: high · resolution: 2k · aspect_ratio: 3:2`

**Technique:** Magnific's official progression. Explore short in Draft and let the art director surprise you; spend words only once you know what to lock.

---

## 2. Character Portrait (identity block)

```
Editorial film photograph of Mara, a woman in her early forties with an oval
face, warm brown skin, short tightly curled black hair, a small scar through the
left eyebrow, and a brass crescent earring. She stands beside an open
overnight-train door holding a folded route map at waist height. Chest-up,
off-center on the right third, looking out of frame left. Cool dawn light from
the platform, one warm carriage light behind her. Charcoal and rust wardrobe,
quiet anticipation.
```
**Settings:** Draft `tiles: 16 · aspect_ratio: 3:4` → Final `quality: high · resolution: 2k · aspect_ratio: 3:4`

**Technique:** medium first → identity sentence written to be reused verbatim → one moment → placement and eyeline → two light sources that already exist in the scene → palette + one mood word.

---

## 3. Environmental Landscape

```
Film photograph of a solitary red research hut on a black volcanic plain at blue
hour. Wet basalt anchors the foreground, the hut sits small in the middle
distance, and snow ridges disappear into low cloud behind it. One warm window,
immense negative space above the horizon. Slate blue, charcoal and signal red.
```
**Settings:** `mode: draft · tiles: 16 · aspect_ratio: 21:9` → `mode: quality · quality: high · resolution: 4k · aspect_ratio: 21:9`

**Technique:** three depth planes named explicitly; scale stated ("sits small"); 16 tiles because 21:9 is approximated at 8.

---

## 4. Action Still

```
Documentary sports photograph from below a glass pedestrian bridge as a runner
passes overhead, the worn sole of the shoe large against the city sky. Face and
torso visible through the next glass panel, sharp enough to read; directional
motion blur in the legs, colored light leaks and rain droplets across the glass.
A decisive mid-stride instant.
```
**Settings:** `mode: quality · quality: high · resolution: 2k · aspect_ratio: 2:3`

**Technique:** unusual point of view does the art direction; motion described as evidence (what's sharp, what's blurred).

---

## 5. Implied Tracking Shot

```
Editorial photograph of one cyclist sprinting left to right through a
rain-darkened night circuit. Panning-shot look: the rider's face and torso stay
sharp while wheels, spectators and amber city lights stretch into horizontal
blur. Curb-level viewpoint, road spray behind the rear tire. No signage or other
riders.
```
**Settings:** `mode: quality · quality: high · resolution: 2k · aspect_ratio: 16:9`

**Technique:** "tracking" is visual language only — no camera parameter exists. One short exclusion sentence at the end replaces a negative prompt.

---

## 6. Style-Reference Scene

```
An aerial view of twelve white horses galloping across a pale salt flat, one
black horse breaking formation near the center, dust lifting into low amber sun,
their long shadows forming diagonal lines across the ground.
```
**Settings:** `mode: draft · tiles: 16 · aspect_ratio: 16:9 · reference_images: [3 coherent gouache-texture refs]` (app: Style tab, same 3 images)

**Technique:** no medium or style words — the reference set carries the look. Every word goes to scene, action and composition. In the app, add refs via the Style tab or they're read as content.

---

## 7. 3D Material Study

```
Knitted 3D miniature world: a teacup lake fed by a small rain cloud, a striped
lighthouse on the rim, a soft rainbow bridge, and a glossy toy sun. Every
element is made of visible yarn and felt except the polished sun. Cozy handmade
scale, clean pastel background, soft window light.
```
**Settings:** `mode: quality · quality: high · resolution: 2k · aspect_ratio: 1:1`

**Technique:** medium as a world ("knitted 3D miniature world") + an explicit material exception so not everything gets the same surface.

---

## 8. Poster With Exact Copy

```
Bold contemporary campaign poster for a coastal night market. A noodle stall
seen through heavy rain, warm lanterns reflecting on cobalt pavement, strong
diagonal awning. Oversized headline "OPEN LATE" painted across the awning in
perspective. Smaller line "FRIDAY — MIDNIGHT" aligned bottom-left. Cobalt,
vermilion, warm cream and black; crisp hierarchy, generous negative space.
Reproduce the text exactly as written. No other logos or text.
```
**Settings:** Final · High · 2K · `2:3` · Brand Kit: <client> (API: `mode: quality · quality: high · resolution: 2k · aspect_ratio: 2:3`)

**Technique:** quoted copy with placement + hierarchy; exact-text corrective line last. If a glyph still drifts, fix it in Auto Layers / Designer — don't reroll.

---

## 9. Branded Series (same skeleton, one variable)

**Fixed:** Brand Kit `<client>` · Style refs `[A, B]` · ratio `3:4` · skeleton below

```
Editorial photograph for a specialty coffee roaster. A barista's hands pour
water in a slow spiral over a ceramic dripper on a pale oak counter. Close
overhead three-quarter view, hands entering from the right. Morning window light
from the left. No other logos or text.
```
Next image changes **only** the second and third sentences:
```
Editorial photograph for a specialty coffee roaster. Burlap sacks of green
beans stacked beside a small drum roaster, a scoop resting on top. Low side view
at sack height. Morning window light from the left. No other logos or text.
```
**Settings:** Final · High · 2K · `3:4` · Brand Kit: <client> · Style: [A, B]

**Technique:** Brand Kit holds palette/tone, Style refs hold rendering, prompt holds scene. Medium, light and text rule stay verbatim — no brand adjectives in the prompt.

---

## 10. Draft → Final Handoff

Draft:
```
Poster concepts for a jazz festival by the sea
```
**Settings:** `mode: draft · tiles: 16 · aspect_ratio: 3:4`

Final (tile 7 chosen — bass on pier, moon upper right, empty sky):
```
Minimal bold poster for a jazz festival by the sea. A lone upright bass
silhouetted on a wooden pier at the lower left, a huge low moon filling the upper
right, a wide band of empty navy sky between them. Cobalt, cream and brass,
screen-printed texture.
```
**Settings:** `mode: quality · quality: high · resolution: 4k · aspect_ratio: 3:4`

**Technique:** no tile ID to promote — the chosen tile's placement, viewpoint and palette are written into the Final prompt. Same ratio as Draft.

---

## 11. API Payloads

Draft exploration:
```json
{
  "prompt": "Poster concepts for a jazz festival by the sea",
  "mode": "draft",
  "tiles": 16,
  "aspect_ratio": "3:4"
}
```

Controlled Final with style references and webhook:
```json
{
  "prompt": "Editorial photograph of a lighthouse on a basalt cliff at dusk, long-exposure sea, warm window light, wide atmospheric framing.",
  "mode": "quality",
  "quality": "high",
  "resolution": "4k",
  "aspect_ratio": "16:9",
  "reference_images": [
    "https://example.com/style-reference-1.jpg",
    "https://example.com/style-reference-2.jpg"
  ],
  "webhook_url": "https://example.com/webhooks/magnific-one"
}
```

Migration — legacy-style payload that will be rejected:
```json
{"prompt": "lighthouse, cinematic, 8k, masterpiece", "negative_prompt": "blurry",
 "seed": 42, "guidance_scale": 7, "num_images": 4, "mode": "final"}
```
Fixed:
```json
{"prompt": "Film photograph of a lighthouse on a basalt cliff at dusk, crisp focus on the tower, warm window light against a cold sea.",
 "mode": "draft", "tiles": 8, "aspect_ratio": "3:2"}
```
**Technique:** quality tags → visible causes; negative → positive description; seed/guidance dropped; 4-up → 8-tile Draft at a ratio that stays exact at 8; `final` → `quality`/`draft`.
