# Mystic 2.5 API Sub-Models - Examples

These variants are only available via API and offer specialized capabilities for specific use cases.

---

## ZEN - Minimalist & Soft Aesthetics

**Key Features:**
- Smoother, cleaner results
- Fewer objects in composition
- Less intricate detail
- Soft, minimalist aesthetic
- Best for clean, simple scenes

---

### Example 1: Minimalist Portrait
```
Prompt: Portrait of person in simple white clothing against soft neutral 
background, minimal composition, clean and serene, soft natural light

Negative: cluttered, busy, colorful, harsh, detailed, ornate

Model: zen
Engine: illusio
Creative Detailing: 25
Resolution: 2K
Aspect Ratio: portrait_2_3
```

---

### Example 2: Zen Garden
```
Prompt: Japanese zen garden with raked sand patterns and single rock, 
minimalist composition, peaceful atmosphere, soft morning light

Negative: colorful, busy, cluttered, people, buildings, ornate

Model: zen
Engine: illusio
Creative Detailing: 20
Resolution: 2K
Aspect Ratio: square_1_1
```

---

### Example 3: Minimalist Architecture
```
Prompt: Modern minimalist interior with single piece of furniture, clean 
lines, soft natural light through large window, serene and spacious

Negative: cluttered, colorful, busy, ornate, dark, many objects

Model: zen
Engine: illusio
Creative Detailing: 28
Resolution: 2K
Aspect Ratio: widescreen_16_9
```

---

### Example 4: Simple Still Life
```
Prompt: Single ceramic vase on clean surface, soft diffused light, 
minimalist composition, elegant simplicity

Negative: multiple objects, cluttered, colorful, busy, ornate, complex

Model: zen
Engine: illusio
Creative Detailing: 22
Resolution: 2K
Aspect Ratio: square_1_1
```

---

### Example 5: Soft Landscape
```
Prompt: Misty rolling hills at dawn, minimal composition, soft pastel 
colors, peaceful and serene, clean atmosphere

Negative: busy, detailed, cluttered, harsh colors, buildings, people

Model: zen
Engine: illusio
Creative Detailing: 25
Resolution: 2K
Aspect Ratio: widescreen_16_9
```

---

### Example 6: Meditation Space
```
Prompt: Minimalist meditation room with single cushion, soft natural 
light, clean white walls, peaceful and calming

Negative: cluttered, busy, colorful, many objects, ornate, detailed

Model: zen
Engine: illusio
Creative Detailing: 20
Resolution: 2K
Aspect Ratio: widescreen_16_9
```

---

### Zen Template:
```
Prompt: [Single subject] [minimal setting], soft [lighting], clean and 
serene, minimalist composition

Negative: cluttered, busy, colorful, many objects, ornate, harsh, detailed

Model: zen
Engine: illusio
Creative Detailing: 20-28 (low for cleanest look)
Resolution: 2K
```

---

## SUPER REAL - Hyper-Realistic Photography

**Key Features:**
- Hyper-realism with sharp details
- Best for medium shots (not close-ups)
- Sharp photographic quality
- Weaker for portraits than editorial_portraits
- Best for product and realistic scenes

---

### Example 7: Product Photography
```
Prompt: Luxury wristwatch on marble surface, dramatic studio lighting 
from 45 degrees, hyper-realistic commercial photography, sharp focus on 
details, shot with Phase One XF

Negative: cartoon, soft focus, cluttered, amateur, artificial

Model: super_real
Engine: sharpy
Creative Detailing: 48
Resolution: 4K
Aspect Ratio: square_1_1
```

---

### Example 8: Automotive Detail
```
Prompt: Close-up of car headlight assembly with intricate LED details, 
rain droplets, hyper-realistic automotive photography, shot with medium 
format camera

Negative: cartoon, soft, blurry, amateur, dirty, damaged

Model: super_real
Engine: sharpy
Creative Detailing: 50
Resolution: 4K
Aspect Ratio: widescreen_16_9
```

---

### Example 9: Food Photography
```
Prompt: Gourmet burger with visible texture details on ingredients, 
dramatic food photography lighting, hyper-realistic, shot with macro lens

Negative: cartoon, soft, blurry, artificial, plastic-looking, amateur

Model: super_real
Engine: sharpy
Creative Detailing: 48
Resolution: 4K
Aspect Ratio: square_1_1
```

---

### Example 10: Interior Design
```
Prompt: Luxury living room interior with visible texture on fabrics and 
materials, natural light, hyper-realistic architectural photography, sharp 
details throughout

Negative: cartoon, soft, cluttered, amateur, dark, blurry

Model: super_real
Engine: sharpy
Creative Detailing: 50
Resolution: 4K
Aspect Ratio: widescreen_16_9
```

---

### Example 11: Nature Macro
```
Prompt: Dew drops on spider web at dawn, hyper-realistic macro photography, 
sharp focus with visible water droplet details, natural bokeh background

Negative: cartoon, artificial, soft, blurry, cluttered, amateur

Model: super_real
Engine: sharpy
Creative Detailing: 52
Resolution: 4K
Aspect Ratio: standard_3_2
```

---

### Example 12: Tech Product Medium Shot
```
Prompt: Professional camera equipment on workspace, hyper-realistic product 
photography, sharp details on dials and textures, shot with technical camera

Negative: cartoon, soft focus, cluttered, amateur, blurry, artificial

Model: super_real
Engine: sharpy
Creative Detailing: 50
Resolution: 4K
Aspect Ratio: widescreen_16_9
```

---

### Super Real Template:
```
Prompt: [Product/subject] [setting], hyper-realistic photography, sharp 
focus on details, shot with [high-end camera]

Negative: cartoon, soft focus, blurry, amateur, artificial

Model: super_real
Engine: sharpy
Creative Detailing: 48-52
Resolution: 4K
```

---

## EDITORIAL PORTRAITS - Professional Portrait Photography

**Key Features:**
- Unmatched realism for close-up portraits
- Best for professional headshots
- Requires VERY long, detailed prompts
- Anatomical issues in wide/distant shots
- ONLY use for close/medium portraits

---

### Example 13: Executive Headshot
```
Prompt: Professional corporate headshot of 42-year-old male executive with 
salt-and-pepper hair styled in modern side part, clean-shaven with defined 
jawline, wearing tailored charcoal gray suit with crisp white dress shirt 
and burgundy silk tie, confident yet approachable expression with slight 
genuine smile showing in eyes, direct eye contact with camera, shot with 
Canon EOS R5 paired with 85mm f/1.4 L IS lens at aperture f/2.8 for optimal 
sharpness while maintaining shallow depth of field, studio lighting setup 
with large octagonal softbox as key light positioned 45 degrees to subject's 
left at 6 feet distance creating soft flattering shadows, white reflector 
fill from right side reducing shadow depth, subtle hair light from behind 
and above separating subject from neutral medium gray seamless background, 
color temperature 5500K for natural skin tones, professional corporate 
portrait photography style with editorial quality

Negative: cartoon, deformed face, asymmetrical eyes, extra fingers, disfigured 
hands, blurry, oversaturated, plastic skin, amateur, harsh lighting, unflattering 
shadows, unnatural colors, low quality

Model: editorial_portraits
Engine: sharpy
Creative Detailing: 42
Resolution: 4K
Aspect Ratio: portrait_2_3
HDR: 45
```

**Note:** This extremely long, detailed prompt is REQUIRED for editorial_portraits model. Short prompts produce poor results.

---

### Example 14: Female Professional Portrait
```
Prompt: Professional portrait of 38-year-old female marketing director with 
shoulder-length auburn hair with subtle balayage highlights styled in soft 
loose waves framing her face, natural makeup featuring warm bronze eyeshadow 
accentuating hazel eyes, neutral pink lip color, wearing fitted navy blue 
blazer over cream silk blouse, delicate gold necklace, confident and warm 
expression conveying approachability and competence, slight genuine smile 
with natural sparkle in eyes, direct camera engagement, shot with Sony A7R V 
camera and Zeiss Batis 85mm f/1.8 lens at f/2.2 aperture creating beautiful 
bokeh while maintaining facial sharpness, professional studio lighting with 
large parabolic softbox as main light from 40 degrees camera left creating 
flattering dimension, silver reflector from right reducing contrast ratio, 
subtle rim light from upper back right separating from soft neutral beige 
background, color grading with slightly warm tones for inviting feel, 
editorial portrait photography with corporate polish

Negative: cartoon, deformed, asymmetrical features, extra fingers, bad anatomy, 
blurry, artificial, oversaturated, harsh lighting, unflattering, amateur, 
low quality, incorrect color

Model: editorial_portraits
Engine: sharpy
Creative Detailing: 40
Resolution: 4K
Aspect Ratio: portrait_2_3
```

---

### Example 15: Artist Portrait
```
Prompt: Editorial portrait of 29-year-old male artist with tousled dark brown 
hair, two-day stubble, expressive brown eyes, wearing paint-splattered denim 
shirt over black t-shirt, contemplative yet intense expression showing creative 
depth, natural unforced connection with camera, shot with Hasselblad X2D 100C 
medium format camera and HC 100mm f/2.2 lens at f/2.8 for exceptional detail 
and smooth bokeh, natural window light as primary source coming from large 
north-facing window creating soft directional illumination with gentle shadows, 
white foam board bounce from opposite side filling shadows while maintaining 
dimension, background showing subtle hint of art studio with bokeh'd painting 
supplies, color palette emphasizing earthy tones and authentic skin rendering, 
editorial portrait photography with artistic documentary quality capturing 
genuine personality

Negative: cartoon, deformed, extra fingers, symmetrical boring pose, 
oversaturated, plastic, harsh studio flash, artificial, amateur, low quality, 
unflattering, bad anatomy

Model: editorial_portraits
Engine: sharpy
Creative Detailing: 38
Resolution: 4K
Aspect Ratio: standard_3_2
```

---

### Example 16: Senior Executive
```
Prompt: Distinguished portrait of 58-year-old female CEO with elegantly 
styled short silver-gray hair in modern sophisticated cut, refined features 
with natural aging grace, wearing timeless black turtleneck and tailored 
blazer, subtle diamond stud earrings, commanding yet warm presence conveying 
decades of leadership experience, calm confident expression with knowing 
gentle smile, direct authoritative yet approachable eye contact, shot with 
Nikon Z9 and Nikkor Z 85mm f/1.2 lens at f/2.0 creating beautiful subject 
separation, classic Rembrandt lighting setup with large gridded softbox as 
key from 45 degrees creating signature triangle of light on shadow side of 
face, fill card reducing shadow to 2:1 ratio, subtle hair light defining 
silver tones, clean neutral gray background, color grading emphasizing 
sophistication and gravitas, high-end editorial portrait photography with 
timeless quality

Negative: cartoon, deformed, ageist smoothing, over-retouched, artificial, 
harsh lighting, unflattering, amateur, low quality, bad anatomy, plastic skin

Model: editorial_portraits
Engine: sharpy
Creative Detailing: 43
Resolution: 4K
Aspect Ratio: portrait_2_3
```

---

### Example 17: Creative Professional
```
Prompt: Editorial portrait of 35-year-old female creative director with 
distinctive platinum blonde pixie cut, bold black-framed glasses, subtle 
nose piercing, wearing vintage band t-shirt under tailored olive green 
blazer, multiple delicate silver rings, expression showing creative 
intelligence and confident individuality, authentic smile with engaging 
energy, shot with Canon EOS R5 and RF 85mm f/1.2 lens at f/1.8 for dramatic 
depth of field isolating subject, window light as primary illumination 
creating soft wrap-around quality from camera right, black v-flat opposite 
creating subtle shadows and dimension, modern industrial loft background 
with exposed brick in pleasing bokeh, color palette with slightly desaturated 
tones and cooler temperature reflecting contemporary creative industry 
aesthetic, editorial portrait with personality and authenticity

Negative: cartoon, generic, oversaturated, harsh flash, artificial, amateur, 
deformed, bad anatomy, low quality, boring, conventional

Model: editorial_portraits
Engine: sharpy
Creative Detailing: 40
Resolution: 4K
Aspect Ratio: social_post_4_5
```

---

### Example 18: Medium Portrait (Safe Zone)
```
Prompt: Medium portrait from waist up of 45-year-old physician in white 
coat over blue scrubs, stethoscope around neck, standing in modern medical 
facility with soft diffused lighting, compassionate professional expression, 
arms crossed comfortably, shot with Sony A7R V and 85mm f/1.4 lens at f/2.8, 
natural light from large windows creating gentle illumination, background 
showing medical environment in soft focus, professional healthcare portrait 
photography with editorial quality and trust-building presence

Negative: cartoon, amateur, harsh lighting, clinical sterile, unflattering, 
deformed hands, bad anatomy, low quality

Model: editorial_portraits
Engine: sharpy
Creative Detailing: 40
Resolution: 4K
Aspect Ratio: portrait_2_3
```

**Note:** Medium portraits work with editorial_portraits. Avoid wide/full body shots.

---

### Editorial Portraits Template:
```
Prompt: Professional [occupation-specific] portrait of [age]-year-old 
[gender] [detailed physical description including hair, features, clothing], 
[expression and emotional quality], [detailed eye contact/engagement], shot 
with [specific camera body] and [specific lens] at [aperture], [extensive 
lighting setup description including key light type, position, modifiers, 
fill, hair/rim lights, ratios], [background description], [color grading 
approach], editorial portrait photography [quality descriptors]

[CRITICAL: Make prompt 200-400 words with extensive detail]

Negative: cartoon, deformed face, asymmetrical eyes, extra fingers, bad 
anatomy, blurry, oversaturated, plastic skin, harsh lighting, unflattering, 
amateur, low quality

Model: editorial_portraits
Engine: sharpy
Creative Detailing: 38-43
Resolution: 4K
Aspect Ratio: portrait_2_3 or social_post_4_5
```

---

## API SUB-MODEL COMPARISON

### When to Use Each:

**Zen:**
- Want: Minimal, clean, soft aesthetic
- Subjects: Single objects, simple scenes, meditation spaces
- Creative Detailing: 20-28 (low)
- Engine: Illusio (always)

**Super Real:**
- Want: Hyper-realistic product/scene photography
- Subjects: Products, medium shots, detailed scenes
- Avoid: Close-up portraits (use editorial_portraits)
- Creative Detailing: 48-52 (high)
- Engine: Sharpy (always)

**Editorial Portraits:**
- Want: Professional headshot/portrait quality
- Subjects: ONLY close-up and medium portraits
- Avoid: Wide shots, full body, groups
- Prompts: MUST be 200-400 words, extremely detailed
- Creative Detailing: 38-43
- Engine: Sharpy (always)
- Resolution: 4K (always)

---

**Pro Tips:**

**Zen:** Embrace minimalism. Less is more. Keep prompts focused on single subjects with clean backgrounds. Low creative detailing + Illusio engine = softest, cleanest results.

**Super Real:** Describe materials, textures, lighting setups in detail. This model rewards technical photography language. Always use 4K resolution.

**Editorial Portraits:** Write EXTENSIVE prompts (200-400 words). Include camera, lens, aperture, lighting setup, background, expression, clothing, and color grading. This model REQUIRES detail to produce professional results. Never use for wide shots or full body - anatomical issues will appear. Stick to close-up and medium portraits only.
