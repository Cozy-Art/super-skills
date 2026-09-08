# Grok Aurora — Best Practices Guide

## The Cinematic Default Problem (and How to Use It)

**Aurora's most important characteristic is its built-in cinematic bias.**

Every prompt you send to Aurora is filtered through an aesthetic lens that favors dramatic lighting, saturated colors, shallow depth of field, and "movie still" production quality. This is both a superpower and a trap:

**When to lean into it:**
- Action scenes, dramatic portraits, sci-fi concept art
- Commercial photography (luxury products, fashion)
- Cinematic storyboard frames
- Any shot where "this looks like a frame from a movie" is a compliment

**When to actively fight it:**
- Documentary photography — add "natural light only, no post-processing, raw aesthetic"
- Minimalist design — add "clean, flat lighting, simple composition"
- Specific art styles — name the style explicitly: "ukiyo-e woodblock print" or "pencil sketch on paper"
- Journalistic or editorial realism — add "photojournalism, available light, candid"

### ✅ When cinematic default helps:
```
A lone warrior stands at the edge of a cliff overlooking a burning city, 
dramatic sunset backlighting, sweeping wide angle, epic fantasy concept art
```
→ Aurora's cinematic bias amplifies everything about this prompt perfectly.

### ✅ When you must override it:
```
A weathered fisherman mending nets on a wooden dock, overcast morning, 
documentary photography, natural light only, Leica M10, no post-processing, 
raw candid moment — avoid: cinematic lighting, dramatic, saturated colors
```
→ Without explicit overrides, this becomes a glamorized movie scene, not documentary.

---

## The Six-Part Prompt Formula

```
[Subject] + [Style/Medium] + [Environment] + [Lighting] + [Mood] + [Technical Details]
```

### Component Guide

**1. Subject** — Who or what, with specific attributes
- ❌ "A woman" → ✅ "A woman in her 60s with silver-streaked black hair, deep laugh lines, wearing a faded denim work shirt"
- ❌ "A car" → ✅ "A 1967 Shelby GT500 in dark blue metallic, slightly dusty, chrome bumper catching light"

**2. Style/Medium** — What kind of image
- Photography: "shot on Canon EOS R5," "Polaroid photograph," "35mm film grain"
- Art: "oil painting," "watercolor sketch," "3D render," "vector illustration"
- Reference: "Greg Rutkowski style," "Studio Ghibli," "National Geographic"
- **Critical:** If you don't specify, Aurora chooses "cinematic photography" by default

**3. Environment** — Where
- "rainy New York City night" / "abandoned Victorian greenhouse"
- Include time of day, weather, season for atmospheric control
- Interior details: furniture, textures, spatial relationships

**4. Lighting** — How it's lit
- Named setups: "Rembrandt lighting," "butterfly lighting," "rim light"
- Natural: "golden hour," "overcast diffused," "harsh noon sun"
- Atmospheric: "volumetric fog," "dust motes in sunbeam," "neon spill"
- Direction: "soft side lighting from the left," "backlit silhouette"

**5. Mood** — Emotional tone
- "peaceful," "ominous," "nostalgic," "tense," "whimsical"
- Can combine: "serene but slightly unsettling"
- Mood influences color grading, contrast, and atmosphere

**6. Technical Details** — Camera specs
- Body: "Leica M10," "ARRI Alexa," "Hasselblad X2D"
- Lens: "35mm Summilux," "85mm f/1.4," "24mm wide angle"
- Settings: "f/1.4 aperture," "shallow depth of field," "deep focus"
- Film: "Kodak Portra 400," "Fujifilm Velvia," "CineStill 800T"

---

## What to Emphasize

### Lighting Terminology That Works
Aurora responds exceptionally well to specific lighting language:

| Term | Effect | Best For |
|------|--------|----------|
| Rembrandt lighting | Dramatic triangle of light on face | Portraits, character work |
| Golden hour | Warm, low-angle natural light | Landscapes, romantic scenes |
| Volumetric fog | Visible light beams through atmosphere | Atmospheric, mysterious |
| Studio strobe | Clean, controlled studio lighting | Product, commercial |
| Neon spill | Colored light from neon sources | Urban, cyberpunk, nightlife |
| Backlit / rim light | Subject outlined with light from behind | Dramatic silhouettes |
| Overcast diffused | Soft, even, shadowless light | Documentary, naturalistic |
| Hard noon sun | Harsh shadows, high contrast | Desert, raw, uncomfortable |
| Candlelight | Warm, flickering, intimate | Period pieces, romance |
| Practical lighting | Light from visible in-scene sources | Realism, noir |

### Camera and Lens Specifications
These drive Aurora's photorealism more than any other prompt element:

**For portraits:** "85mm f/1.4" — classic portrait compression and bokeh
**For environmental:** "35mm f/2.0" — wide enough for context, still shallow DOF
**For product:** "100mm macro f/5.6" — sharp detail, controlled DOF
**For landscape:** "24mm f/8" — deep focus, full scene sharpness
**For cinematic:** "Cooke Speed Panchro vintage lens" — period-appropriate character
**For documentary:** "Leica M10, 35mm Summilux" — street photography authority

### Composition Language
- "Rule of thirds composition" — subject at intersection points
- "Centered symmetrical" — Kubrick-style formal framing
- "Dynamic diagonal" — energy and movement
- "Wide angle shot" / "extreme close-up" / "medium shot"
- "Dutch angle" — tilted frame for unease
- "Leading lines" — environmental lines drawing eye to subject
- "Negative space" — isolation of subject

---

## What to Avoid

### Vague Prompts
| ❌ Vague | ✅ Specific |
|---------|-----------|
| "A cool picture of a city" | "Cyberpunk Tokyo street at night, neon signs reflecting on wet pavement, dense urban atmosphere, Blade Runner aesthetic" |
| "A portrait of someone" | "Close-up portrait of a 40-year-old jazz musician, saxophone reflected in his glasses, warm amber spotlight, smoke curling in backlight" |
| "A nice landscape" | "Misty dawn over rice terraces in Bali, layers of green descending into fog, single farmer figure on distant terrace, shot on Fujifilm GFX 100S" |

### Superlative Spam
Wastes prompt space and adds no visual information:
- ❌ "Beautiful amazing stunning gorgeous incredible breathtaking"
- ✅ "Dramatic cinematic lighting, shallow depth of field" (actual visual descriptors)

### Contradictory Instructions
Aurora tries to satisfy everything and fails at everything:
- ❌ "Realistic photograph in anime style"
- ✅ "Anime-style illustration with realistic lighting and proportions"
- ❌ "Bright and dark at the same time"
- ✅ "High-contrast scene with bright highlights and deep shadows"

---

## Negative Guidance Strategy

Aurora doesn't have a separate `negative_prompt` parameter. Instead, include exclusions inline:

### Syntax Options

**End-of-prompt exclusion:**
```
Portrait of a businesswoman, professional photography, natural lighting. 
Avoid: cartoon style, anime, illustration, distorted features, extra fingers
```

**Integrated avoidance:**
```
Portrait of a businesswoman, professional photography, natural lighting, 
NOT anime or cartoon style, anatomically correct hands, realistic proportions
```

**Style override (fighting cinematic default):**
```
Documentary photograph of a street market, natural available light, 
raw unprocessed aesthetic, NOT cinematic, NOT dramatic lighting, 
NOT color graded, candid photojournalism
```

### Common Negative Guidance Sets

**For photorealism:**
```
avoid: cartoon, anime, illustration, CGI look, plastic skin, oversaturated, 
extra fingers, distorted features
```

**For specific art styles (fighting cinematic bias):**
```
avoid: photorealistic, cinematic lighting, dramatic shadows, lens flare, 
movie still aesthetic
```

**For clean commercial photography:**
```
avoid: grunge, distressed, vintage filter, film grain, noise, imperfections
```

---

## Character Consistency Strategies

### Method 1: Locked Character Description
Create a detailed character "sheet" and paste it identically into every prompt:

**Character anchor (reuse verbatim):**
```
A man in his late 40s with a strong jaw, close-cropped salt-and-pepper hair, 
a thin scar above his right eyebrow, wearing a dark navy peacoat with the 
collar turned up, five o'clock shadow
```

**Prompt A:** "[character anchor], walking through a rain-soaked London street at night, reflected in a shop window, shot on Leica M10, 35mm, available light"

**Prompt B:** "[character anchor], seated at a wooden pub table, pint glass in hand, warm amber light from a fireplace to his left, shallow depth of field"

### Method 2: Seed Locking
Use the same `--s` seed value across all related generations to maintain visual consistency:
```
--s 42891  ← use this exact value for every image in the series
```

### Method 3: Image-to-Image Reference
Upload a previously generated character image and prompt edits that change the scene while preserving the character:
```
[Provide image_url of established character shot]
Place this character in a different setting: standing on a rooftop 
at dawn, city skyline behind them, wind in their coat. Maintain 
all character details from the reference image.
```

### Method 4: Conversational Refinement
Within a single Grok chat session:
1. Generate initial character image
2. "Keep the character exactly the same but change the background to a desert highway"
3. "Same character, same style, but now at night with neon lighting"

---

## Iterative Refinement Workflow

### The Three-Step Process

**Step 1: Broad concept**
```
Dragon flying over mountains
```

**Step 2: Add specificity**
```
Eastern dragon flying over misty Chinese mountains, traditional ink painting style
```

**Step 3: Full detail**
```
Serpentine Chinese dragon weaving through Huangshan mountain peaks, 
traditional Song Dynasty ink wash painting style, subtle red accents 
on the dragon's mane, hanging scroll composition format, museum 
quality reproduction, mist filling the valleys between peaks
```

### Layered Construction
For complex scenes, build prompts in layers:

1. **Core subject:** "A jazz singer at a microphone"
2. **+ Environment:** "in a smoky 1950s basement club, exposed brick walls"
3. **+ Lighting:** "single warm spotlight from above, the rest of the room in shadow"
4. **+ Camera:** "shot on ARRI Alexa LF, 50mm Cooke S4i lens, shallow focus"
5. **+ Mood:** "intimate, raw, the moment before the first note"

---

## Style Transfer via Prompt

Aurora handles style through prompt description — no separate style parameter:

### Photography Styles
- "National Geographic style" → dramatic nature, perfect composition
- "Vogue editorial" → high fashion, stylized
- "Henri Cartier-Bresson inspired" → decisive moment, black and white
- "Polaroid photograph" → soft colors, white border, analog feel

### Art Styles
- "Greg Rutkowski style" → detailed fantasy art
- "Studio Ghibli" → animated, pastoral, detailed backgrounds
- "Monet" → impressionist, soft brushwork, light-focused
- "Banksy" → stencil street art, social commentary

### Media Types
- "Oil painting on canvas with visible brushstrokes"
- "Pencil sketch on aged paper"
- "3D render, Octane, subsurface scattering"
- "Vector illustration, flat colors, clean lines"
- "Watercolor on cold-press paper, wet edges bleeding"

---

## Troubleshooting

### Image Looks Generic/Flat
- Add specific lighting direction and quality
- Include camera and lens specifications
- Name a style reference (artist, studio, photographer)
- Add composition language (rule of thirds, leading lines)

### Can't Escape Cinematic Look
- Explicitly name the target style ("documentary," "minimalist," "editorial")
- Add negative guidance: "avoid: cinematic, dramatic lighting, color graded"
- Reference a non-cinematic photographer or artist
- Specify "natural available light" or "flat even lighting"

### Characters Change Between Images
- Lock character description word-for-word
- Use same seed value (`--s`) across all images
- Use image-to-image with established character as reference
- Stay within same chat session for conversational refinement

### Hands/Fingers Look Wrong
- Add "anatomically correct hands with five fingers" to prompt
- Frame the shot to hide hands (behind back, in pockets, holding objects)
- Use medium/wide shots where hands are small in frame
- Post-process with inpainting tools

### Text in Image Doesn't Render
- Aurora is actually strong at text rendering — ensure text is clearly described
- "A neon sign reading OPEN 24 HOURS" (be explicit about text content)
- Keep text short (1-5 words renders most reliably)
- Specify font style: "bold sans-serif," "elegant script," "monospace"

### Output Colors Are Wrong
- Specify colors explicitly: "deep navy," "warm amber," "cool cyan"
- Reference color palettes: "teal and orange color palette," "muted earth tones"
- For accurate brand colors, describe them precisely (no HEX support)

---

## Version Information

- **Guide Version:** 1.0
- **Covers:** Grok Aurora (`grok-imagine-image`)
- **Last Updated:** 2026-04-18
- **Maintained By:** Visual Horizon Studio
