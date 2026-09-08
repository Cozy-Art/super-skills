# Grok Aurora — Text-to-Image Examples

Examples organized by use case, drawing from the recurring example projects to demonstrate cross-skill continuity.

**Canonical Projects:**
- 🎬 **Shadows of Ashford** — 1940s film noir detective story
- 🚀 **Stellar Drift** — Sci-fi short film, derelict space station
- 🎵 **Neon Pulse** — Electronic music video, urban nightlife
- 🌸 **Aurelia** — Luxury fragrance commercial
- ⚔️ **Iron Crown** — Dark fantasy short film
- 🌊 **Forgotten Waters** — Environmental documentary

---

## PHOTOREALISTIC PORTRAITS

### Example 1: Noir Detective — Dramatic Close-Up (Shadows of Ashford)
```
Prompt: Close-up portrait of a weathered male detective in his late 40s, 
three-day stubble, tired eyes with sharp intelligence, dark fedora tilted 
low casting a shadow across his forehead. Single harsh desk lamp from the 
right creating deep Rembrandt lighting on his face. High contrast black 
and white, pushed Tri-X 400 film grain, shot on Leica M6 with 50mm 
Summicron lens at f/2. Noir atmosphere, smoke curling in the backlight.

Model: grok-imagine-image
Resolution: 2k
Aspect Ratio: 3:4
N: 4
Seed: null

Director's Notes: Aurora's cinematic default works perfectly here — noir IS 
cinematic. Leica M6 + Summicron reference produces authentic street photography 
rendering. Rembrandt lighting specified by name rather than describing the 
triangle pattern. Film stock reference (Tri-X 400) handles grain and contrast 
without additional adjectives.
```

---

### Example 2: Astronaut Discovery — Emotional Close-Up (Stellar Drift)
```
Prompt: Extreme close-up of a female astronaut in her 30s, cropped dark 
hair pressed against the inside of a scratched helmet visor, tears floating 
as tiny spheres in zero gravity near her eyes. Her expression shifts between 
awe and grief. The only light source is a pulsing green glow from an unseen 
console reflected in the visor, casting the left side of her face in emerald 
while the right falls into deep shadow. Shot on ARRI Alexa Mini LF with 
Cooke S7i 75mm lens, extremely shallow depth of field, anamorphic oval 
bokeh visible in the visor reflection. Science fiction, Ridley Scott aesthetic.

Model: grok-imagine-image
Resolution: 2k
Aspect Ratio: 16:9
N: 4
Seed: null

Director's Notes: Ridley Scott reference plus anamorphic bokeh locks the sci-fi 
cinema feel. Single-source green light creates dramatic face split. Floating 
tears in zero gravity test Aurora's physics understanding. Cooke S7i lens 
reference produces warm, characterful rendering.
```

---

### Example 3: Dancer in Neon — Full Body Action (Neon Pulse)
```
Prompt: A young male dancer mid-leap in an abandoned warehouse, body 
fully extended, wearing a reflective silver jacket catching colored light. 
Triple neon tubes on the walls cast hot pink, electric cyan, and deep violet 
across his body and the concrete floor. Motion blur on his trailing foot. 
Wide angle shot from low, looking up, making the dancer appear to fly. 
Shot on Sony FX6, 16mm wide angle lens, f/2.8. CineStill 800T film look 
with halation glow around the neon sources. Energetic, electric atmosphere.

Model: grok-imagine-image
Resolution: 2k
Aspect Ratio: 16:9
N: 4
Seed: null

Director's Notes: Low wide angle exaggerates the leap for visual drama. 
CineStill 800T reference produces characteristic red halation around 
bright neon sources — Aurora handles this film stock well. Triple color 
neon creates complex light interactions on the reflective jacket. Motion 
blur on trailing foot implies movement without blurring the whole figure.
```

---

## PRODUCT AND COMMERCIAL PHOTOGRAPHY

### Example 4: Fragrance Bottle — Hero Shot (Aurelia)
```
Prompt: Luxury product photograph of a sculptural glass perfume bottle 
with an Art Deco gold cap, amber liquid refracting warm light through 
faceted cuts in the glass. The bottle sits on a slab of white Carrara 
marble with grey veining, a single white peony bloom resting beside it 
with petals slightly open. Soft studio key light from upper left with a 
crisp edge highlight along the bottle's left contour, warm backlight 
creating a golden halo through the liquid. Shot on Hasselblad X2D with 
120mm macro lens, f/5.6, focus stacked for edge-to-edge sharpness. 
Seamless gradient background from warm ivory to soft gold. Ultra-premium 
commercial photography, Vogue still life editorial quality.

Model: grok-imagine-image
Resolution: 2k
Aspect Ratio: 1:1
N: 4
Seed: null

Director's Notes: Aurora's cinematic bias enhances luxury product photography 
naturally. Hasselblad X2D provides medium-format quality. Focus stacking 
specified for macro sharpness. Edge highlight and backlight create 
dimensionality. Vogue reference anchors premium editorial quality.
```

---

### Example 5: Fantasy Weapon — Prop Photography (Iron Crown)
```
Prompt: A battle-worn medieval longsword lying on a rough stone altar in 
a dark dungeon, the blade showing nicks and dried residue, crossguard 
wrought iron with a wolf-head motif. The leather grip is sweat-darkened 
with visible wear. A single shaft of dusty light from above catches the 
blade's edge, creating a bright line along the steel. Everything else 
falls into deep shadow. Cinematic still life, ARRI Alexa Mini LF with 
50mm Cooke S7i lens, shallow depth of field, only the sword sharp. 
Moody chiaroscuro lighting, dark fantasy aesthetic.

Model: grok-imagine-image
Resolution: 2k
Aspect Ratio: 16:9
N: 4
Seed: null

Director's Notes: Material descriptions (wrought iron, sweat-darkened leather, 
nicked blade) drive Aurora's rendering. Chiaroscuro lighting reference creates 
dramatic light-to-shadow ratio. Aurora's cinematic default enhances the dark 
fantasy mood naturally. Single light shaft provides visual focus.
```

---

## TYPOGRAPHY AND TEXT RENDERING

### Example 6: Film Poster with Text (Shadows of Ashford)
```
Prompt: A classic noir film poster. At the top in bold condensed white 
lettering: SHADOWS OF ASHFORD. Below in smaller elegant italic serif: 
A city of secrets. A detective with nothing left to lose. A lone figure 
in trench coat and fedora stands silhouetted at the end of a rain-slicked 
alley, backlit by a single amber streetlamp casting a long shadow toward 
the viewer. Deep navy and charcoal palette with amber accent from the 
streetlight. Heavy film grain overlay, 1940s theatrical one-sheet format. 
Vintage movie poster design, hand-painted quality.

Model: grok-imagine-image
Resolution: 2k
Aspect Ratio: 2:3
N: 4
Seed: null

Director's Notes: Text rendering is an Aurora strength — title and tagline 
described naturally in the prompt without special syntax. Two different text 
styles specified (bold condensed vs elegant italic serif). Silhouetted figure 
avoids facial rendering challenges while maintaining noir drama.
```

---

### Example 7: Neon Signage (Neon Pulse)
```
Prompt: A rain-soaked brick wall of an underground music venue at night. 
A large neon sign reading NEON PULSE glows in hot pink, buzzing slightly, 
with a smaller cyan neon sign below reading LIVE TONIGHT. A black metal 
door is partially open, warm amber light spilling from inside. Wet 
pavement in the foreground reflects the neon colors in elongated streaks. 
Urban nightlife photography, gritty, shot on Leica Q3 with 28mm lens. 
CineStill 800T look with halation around the neon tubes.

Model: grok-imagine-image
Resolution: 2k
Aspect Ratio: 9:16
N: 4
Seed: null

Director's Notes: Aurora's text rendering handles neon signs well. Two separate 
text strings at different sizes test hierarchy rendering. Wet pavement reflections 
create depth and visual richness. Portrait orientation for venue entrance / 
social media format.
```

---

## ENVIRONMENT AND LANDSCAPE

### Example 8: Cyberpunk District — Establishing Shot (Neon Pulse)
```
Prompt: Wide establishing shot of a rain-soaked cyberpunk district at midnight, 
towering residential blocks covered in holographic advertisements and tangled 
power cables. A narrow pedestrian street below is crowded with food stalls 
under plastic tarps, steam rising from grills mixing with neon fog. Hot pink 
and electric cyan dominate from the signage, with warm amber patches from food 
stall lanterns below. Low angle looking up between buildings, anamorphic 
lens flare streaking horizontally across the frame from a distant spotlight. 
Blade Runner aesthetic, cinematic, atmospheric, dense and layered.

Model: grok-imagine-image
Resolution: 2k
Aspect Ratio: 16:9
N: 4
Seed: null

Director's Notes: Aurora's cinematic default is PERFECT for cyberpunk — let it 
run. Blade Runner reference anchors the visual language. Anamorphic lens flare 
adds authenticity. Multiple light source types (neon, lanterns, steam) create 
atmospheric depth. Low angle emphasizes urban scale.
```

---

### Example 9: Frozen Fortress — Epic Landscape (Iron Crown)
```
Prompt: A massive dark stone fortress carved into a frozen mountain cliff, 
seen from across a wind-swept ice field. The walls are granite streaked with 
ice, narrow arrow slits glowing faintly orange from fires within. A blizzard 
wall approaches from the left, the sky grey-white with storm. In the 
foreground, a line of armored riders on dark horses moves single-file toward 
the fortress gate, cloaks whipping in wind. Golden hour light breaking through 
storm clouds on the far right, catching the mountain peaks. Epic fantasy 
landscape, matte painting quality, highly detailed, concept art for a AAA 
fantasy film.

Model: grok-imagine-image
Resolution: 2k
Aspect Ratio: 16:9
N: 4
Seed: null

Director's Notes: Multiple depth layers (foreground riders, midground fortress, 
background mountain and storm) create epic scale. Competing light sources 
(orange interior vs golden hour break) create visual tension. "Matte painting 
quality" and "AAA fantasy film" tell Aurora to render at maximum production value, 
which aligns perfectly with its cinematic bias.
```

---

## CINEMATIC STILLS

### Example 10: Interrogation Scene (Shadows of Ashford)
```
Prompt: A tense interrogation in a 1940s police station. A detective in 
rolled shirtsleeves leans forward across a battered wooden table, cigarette 
smoke curling between his fingers. Across the table, a woman in a dark 
dress sits rigidly upright, chin raised, defiant expression. A single bare 
bulb hangs between them casting harsh downward light with deep eye-socket 
shadows on both faces. The room is dark beyond the cone of light, 
institutional green walls barely visible at edges. Two-shot, slightly low 
angle favoring the detective. Shot on vintage Cooke Speed Panchro lenses, 
black and white, high contrast noir. Avoid: color, modern elements.

Model: grok-imagine-image
Resolution: 2k
Aspect Ratio: 16:9
N: 4
Seed: null

Director's Notes: Cooke Speed Panchro lens reference provides period-appropriate 
rendering. Single practical light source (bare bulb) is canonical noir. Low 
angle establishes power dynamic. Inline negative guidance ("Avoid: color, 
modern elements") prevents anachronisms.
```

---

### Example 11: Zero Gravity Garden (Stellar Drift)
```
Prompt: Interior of a sealed laboratory aboard a derelict space station. 
The door has just opened revealing a thriving garden growing in zero gravity — 
a small tree with roots spiraling outward in weightless tendrils, water 
droplets hanging suspended like tiny lenses reflecting green bioluminescent 
light from moss on the walls. An astronaut's gloved hand enters frame from 
the left, reaching toward a floating flower. Medium shot through the doorframe, 
the metal edge creating a natural vignette. Warm green and gold tones inside 
the garden contrast sharply with cold blue corridor behind. Cinematic science 
fiction, anamorphic 2.39:1 aspect feel, ARRI Alexa with Panavision C-Series 
anamorphic lens. Avoid: cartoon, anime, CGI look.

Model: grok-imagine-image
Resolution: 2k
Aspect Ratio: 16:9
N: 4
Seed: null

Director's Notes: Temperature contrast (warm garden vs cold corridor) creates 
visual narrative. Doorframe-as-vignette adds depth and framing. Suspended water 
droplets test physics rendering. Panavision C-Series anamorphic reference 
produces classic sci-fi lens character.
```

---

## DOCUMENTARY / ENVIRONMENTAL

### Example 12: Dried Lake — Environmental Portrait (Forgotten Waters)
```
Prompt: A weathered fishing boat with peeling turquoise paint rests on 
cracked earth where a lake once was, hull tilted at an angle on dried mud. 
A single elderly fisherman in a worn sun-bleached coat sits on the gunwale, 
looking at the distant water line now hundreds of meters away. Early morning, 
hazy sun through dust. Other abandoned boats visible in background, some 
half-buried. Documentary photography, natural light only, Leica Q3 with 
28mm lens, muted warm palette, dusty atmosphere, no post-processing. 
Avoid: cinematic, dramatic, color graded, saturated.

Model: grok-imagine-image
Resolution: 2k
Aspect Ratio: 3:2
N: 4
Seed: null

Director's Notes: CRITICAL to override cinematic default here with explicit 
"documentary photography, natural light only" and inline negative guidance. 
Leica Q3 reference anchors documentary authority. 28mm wide angle includes 
environmental context. "No post-processing" fights Aurora's tendency to 
color-grade everything.
```

---

### Example 13: Underwater Ruins (Forgotten Waters)
```
Prompt: Underwater photograph of a submerged fishing village, stone house 
rooftops visible through murky green water, fish swimming through a 
crumbling doorway. Shafts of sunlight penetrate from the surface above, 
creating visible light beams through particulate water. A rusted bicycle 
leans against a submerged wall, covered in algae and barnacles. Slightly 
above angle, looking down through the water column. National Geographic 
underwater photography, natural light, no flash. Moody, haunting, 
environmental documentary aesthetic.

Model: grok-imagine-image
Resolution: 2k
Aspect Ratio: 16:9
N: 4
Seed: null

Director's Notes: National Geographic reference provides documentary authority 
with visual impact. "No flash" prevents Aurora from adding artificial underwater 
lighting. Particulate water creates volumetric light shafts. Domestic objects 
(bicycle, doorway) underwater create emotional dissonance.
```

---

## STYLIZED / ART DIRECTION

### Example 14: War Council — Painterly (Iron Crown)
```
Prompt: An aging king in tarnished silver armor stands behind a massive 
round stone table with a carved map of a fantasy kingdom, both hands planted 
on the surface, looking down with grim determination. Battle scars across 
his left cheek, grey-streaked hair pulled back. A hooded advisor in dark 
green robes points at a position on the map from the right side. Warm 
orange torchlight from wall sconces mixes with cold blue moonlight from 
a narrow window behind the king, creating dual-colored rim lights. Low 
angle from table level. Oil painting style with visible brushwork, 
classical composition, chiaroscuro, reminiscent of Caravaggio. Avoid: 
photorealistic, modern, clean digital render.

Model: grok-imagine-image
Resolution: 2k
Aspect Ratio: 16:9
N: 4
Seed: null

Director's Notes: Caravaggio reference + "oil painting with visible brushwork" 
steers Aurora away from photorealism toward painterly rendering. Negative 
guidance reinforces: "avoid photorealistic, clean digital render." Dual 
light temperatures (orange torchlight vs blue moonlight) create the 
classical warm/cool contrast.
```

---

### Example 15: Surrealist Music Video Frame (Neon Pulse)
```
Prompt: A dancer suspended in mid-air inside a giant transparent sphere 
floating above a city at night, body contorted in an impossible pose, 
trailing ribbons of light from her fingertips. The city below is a grid 
of neon, out of focus. The sphere is cracked, light leaking out through 
fracture lines. Stars visible through the sphere's upper half. Surrealist 
composition, inspired by Gregory Crewdson's staged photographs meets 
anime energy. Vivid electric colors against deep black sky. Wide shot, 
dramatic, ethereal. Shot on Phase One IQ4 150MP, extreme sharpness.

Model: grok-imagine-image
Resolution: 2k
Aspect Ratio: 9:16
N: 4
Seed: null

Director's Notes: Style blend: "Gregory Crewdson meets anime energy" gives 
Aurora a specific direction that leverages its cinematic default while adding 
surreal elements. Phase One IQ4 reference provides extreme resolution rendering. 
Portrait orientation for music video / social media format.
```

---

### Example 16: Brand Mood — Luxury Ingredients (Aurelia)
```
Prompt: An extreme macro photograph of a single drop of golden perfume 
falling into a shallow pool of liquid on a white marble surface, the impact 
creating a tiny crown splash frozen in time. Inside the drop, refracted 
light creates a miniature rainbow. Scattered around the pool: three dried 
rose petals, a curl of vanilla bean, and a sliver of sandalwood bark. 
Soft overhead studio lighting with a single warm accent light from behind 
the drop. Shot on Canon EOS R5 with Canon RF 100mm f/2.8L Macro, f/4, 
high-speed flash freeze. Ultra-clean commercial photography, luxury brand 
advertising quality. Avoid: messy, cluttered, dark, moody.

Model: grok-imagine-image
Resolution: 2k
Aspect Ratio: 1:1
N: 4
Seed: null

Director's Notes: Macro photography with flash freeze is technically precise — 
Aurora handles it well. "Inside the drop, refracted light" tests rendering 
physics. Negative guidance ("avoid: messy, cluttered, dark, moody") pushes 
away from Aurora's dramatic default toward clean luxury commercial aesthetic.
```

---

## Version Information

- **Examples Version:** 1.0
- **Covers:** Grok Aurora (`grok-imagine-image`)
- **Last Updated:** 2026-04-18
- **Maintained By:** Visual Horizon Studio
