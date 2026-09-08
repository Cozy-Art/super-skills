# Stable Diffusion 3.5 — Parameters Reference

Complete parameter specifications for all SD3.5 variants across all major platforms.

---

## Model Variants at a Glance

| Specification | SD3.5 Large | SD3.5 Large Turbo | SD3.5 Medium |
|--------------|------------|-------------------|--------------|
| Parameters | 8.1 billion | 8.1 billion | 2.5 billion |
| Architecture | MMDiT + QK Normalization | MMDiT + ADD (Adversarial Diffusion Distillation) | MMDiT-X (improved architecture) |
| Max resolution | 1 megapixel | 1 megapixel | **2 megapixels** |
| Min resolution | ~0.25 MP | ~0.25 MP | 0.25 MP |
| Default size | 1024×1024 | 1024×1024 | 1024×1024 |
| Recommended steps | **20–35** | **4 exactly** | **20–30** |
| Default CFG | 3.5 | 1.0 | 3.5–5.0 |
| Community CFG | **4.4** | 1.0 | **4.4** |
| Speed (12GB GPU) | ~2+ minutes | ~10 seconds | Moderate |
| Text encoders | 2× CLIP + T5-XXL | 2× CLIP + T5-XXL | 2× CLIP + T5-XXL |
| Hardware target | Professional / high-end consumer | Consumer | Consumer "out of the box" |
| Best for | Maximum quality, complex scenes | Speed, rapid prototyping, batch | Customization, LoRA training, balanced quality |
| Open weights | ✅ Hugging Face (Apache 2.0) | ✅ | ✅ |

---

## Core API Parameters

| Parameter | Type | Default | Range | Notes |
|-----------|------|---------|-------|-------|
| `prompt` | string | — | Max 10,000 chars | Required. Natural language or keywords. |
| `negative_prompt` | string | — | Max 10,000 chars | Use sparingly — minimal is better in SD3.5 |
| `aspect_ratio` | string | `1:1` | 9 values (see table) | Text-to-image only; ignored in img2img |
| `seed` | integer | Random | 0–4,294,967,295 | For reproducibility |
| `output_format` | string | varies | `png`, `jpeg`, `webp` | Output file format |
| `mode` | string | `text-to-image` | `text-to-image`, `image-to-image` | Generation mode |
| `cfg` / `guidance_scale` | float | 3.5 (Large) / 1.0 (Turbo) | See CFG table | Community default: **4.4** for Large/Medium |
| `steps` / `num_inference_steps` | integer | 35 (Large) / 4 (Turbo) | 1–50 | 20–25 for Large; **exactly 4** for Turbo |
| `prompt_strength` (img2img) | float | 0.85 | 0–1 | How much output deviates from input image |
| `width` × `height` | integer | 1024×1024 | Divisible by 8 | Within resolution limits per variant |

---

## Guidance Scale (CFG) Deep Dive

| CFG Value | Effect | Use Case |
|-----------|--------|---------|
| 1.0 | Prompt nearly ignored; very creative/abstract | Abstract art, exploration, **Turbo default** |
| 3.5–4.4 | Good balance of creativity and adherence | **Recommended default range for SD3.5** |
| 5.5–7.1 | Increased detail definition; risk of illogical details | Complex prompts needing stronger adherence |
| 7–9 | Strong prompt adherence; SDXL-era range | ⚠️ Not recommended for SD3.5 |
| 12–16 | Very strict adherence; artifacts likely | Detailed prompts needing precise elements |
| 17–20 | Maximum adherence; quality degrades | Not recommended |

**Community consensus:** CFG **4.4** is the validated sweet spot for SD3.5 Large and Medium — popularized on CivitAI, produces balanced results across most art styles.

**Turbo:** Always use CFG **1.0** — it was distilled at this value and performs best with it.

---

## Inference Steps by Variant

| Model | Recommended | Notes |
|-------|------------|-------|
| SD3.5 Large | 20–35 | 20 steps is visually comparable to 30; diminishing returns beyond 25 |
| SD3.5 Large Turbo | **4 exactly** | Designed via Adversarial Diffusion Distillation for exactly 4 steps |
| SD3.5 Medium | 20–30 | Good balance on consumer hardware |

**Steps warning:** More steps ≠ better quality in SD3.5. Beyond 25 for Large, quality gains are minimal. Turbo at anything other than 4 steps produces degraded output.

---

## Aspect Ratios and Pixel Dimensions

All dimensions must be **divisible by 8**.

**SD3.5 Large / Large Turbo** (max 1 megapixel):

| Aspect Ratio | Pixel Dimensions | Typical Use |
|-------------|-----------------|------------|
| `1:1` | 1024×1024 | Social media, profiles |
| `3:2` | ~1248×832 | Photography, landscape |
| `2:3` | ~832×1248 | Portrait, poster |
| `4:3` | ~1152×896 | Presentations |
| `3:4` | ~896×1152 | Vertical frames |
| `16:9` | ~1344×768 | YouTube, widescreen |
| `9:16` | ~768×1344 | TikTok, Stories |
| `21:9` | Ultrawide | Cinematic banners |
| `5:4` / `4:5` | Various | Standard photos |

**SD3.5 Medium:** Supports 0.25–2 megapixels — wider range than Large.

**Resolution caution:** SD3.5 Large is sensitive to high-res generation above 1024×1024. Results may degrade at resolutions significantly above 1 MP. Use Medium if you need higher resolution.

---

## Text Encoder Architecture

SD3.5 uses **three text encoders** — this is the key architectural difference from SDXL:

| Encoder | Token Window | Behavior |
|---------|-------------|---------|
| CLIP (×2) | 77 tokens each | Truncates prompt beyond 77 tokens |
| T5-XXL | Up to 512 tokens | Handles longer context; parses sentence structure |

**Practical implications:**
- The first ~77 tokens (~60 words) carry the most weight across all three encoders
- Critical elements (style, subject, key composition) must appear in the first 77 tokens
- Longer prompts work but with diminishing positional weight beyond 77 tokens
- Most UIs split prompts into 75-token chunks for CLIP, pass full text to T5
- T5's sentence understanding is why natural language outperforms keyword lists for complex scenes

---

## Output Formats

| Format | Notes |
|--------|-------|
| PNG | Lossless, largest file size — best for designs with sharp edges or text |
| JPEG | Lossy compression, smaller files — best for photorealistic images |
| WebP | Modern format, good compression — best for web delivery |

---

## Platform Availability

| Platform | Models Available | Notes |
|----------|-----------------|-------|
| **Hugging Face** | Large, Large Turbo, Medium (open weights) | Apache 2.0 license |
| **Stability AI API** | Large | Official API |
| **AWS Bedrock** | SD3.5 Large | Max 10,000 chars prompt |
| **Replicate** | Large, Large Turbo | Per-image pricing |
| **DeepInfra** | Medium | |
| **ComfyUI** | All three | Full parameter access; recommended for advanced workflows |
| **Automatic1111** | All three | Standard SD UI; good LoRA support |

---

## Image-to-Image Parameters

When `mode: "image-to-image"`:

| `prompt_strength` | Effect |
|------------------|--------|
| 0.3–0.5 | Preserves most of the original image |
| 0.6–0.75 | Balanced — significant changes while maintaining structure |
| 0.85 (default) | Allows substantial deviation |
| 0.9–1.0 | Maximum creative freedom from input |

**Note:** `aspect_ratio` is ignored in img2img mode — output matches input image dimensions.

---

## SDXL → SD3.5 Migration Checklist

| SDXL habit | SD3.5 change |
|-----------|-------------|
| Long negative prompt ("deformed, disfigured, ugly...") | ✅ Reduce to minimal essentials or **remove entirely** |
| Prompt weighting `(keyword:1.2)` | ✅ Remove — silently ignored; use positional emphasis or natural language instead |
| CFG 7–9 | ✅ Drop to **4.4** as starting point |
| 30–40 steps | ✅ Reduce to 20–25 for Large; **4 for Turbo** |
| Artist names for style control | ✅ Replace with visual descriptions: "painted in ink wash and watercolor" |
| Style instruction at end of prompt | ✅ Move style to the **beginning** |
| Keyword comma lists for complex scenes | ✅ Use natural language sentences for spatial relationships |
| Expecting extensive LoRA ecosystem | ⚠️ SD3.5 LoRA ecosystem is smaller than SDXL's; use SD3.5 Medium for fine-tuning |

---

## Recommended Parameter Sets by Use Case

| Use case | Model | CFG | Steps | Aspect |
|----------|-------|-----|-------|--------|
| Maximum quality production | Large | 4.4 | 25–35 | Match use case |
| Speed / batch iteration | Large Turbo | 1.0 | **4** | Match use case |
| Consumer hardware | Medium | 4.4 | 20–30 | Match use case |
| Custom fine-tuning base | Medium | 4.4 | 20–30 | 1:1 for training |
| Text rendering | Large | 4.4–5.5 | 25–35 | Match design |
| Complex multi-element scene | Large | 4.4 | 25–35 | 16:9 or 3:2 |
| Portrait / character | Large | 4.4 | 25–30 | 2:3 |
| Product photography | Large | 4.4–5.0 | 25–30 | 1:1 or 3:2 |
