# Mystic 2.5 Standard (Realism) - Examples

The Standard variant excels at photorealism with natural colors and is the only variant supporting Custom Characters and Custom Styles (LoRA).

**Key Features:**
- Natural color palette
- "Less AI look"
- LoRA compatible
- Versatile for photography and illustrations
- 50 credits/image

---

## PHOTOREALISTIC PORTRAITS

### Example 1: Professional Headshot
```
Prompt: Corporate headshot of 40-year-old male executive, navy suit and tie, 
confident expression, shot with Canon EOS R5 and 85mm f/1.4 at f/2.8, studio 
lighting with softbox key

Negative: cartoon, deformed face, asymmetrical eyes, extra fingers, blurry, 
oversaturated, plastic skin

Variant: Standard (realism)
Engine: Sharpy
Creative Detailing: 40
Resolution: 4K
Aspect Ratio: portrait_2_3
Fixed Generation: true
```

---

### Example 2: Environmental Portrait
```
Prompt: Portrait of carpenter in workshop surrounded by tools and wood shavings, 
worn apron, focused expression, natural window light from left, shot with 
Nikon Z9 and 35mm f/1.4

Negative: cartoon, artificial, over-processed, cluttered background, blurry

Variant: Standard (realism)
Engine: Sparkle
Creative Detailing: 38
Resolution: 2K
Aspect Ratio: standard_3_2
```

---

### Example 3: Lifestyle Portrait
```
Prompt: Young woman reading book in cozy cafe, soft afternoon light through 
window, latte on table, relaxed expression, candid moment, shot with Sony A7R V

Negative: posed, artificial, oversaturated, cartoon, extra fingers

Variant: Standard (realism)
Engine: Illusio
Creative Detailing: 33
Resolution: 2K
Aspect Ratio: classic_4_3
```

---

## CUSTOM CHARACTERS (LoRA)

### Example 4: Character Consistency - Detective Series
```
[Custom Character trained: "detective_noir" from 10 reference images]

Prompt: @detective_noir::80 examining evidence under desk lamp in dim office, 
trench coat and fedora, noir aesthetic, shot with ARRI Alexa LF

Negative: bright colors, cartoon, cheerful, modern, oversaturated

Variant: Standard (realism) - REQUIRED for LoRA
Engine: Sharpy
Creative Detailing: 40
Styling > Characters > detective_noir: Strength 80
Resolution: 2K
Aspect Ratio: widescreen_16_9
```

---

### Example 5: Character in Different Scene
```
[Same Custom Character: "detective_noir"]

Prompt: @detective_noir::80 walking through rain-soaked alley at night, 
neon signs reflecting in puddles, film noir atmosphere

Negative: bright daylight, cartoon, colorful, cheerful, oversaturated

Variant: Standard (realism)
Engine: Sharpy
Creative Detailing: 42
Styling > Characters > detective_noir: Strength 80
Resolution: 2K
Aspect Ratio: widescreen_16_9
Fixed Generation: true (for series consistency)
```

---

### Example 6: Character Close-up
```
[Same Custom Character: "detective_noir"]

Prompt: @detective_noir::85 close-up portrait, contemplative expression, 
harsh side lighting, shadows across face, noir aesthetic

Negative: smiling, bright, cartoon, oversaturated, soft lighting

Variant: Standard (realism)
Engine: Sharpy
Creative Detailing: 38
Styling > Characters > detective_noir: Strength 85
Resolution: 4K
Aspect Ratio: portrait_2_3
```

---

## PRODUCT PHOTOGRAPHY

### Example 7: Luxury Watch
```
Prompt: Luxury watch product shot on black velvet surface, dramatic studio 
lighting from 45 degrees, sharp details on metal and crystal, shot with 
Phase One XF, commercial photography

Negative: cluttered, busy background, reflections, fingerprints, cartoon

Variant: Standard (realism)
Engine: Sharpy
Creative Detailing: 48
Resolution: 4K
Aspect Ratio: square_1_1
HDR: 45 (controlled detail)
```

---

### Example 8: Food Photography
```
Prompt: Artisan coffee latte with intricate latte art foam design, rustic 
wooden table, soft natural morning light, shot with Sony A7R V and macro lens

Negative: artificial, plastic, oversaturated, cluttered, cartoon

Variant: Standard (realism)
Engine: Sparkle
Creative Detailing: 42
Resolution: 2K
Aspect Ratio: square_1_1
```

---

### Example 9: Product on White
```
Prompt: Modern headphones product shot on pure white seamless background, 
clean studio lighting, commercial photography style, sharp focus

Negative: shadows, gray background, reflections, cluttered, cartoon

Variant: Standard (realism)
Engine: Sharpy
Creative Detailing: 50
Resolution: 4K
Aspect Ratio: square_1_1
```

---

## NATURAL LANDSCAPES

### Example 10: Mountain Vista
```
Prompt: Misty mountain landscape at dawn, soft light filtering through fog, 
layers of ridges fading into distance, peaceful atmosphere, shot with 
Hasselblad X2D

Negative: oversaturated, HDR, people, buildings, cartoon, artificial

Variant: Standard (realism)
Engine: Illusio
Creative Detailing: 30
Resolution: 2K
Aspect Ratio: widescreen_16_9
```

---

### Example 11: Coastal Scene
```
Prompt: Rocky coastline at golden hour, waves crashing on rocks, warm sunset 
light, long exposure water blur effect, landscape photography

Negative: people, bright midday, oversaturated, cartoon, cluttered

Variant: Standard (realism)
Engine: Sparkle
Creative Detailing: 35
Resolution: 2K
Aspect Ratio: standard_3_2
```

---

## ARCHITECTURAL PHOTOGRAPHY

### Example 12: Modern Interior
```
Prompt: Minimalist modern living room with floor-to-ceiling windows, natural 
light, neutral color palette, architectural photography, shot with tilt-shift 
lens

Negative: cluttered, colorful, people, messy, cartoon, fisheye distortion

Variant: Standard (realism)
Engine: Sharpy
Creative Detailing: 40
Resolution: 4K
Aspect Ratio: widescreen_16_9
```

---

### Example 13: Historic Building Exterior
```
Prompt: Gothic cathedral facade at dusk, architectural details highlighted 
by warm artificial lighting, deep blue sky, architectural photography

Negative: people, crowds, modern, cartoon, oversaturated, daytime bright

Variant: Standard (realism)
Engine: Sharpy
Creative Detailing: 45
Resolution: 4K
Aspect Ratio: traditional_3_4
```

---

## CUSTOM STYLES (LoRA)

### Example 14: Applying Custom Style
```
[Custom Style trained: "watercolor_modern" from artist examples]

Prompt: Portrait of young artist in studio, paint-splattered apron, 
natural window light

Negative: cartoon, 3D render, photograph, realistic

Variant: Standard (realism) - REQUIRED for LoRA
Engine: Illusio
Creative Detailing: 35
Styling > Styles > watercolor_modern: Strength 85
Adherence: 40 (lower for more style influence)
Resolution: 2K
```

---

### Example 15: Style + Character Combined
```
[Custom Character: "artist_sarah", Custom Style: "watercolor_modern"]

Prompt: @artist_sarah::75 painting at easel in bright studio

Negative: photograph, realistic, 3D, cartoon

Variant: Standard (realism)
Engine: Illusio
Creative Detailing: 30
Styling > Characters > artist_sarah: Strength 75
Styling > Styles > watercolor_modern: Strength 80
Adherence: 35
Resolution: 2K
```

---

## ILLUSTRATIVE (Still Using Standard)

### Example 16: Book Cover Style
```
Prompt: Fantasy warrior with ornate armor standing atop mountain peak, 
dramatic clouds, epic composition, digital illustration aesthetic

Negative: photograph, realistic, cartoon, childish, bright primary colors

Variant: Standard (realism) - yes, can do illustrations too
Engine: Sparkle
Creative Detailing: 50
Resolution: 2K
Aspect Ratio: traditional_3_4
```

---

## STYLE REFERENCE (Image-to-Image)

### Example 17: Style Transfer from Reference
```
[Upload style reference image: impressionist painting]

Prompt: Mountain landscape with lake, trees in foreground, peaceful atmosphere

Negative: photograph, realistic, sharp details, modern

Variant: Standard (realism)
Engine: Illusio
Creative Detailing: 35
Style Reference: [uploaded image]
Adherence: 30 (low = closer to reference style)
HDR: 35 (low = more artistic)
Resolution: 2K
```

---

## CAMERA SPECIFICATION EXAMPLES

### Example 18: Cinema Camera Look
```
Prompt: Portrait of musician with guitar in moody warehouse space, 
cinematic lighting, shot with ARRI Alexa Mini and Cooke Anamorphic lens

Negative: snapshot, amateur, flat lighting, cartoon, oversaturated

Variant: Standard (realism)
Engine: Sharpy
Creative Detailing: 42
Resolution: 2K
Aspect Ratio: widescreen_16_9
```

---

### Example 19: Medium Format Photography
```
Prompt: Fashion editorial portrait in minimalist studio, soft even lighting, 
shot with Hasselblad H6D-100c and 80mm lens, medium format aesthetic

Negative: snapshot, busy, cluttered, oversaturated, cartoon, artificial

Variant: Standard (realism)
Engine: Sharpy
Creative Detailing: 40
Resolution: 4K
Aspect Ratio: portrait_2_3
```

---

## PARAMETER VARIATIONS

### Example 20: Low Creative Detailing (Natural Look)
```
Prompt: Casual portrait of grandmother reading to child, warm living room, 
afternoon light, tender moment

Negative: artificial, staged, oversaturated, cartoon, plastic

Variant: Standard (realism)
Engine: Illusio
Creative Detailing: 25 (low for soft, natural)
Resolution: 2K
Aspect Ratio: classic_4_3
```

---

### Example 21: High Creative Detailing (Maximum Detail)
```
Prompt: Macro photograph of mechanical watch movement, intricate gears and 
springs, sharp focus, commercial product photography

Negative: blurry, soft, cartoon, low detail, artificial colors

Variant: Standard (realism)
Engine: Sharpy
Creative Detailing: 65 (high for maximum detail)
Resolution: 4K
Aspect Ratio: square_1_1
```

---

## QUICK TEMPLATES

### Portrait Template:
```
Prompt: [Age/gender] [occupation/role], [clothing], [expression], 
[lighting], shot with [camera]

Negative: cartoon, deformed, extra fingers, blurry, oversaturated

Variant: Standard (realism)
Engine: Sharpy or Sparkle
Creative Detailing: 35-45
Resolution: 2K or 4K
```

### Product Template:
```
Prompt: [Product] on [surface], [lighting setup], shot with [camera], 
commercial photography

Negative: cluttered, cartoon, low quality, artificial

Variant: Standard (realism)
Engine: Sharpy
Creative Detailing: 45-50
Resolution: 4K
```

### Character Template (LoRA):
```
Prompt: @character_name::[strength] [action/pose], [environment], 
[style/aesthetic]

Negative: [opposite of desired aesthetic]

Variant: Standard (realism) - REQUIRED
Engine: Based on aesthetic
Creative Detailing: 35-45
Styling > Characters > [name]: Strength [70-90]
```

---

**Pro Tip for Standard Variant:** This is your go-to for anything requiring natural photorealism or LoRA compatibility. When in doubt, start here. The natural color palette and "less AI look" make it the most versatile option in the Mystic 2.5 family.
