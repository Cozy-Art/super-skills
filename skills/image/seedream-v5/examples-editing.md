# Seedream 5.0 — Editing, Reference & Multi-Image Examples

Examples covering Seedream's editing capabilities: example-based editing (5.0 Lite), reference-based generation, visual marker editing (4.5), multi-image generation with consistency, and image compositing workflows.

---

## EXAMPLE-BASED EDITING (5.0 Lite Only)

The signature feature of Seedream 5.0 Lite. Provide a before/after image pair showing a transformation, then apply that learned transformation to a new target image.

### Example 1: Day-to-Night Conversion (Neon Pulse)

**Setup:**
- Image 1 (Before): Daytime street scene — bright sunlight, blue sky, pedestrians casting sharp shadows
- Image 2 (After): Same street at night — neon signs lit, wet pavement reflections, warm window glow
- Image 3 (Target): Daytime establishing shot of the warehouse venue entrance

**Edit Prompt:**
```
Reference the change from Image 1 to Image 2, apply the same 
operation to Image 3. Maintain all architectural details and 
composition from Image 3.
```

```
Variant: Seedream 5.0 Lite
Image Size: auto_2K

Director's Notes: Example-based editing learns the day→night transformation 
(lighting shift, neon activation, wet pavement reflections, sky change) from 
the before/after pair, then applies it to the target shot. More reliable than 
describing "make it nighttime" because the model learns the SPECIFIC style of 
night (neon-lit urban vs moonlit rural vs blue-hour twilight).
```

---

### Example 2: Material Swap — Wood to Stone (Iron Crown)

**Setup:**
- Image 1 (Before): A wooden throne with carved armrests, warm brown tones
- Image 2 (After): Same throne converted to rough-hewn dark granite, cold grey tones
- Image 3 (Target): A wooden banquet table in the great hall

**Edit Prompt:**
```
Reference the material transformation from Image 1 to Image 2, 
apply the same material change to Image 3. Convert the wooden 
surface to the same rough-hewn dark granite, preserving the 
furniture shape and scene composition.
```

```
Variant: Seedream 5.0 Lite
Image Size: auto_2K

Director's Notes: Material swaps are notoriously difficult to describe in text 
because "dark granite" means different things to different renderers. By showing 
the model the EXACT granite treatment (texture, color, surface finish) on a 
similar object, it applies the identical material to the new target.
```

---

### Example 3: Color Grading Transfer (Shadows of Ashford)

**Setup:**
- Image 1 (Before): Color photograph of a city street, neutral grading
- Image 2 (After): Same photograph with classic noir treatment — desaturated, high contrast, crushed blacks, slight sepia warmth in highlights
- Image 3 (Target): Color photograph of the detective's office interior

**Edit Prompt:**
```
Reference the color grading change from Image 1 to Image 2, 
apply the identical color treatment to Image 3. Preserve all 
scene content and composition.
```

```
Variant: Seedream 5.0 Lite
Image Size: auto_2K

Director's Notes: Color grading transfer captures the exact tonal curve, 
saturation level, and highlight/shadow treatment. Far more precise than 
describing "make it noir" because there are dozens of valid noir grades. 
The before/after pair locks the specific grade.
```

---

### Example 4: Style Transfer — Photo to Illustration (Aurelia)

**Setup:**
- Image 1 (Before): Photograph of a rose in natural light
- Image 2 (After): Same rose rendered as a delicate watercolor botanical illustration with visible brush texture and paper grain
- Image 3 (Target): Photograph of the Aurelia perfume bottle on marble

**Edit Prompt:**
```
Reference the photographic-to-watercolor transformation from 
Image 1 to Image 2, apply the same artistic treatment to Image 3. 
Maintain the product's recognizable form and proportions.
```

```
Variant: Seedream 5.0 Lite
Image Size: auto_2K

Director's Notes: Style transfers between media (photo → watercolor, photo → 
oil painting, photo → pencil sketch) benefit enormously from example-based 
editing because the specific interpretation of "watercolor" (wet vs dry brush, 
transparency level, paper texture) is captured from the example pair.
```

---

## REFERENCE-BASED GENERATION

Using reference images to maintain character, style, or product consistency across new scenes.

### Example 5: Character Consistency — New Scene (Stellar Drift)

**Reference Image:** The astronaut character from Example 2 (established shot)

**Prompt:**
```
Based on the character in the reference image, generate the same 
astronaut character now standing on the exterior hull of the space 
station, magnetic boots attached, looking out at a distant blue nebula. 
The EVA suit shows the same wear patterns and scratched visor. 
Wide shot, the curve of the station hull visible, stars and nebula 
in background. Cinematic science fiction, ARRI Alexa Mini with 
16mm ultra-wide lens, deep focus.
```

```
Variant: Seedream 5.0 Lite
Image Size: landscape_16_9
Reference Images: 1 (character reference)

Director's Notes: Character reference maintains facial features, suit details, 
and wear patterns from the established shot. New environment (exterior hull, 
nebula) tests whether the character transfers cleanly to a radically different 
setting. Ultra-wide 16mm lens chosen for environmental scale.
```

---

### Example 6: Product Design Variations (Aurelia)

**Reference Image:** The established Aurelia perfume bottle (from Example 4 in text-to-image)

**Prompt:**
```
Based on the perfume bottle design in the reference image, generate 
four product variations: the same bottle shape in (1) frosted cobalt 
blue glass with silver cap, (2) clear crystal with rose gold cap, 
(3) matte black glass with gunmetal cap, and (4) pale jade green 
glass with brass cap. Maintain identical bottle proportions and 
Art Deco cap design across all variations. Each bottle shown on a 
simple pedestal with matching subtle background gradient. Luxury 
product photography, consistent studio lighting.
```

```
Variant: Seedream 5.0 Lite
Image Size: landscape_16_9
Max Images: 4
Reference Images: 1 (product reference)

Director's Notes: Multi-image generation (max_images: 4) with product reference 
maintains bottle silhouette while varying only material and color. This is a 
common commercial workflow — generating colorway options from an established 
design. "Identical bottle proportions" is key to ensuring variants feel like 
the same product line.
```

---

### Example 7: Sketch-to-Render — Set Design (Iron Crown)

**Reference Image:** A rough pencil sketch/wireframe of the great hall interior showing columns, throne position, window arches, and ceiling height

**Prompt:**
```
Convert this sketch into a high-fidelity photorealistic render of 
a medieval great hall interior. The hall features massive stone 
columns with carved wolf motifs, a raised stone throne platform at 
the far end, tall narrow arched windows with iron frames letting 
in cold blue daylight, and heavy timber ceiling beams darkened 
with centuries of smoke. Torches in iron sconces provide warm 
amber light along the columns. The floor is worn flagstone with 
visible mortar joints. Cinematic production design, Game of Thrones 
quality, ARRI Alexa Mini LF with 21mm Angénieux Optimo lens.
```

```
Variant: Seedream 5.0 Lite
Image Size: landscape_16_9
Reference Images: 1 (sketch/wireframe)

Director's Notes: Sketch-to-render workflow preserves the spatial layout from 
the wireframe while adding material detail, lighting, and atmospheric depth. 
The prompt provides material specifications (stone, timber, flagstone, iron) 
that the model applies to the sketch's spatial framework. 21mm ultra-wide 
lens reference captures the full hall interior.
```

---

## VISUAL MARKER EDITING (4.5)

Seedream 4.5 supports drawing directly on images with arrows, bounding boxes, colored regions, and doodles to indicate edit locations.

### Example 8: Set Dressing Insertion (Shadows of Ashford)

**Source Image:** The detective's office interior (empty desk area)
**Visual Markers:** Red bounding box on the desk surface, blue arrow pointing to the wall behind the desk

**Edit Prompt:**
```
Insert a vintage rotary telephone where the red area is marked 
on the desk. Add a framed city map from the 1940s where the blue 
arrow points on the wall. Keep the original noir lighting and 
atmosphere unchanged.
```

```
Variant: Seedream 4.5
Image Size: match source
Strength: 0.7
Guidance Scale: 8.0
Negative Prompt: modern objects, digital devices, bright colors, cartoon

Director's Notes: Visual marker editing provides pixel-precise placement that 
even JSON structured prompts can't match for insertion tasks. Strength 0.7 
balances edit integration with source preservation. Negative prompt prevents 
anachronistic objects.
```

---

## MULTI-IMAGE COMPOSITING (4.5 and 5.0)

Combining elements from multiple source images into a new composition.

### Example 9: Character + Environment Composite (Neon Pulse)

**Source Images:**
- Image 1: The dancer character (isolated, clean background)
- Image 2: The cyberpunk district establishing shot (no people)

**Prompt (5.0 Lite):**
```
Place the dancer from Image 1 into the street scene from Image 2. 
Position the dancer in the center of the pedestrian street, 
mid-movement with the reflective jacket catching the neon light 
from the surrounding signs. Match the lighting temperature and 
color cast of the environment onto the dancer's figure. Maintain 
the rain-wet pavement reflections beneath the dancer's feet.
```

```
Variant: Seedream 5.0 Lite
Image Size: landscape_16_9
Reference Images: 2

Director's Notes: Multi-image compositing merges character and environment 
while maintaining lighting consistency. The key instruction is "match the 
lighting temperature and color cast" — without this, the composited character 
can look pasted-on. Wet pavement reflections beneath feet ground the character 
in the environment.
```

---

### Example 10: Outfit Swap (Aurelia)

**Source Images:**
- Image 1: Model in a plain white t-shirt (reference for pose and body)
- Image 2: Close-up of a cream silk blouse with gold embroidery details

**Prompt (5.0 Lite):**
```
Dress the model in Image 1 with the blouse from Image 2. 
Maintain the model's exact pose, expression, and background. 
The blouse should drape naturally according to the body position, 
with fabric weight and movement consistent with real silk. 
Adjust lighting on the blouse to match the scene lighting.
```

```
Variant: Seedream 5.0 Lite
Image Size: auto_2K
Reference Images: 2

Director's Notes: Wardrobe swap is a common production workflow — changing 
outfit without reshooting. Key instructions: "drape naturally according to 
body position" prevents flat texture mapping, and "fabric weight and movement 
consistent with real silk" ensures material authenticity. Lighting match 
instruction prevents the blouse from looking composited.
```

---

## MULTI-IMAGE CONSISTENCY WORKFLOWS

### Example 11: Character Sheet Generation (Iron Crown)

**Prompt:**
```
A character reference sheet for a fantasy king: an aging man in his 
late 50s with a prominent battle scar across his left cheek, grey-streaked 
dark hair pulled back, strong jaw, weary but resolute eyes. He wears 
tarnished silver plate armor with a fur-lined dark cloak and a heavy 
iron crown with minimal ornamentation.

Generate a set of four views: front-facing portrait from shoulders up, 
three-quarter view showing armor detail, profile view showing the scar, 
and full-body standing pose with cloak and sword at hip. Consistent 
character appearance across all views. Clean neutral grey background, 
even studio lighting, concept art reference sheet format.
```

```
Variant: Seedream 5.0 Lite
Image Size: landscape_16_9
Max Images: 4
Seed: null

Director's Notes: Character sheet generation uses multi-image output 
(max_images: 4) for consistency. Character description locked with extreme 
specificity (battle scar location, hair style, armor condition, crown design) 
to ensure all four views depict the same person. Neutral background and even 
lighting remove variables, isolating character design.
```

---

### Example 12: Location Continuity — Three Angles (Forgotten Waters)

**Prompt Series (run as 3 separate generations with locked seed):**

**Shot A:**
```
A dried lake bed stretching to the horizon, cracked earth in hexagonal 
patterns, an abandoned turquoise fishing boat tilted on its side in the 
midground, distant mountains under hazy sky. Wide establishing shot, 
28mm lens, documentary photography, Leica Q3, muted warm palette, 
early morning soft light from the left.
```

**Shot B (same seed):**
```
The same dried lake bed with cracked hexagonal earth patterns. Medium 
shot of the abandoned turquoise fishing boat, showing peeling paint 
detail, a coiled rope on the gunwale, and dried seaweed tangled in 
the hull. 50mm lens, documentary photography, Leica Q3, muted warm 
palette, early morning soft light from the left.
```

**Shot C (same seed):**
```
The same dried lake bed setting. Close-up detail of the cracked earth 
surface, a small dead fish skeleton partially buried in the dried mud, 
the shadow of the turquoise fishing boat falling across the frame from 
the right. 100mm macro lens, documentary photography, Leica Q3, muted 
warm palette, early morning soft light from the left.
```

```
Variant: Seedream 5.0 Lite
Image Size: landscape_16_9
Seed: [use same seed for all three]

Director's Notes: Location continuity across three focal lengths (wide → 
medium → close-up) using identical seed, camera brand, palette, and lighting 
description. Each shot references the same environmental elements (cracked 
hexagonal earth, turquoise boat) to reinforce spatial continuity. This 
simulates a real documentary shoot pattern: establish → detail → intimate.
```

---

## 4.5 ITERATIVE REFINEMENT WORKFLOW

### Example 13: Progressive Parameter Tuning (Shadows of Ashford)

**Round 1 — Baseline:**
```
Prompt: A rain-soaked city street at night, 1940s urban America, art deco 
buildings lining both sides, a lone figure walking away from camera under 
a streetlight, noir atmosphere.

Negative Prompt: modern cars, bright colors, daytime, cartoon
Variant: Seedream 4.5
Guidance Scale: 7.0
Steps: 30
Seed: 42891
```

**Round 2 — Too literal, reduce guidance:**
```
[Same prompt]
Guidance Scale: 5.5  ← lowered for more artistic interpretation
Steps: 30
Seed: 42891  ← same seed to compare
```

**Round 3 — Composition good, increase detail:**
```
[Same prompt, refined:]
Prompt: A rain-soaked city street at night, 1940s urban America, art deco 
buildings with geometric facades lining both sides, a lone figure in a 
dark overcoat walking away from camera toward a pool of amber streetlight, 
wet pavement reflecting building silhouettes, noir atmosphere, pushed 
Tri-X 400 film grain.

Negative Prompt: modern cars, modern signage, bright colors, daytime, 
cartoon, soft focus, clean streets
Guidance Scale: 7.0  ← restored for prompt adherence
Steps: 40  ← increased for detail
Seed: 42891  ← same seed
```

```
Director's Notes: Iterative refinement workflow using 4.5's parameter controls. 
Seed stays locked to isolate the effect of each parameter change. Guidance 
scale adjusts prompt literal-ness. Inference steps increase detail quality. 
Negative prompt grows to address specific artifacts from previous rounds. 
This workflow is not possible with 5.0 Lite (no guidance_scale or negative_prompt).
```

---

## Version Information

- **Examples Version:** 1.0
- **Covers:** Seedream 5.0 Lite (editing, reference, multi-image), Seedream 4.5 (markers, iterative refinement)
- **Last Updated:** 2026-04-18
- **Maintained By:** Visual Horizon Studio
