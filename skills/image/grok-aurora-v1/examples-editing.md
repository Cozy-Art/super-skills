# Grok Aurora — Editing, Reference & Multi-Image Examples

Examples covering Aurora's editing capabilities: single-image editing via `image_url`, multi-image editing with up to 3 sources via `image_urls`, conversational refinement chains, character consistency workflows, and style transfer techniques.

---

## SINGLE-IMAGE EDITING

### Example 1: Time-of-Day Shift (Neon Pulse)

**Source Image:** Daytime wide shot of the warehouse venue entrance — bright sunlight, blue sky, empty street

**Edit Prompt:**
```
Transform this scene to night. Activate all the neon signage on the 
building. Make the pavement wet and reflecting colored neon light. Add 
a line of people queuing at the door. Keep all architectural details 
identical. Atmospheric urban nightlife photography.

Model: grok-imagine-image
Resolution: 2k
Aspect Ratio: auto (follows input)
Reference Images: 1 (via image_url)

Director's Notes: Aurora's image editing understands scene transformation — 
it changes lighting, activates signs, adds reflections, and adds crowd 
while preserving the building structure. "Keep all architectural details 
identical" is key to preventing structural drift.
```

---

### Example 2: Costume Change (Iron Crown)

**Source Image:** The king character in tarnished silver armor

**Edit Prompt:**
```
Replace the king's armor with flowing royal robes in deep crimson and 
gold embroidery, fur-lined collar. Keep the exact same face, expression, 
pose, background, and lighting. The robes should drape naturally based 
on his body position. He is now in his throne room, not battlefield armor.

Model: grok-imagine-image
Resolution: 2k
Aspect Ratio: auto
Reference Images: 1

Director's Notes: Costume change editing preserves character identity while 
swapping wardrobe. "Drape naturally based on body position" prevents flat 
texture mapping. "Exact same face, expression, pose" locks the character.
```

---

### Example 3: Background Replacement (Aurelia)

**Source Image:** Fragrance bottle product shot on white background

**Edit Prompt:**
```
Keep the perfume bottle, peony, and marble slab exactly as they are. 
Replace the white background with a sunset garden scene — blurred 
lavender fields stretching to a golden horizon. Add warm sunset light 
from behind, creating a golden rim on the bottle and a warm glow 
through the amber liquid. Maintain commercial photography quality.

Model: grok-imagine-image
Resolution: 2k
Aspect Ratio: auto
Reference Images: 1

Director's Notes: Background replacement while maintaining foreground product 
integrity. The key instruction is adding rim light that connects the product 
to the new environment — without this, the product looks pasted onto the new 
background. "Maintain commercial photography quality" prevents quality drop.
```

---

### Example 4: Atmosphere Enhancement (Shadows of Ashford)

**Source Image:** The detective in an alley, daytime lighting, flat atmosphere

**Edit Prompt:**
```
Dramatically change the atmosphere while keeping the character and 
composition identical. Make it night, add rain that creates puddles 
reflecting a distant streetlight. Add volumetric fog catching a shaft 
of amber light from a doorway on the left. Convert to high-contrast 
black and white with only the amber light remaining as selective color. 
Film noir aesthetic, heavy grain.

Model: grok-imagine-image
Resolution: 2k
Aspect Ratio: auto
Reference Images: 1

Director's Notes: Complex atmospheric transformation: time change + weather 
+ fog + color treatment, all while maintaining character and composition. 
Selective color (amber only against B&W) is an advanced rendering technique 
that Aurora handles well.
```

---

## MULTI-IMAGE EDITING (Up to 3 Sources)

### Example 5: Character + Environment Composite (Stellar Drift)

**Source Images:**
- Image 1: The astronaut character in EVA suit (clean background)
- Image 2: The derelict space station corridor (no people)

**Edit Prompt:**
```
Place the astronaut from Image 1 into the corridor from Image 2. 
Position her floating weightlessly in the center of the corridor, 
one hand reaching toward the bioluminescent fungi on the wall. 
Match the lighting from Image 2 onto the astronaut — the blue 
bioluminescent glow should illuminate her suit and visor. Add 
dust particles floating in the light around her. Maintain the 
cinematic science fiction atmosphere.

Model: grok-imagine-image
Resolution: 2k
Aspect Ratio: auto (follows Image 1)
Reference Images: 2 (via image_urls)

Director's Notes: Multi-image compositing with lighting match is the key 
challenge. "Match the lighting from Image 2 onto the astronaut" prevents 
the composited figure from looking artificially placed. Floating dust 
particles help blend the elements.
```

---

### Example 6: Style Merge — Two Art Directions (Neon Pulse)

**Source Images:**
- Image 1: Photorealistic shot of the dancer mid-leap
- Image 2: A reference image of a vivid neon oil painting style (abstract, thick brushstrokes, saturated colors)

**Edit Prompt:**
```
Apply the painting style from Image 2 to the dancer scene in Image 1. 
Convert the photograph into a vivid neon oil painting with thick, 
visible brushstrokes. Maintain the dancer's pose and composition 
but render everything in the painterly style — neon colors melting 
and bleeding across the canvas, especially around the motion blur 
areas. Heavy impasto texture on the light sources.

Model: grok-imagine-image
Resolution: 2k
Aspect Ratio: auto
Reference Images: 2

Director's Notes: Style transfer using multi-image input. Image 1 provides 
composition and content; Image 2 provides target aesthetic. "Heavy impasto 
texture on the light sources" adds specific painterly detail where the 
brightest areas would naturally receive the thickest paint.
```

---

### Example 7: Three-Image Composite — Product in Scene with Model (Aurelia)

**Source Images:**
- Image 1: The Aurelia perfume bottle (isolated product shot)
- Image 2: A model's hand and wrist in an elegant pose
- Image 3: A golden-hour garden background with lavender

**Edit Prompt:**
```
Combine all three images: place the perfume bottle from Image 1 
in the hand from Image 2, with the garden from Image 3 as the 
background. The model's hand holds the bottle delicately at a 
slight tilt. Match the golden-hour lighting from Image 3 across 
the hand and bottle — warm amber light from behind, soft fill 
from the front. The bottle's amber liquid should glow where the 
backlight passes through it. Shallow depth of field with the 
garden softly blurred. Luxury advertising photography quality.

Model: grok-imagine-image
Resolution: 2k
Aspect Ratio: 3:4
Reference Images: 3 (via image_urls)

Director's Notes: Three-source compositing — Aurora's maximum. Each image 
contributes one element: product, human element, environment. Lighting 
consistency across all three is the critical instruction. Aspect ratio 
explicitly set to 3:4 (portrait) rather than defaulting to Image 1's ratio.
```

---

## CONVERSATIONAL REFINEMENT CHAINS

### Example 8: Iterative Character Development (Iron Crown)

**Within a single Grok chat session:**

**Turn 1 — Establish base:**
```
A medieval king in his late 50s, battle scar across his left cheek, 
grey-streaked dark hair pulled back, strong jaw, weary but resolute eyes. 
He wears tarnished silver plate armor with a fur-lined dark cloak and 
a heavy iron crown with minimal ornamentation. Standing in a great hall, 
cold blue window light from behind. Portrait from waist up. Epic fantasy, 
cinematic, oil painting quality with visible brushwork.
```

**Turn 2 — Adjust lighting:**
```
Keep everything identical but change the lighting. Replace the cold 
blue window light with warm orange torchlight from the left side. 
Add rim light from behind in cold blue to separate him from the 
dark background. More dramatic shadows.
```

**Turn 3 — Change expression:**
```
Same everything, but change his expression from resolute to 
deeply troubled. Furrow the brow, slight downward look, weight 
of decisions visible in his face. The crown should feel heavy.
```

**Turn 4 — Scene context:**
```
Now pull back to a wide shot. Same character, same lighting, same 
expression. Show the full great hall — massive stone columns, long 
table with a carved map, two hooded advisors standing at a distance. 
The king stands alone at the head of the table. Cold and imposing 
architecture. Sense of isolation and burden of leadership.
```

```
Director's Notes: Conversational refinement chain — each turn builds 
on the previous without rewriting the full prompt. This is an 
advantage of the conversational interface over API-only access. 
The model retains character description, style, and composition 
from earlier turns while applying the specific changes requested.
```

---

### Example 9: Style Exploration — Same Subject (Forgotten Waters)

**Within a single Grok chat session:**

**Turn 1 — Photorealistic baseline:**
```
A dried lake bed stretching to the horizon, cracked earth in hexagonal 
patterns, an abandoned turquoise fishing boat tilted on its side. 
Hazy morning sun, distant mountains. Documentary photography, Leica Q3, 
28mm lens, natural light, muted warm palette.
```

**Turn 2 — Watercolor treatment:**
```
Same scene, same composition, but render it as a watercolor painting 
on cold-press paper. Wet-on-wet technique, colors bleeding at edges, 
visible paper texture. Muted earth tones with the turquoise boat as 
the only saturated element.
```

**Turn 3 — Woodblock print:**
```
Same scene again, but now as a Japanese ukiyo-e woodblock print. 
Flat areas of color, bold outlines, stylized clouds, limited color 
palette of indigo, ochre, and turquoise. Horizontal format, 
resembling a Hokusai landscape study.
```

**Turn 4 — Abstract expressionist:**
```
One more: same scene, but now as an abstract expressionist painting. 
Large gestural brushstrokes, palette knife texture, the boat reduced 
to angular turquoise shapes against cracked brown earth. Franz Kline 
meets desert landscape. High energy, emotional, not literal.
```

```
Director's Notes: Style exploration using conversational refinement — 
same subject through four radically different artistic treatments. This 
workflow helps directors find the right visual language for a project. 
Each turn explicitly references "same scene" to maintain compositional 
consistency while transforming the rendering style.
```

---

## CHARACTER CONSISTENCY SERIES

### Example 10: Locked Description Across Scenes (Shadows of Ashford)

**Character Anchor (reuse verbatim in every prompt):**
```
A male detective in his late 40s with a strong jaw, close-cropped 
salt-and-pepper hair, deep-set grey eyes with permanent dark circles, 
a thin white scar above his right eyebrow. Wearing a dark charcoal 
trench coat with the collar turned up, slightly loosened dark tie, 
five o'clock shadow.
```

**Shot A — Office (use seed --s 72834):**
```
[character anchor], sitting at a cluttered desk in a dim office, 
harsh desk lamp from the right, files and whiskey bottle visible, 
reading a case file with intense concentration. Shot on ARRI Alexa LF, 
50mm lens, shallow depth of field. Black and white, high contrast noir. 
--s 72834

Model: grok-imagine-image
Resolution: 2k
Aspect Ratio: 16:9
Seed: 72834
```

**Shot B — Rain Alley (same seed --s 72834):**
```
[character anchor], walking through a rain-soaked alley at night, 
hands in coat pockets, streetlight behind creating a long shadow 
ahead. Neon sign reflection in a puddle. Shot on ARRI Alexa LF, 
35mm lens, deep focus. Black and white, high contrast noir. 
--s 72834

Model: grok-imagine-image
Resolution: 2k
Aspect Ratio: 16:9
Seed: 72834
```

**Shot C — Confrontation (same seed --s 72834):**
```
[character anchor], leaning against a brick wall under a fire escape, 
lighting a cigarette, the match flame illuminating only his face 
and the scar above his eyebrow. Dark alley, distant city lights 
softly out of focus. Shot on ARRI Alexa LF, 85mm lens, extreme 
shallow depth of field. Black and white, high contrast noir. 
--s 72834

Model: grok-imagine-image
Resolution: 2k
Aspect Ratio: 16:9
Seed: 72834
```

```
Director's Notes: Three-shot character consistency series using the 
triple-lock technique: (1) identical character anchor description, 
(2) locked seed value (--s 72834), (3) consistent camera/style 
references (ARRI Alexa LF, B&W noir). Only the scene, action, and 
lens change between shots. This is the most reliable character 
consistency method available in Aurora.
```

---

## Version Information

- **Examples Version:** 1.0
- **Covers:** Grok Aurora editing, multi-image, conversational refinement, character consistency
- **Last Updated:** 2026-04-18
- **Maintained By:** Visual Horizon Studio
