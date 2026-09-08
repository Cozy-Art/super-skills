# Stable Diffusion 3.5 — Continuity and Reference Features

---

## Seed-Based Reproducibility

Seed locking is the **primary consistency mechanism** in SD3.5. Every generation returns a seed — resubmitting the same prompt + seed + parameters produces nearly identical results.

### Workflow

1. **Generate freely** with random seeds to explore directions
2. **Find a strong result** — note the seed from the UI or API response
3. **Lock the seed** — same seed + same prompt + same parameters = same output
4. **Change one variable at a time** — only prompt OR parameters, not both simultaneously
5. **Document seed + prompt + CFG + steps** as a reusable recipe

> Seed + changed prompt = controlled variation. Seed alone does not guarantee the same image if any other parameter changes.

### Cross-Platform Seed Behavior

Seeds may not transfer between platforms (ComfyUI vs. A1111 vs. API) even with the same prompt and parameters. Treat seeds as platform-specific.

---

## Image-to-Image Generation

SD3.5 supports img2img where an input image guides the generation.

### Key Parameter: `prompt_strength` / `strength`

Controls how much the output deviates from the input image:

| Value | Effect | Use Case |
|-------|--------|---------|
| 0.3–0.5 | Preserves most of the original | Light stylistic adjustments, color grading |
| 0.5–0.65 | Moderate changes, maintains structure | Style transfer keeping composition |
| 0.7–0.8 | Significant changes | Converting sketch to finished image |
| **0.85** (default) | Substantial deviation | Strong creative reinterpretation |
| 0.9–1.0 | Maximum creative freedom | Nearly new generation from loose reference |

**Important:** The `aspect_ratio` parameter is **ignored** in img2img mode — output matches input image dimensions.

### Img2Img Use Cases

- **Sketch to render:** Rough sketch → finished illustration at `prompt_strength: 0.7–0.8`
- **Style transfer:** Photo → painting style at `prompt_strength: 0.6–0.75`
- **Variation generation:** Finished image → similar variation at `prompt_strength: 0.4–0.6`
- **Upscale + rework:** Lower resolution to higher quality with same composition at `prompt_strength: 0.3–0.5`

---

## IP-Adapter: Reference Image Consistency

The **InstantX SD3.5 Large IP-Adapter** enables reference-image-guided generation — maintaining visual identity (face, character, style, object) across generations.

### Core Parameter

**`ipadapter_scale`** — Controls balance between reference image adherence vs. text prompt:
- Default: **0.5**
- Higher values (0.7–0.9): Stronger visual reference adherence
- Lower values (0.3–0.4): Text prompt dominates; reference is a subtle influence

### Supported Modes

| Mode | What it preserves | Typical `ipadapter_scale` |
|------|------------------|--------------------------|
| **Style transfer** | Visual rendering style, color relationships, texture treatment | 0.4–0.6 |
| **Character consistency** | Facial identity, distinctive features across scenes | 0.6–0.8 |
| **Object reference** | Specific object appearance, shape, material | 0.5–0.7 |

### IP-Adapter Workflow

1. Prepare a clean reference image (front-facing for characters; clear subject for objects/style)
2. Load IP-Adapter weights in ComfyUI or A1111
3. Set `ipadapter_scale` based on mode (start at 0.5)
4. Write a text prompt describing the new scene — **do not describe the reference image itself** (it's already provided)
5. Iterate on `ipadapter_scale` to balance adherence vs. creative freedom

### Compatibility

- Compatible with **ControlNet** modules (Canny, Tile, Pose) for combined structural + reference control
- Works with LoRA fine-tunes loaded on top of SD3.5 Large
- Best supported in **ComfyUI** workflow environments

---

## ControlNet Structural Guidance

SD3.5 ControlNet modules provide structural constraints — the model generates new content while respecting the spatial structure from a control image.

### Available Modules

| Module | What it uses | What it preserves |
|--------|-------------|------------------|
| **Canny** | Edge detection map | Precise outlines, architectural lines, object boundaries |
| **Tile** | Downsampled layout | Overall composition, color distribution, spatial arrangement |
| **Pose** | OpenPose skeleton map | Human body positioning, gestures, limb placement |

### When to Use Each

**Canny:**
- Converting architectural drawings or sketches to rendered images
- Maintaining precise object contours from a reference
- Re-stylizing an image while preserving exact outlines

**Tile:**
- Light stylistic re-rendering while maintaining composition
- Upscaling and enhancement workflows
- Consistent lighting direction across variations

**Pose:**
- Multi-shot character series with consistent body positions
- Generating characters in specific poses from reference
- Action sequences with defined movement

### ControlNet + IP-Adapter Combination

Using Pose (ControlNet) + Character (IP-Adapter) together:
- ControlNet controls the body pose
- IP-Adapter maintains the character's face/identity
- Text prompt describes the scene and style

This combination is the most powerful tool for character consistency across shots in SD3.5.

---

## LoRA Fine-Tuning

**SD3.5 Medium** is the recommended base for LoRA training — designed specifically for customization.

### LoRA Scale (Inference)

The `lora_scale` parameter controls LoRA influence at inference:
- **0.7–0.8:** Recommended for style LoRAs
- **0.8–1.0:** Recommended for character/identity LoRAs
- **0.5–0.7:** When combining multiple LoRAs

### LoRA Use Cases

- **Character LoRA:** Train on 10–20 images of a specific character → consistent face across all generations
- **Style LoRA:** Train on a specific artist's work (with permission) or design style → consistent aesthetic
- **Product LoRA:** Train on product images → consistent product appearance in marketing materials

### Ecosystem Note

The SD3.5 LoRA ecosystem is significantly smaller than SDXL's as of October 2024. CivitAI has growing community LoRAs, but expect fewer options than SDXL. SD3.5 Medium is the best variant for custom training.

---

## Multi-Shot Consistency Strategies

SD3.5 does not have native character locking. Use these approaches in combination:

### Tier 1: Seed + Detailed Description (API and Web)

- Lock seed from best character generation
- Copy-paste exact character description verbatim into every new prompt
- Change only the scene elements (environment, action, camera angle)
- Keep CFG and step count identical across the series

**Character description template:**
```
[gender], [age], [hair color and style], [eye color], [skin tone], [distinctive features], [clothing description]
```
Freeze this string. Do not paraphrase.

### Tier 2: IP-Adapter (ComfyUI / A1111)

- Generate canonical character image (neutral pose, front-facing)
- Use as IP-Adapter reference at `ipadapter_scale: 0.65–0.75`
- Describe new scene in text prompt
- Add Canny or Tile ControlNet for additional structural consistency

### Tier 3: ControlNet Pose (ComfyUI)

- Extract OpenPose skeleton from reference image
- Use Pose ControlNet to maintain body positioning
- Combine with IP-Adapter for face consistency

### Tier 4: LoRA (ComfyUI / A1111 with training)

- Train character LoRA on 10–20 reference images
- Load at `lora_scale: 0.85–0.95` for strong identity lock
- Most consistent method; requires training investment

### Inpainting for Corrections

When a generated image is close but has specific inconsistencies:
- Use ComfyUI or A1111's inpainting mode
- Mask only the problem area
- Use a targeted prompt for just the masked region
- Keep `prompt_strength` low (0.5–0.65) to blend with surrounding content

---

## CLIP vs. T5-XXL Prompt Split (Advanced ComfyUI)

ComfyUI allows sending different prompts to the CLIP encoders and T5-XXL separately:

- **CLIP prompt:** Short, keyword-focused — style, subject, quality indicators
- **T5-XXL prompt:** Full natural language description — spatial relationships, narrative, detail

This advanced technique lets you leverage CLIP's keyword parsing and T5's language understanding independently. Most users don't need it, but it provides fine-grained control for experienced practitioners.

---

## Platform-Specific Notes

**ComfyUI:**
- Full access to all three text encoders separately
- Best platform for IP-Adapter + ControlNet combinations
- Full LoRA support
- Manual CFG, step, and sampler control

**Automatic1111:**
- Standard SD UI; good LoRA support
- Supports img2img, inpainting
- Some IP-Adapter support via extensions

**Stability AI API / AWS Bedrock:**
- Simplified parameter set (no direct encoder access)
- Reliable for text-to-image and img2img
- No LoRA loading

**Replicate:**
- API-based; per-image pricing
- Good for batch generation
- Limited to core parameters
