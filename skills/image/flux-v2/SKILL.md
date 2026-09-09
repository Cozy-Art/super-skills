---
name: flux-2-prompts
description: Generate optimized prompts for Black Forest Labs FLUX.2 image generation, covering text-to-image, multi-reference editing and JSON structured prompting. Use this skill whenever a user mentions FLUX, Flux 2, or BFL image generation, or wants prompts involving multiple reference images with explicit per-image roles, photographic control, or in-image text rendering. Always use this skill instead of guessing at FLUX prompt structure from general knowledge — BFL binds multiple references through bare natural-language ordinals rather than any sigil or bracket, and its JSON structured prompting is pasted into the single prompt string rather than sent as a separate request field.
---

# Flux 2 Image Generation Prompt Formatter

## Purpose

Converts structured scene, shot, and character data into optimized Flux 2 image generation prompts. Flux 2 is a family of models spanning from sub-second generation (Klein) to maximum quality (Max), all sharing a core architecture with exceptional prompt following, photorealistic rendering, hex color precision, and multi-reference image support.

This SKILL handles **variant selection** — choosing the right Flux 2 model for the task — as well as generating optimized prompts. The variant matters because each has different strengths, parameter support, and cost profiles.

This SKILL outputs two formats:
1. **Human-readable description** — Natural language for director review and copy-paste into platforms (Freepik, ComfyUI, Weavy, BFL Playground)
2. **Structured JSON** — Machine-readable format for API integrations (BFL API, Replicate, Fal.ai, Together AI)

---

## Variant Selection Guide

### The Family at a Glance

| Variant | Best For | Speed | Quality | Multi-Ref | Cost | Key Differentiator |
|---------|----------|-------|---------|-----------|------|-------------------|
| **Pro** | Production work at scale | Fast (<10s) | Excellent | Up to 8 images | $$ | Best quality-to-cost ratio |
| **Max** | Maximum quality, grounding search | Fast | Highest | Up to 10 images | $$$$ | Web grounding, best consistency |
| **Flex** | Typography, fine details, developer control | Medium | High | Up to 8 images | $$$ | Adjustable steps + guidance |
| **Klein 9B** | Fast iteration, real-time apps | Sub-second | Good+ | Up to 4 images | $ | Open weights, local GPU |
| **Klein 4B** | Highest volume, consumer GPU | Sub-second | Good | Up to 4 images | $ | Apache 2.0, 13GB VRAM |
| **Kontext** | Character consistency, iterative editing | Fast | High | 1 reference | $$ | Identity preservation across scenes |

### When to Use Each Variant

**Use Pro when:**
- Generating final production stills, storyboard frames, or character references
- You need the best balance of quality, speed, and cost
- Multi-reference compositing (up to 8 images)
- Most workflows default here

**Use Max when:**
- You need absolute best quality and consistency
- Grounding search is useful (real-world product visualization, current styles)
- Maximum multi-reference support (up to 10 images)
- Character consistency is critical and cost is secondary
- Complex multi-reference compositing

**Use Flex when:**
- Text or typography must appear in the image (signs, screens, titles, posters)
- You need fine control over steps and guidance scale
- Developer/pipeline integration requiring parameter tuning
- Illustrations or stylized renders where you want to dial in the look

**Use Klein (9B) when:**
- Rapid iteration and concept exploration
- Real-time preview in ComfyUI or interactive tools
- Good quality needed but speed is priority
- Budget-conscious high-volume generation

**Use Klein (4B) when:**
- Highest volume batch generation
- Running locally on consumer GPU (13GB VRAM)
- Prototyping and rough concept art
- LoRA training and fine-tuning workflows

**Use Kontext when:**
- Maintaining character identity across multiple scenes
- Iterative editing: step-by-step refinement of a single image
- Style transfer while preserving character features
- "Same character, different scene" workflows

---

```
You are an expert Flux 2 prompt engineer working within a film production pipeline. Your task is to convert structured scene and shot data into optimized Flux 2 image generation prompts, selecting the appropriate Flux 2 variant for the task.

CRITICAL RULES FOR FLUX 2:

1. VARIANT SELECTION: Always recommend a specific Flux 2 variant based on the task:
   - Pro: Default for most production work (stills, storyboards, character refs)
   - Max: When maximum quality or multi-reference consistency is critical
   - Flex: When text/typography appears in the image, or fine parameter control is needed
   - Klein: When speed matters more than maximum quality (iteration, previews)
   - Kontext: When maintaining character identity across scenes

2. FRONT-LOAD KEY CONCEPTS: The first 5-10 words carry the most weight. Place the most important visual element first. Structure: most important → supporting details → atmosphere.

3. OPTIMAL LENGTH: 12-25 words for simple prompts. Up to 512 tokens (T5 encoder) for complex scenes. Shorter is almost always better with Flux 2.

4. NO NEGATIVE PROMPTS: Flux 2 does NOT support negative prompts. Describe ONLY what you want. Never use "no," "without," "avoid," or exclusions in the prompt text.
   - Instead of "no blur" → "sharp focus throughout"
   - Instead of "no people" → "empty scene"
   - Instead of "no artifacts" → "clean, detailed rendering"

5. CAMERA AND LENS SPECIFICITY: Flux 2 responds exceptionally well to specific photographic language. Always specify camera model, lens, and film stock when the shot calls for realism:
   - "Shot on Sony A7IV, 85mm f/1.4, shallow depth of field"
   - "Shot on Fujifilm X-T5, 35mm f/1.4, natural grain"
   - "Kodak Portra 400 film, warm organic colors, natural grain"
   - "Early digital camera, slight noise, flash photography, 2000s digicam style"

6. HEX COLOR PRECISION: Flux 2 supports exact color matching via hex codes. Always link colors to specific objects:
   - "The car is #FF0000"
   - "Her dress is color #1E3A5F"
   - "Background gradient starting with #02eb3c finishing with #edfa3c"
   NEVER apply hex codes to the entire scene — always bind them to specific objects.

7. JSON STRUCTURED PROMPTS: For complex scenes with multiple subjects, use JSON format. Flux 2 natively understands JSON prompts:
   ```json
   {
     "scene": "description",
     "subjects": [{"description": "...", "position": "...", "action": "..."}],
     "style": "...",
     "lighting": "...",
     "camera": {"angle": "...", "lens": "...", "depth_of_field": "..."}
   }
   ```

8. MULTI-REFERENCE IMAGES: When reference images are provided, point to specific images by index:
   - "Use the character from image 1, the background from image 2, and the lighting style from image 3"
   - Pro/Max/Flex: Up to 8-10 reference images
   - Klein: Up to 4 reference images

9. STYLE ERA ANCHORING: For photorealistic results, anchor to a specific photographic era and equipment:
   - Modern digital: "shot on Sony A7IV, clean sharp, high dynamic range"
   - 2000s digicam: "early digital camera, slight noise, flash photography, candid"
   - 80s vintage: "film grain, warm color cast, soft focus, 80s vintage photo"
   - Analog film: "shot on Kodak Portra 400, natural grain, organic colors"

10. FLEX-SPECIFIC: When outputting for Flex variant, include recommended steps and guidance values:
    - Low steps (6-10): Fast previews, good for iteration
    - Medium steps (20-30): Good balance of quality and speed
    - High steps (40-50): Maximum quality, best typography rendering
    - Guidance: 3.0-5.0 (creative freedom) to 7.0-10.0 (strict prompt adherence)

OUTPUT FORMAT:

Return EXACTLY two sections:

HUMAN_READABLE:
[A natural language prompt optimized for copy-paste into Flux 2 interfaces. For simple shots, keep to 12-25 words. For complex scenes, use up to 50-75 words in flowing prose. Include a note indicating which variant to use.]

JSON:
[A valid JSON object following the Flux 2 schema, with the recommended variant specified and all applicable parameters. For complex scenes, use the JSON structured prompt format within the prompt field.]
```

---

## Model Specification

### Generation Type
**Image generation** (text-to-image, image-to-image editing, multi-reference compositing, character consistency via Kontext)

### Output Format
- PNG (default, highest quality)
- JPEG
- WebP

### Prompt Length Limits
- **CLIP encoder:** 77 tokens (warning can be safely ignored — T5 handles overflow)
- **T5 encoder:** 512 tokens (256 for Schnell/Klein distilled variants)
- **Optimal:** 12-25 words for best results
- **Maximum effective:** ~512 tokens for complex JSON prompts
- **Weight priority:** First 5-10 words carry the most influence

### Required Fields
| Field | Type | Description |
|-------|------|-------------|
| `prompt` | string | Natural language or JSON structured prompt |

### Core Optional Fields
| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `variant` | string | "pro" | Flux 2 variant: "pro", "max", "flex", "klein_9b", "klein_4b", "kontext" |
| `width` | integer | 1024 | Output width (multiple of 16, max 4MP total) |
| `height` | integer | 1024 | Output height (multiple of 16, max 4MP total) |
| `aspect_ratio` | string | "1:1" | Aspect ratio: "1:1", "16:9", "9:16", "4:3", "3:4", "21:9" |
| `seed` | integer | null | Seed for reproducibility |
| `guidance` | float | 4.5 | [Flex only] Prompt adherence: 1.5-10.0 |
| `steps` | integer | 50 | [Flex only] Inference steps: 1-50 |

### Multi-Reference Fields
| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `image_urls` | array | [] | Reference images (Pro/Max/Flex: up to 8-10; Klein: up to 4) |
| `image_prompt` | string | null | [Kontext] Reference image for character consistency |

### Resolution Limits by Variant
| Variant | Min | Max | Default | Notes |
|---------|-----|-----|---------|-------|
| Pro | 64×64 | 4MP | 1024×1024 | Any aspect ratio |
| Max | 64×64 | 4MP | 1024×1024 | Any aspect ratio, grounding search |
| Flex | 64×64 | 4MP | 1024×1024 | Adjustable steps + guidance |
| Klein | 64×64 | ~1MP | 1024×1024 | Optimized for speed |
| Kontext | — | 1024×1024 | 1024×1024 | Aspect ratio presets |

### Multi-Reference Capacity
| Variant | Max References | Total Input Capacity |
|---------|--------------|---------------------|
| Pro | 8 images | 9MP (input + output) |
| Max | 10 images | 9MP |
| Flex | 8 images | 9MP |
| Klein | 4 images | Limited |
| Kontext | 1 image | Single reference |

---

## Prompt Engineering Best Practices

### Do's
1. **Front-load key concepts** — The first 5-10 words dominate. "Photorealistic portrait of a woman in a garden" beats "In a garden there is a woman for a photorealistic portrait"
2. **Use specific camera language** — "Shot on Canon 5D Mark IV, 85mm f/1.8" dramatically outperforms "professional photo"
3. **Use hex codes for brand colors** — "#FF5733 jacket" not "orange-red jacket"
4. **Keep it short** — 12-25 words for most prompts. Only use longer prompts for genuinely complex scenes
5. **One variable per iteration** — When refining, change only one element at a time
6. **Add lighting modifiers last** — Flux distinguishes lighting strongly; place after subject and scene
7. **Use JSON for multi-subject scenes** — Structured prompts give better spatial control
8. **Specify film stock for era-specific looks** — "Kodak Portra 400" vs generic "film look"
9. **Use seed values** for reproducibility and minor variations (±1-5 seed difference)
10. **Reference images by index** when using multi-reference: "character from image 1"

### Don'ts
1. **NEVER use negative prompts** — Flux ignores them completely. No "no," "without," "avoid," "don't"
2. **Don't bury important concepts** — Concepts after the first 10 words get progressively less weight
3. **Don't use generic descriptors** — "beautiful" and "professional" are near-meaningless; be specific
4. **Don't overstuff** — A 200-word prompt will perform worse than a focused 20-word prompt
5. **Don't mix incompatible eras** — "Shot on iPhone 15, vintage 1970s Polaroid" creates confusion
6. **Don't apply hex colors to the whole scene** — Always bind to specific objects
7. **Don't ignore the variant choice** — Using Klein for a final production render wastes potential; using Max for quick iteration wastes budget

### Model-Specific Tips

**Pro Tips:**
- Best default overall. Use for everything unless you have a specific reason for another variant.
- Multi-reference compositing works exceptionally well for maintaining character across scenes.

**Max Tips:**
- Grounding search lets you reference real-world products, current fashion, and trending styles without providing reference images.
- Best character consistency across complex edits with changing environments.
- Worth the cost premium for hero shots and key frames.

**Flex Tips:**
- Typography sweet spot: 40-50 steps with guidance 7-8 for clean, legible text.
- For illustration styles, lower guidance (3-4) gives more creative freedom.
- Steps control is powerful: 6 steps for quick preview, 50 for final render — same prompt, vastly different results.
- Freepik labels this as good for illustration work — lower guidance with artistic style prompts produces painterly, expressive results.

**Klein Tips:**
- Perfect for ComfyUI iteration workflows: generate 20 variations in the time Max generates 1.
- Klein 4B Base supports LoRA training — train custom styles on your project's visual language.
- Don't use prompt upsampling (Klein doesn't include it) — write detailed, descriptive prompts directly.

**Kontext Tips:**
- Upload your character reference, then describe only what changes (new scene, new pose, new outfit).
- Works as iterative editing: generate → refine → generate → refine in steps.
- Best for "same face, different scene" workflows across a film project.

---

## Common Issues & Solutions

### Issue: Important details ignored in long prompts
**Solution:** Flux heavily weights the first 5-10 words. Restructure: put the most critical element first. If you need a complex scene, switch to JSON structured prompts where each element is explicitly positioned.

### Issue: Colors don't match brand guidelines
**Solution:** Use hex codes bound to specific objects: "The logo is #1A73E8, the background is #F8F9FA." Don't use generic color names for precision work.

### Issue: Text in image is garbled
**Solution:** Switch to Flex variant. Set steps to 40-50 and guidance to 7-8. Place the text instruction early in the prompt. Keep text to 3-5 words. Example: "A neon sign reading 'OPEN 24 HOURS' in a rainy alley"

### Issue: Character looks different across generations
**Solution:** Use Kontext for identity preservation across scenes. Or use Pro/Max with multi-reference: upload the anchor image and reference it explicitly. Keep the character description identical word-for-word across prompts. Use the same seed range.

### Issue: Results feel generic despite detailed prompts
**Solution:** Anchor to specific photographic equipment: "Shot on Hasselblad X2D, 90mm f/3.2" instantly adds authentic character. Add film stock: "Kodak Ektar 100" for vivid, or "Ilford HP5" for dramatic B&W.

### Issue: Flux ignoring my negative prompt
**Solution:** Flux 2 has NO negative prompt support. Remove all negations. Rephrase everything as positive: describe what you want, not what you don't want.

### Issue: Multi-reference results are muddy or confused
**Solution:** Be explicit about which image provides which element: "Use the face from image 1, the outfit from image 2, and the background from image 3." Don't exceed the reference limit for your variant.

---

## JSON Structured Prompting (Advanced)

For complex scenes with multiple subjects, Flux 2 natively understands JSON prompts. This is especially powerful with Pro and Max variants.

### Basic Structure
```json
{
  "scene": "overall environment description",
  "subjects": [
    {
      "description": "detailed subject description",
      "position": "where in the frame",
      "action": "what they're doing",
      "color_palette": ["#hex1", "#hex2"]
    }
  ],
  "style": "artistic or photographic style",
  "lighting": "lighting description",
  "mood": "emotional tone",
  "background": "background details",
  "composition": "framing and layout",
  "camera": {
    "angle": "camera angle",
    "lens": "lens specification",
    "depth_of_field": "focus behavior"
  }
}
```

### When to Use JSON vs Natural Language
- **Natural language:** Simple scenes, single subjects, quick iteration, copy-paste into UI platforms
- **JSON:** Multi-subject scenes, precise positioning, hex color control, pipeline automation, API integrations

---

## Continuity Workflows

### Character Consistency Across Scenes (Kontext)
1. Generate anchor portrait of character using Pro/Max
2. Switch to Kontext variant
3. Upload anchor as reference image
4. Prompt describes only the new scene: "Same woman standing on a rooftop at sunset, wind in her hair"
5. Kontext preserves identity while changing environment

### Character Consistency via Multi-Reference (Pro/Max)
1. Generate anchor portrait (use as reference image 1)
2. Generate or source environment image (reference image 2)
3. Prompt: "Place the woman from image 1 into the scene from image 2, maintaining her exact appearance. Adapt lighting to match the environment."

### Style Consistency Across a Project
1. Establish a "style anchor" image that defines the project's visual language
2. Include this as a reference image in every generation
3. Keep camera/lens specifications identical across all prompts
4. Use seed ranges (e.g., seeds 1000-1100) for subtle variation within consistency

## Reference Files

Load these when you need depth on a specific topic:

- [schema.json](schema.json) — Output validation schema for the Flux 2 prompt object: required `prompt` and `variant` fields, the per-variant enums, and the JSON structured-prompt shape.
- [examples.json](examples.json) — Six annotated input/output pairs across the family: character reference lead portrait (Pro), cinematic storyboard wide (Max), typography-heavy evidence board (Flex), fast concept variations (Klein 9B), identity preservation across scenes (Kontext), and a complex multi-subject JSON structured prompt (Pro).

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
