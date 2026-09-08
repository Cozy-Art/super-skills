---
name: qwen-image-prompts
description: Generate optimized prompts for Alibaba's Qwen Image family, including Qwen-Image v1, Qwen-Image-2512, and the current flagship Qwen-Image-2.0 / Qwen-Image-2.0-Pro. Use this skill whenever a user mentions Qwen Image, Qwen-Image-2.0, Tongyi Lab image generation, or asks for prompts targeting fal.ai, DashScope, Atlas Cloud, Replicate, or ComfyUI deployments of Qwen Image. Also trigger for any image generation task requiring best-in-class multilingual text rendering (Chinese/English/bilingual posters, menus, signage), infographics, slide layouts, multi-element poster design, product photography, character consistency with LoRA, ControlNet-guided generation, or image-to-image editing with the Qwen-Image-Edit models. Always use this skill — Qwen Image uses a language model text encoder (Qwen2.5-VL) that requires natural prose sentences, not tag lists, and has unique front-loading rules, text rendering workflows, and parameter behaviors that differ significantly from diffusion-model conventions.
---

# Qwen Image Prompt Generator

Generate optimized prompts for Alibaba's Qwen Image family — distinguished by industry-leading multilingual text rendering (Chinese + English), native 2K resolution, and a unified generation-plus-editing architecture.

## Which Model Are You Targeting?

| Version | When to use |
|---------|------------|
| **Qwen-Image-2.0 / Pro** | Default for all new work — API via fal.ai or DashScope |
| **Qwen-Image-2512** | Local/ComfyUI deployment (best open-weights option as of May 2026) |
| **Qwen-Image-Edit** (2509/2511) | Multi-image editing, ControlNet, pose transfer, outfit swap |

For all cases, prompt structure and syntax rules are the same. Only the API parameters differ, and those are the director's to set in their own tool.

## The One Rule That Overrides Everything

**Front-load the subject.** The Qwen2.5-VL language encoder weights earlier tokens more heavily. The most important element must come first.

❌ **Weak:**
```
A nice landscape photo featuring somewhere a red sports car
```

✅ **Strong:**
```
Red sports car on mountain road, aerial drone shot, golden hour lighting, cinematic wide angle
```

## The Five-Element Framework

```
[Subject + Core Action] → [Environment / Setting] → [Style / Rendering Mode] → [Lighting / Atmosphere] → [Text / Layout (if needed)]
```

**Standard image:**
```
A 28-year-old East Asian woman with natural curly hair, wearing a white linen shirt,
standing in soft window light indoors. Candid, unposed expression.
Editorial photography style. Shallow depth of field. Clean white background, slightly blurred.
```

**Poster with text (Qwen-Image-2.0):**
```
A vertical event poster. Background: deep navy blue with subtle star-field grain texture.
Center: a geometric illustration of a mountain range in gold line art.
Top third: the text "ALTITUDE FESTIVAL" in large bold condensed sans-serif, white, all caps.
Below title: "June 20–22 | Telluride, Colorado" in smaller weight, gold color.
Bottom: "altitudefestival.com" in minimal small caps, white.
Balanced whitespace. Modern editorial design. Print-ready at 2K resolution.
```

## Syntax Rules (Critical)

- ✅ **Natural language sentences and paragraphs** — the model uses an LLM text encoder
- ✅ **Quote exact in-image text strings:** `The sign reads "GRAND OPENING" in bold red letters`
- ✅ **Chinese characters directly in prompt** for Chinese in-image text
- ✅ **One clear style anchor** per prompt (pick one, not a contradiction)
- ❌ **No tag lists:** booru/Danbooru comma-separated tags produce worse results
- ❌ **No weight syntax:** `(keyword:1.3)` is not parsed, may cause artifacts
- ❌ **No quality boosters:** "8K, ultra HD, masterpiece" — ignored; describe the visual instead

## Prompt Length by Use Case

| Use case | Target length |
|----------|--------------|
| Simple portrait / landscape | 15–50 words |
| Standard production image | 50–150 words |
| Poster / product with text | 100–300 words |
| Infographic / slide / multi-element layout | 300–500+ words (2.0 only, up to 1,000 tokens) |

## Text Rendering Workflow (Qwen's Superpower)

1. Enclose exact strings in quotes: `"MORNING RITUAL"`
2. Describe font style: serif/sans-serif, bold/italic
3. Specify color: cream white, gold, deep navy
4. Give spatial context: "top-center," "bottom third," "centered below the illustration"
5. Use `output_format: "png"` — preserves text sharpness vs. JPEG compression
6. Avoid `acceleration: "high"` for any image containing text
7. For Chinese text: write the characters directly in the prompt (not romanized)

## Negative Prompt Format

NLP sentences, not keyword dumps:

✅ `"No watermarks, no distorted faces, no blurry backgrounds, avoid artificial plastic skin texture"`

❌ `"blurry, bad anatomy, ugly, deformed, watermark, low quality, extra limbs"`

**All-purpose negative:**
```
No distortion, no watermarks, no text artifacts, no duplicate subjects, no overexposed highlights
```

## Ideation → Production Workflow

1. **Explore:** 15–20 steps, random seed — find the right direction
2. **Refine:** 25–28 steps, lock seed — adjust prompt wording incrementally
3. **Finalize:** 35–40 steps (or Pro endpoint) — final production render

Lock `enable_prompt_expansion: false` during testing — the auto-rewrite feature makes iterative results non-reproducible.

## Reference Files

Load these when you need depth on a specific topic:

- **`parameters.md`** — Complete parameter tables for Qwen-Image v1/2512 (fal.ai), Qwen-Image-2.0 (fal.ai + DashScope), image size presets, sampler/scheduler recommendations for ComfyUI, CFG and shift parameter guidance, output formats, generation speed reference, supported task types, and pricing across all platforms.

- **`best-practices.md`** — Front-loading discipline, what to emphasize (specific visual attributes, camera language, style anchors, mood), anti-pattern table with fixes, text rendering deep-dive, negative prompt strategy, consistency workflow, bilingual prompt guidance, and composition techniques by content type (portrait, landscape, poster, product, infographic, character).

- **`continuity-and-editing.md`** — Seed-based reproducibility workflow, image-to-image reference with positional label syntax, multi-image reference community tips, supported reference modes (scene placement, outfit swap, pose transfer, style transfer), LoRA for character/style consistency (scale recommendations, Lightning LoRA), Next-Scene cinematic transition endpoint, ControlNet support (depth/edge/pose/sketch), and the unified 2.0 editing workflow.

- **`examples.md`** — 7 fully annotated example prompts: simple photorealistic portrait, environment/landscape, poster with in-image text, product/e-commerce, infographic/slide, character scene with artistic style, and complex multi-character composite. Includes quick-start templates and a version-routing guide (which example requires 2.0 vs. works on v1/2512).
