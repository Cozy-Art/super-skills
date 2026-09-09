---
name: freepik-mystic-2-5-prompts
description: Generate optimized prompts for Freepik Mystic 2.5 image generation across its Standard, Flexible and Fluid variants, with 1K/2K/4K output and LoRA-based Custom Characters and Styles. Use this skill whenever a user mentions Mystic, Freepik Mystic, or wants prompts for photorealistic imagery on this model. Also trigger for requests involving trained character LoRAs addressed by name. Always use this skill instead of guessing at Mystic prompt structure from general knowledge — it rewards concise prompts where most models reward detail, and its variants differ in what they support.
---

# Freepik Mystic 2.5 - Prompt Generation Skill

## Model Overview

Freepik Mystic 2.5 is an advanced AI image generation system built on Flux foundations with Magnific.ai technology. The 2.5 family includes three primary variants (Standard, Flexible, Fluid) plus three API-only sub-models, each optimized for specific use cases. Known for exceptional prompt adherence, photorealism capabilities, and LoRA compatibility (Standard variant only).

**Platform:** Freepik Studio / Freepik API  
**Technology:** Flux (12B parameters) + Stable Diffusion + Magnific.ai upscaling

---

You are a prompt engineer specializing in Freepik Mystic 2.5, an advanced image generation platform with multiple variant models. Your role is to craft concise, direct prompts that leverage each variant's unique strengths: Standard (realism + LoRA), Flexible (vivid colors + prompt adherence), and Fluid (cinematic consistency + speed).

### Core Principles

1. **Concise, direct language over lengthy descriptions** - Mystic excels with focused prompts
2. **Let the model variant handle the heavy lifting** - Standard for realism, Flexible for fantasy, Fluid for cinematic
3. **Avoid style keywords in prompts** - Use UI style selector or LoRA styles instead
4. **Negative prompts for refinement** - Better than cluttering main prompt
5. **Camera/lighting specs enhance photorealism** - Especially for Standard/Super Real variants

### The Three Primary Variants

**Mystic 2.5 (Standard) - `realism` model:**
- Most versatile, natural color palette
- LoRA compatible (Custom Characters/Styles)
- "Less AI look" than competitors
- Best for: Photography, natural scenes, illustrations with LoRA
- Credits: 50/image

**Mystic 2.5 Flexible - `flexible` model:**
- Best prompt adherence in the family
- Vivid, saturated colors (HDR look)
- No LoRA support
- Best for: Illustrations, fantasy, branding, specific visual styles
- Credits: 80/image

**Mystic 2.5 Fluid - `fluid` model:**
- Fastest generation, smoothest visuals
- Excellent consistency for cinematic frames
- Over-moderated (Google Imagen 3 backend, some words flagged)
- Best for: Cinematic stills, campaigns, high-volume production
- Credits: 80/image

### API-Only Sub-Models

**Zen (`zen`):**
- Smoother, cleaner results with fewer objects
- Minimalist aesthetic
- Best for: Minimalist compositions, soft aesthetics

**Super Real (`super_real`):**
- Hyper-realism with sharp details
- Weaker for close-ups than editorial_portraits
- Best for: Medium shots, realistic photography

**Editorial Portraits (`editorial_portraits`):**
- Unmatched realism for close-up portraits
- Requires extremely long, detailed prompts
- Anatomical issues in wide/distant shots
- Best for: Close-up and medium portrait shots

---

## Mystic 2.5-Specific Capabilities

### Character References
- Syntax: `@character_name` in prompt
- Adjustable strength: `@character_name::strength` (e.g., `@john::200`)
- Character strength ~80% produces best results
- Only works with `realism` model (LoRA-compatible)

### Permutation Prompts
- Use pipe syntax: `a black cat|a red cat|a yellow cat`
- Generates multiple variants in one request

### AI Prompt Enhancement
- Toggle "AI prompt" to auto-expand short prompts
- Example: "A dog" → "A black German Shepherd standing alert on a rocky hilltop with a panoramic view of a valley during sunset"
- Avoid when prompt is already detailed

### Fixed Generation
- Enable for identical outputs with same settings
- Essential for iterative fine-tuning
- Deterministic results for consistent workflows

### Resolution Options
- 1K (1024px): 10-20s generation
- 2K (2048px): 20-40s generation (recommended)
- 4K (4096px): 40-90s generation
- Output: PNG format

### Engine Options (Upscaling Pipeline)
- **Automatic**: System selects best (default)
- **Illusio** (`magnific_illusio`): Smoother illustrations, landscapes, softer look
- **Sharpy** (`magnific_sharpy`): Sharpest details, best for photographs
- **Sparkle** (`magnific_sparkle`): Middle ground, good for realism

---

## Best Practices from Freepik

### Official Guidelines (DO):
- ✅ Use concise, direct prompts
- ✅ Use negative prompts for intricate details
- ✅ Specify camera models for photorealism (Canon EOS R5, ARRI Alexa)
- ✅ Fix faces/hands with Retouch or Upscale tools
- ✅ Character reference strength ~80% for best results

### Official Guidelines (DON'T):
- ❌ Don't use lengthy descriptions
- ❌ Don't include contradictory terms (e.g., "light winter clothes")
- ❌ Don't specify styles in prompts (use UI selector)
- ❌ Don't specify pixels, sizes, or quality in text
- ❌ Don't mention final usage ("for website header")
- ❌ Avoid "Prompt Enhancer" with detailed prompts
- ❌ Avoid words ending in '-tly' unless necessary
- ❌ Avoid the word "background" (causes blurriness)

---

## Parameter Strategy

### Creative Detailing (0-100)
- Default: 33
- Higher: More detail per pixel but more HDR/artificial
- Very high: Causes artifacts like misplaced eyes
- Recommended: 33-50 for realism, 40-60 for fantasy

### Adherence (0-100)
- Default: 50
- Higher: More faithful to prompt
- Lower: More creative, closer to style reference
- Use with style transfer

### HDR (0-100)
- Default: 50
- Higher: More detailed but more "AI look"
- Lower: More natural/artistic
- Balance with creative detailing

---

## Related Files

- [parameters.json](parameters.json) - Complete specifications: variants, engines, resolutions, numeric ranges
- [best-practices.md](best-practices.md) - Variant-specific optimization, camera specs, negative prompt templates
- [examples/standard-realism.md](examples/standard-realism.md) - Standard variant examples with LoRA usage
- [examples/flexible-vivid.md](examples/flexible-vivid.md) - Flexible variant examples with illustrations/fantasy
- [examples/fluid-cinematic.md](examples/fluid-cinematic.md) - Fluid variant examples with consistency focus
- [examples/api-submodels.md](examples/api-submodels.md) - Zen, Super Real, Editorial Portraits examples

---

## Important Notes

**Key Differences from Competitors:**

**vs Midjourney v7:**
- ✅ **Resolution advantage** - 1K/2K/4K vs MJ's 1024x1024
- ✅ **LoRA support** - Custom Characters/Styles (Standard only)
- ✅ **Photorealism** - Better for realistic photography
- ❌ **Prompt length** - Concise required vs MJ's 20-60 words
- ❌ **Artistic range** - MJ stronger for pure artistic styles

**vs Gemini 3 Pro:**
- ✅ **Three specialized variants** - vs Gemini's single model
- ✅ **LoRA customization** - Custom Characters/Styles
- ❌ **Reference images** - No multi-reference like Gemini's 14
- ❌ **Text rendering** - Neither excels at in-image text

**Platform:**
- Web interface: freepik.com/ai/image-generator
- API available with various endpoints
- Premium+/Pro plans: Unlimited generation (excluding LoRA training)
- Built on Flux (12B parameters) + Magnific.ai

**Common Issues:**
- **Face/hand distortion**: Use Retouch or Upscale tools, not re-prompting
- **LoRA compatibility**: Only Standard (realism) supports Custom Characters/Styles
- **"Background" keyword**: Causes blurriness, avoid in prompts
- **Over-moderation (Fluid)**: Words like "war" may be flagged (Google Imagen 3 backend)

**Technology Stack:**
- Flux foundation (Black Forest Labs, 12B parameters)
- Stable Diffusion processes
- Magnific.ai upscaling technology
- Developed with input from photographers, VFX specialists, digital artists

**Credit Costs:**
- Standard: 50 credits/image
- Flexible: 80 credits/image
- Fluid: 80 credits/image
- Premium+/Pro: Unlimited (excluding LoRA training costs)

**Post-Generation Tools:**
- Upscale: Enhance resolution, adjust imagination level
- Reimagine: Create variations preserving composition
- Expand: Outpaint/extend boundaries
- Retouch: Selective editing
- Video: Convert to AI video
- Mockup: Product placement

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
