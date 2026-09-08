# Freepik Mystic 2.5 - Best Practices Guide

## The Concise Prompt Philosophy

**Mystic 2.5's core strength is doing more with less.**

Unlike some AI models that benefit from lengthy, detailed prompts, Mystic excels with concise, direct language. The model's advanced understanding means you don't need to over-explain.

### ✅ Good (Concise):
```
Weathered detective in noir attire, rain-soaked alley, harsh streetlight, 
shot with ARRI Alexa LF
```

### ❌ Bad (Over-detailed):
```
A detective who looks weathered and has been working for many years wearing 
classic film noir style clothing including a dark trench coat and fedora hat 
standing in an urban alleyway that is wet from recent rainfall with harsh 
artificial lighting from a streetlight creating dramatic shadows, photographed 
using professional cinema camera equipment specifically the ARRI Alexa LF with 
cinematic color grading and depth of field...
```

**The first prompt will produce better results.**

---

## Variant Selection: When to Use Which Model

### Standard (Realism) - The Versatile Workhorse

**Best for:**
- Natural, photorealistic scenes
- Projects using Custom Characters (LoRA)
- Projects using Custom Styles (LoRA)
- General-purpose photography
- "Less AI look" aesthetic

**Parameter Recommendations:**
- Creative Detailing: 33-50
- Engine: Sharpy for photos, Sparkle for versatility
- Resolution: 2K (sweet spot)

**Strengths:**
- Natural color palette
- LoRA compatible
- Realistic without over-processing

**When NOT to use:**
- Need vivid, saturated fantasy colors → Use Flexible
- Need fastest generation for volume → Use Fluid

---

### Flexible - The Illustration Powerhouse

**Best for:**
- Fantasy illustrations
- Branding assets requiring vivid colors
- Stylized artwork
- Best possible prompt adherence
- Scenes requiring saturated HDR look

**Parameter Recommendations:**
- Creative Detailing: 40-60
- Engine: Automatic or Sparkle
- Resolution: 2K

**Strengths:**
- Best prompt adherence in family
- Vivid, saturated colors
- HDR aesthetic

**Limitations:**
- No LoRA support (cannot use Custom Characters/Styles)
- HDR look may be too saturated for some use cases

---

### Fluid - The Cinematic Specialist

**Best for:**
- Cinematic storyboard frames
- High-volume production
- Image sequences for video conversion
- Visual campaigns
- Consistency across related shots

**Parameter Recommendations:**
- Creative Detailing: 33 (default)
- Engine: Automatic
- Resolution: 2K

**Strengths:**
- Fast generation
- Smooth, consistent visuals
- Excellent for cinematic work
- Best for converting to video (Kling, etc.)

**Limitations:**
- Over-moderated (Google Imagen 3 backend)
- Words like "war" may be flagged
- No LoRA support

---

## API Sub-Models (Advanced Usage)

### Zen - The Minimalist

**When to use:**
- Clean, simple compositions
- Soft aesthetic required
- Fewer objects preferred
- Minimalist design

**Settings:**
- Creative Detailing: 20-40 (lower for cleaner look)
- Engine: Illusio (soft aesthetic)

---

### Super Real - The Hyper-Realist

**When to use:**
- Product photography
- Medium-shot photography
- Sharp photographic detail needed
- Hyper-realistic aesthetic

**Settings:**
- Creative Detailing: 40-50
- Engine: Sharpy (maximum detail)
- Resolution: 2K or 4K

**Limitation:** Weaker for close-up portraits than Editorial Portraits

---

### Editorial Portraits - The Portrait Specialist

**When to use:**
- Professional headshots
- Close-up portrait photography
- Editorial quality needed
- Medium portrait shots

**CRITICAL:** Use extremely long, detailed prompts with this model.

**Example:**
```
Professional headshot of a 35-year-old female executive with shoulder-length 
auburn hair styled in soft waves, wearing a tailored navy blazer over white 
silk blouse, subtle natural makeup highlighting green eyes, confident yet 
approachable expression with slight genuine smile, direct eye contact with 
camera, shot with Canon EOS R5 and 85mm f/1.4 lens at f/2.8, studio lighting 
with large softbox as key light from 45 degrees, white reflector fill, soft 
rim light separating from neutral gray background, shallow depth of field 
isolating subject, professional corporate portrait style
```

**Settings:**
- Creative Detailing: 33-50
- Engine: Sharpy
- Resolution: 4K (this model excels at high res)

**Limitation:** Anatomical problems in wide/distant shots - only use for close/medium

---

## Camera Specifications for Photorealism

### Why Camera Specs Matter

Including camera model and lens information helps Mystic understand the intended photographic aesthetic.

### Recommended Camera References

**Cinema Cameras:**
- ARRI Alexa LF
- ARRI Alexa Mini
- RED Komodo
- Sony Venice

**Photography Cameras:**
- Canon EOS R5
- Nikon Z9
- Sony A7R V
- Hasselblad X2D

**Lens Specifications:**
- 85mm f/1.4 (portrait classic)
- 35mm f/1.4 (environmental portrait)
- 24-70mm f/2.8 (versatile)
- 70-200mm f/2.8 (telephoto)

### ✅ Example with Camera Spec:
```
Portrait of a musician, shot with Canon EOS R5 and 85mm f/1.4 at f/2.0, 
shallow depth of field, studio lighting
```

This tells Mystic: shallow depth of field, professional quality, portrait aesthetic.

---

## Negative Prompts Strategy

### Why Negative Prompts Matter

Better to refine with negatives than clutter the main prompt.

### Essential Negatives Template

**For Photorealism:**
```
cartoon, illustration, painting, drawing, anime, CGI, 3D render, artificial, 
over-processed, oversaturated, plastic skin
```

**For Portraits:**
```
cartoon, deformed face, asymmetrical eyes, extra fingers, missing fingers, 
disfigured hands, blurry, low quality, bad anatomy
```

**For Illustrations (Flexible variant):**
```
photorealistic, photograph, overly dark, muddy colors, dull, boring composition
```

**For Cinematic (Fluid variant):**
```
static, flat lighting, amateur, low quality, distorted, warped
```

### Variant-Specific Negatives

**Standard (Realism):**
- Add: "oversaturated, HDR, over-processed"
- Goal: Keep natural look

**Flexible:**
- Add: "dull, desaturated, muted colors"
- Goal: Maintain vivid look but avoid muddy

**Fluid:**
- Add: "inconsistent style, jarring composition"
- Goal: Maintain cinematic consistency

---

## Custom Characters (LoRA) - Standard Only

### CRITICAL: Only works with Standard (realism) variant

**If you switch to Flexible or Fluid, LoRAs are silently disabled.**

### Training Custom Characters

**Requirements:**
- 5-15 reference images of character
- Consistent lighting preferred
- Multiple angles helpful
- Clear, high-quality images

**Training Process:**
1. Upload reference images to Freepik
2. Train Custom Character LoRA
3. Name your character (e.g., "sarah_detective")
4. Wait for training completion

### Using Custom Characters

**Basic syntax:**
```
@sarah_detective in noir office examining evidence
```

**With strength adjustment:**
```
@sarah_detective::80 in noir office examining evidence
```

**Strength guidelines:**
- Default: 100
- Recommended: 80 (best results per community)
- Higher (150-200): Stronger adherence, less variation
- Lower (40-60): More variation, character hints

### ✅ Good Character Prompt:
```
@sarah_detective::80 walking through rain-soaked city street at night, 
trench coat and fedora, noir aesthetic, shot with ARRI Alexa

Negative: cartoon, bright colors, smooth skin

Variant: Standard (realism)
Engine: Sharpy
Creative Detailing: 40
```

---

## Avoiding Common Mistakes

### Mistake 1: Using "Background"

**Problem:** The word "background" causes blurriness in that area.

❌ Bad: `Portrait with blurred background`  
✅ Good: `Portrait with soft bokeh behind subject`

---

### Mistake 2: Contradictory Terms

**Problem:** Confuses the model.

❌ Bad: `Light winter clothes` (contradictory)  
✅ Good: `Light jacket in winter setting`

❌ Bad: `Bright dark scene`  
✅ Good: `Brightly lit scene` or `Dark moody scene`

---

### Mistake 3: Specifying Technical Details in Prompt

**Problem:** Wastes prompt space, set via parameters instead.

❌ Bad: `High quality 4K resolution professional photograph`  
✅ Good: Set resolution to 4K in parameters, remove from prompt

❌ Bad: `Ultra detailed sharp focus 300 DPI`  
✅ Good: Adjust Creative Detailing parameter

---

### Mistake 4: Words Ending in '-tly'

**Problem:** Often unnecessary and can confuse the model.

❌ Avoid: `perfectly`, `beautifully`, `expertly`  
✅ Better: Direct description of what you want

❌ Bad: `beautifully lit portrait`  
✅ Good: `soft natural lighting, flattering portrait`

---

### Mistake 5: Using Prompt Enhancer with Detailed Prompts

**Problem:** AI expansion can conflict with your intent.

**When to use Prompt Enhancer:**
- ✅ Simple, vague prompts: "a dog", "sunset", "portrait"

**When NOT to use:**
- ❌ Already detailed prompts with specific requirements
- ❌ When using Custom Characters
- ❌ When precise control is needed

---

### Mistake 6: Re-prompting for Face/Hand Issues

**Problem:** Generates entirely new image instead of fixing.

**Correct approach:**
1. Generate image
2. Use **Retouch** tool to fix specific face/hand area
3. Or use **Upscale** with "none" imagination level

**Don't:** Regenerate with `Negative: deformed hands, bad face`

**The tools exist specifically for fixing anatomy issues.**

---

## Creative Detailing Parameter Strategy

### Understanding the Scale (0-100)

**Low (0-30):**
- Less detail per pixel
- Softer, more natural
- Less "AI look"
- Use for: Minimalist, soft aesthetics

**Medium (30-50) - Recommended Default:**
- Balanced detail
- Natural but refined
- Sweet spot for most use cases
- Use for: Photography, general illustrations

**High (50-70):**
- High detail per pixel
- More saturated/HDR
- "Polished" look
- Use for: Fantasy, vivid illustrations

**Very High (70-100):**
- Maximum detail
- Risk of artifacts (misplaced eyes, etc.)
- Over-processed look
- Use sparingly: Specific technical needs only

### Variant-Specific Recommendations

**Standard (Realism):**
- Portrait photography: 33-40
- Product photography: 40-50
- Landscapes: 30-45

**Flexible:**
- Fantasy illustrations: 45-60
- Branding/logos: 50-65
- Vibrant scenes: 40-55

**Fluid:**
- Cinematic frames: 33 (default, don't change)
- Storyboards: 30-40

---

## Engine Selection Guide

### Automatic (Default)

**When to use:**
- Unsure which engine to pick
- General-purpose work
- Let system optimize

**Result:** System selects best engine for your prompt/model combination.

---

### Illusio (Soft & Smooth)

**When to use:**
- Landscapes
- Nature scenes
- Soft illustrations
- Dreamy aesthetics

**Aesthetic:** Smoother, softer, less grain

**Example:**
```
Misty forest at dawn, soft light filtering through trees, peaceful atmosphere

Variant: Standard or Zen
Engine: Illusio
Creative Detailing: 30
```

---

### Sharpy (Maximum Detail)

**When to use:**
- Photography
- Product shots
- Portraits (when detail needed)
- Hyper-realistic scenes

**Aesthetic:** Sharpest details, photographic grain

**Example:**
```
Product shot of luxury watch on black velvet, studio lighting, sharp details, 
shot with Phase One XF

Variant: Standard or Super Real
Engine: Sharpy
Creative Detailing: 45
```

---

### Sparkle (Balanced)

**When to use:**
- Versatile middle ground
- Realism with some smoothness
- General photography
- When unsure between Illusio/Sharpy

**Aesthetic:** Balanced sharpness and smoothness

**Example:**
```
Portrait of entrepreneur in modern office, natural window light, professional

Variant: Standard
Engine: Sparkle
Creative Detailing: 40
```

---

## Fixed Generation Parameter

### What It Does

When enabled, identical settings produce identical images (deterministic output).

### When to Enable

**Always enable for:**
- Iterative fine-tuning (testing small prompt changes)
- A/B testing different parameters
- Batch work requiring consistency
- Production workflows

**Disable for:**
- Exploring variations
- Creative exploration
- One-off generations

---

## Aspect Ratio Strategy

### Most Common Ratios

**Square (1:1):**
- Social media posts
- Profile pictures
- Product shots

**Landscape (16:9, 4:3):**
- Banners
- YouTube thumbnails
- Presentations

**Portrait (9:16, 3:4):**
- Instagram Stories
- Phone wallpapers
- Vertical video frames

**Cinematic (21:9, 2.35:1):**
- Widescreen storyboards
- Cinematic frames for Fluid variant

### Variant Compatibility

- **Standard:** All ratios supported
- **Flexible:** All ratios supported
- **Fluid:** All ratios supported (best for cinematic 16:9, 21:9)

---

## Multi-Shot Consistency (Fluid Variant)

### Why Fluid for Sequences

Fluid excels at maintaining visual consistency across multiple related images.

### Workflow for Image Sequences

**Step 1:** Plan shot progression
```
Shot 1: Wide establishing
Shot 2: Medium action
Shot 3: Close-up detail
```

**Step 2:** Use consistent parameters
- Same Creative Detailing value
- Same Engine
- Same Resolution
- Enable Fixed Generation

**Step 3:** Generate with Fluid variant
```
Shot 1 Prompt: Wide shot of detective office, desk cluttered with files, 
window with venetian blinds, noir aesthetic

Shot 2 Prompt: Medium shot of detective examining photograph at desk, 
harsh desk lamp, noir aesthetic

Shot 3 Prompt: Close-up of detective's hands holding old photograph, 
harsh desk lamp, noir aesthetic

Variant: Fluid
Engine: Automatic
Creative Detailing: 33
Fixed Generation: Enabled
```

**Result:** Visually consistent sequence ready for video conversion

---

## Quick Reference Checklist

Before generating with Mystic 2.5:

- [ ] **Variant selected** based on use case (Standard/Flexible/Fluid)
- [ ] **Prompt is concise** and direct (not overly long)
- [ ] **No contradictory terms** in prompt
- [ ] **No technical specs** in prompt text (use parameters)
- [ ] **Camera spec included** (if photorealism)
- [ ] **Negative prompt** prepared for refinement
- [ ] **Engine selected** appropriately (or Automatic)
- [ ] **Creative Detailing** set for aesthetic needs
- [ ] **Resolution** appropriate for use case
- [ ] **Fixed Generation** enabled if iterating
- [ ] **LoRA compatibility** checked (Standard only)

---

## Template Library

### Photorealistic Portrait:
```
Prompt: [Age/gender] [occupation], [clothing], [expression], shot with 
[camera] and [lens], [lighting setup]

Negative: cartoon, deformed, asymmetrical, extra fingers, blurry

Variant: Standard (or Editorial Portraits for close-up)
Engine: Sharpy
Creative Detailing: 35-45
Resolution: 2K or 4K
```

### Fantasy Illustration:
```
Prompt: [Subject] [action] in [fantastical environment], [art style], 
[color palette], [mood]

Negative: photorealistic, dull, desaturated, boring

Variant: Flexible
Engine: Automatic or Sparkle
Creative Detailing: 45-60
Resolution: 2K
```

### Cinematic Frame:
```
Prompt: [Shot type] of [subject] [action], [environment], cinematic, 
shot with [cinema camera]

Negative: static, flat, amateur, low quality

Variant: Fluid
Engine: Automatic
Creative Detailing: 33
Resolution: 2K
Fixed Generation: Enabled (for sequences)
```

### Product Photography:
```
Prompt: [Product] on [surface/background], [lighting setup], shot with 
[camera], commercial photography

Negative: cartoon, cluttered, busy, low quality

Variant: Standard or Super Real
Engine: Sharpy
Creative Detailing: 40-50
Resolution: 4K
```

---

**Pro Tip:** Start with variant defaults (Standard: 33 creative detailing, Sharpy engine, 2K resolution) and only adjust if needed. Mystic's defaults are well-tuned for most use cases.
