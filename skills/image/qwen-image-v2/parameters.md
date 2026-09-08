# Qwen Image — Parameters Reference

Complete API and ComfyUI parameter specifications for the full Qwen Image family.

---

## Model Family Routing

| Version | Release | Architecture | Status |
|---------|---------|-------------|--------|
| Qwen-Image v1 (base) | Aug 2025 | 20B MMDiT, Apache-2.0 | Open-source |
| Qwen-Image-Edit-2509 | Sep 2025 | 20B MMDiT | Open-source; editing + ControlNet |
| Qwen-Image-2512 | Dec 2025 | 20B MMDiT | Best open-weights option (May 2026) |
| Qwen-Image-Edit-2511 | Nov 2025 | 20B MMDiT | Improved editing vs. 2509 |
| **Qwen-Image-2.0** | Feb 10, 2026 | 7B unified | Closed API; native 2K; 1K-token prompts |
| **Qwen-Image-2.0-Pro** | Apr 22, 2026 | 7B unified | Best production quality; closed API |

**Recommendation:** Target Qwen-Image-2.0 or 2.0-Pro for all new API work. Use Qwen-Image-2512 for local/ComfyUI deployment.

---

## Qwen-Image v1 / 2512 — fal.ai API (Full Parameter Access)

| Parameter | Type | Default | Range / Options | Notes |
|-----------|------|---------|-----------------|-------|
| `prompt` | string | — | Any text | Required |
| `image_size` | enum or object | `landscape_4_3` | See presets below | Also accepts `{width, height}` |
| `num_inference_steps` | integer | 30 | 2–250 | 20 for drafts; 40 for final |
| `guidance_scale` | float | **2.5** | 0–20 | Community recommends 2.5–5; above 5 causes contrast artifacts |
| `seed` | integer | random | Any integer | Same seed + same prompt = same output |
| `negative_prompt` | string | `" "` | Any text | NLP sentences, not keyword dumps |
| `num_images` | integer | 1 | 1–4 | Batch generation |
| `output_format` | enum | `png` | `jpeg`, `png` | Use PNG for text-heavy designs |
| `acceleration` | enum | `none` | `none`, `regular`, `high` | ⚠️ `high` degrades text legibility — never use for images with text |
| `use_turbo` | boolean | false | true/false | Forces 10 steps + CFG 1.2; fast but lower quality |
| `loras` | array | — | Up to 3 LoRAs | `{path: URL, scale: 0–2}` per entry |
| `enable_safety_checker` | boolean | true | true/false | NSFW filter |

---

## Qwen-Image 2.0 — fal.ai API

| Parameter | Type | Default | Range / Options | Notes |
|-----------|------|---------|-----------------|-------|
| `prompt` | string | — | **Up to 1,000 tokens** | Required; Chinese + English natively supported |
| `negative_prompt` | string | `""` | Max 500 chars | NLP sentences preferred |
| `image_size` | enum or object | `square_hd` | See presets below | Custom: 512–2048 each side |
| `enable_prompt_expansion` | boolean | true | true/false | ⚠️ **Disable when testing exact phrasing** — LLM auto-rewrites prompt; results become non-reproducible |
| `seed` | integer | random | 0–2,147,483,647 | |
| `num_images` | integer | 1 | 1–4 | |
| `output_format` | enum | `png` | `jpeg`, `png`, `webp` | WebP added in 2.0 |
| `enable_safety_checker` | boolean | true | true/false | |
| `sync_mode` | boolean | false | true/false | Returns data URI; no request history |

**Parameters removed from 2.0 (do not pass — will error):**
- `guidance_scale` / CFG — managed internally
- `num_inference_steps` — managed internally
- `acceleration` — not exposed
- `use_turbo` — not exposed

---

## Atlas Cloud / DashScope API

| Parameter | Values |
|-----------|--------|
| `size` | `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `3:2`, `2:3` |
| `width` / `height` | 512–2048 pixels each |
| `seed` | -1 for random, or integer |

**DashScope model IDs:**
- `qwen-image-2.0-pro` — Pro tier (¥0.50/image, ~$0.07)
- `qwen-image-plus` — Plus tier (¥0.20/image, ~$0.027)

---

## Image Size Presets (fal.ai enum)

| Enum Value | Dimensions | Best For |
|------------|-----------|---------|
| `square` | 512×512 | Quick tests |
| `square_hd` | 1024×1024 | Default; portraits, icons |
| `portrait_4_3` | 768×1024 | Social content |
| `portrait_16_9` | 576×1024 | Mobile / Reels |
| `landscape_4_3` | 1024×768 | Landscape photos |
| `landscape_16_9` | 1024×576 | Widescreen / YouTube |
| Custom `{width, height}` | 512–2048 | Posters, slides, any ratio |

**Resolution notes:**
- Qwen-Image v1/2512: community-tested to 2048×2048; native sweet spot 1024–1344px longest side
- Qwen-Image-2.0: natively trained at 2K (2048×2048); generates at full resolution without upscaling artifacts
- Outputs above 2048px on either side may produce quality degradation

---

## Sampler / Scheduler (ComfyUI / Local Deployment)

Community-validated combinations for open-weights models:

| Sampler | Scheduler | Notes |
|---------|-----------|-------|
| `euler` | `sgm_uniform` or `beta` | Default; reliable |
| `euler` | `res_multistep` | Good detail |
| `ddim` | `ddim_uniform` | Excellent results — pair these exactly |
| `er_sde` | `kl_optimal` + power sigmas | Advanced; very fine details |

**Steps:**
- 20 for drafts
- 40 for standard/final
- 8 with Lightning LoRA for speed (~4× faster, slightly lower quality)

**CFG (guidance_scale):**
- Default: **2.5**
- Increase to 4–5 for stronger prompt adherence
- Above 5: contrast artifacts appear
- Do not exceed 5

**Shift parameter (local deployments):**
- If outputs are blurry or washed out → **raise shift to 12–13**
- This resolves most bad-output issues on local deployments

**ComfyUI node chain:**
```
GGUF Loader → CLIPLoader (Qwen2.5-VL) → VAE → LoRA Loader → KSampler
```

---

## Output Formats

| Format | Use Case | Notes |
|--------|---------|-------|
| PNG | Text-heavy designs, graphics, logos | Lossless; largest file; preserves sharp edges — **use for any image with text** |
| JPEG | Photorealistic images, landscapes | Smaller file; compression artifacts near text edges |
| WebP | Web delivery, balanced | Only available on Qwen-Image-2.0 API |

---

## Pricing (API)

| Platform | Endpoint | Price |
|----------|----------|-------|
| fal.ai | `fal-ai/qwen-image` (v1 Standard) | $0.02/megapixel |
| fal.ai | `fal-ai/qwen-image-max/text-to-image` (Max) | Higher (see fal.ai) |
| fal.ai | `fal-ai/qwen-image-2/text-to-image` (2.0 Std) | $0.035/image |
| DashScope | `qwen-image-2.0-pro` (Pro) | ¥0.50/image (~$0.07) |
| DashScope | `qwen-image-plus` (Plus) | ¥0.20/image (~$0.027) |
| Replicate | Qwen-Image | $0.030/image |

---

## Generation Speed Reference

| Hardware | Steps | Time |
|----------|-------|------|
| RTX 4090 (24GB) | 40 steps | ~71–94 seconds |
| RTX 4090 | 8 steps (Lightning LoRA) | ~15 seconds |
| Google Colab L4 | 40 steps | ~2.5 minutes |
| Google Colab L4 | 8 steps (Lightning) | ~1 minute |
| API (Qwen-Image-2.0) | Cloud-hosted | **5–8 seconds** |

---

## Supported Task Types (Edit Models)

| `task_type` | Description |
|-------------|-------------|
| `text_to_image` | Standard generation from text |
| `image_to_image` | Reference-guided generation |
| `inpainting` | Fill masked region (requires mask + source image) |
| `outpainting` | Expand canvas beyond original borders |
| `sketch_guidance` | Convert rough sketch to polished render |

---

## Platform Access Summary

| Platform | Models Available | Notes |
|----------|-----------------|-------|
| **chat.qwen.ai** | Qwen-Image-2.0 (latest) | Free web UI; T2I mode toggle |
| **fal.ai** | v1, 2.0 std/max, Edit variants | Full API + playground; per-megapixel or per-image pricing |
| **Alibaba DashScope** | 2.0-pro, plus, max | Official API; ¥-denominated pricing |
| **Atlas Cloud** | Max, Plus, Edit-Plus | Side-by-side model comparison |
| **ComfyUI (local)** | v1, 2512, Edit-2511 (open weights) | Full parameter access; GGUF/FP8/BF16 |
| **Replicate** | Qwen-Image | $0.030/image |
| **RunDiffusion** | Edit-2509 | Pre-built ComfyUI workflow in cloud |

---

## Technical Specifications

### Model Architecture

| Spec | Qwen-Image v1/2512 | Qwen-Image-2.0 |
|------|--------------------|----------------|
| Parameters | 20B | 7B |
| Architecture | MMDiT (Multimodal Diffusion Transformer) | Unified generative LM |
| Text Encoder | Qwen2.5-VL-7B | Qwen2.5-VL (integrated) |
| VAE | `qwen_image_vae.safetensors` | Integrated |
| Native Resolution | 1328×1328 (practical: 1024–1344) | **2048×2048 (native 2K)** |
| Max Supported | ~2048×2048 | 2048×2048 per side |
| Open Source | ✅ Apache-2.0 | ❌ Closed as of May 2026 |
| VRAM (local) | Min 8GB; 24GB for full quality | 7B ≈ 14–16GB est. |
| Inference speed (API) | 71–94s on 4090 | **5–8 seconds** |
| Prompt token limit | ~200–300 practical | **1,000 tokens** |
| Prompt expansion | Not available | `enable_prompt_expansion` toggle |
| Output formats | PNG, JPEG | PNG, JPEG, WebP |

---

## Version Differences: v1/2512 → 2.0 Migration

### What Changed

| Feature | v1/2512 | Qwen-Image-2.0 |
|---------|---------|----------------|
| Architecture | Separate gen + edit models (20B each) | Single unified 7B model |
| Native resolution | 1328×1328 | Native 2K (2048×2048) |
| Prompt token limit | ~200–300 practical | **1,000 tokens** |
| Text rendering | Strong | Improved — "no more glitchy letters" |
| Human realism | Good | Significantly improved (hair strands, pores) |
| Open source | ✅ Apache-2.0 | ❌ Closed |

### Migration Checklist

1. ✅ Increase prompt length — 1,000-token budget allows element-by-element layout descriptions
2. ✅ Set `enable_prompt_expansion: false` during testing
3. ✅ Remove: `guidance_scale`, `num_inference_steps`, `acceleration`, `use_turbo` — all removed from 2.0 API
4. ✅ Trim negative prompts to 500-character limit
5. ✅ Expect richer texture detail without extra prompting (hair, fur, skin pores now render by default)
6. ✅ Switch `output_format` to `webp` if file size matters (new in 2.0)
7. ✅ Use Pro endpoint for production (April 2026 snapshot; better texture/lighting/materials)
