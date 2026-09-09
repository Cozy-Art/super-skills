---
name: seedream-4-5-prompts
description: Generate optimized prompts for ByteDance Seedream 4.5 image generation, covering text-to-image, reference-based generation, multi-image compositing and instruction-based editing with guidance-scale and negative-prompt control. Use this skill whenever a user mentions Seedream 4, Seedream 4.5, or wants prompts on this tier rather than Seedream 5. Also trigger for requests involving in-image text rendering or multi-image workflows. Always use this skill instead of guessing at Seedream prompt structure from general knowledge — 4.5 and 5.0 differ in whether a reasoning layer is present, which changes how much the prompt must spell out.
---

# Seedream 4.5 Image Generation Prompt Formatter

## Purpose

Converts structured scene, shot, and character data into optimized Seedream 4.5 image generation prompts. Seedream 4.5 excels at photorealistic rendering, superior text rendering in images, multi-image consistency (up to 14 images per generation), and high-resolution output up to 4K. It is particularly strong with natural language prompts and supports advanced multi-reference workflows for character and style consistency.

This SKILL outputs two formats:
1. **Human-readable description** — Natural language for director review and copy-paste into platforms like Freepik, Scenario, or Weavy
2. **Structured JSON** — Machine-readable format for API integrations (BytePlus, Segmind, Scenario, etc.)

---

```
You are an expert Seedream 4.5 prompt engineer working within a film production pipeline. Your task is to convert structured scene and shot data into optimized Seedream 4.5 image generation prompts.

CRITICAL RULES FOR SEEDREAM 4.5:

1. USE NATURAL LANGUAGE: Write coherent, descriptive sentences — NOT comma-separated keyword lists. Seedream 4.5 has strong natural language understanding and performs better with fluent prose than keyword stacking.

2. PROMPT LENGTH: Keep prompts between 50-200 words (under 600 words maximum). Concise, focused prompts outperform verbose ones. Excessively long prompts scatter the model's attention.

3. SUBJECT-FIRST STRUCTURE: Always lead with the main subject, then layer in environment, lighting, and style. Follow this priority order:
   - Subject (who/what) + Action/State (doing what)
   - Environment/Setting (where)
   - Lighting conditions (how lit)
   - Style/Aesthetic (what it looks like)
   - Technical details (camera, lens, composition)

4. POSITIVE FRAMING ONLY: Describe what you WANT to see. Do not use negations. If you must exclude elements, use the negative_prompt field in the JSON output — never embed exclusions in the main prompt.

5. LIGHTING IS CRITICAL: Always specify lighting explicitly. Seedream 4.5 renders lighting with high fidelity. Use terms like:
   - "golden hour side lighting"
   - "soft diffused overhead light"
   - "dramatic chiaroscuro with a single key light from the left"
   - "neon-lit with cool blue and magenta spill"

6. CAMERA AND LENS LANGUAGE: When the shot data specifies camera details, translate them into photographic language:
   - Wide shot → "wide-angle lens, 24mm"
   - Medium shot → "50mm standard lens"
   - Close-up → "85mm portrait lens, shallow depth of field"
   - Extreme close-up → "macro lens, extreme shallow depth of field"

7. MULTI-IMAGE CONSISTENCY: When generating for sequences or multi-shot scenes, include consistency anchors:
   - Repeat character descriptions verbatim across prompts
   - Specify "same character" or use reference image instructions
   - Keep lighting and style descriptors identical
   - Use similar seed ranges for related images

8. STYLE SPECIFICITY: Translate structured style data into concrete visual language:
   - "cinematic" → "cinematic photography, anamorphic lens flare, film grain, shallow depth of field"
   - "documentary" → "photojournalistic style, available light, handheld feel, 35mm"
   - "noir" → "high-contrast black and white, deep shadows, venetian blind lighting"
   - "ethereal" → "soft focus, pastel tones, diffused backlight, dreamy atmosphere"

OUTPUT FORMAT:

Return EXACTLY two sections:

HUMAN_READABLE:
[A natural language prompt ready to copy-paste into Seedream 4.5 interfaces. This should be a single flowing paragraph or two short paragraphs, 50-200 words. Written as if describing the image to a photographer.]

JSON:
[A valid JSON object following the Seedream 4.5 schema, with all applicable parameters filled in based on the shot data. Include platform-specific variants when the shot data specifies a target platform.]
```

---

## Model Specification

### Generation Type
**Image generation** (text-to-image, image-to-image, image editing, multi-image consistency)

### Output Format
Seedream 4.5 generates still images in the following formats:
- PNG (default, highest quality)
- JPEG (compressed, faster delivery)
- WebP (web-optimized)

### Prompt Length Limits
- **Recommended:** 50–200 words for optimal results
- **Maximum:** 600 English words (official BytePlus recommendation)
- **Platform ceiling:** Up to 10,000 characters on some platforms (for JSON prompts)
- **Key principle:** Concise natural language > keyword stacking

### Required Fields
| Field | Type | Description |
|-------|------|-------------|
| `prompt` | string | Natural language scene description (50-200 words recommended) |

### Core Optional Fields
| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `negative_prompt` | string | null | Elements to exclude from generation |
| `size` | string | "1K" | Resolution preset: "1K", "2K", "4K", or custom |
| `width` | integer | 1024 | Custom width in pixels (max 4096) |
| `height` | integer | 1024 | Custom height in pixels (max 4096) |
| `aspect_ratio` | string | "1:1" | Aspect ratio: "1:1", "16:9", "9:16", "4:3", "3:4", "21:9" |
| `guidance_scale` | float | 8.0 | Prompt adherence strength (higher = more literal) |
| `steps` | integer | 40 | Inference steps (higher = more refined) |
| `seed` | integer | null | Seed for reproducibility |
| `max_images` | integer | 1 | Number of images to generate (1-15) |

### Multi-Image & Reference Fields
| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `image_urls` | array | [] | Reference images for consistency (max 14) |
| `sequential_image_generation` | string | "disabled" | Batch mode: "disabled" or "auto" |
| `watermark` | boolean | false | Add watermark to output |

### Supported Aspect Ratios
| Ratio | Dimensions (at 1K) | Use Case |
|-------|-------------------|----------|
| 1:1 | 1024×1024 | Social media, portraits |
| 16:9 | 1820×1024 | Widescreen, cinematic stills |
| 9:16 | 1024×1820 | Mobile, vertical content |
| 4:3 | 1182×1024 | Film photography frame |
| 3:4 | 1024×1365 | Portrait orientation |
| 21:9 | 2184×1024 | Ultrawide cinematic |

### API Limits
- **Max prompt length:** 600 words (recommended), 10,000 characters (platform maximum)
- **Max resolution:** 4096×4096 pixels
- **Max reference images:** 14 per generation
- **Max batch size:** 15 images (input + output combined)
- **Max images per generation:** 15

---

## Prompt Engineering Best Practices

### Do's
1. **Write in natural sentences** — "A young woman standing in a sunlit meadow" beats "woman, meadow, sunlight, standing"
2. **Lead with the subject** — Place the main focus in the first sentence
3. **Specify lighting explicitly** — Seedream renders lighting with exceptional fidelity
4. **Use camera/lens language** — "85mm portrait lens, f/2.0, shallow depth of field" dramatically improves realism
5. **Include mood and atmosphere** — "melancholic," "jubilant," "tense" guide the model's aesthetic choices
6. **Use reference images** — Upload examples for character consistency, style matching, and multi-view generation
7. **Leverage seed values** — Use identical or nearby seeds for related images in a sequence
8. **Use negative prompts in the JSON field** — "distorted anatomy, blurry, low quality, text artifacts" for cleaner results
9. **Iterate systematically** — Generate multiple versions, change one variable at a time
10. **Use sequence mode** — Enable for multi-image consistency when generating related shots

### Don'ts
1. **Don't use keyword-only prompts** — Natural language always outperforms keyword spam
2. **Don't overload a single prompt** — Break complex changes into sequential steps (1-2 changes per iteration)
3. **Don't embed negations in the prompt** — Use the negative_prompt field instead
4. **Don't mix incompatible style keywords** — "watercolor photorealistic" confuses the model
5. **Don't exceed 200 words without reason** — Longer prompts scatter the model's attention
6. **Don't ignore reference images** — Always upload context images for editing tasks
7. **Don't expect perfection on first generation** — Plan for 3-5 iterations

### Model-Specific Tips
1. **Text rendering:** Seedream 4.5 has best-in-class text rendering. For text in images, keep it to 3-7 words, specify font style ("bold sans-serif," "elegant script"), and place text instructions early in the prompt.
2. **Multi-image consistency:** Use trigger phrases like "a series of," "a set of images," or "generate multiple images" to activate multi-image mode. Enable sequence mode in supported platforms.
3. **Character consistency across shots:** Establish a detailed character description once, then repeat it verbatim in every prompt. Use reference images when available. Specify "same character" explicitly.
4. **Product photography:** Seedream excels at product shots. Use "Place the product in Picture 1 into the scene in Picture 2 and adapt it to the scene's lighting, shadow, image quality" for compositing.
5. **Resolution strategy:** Generate at 2K for iteration speed, then regenerate finals at 4K. The quality difference is significant at 4K.

---

## Common Issues & Solutions

### Issue: Character appearance drifts between generated images
**Solution:** Create a locked character description block (hair color, skin tone, clothing, distinguishing features) and paste it identically into every prompt. Use reference images and seed values. Enable sequence mode.

### Issue: Prompt seems partially ignored
**Solution:** The prompt is too long or the critical details are buried. Move the most important elements to the first sentence. Keep total prompt under 150 words for best adherence.

### Issue: Style keywords conflict and produce muddy results
**Solution:** Pick ONE primary style direction. Don't mix "watercolor" with "photorealistic" or "anime" with "oil painting." If you need hybrid styles, be very explicit: "digital illustration with oil painting texture overlays."

### Issue: Text in image is garbled or misspelled
**Solution:** Keep text to 3-5 words. Place the text instruction early in the prompt. Specify the exact text in quotes. Use "bold," "clean," "legible" as modifiers. Seedream 4.5 handles text better than most models, but long strings still fail.

### Issue: Multi-image generation produces inconsistent results
**Solution:** Ensure sequential_image_generation is set to "auto." Use identical style descriptors across all images. Upload ALL reference images before generating. Specify which reference is for character, background, and style explicitly.

### Issue: Lighting looks flat or generic
**Solution:** Never rely on default lighting. Always specify light source, direction, quality, and color temperature. "Warm golden hour light from the left, long shadows, slight lens flare" is far better than "good lighting."

---

## Multi-Image Workflow

### Generating Consistent Character Across Multiple Shots

**Step 1: Establish the character**
```
A confident woman in her early 30s with auburn shoulder-length hair, 
warm brown eyes, light freckles across her nose. She wears a navy 
wool peacoat over a cream turtleneck. Photorealistic portrait style, 
85mm lens, soft natural light.
```

**Step 2: Lock the description, change the scene**
```
[SAME CHARACTER BLOCK from Step 1]. She stands at the edge of a rain-soaked 
city bridge at dusk, looking out at the skyline. Cinematic photography, 
35mm lens, neon city lights reflected in wet pavement, moody blue-orange 
color palette.
```

**Step 3: Use reference images**
Upload the Step 1 output as a reference image. In the prompt:
```
Use Image 1 for the character reference. [CHARACTER BLOCK]. She sits in 
a warmly lit café, holding a ceramic coffee mug, smiling softly at someone 
off-camera. Medium shot, 50mm lens, warm ambient lighting from overhead 
fixtures, shallow depth of field.
```

### Multi-Reference Syntax
```
Use Image 1 for the character, Image 2 for the background, and apply 
the style from Image 3.
```

### Multi-View Generation
```
Refer to this image, generate three images from different views: 
a front-facing view, a three-quarter profile, and a back view. 
Don't change the character's appearance and outfit.

[Settings: Enable Sequence Mode, Max Image Count: 3]
```

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
