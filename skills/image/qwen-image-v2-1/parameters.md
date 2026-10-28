# Qwen-Image-2.1 — Parameters

Open weights: `Qwen/Qwen-Image-2.1` (Hugging Face / ModelScope) · Diffusers class `QwenImage21Pipeline` · licence: **Qwen Research License Agreement** (not Apache 2.0 — review before commercial use). Released 2026-09-20.

*Verified against the QwenLM/Qwen-Image-2.1 GitHub README, the Hugging Face model card, the Diffusers `qwenimage21` pipeline docs, Qwen's official PE system prompts, the ComfyUI Qwen-Image-2.1 tutorial, Alibaba Cloud Model Studio and Runware model pages, October 2026.*

## Install

`torch>=2.4.0` · `transformers>=5.17` · `diffusers` from GitHub source (`pip install git+https://github.com/huggingface/diffusers`) · `accelerate` · `pillow`.

```python
import torch
from diffusers import QwenImage21Pipeline
pipe = QwenImage21Pipeline.from_pretrained("Qwen/Qwen-Image-2.1", torch_dtype=torch.bfloat16).to("cuda")
# low VRAM: build without .to("cuda") and call pipe.enable_model_cpu_offload()
```

## `QwenImage21Pipeline.__call__`

| Parameter | Default | Values / behaviour | Recommendation |
|---|---|---|---|
| `prompt` | `None` | str or list[str] | Natural language. Or pass `prompt_embeds` + `prompt_embeds_mask`. |
| `image` | `None` | PIL / numpy / tensor, or ordered list | None = T2I. A list is **one shared reference set** for every prompt in the batch, read in list order. Official max **10**. |
| `negative_prompt` | `None` | str / list | **Ignored unless `true_cfg_scale > 1`.** |
| `true_cfg_scale` | `1.0` | float | 2.1 is designed to sample without guidance. >1 + negative prompt enables CFG and doubles work per step. |
| `height`, `width` | `None` | int px | If omitted, derived from the condition image's aspect ratio and `output_resolution`. **Always pass both** from the preset table. |
| `num_inference_steps` | `40` | int | Ignored if `sigmas` or the checkpoint's `sample_sigmas` is in use. |
| `sigmas` | `None` | list[float], excluding terminal | Overrides schedule; length sets step count. Advanced. |
| `num_images_per_prompt` | `1` | int | VRAM scales with it. |
| `generator` | `None` | `torch.Generator` or list | Fixed `manual_seed` for comparisons. |
| `latents` | `None` | tensor | Reuse noise to compare prompt variants. |
| `output_type` | `"pil"` | `pil` `np` `pt` `latent` | |
| `return_dict` | `True` | bool | |
| `attention_kwargs` | `None` | dict | Passed to the attention processor. |
| `callback_on_step_end` / `_tensor_inputs` | `None` / `["latents"]` | | Per-step inspection. |
| `output_resolution` | `1024` | int | Target side used to derive `height`/`width` and to **resize condition images**. |
| `use_kv_cache` | `True` | bool | Caches text + reference K/V after step 1. **Toggling it changes the sample in bf16** — fix it alongside the seed. |

Pipeline output is an in-memory image (RGB or RGBA). Save PNG for alpha, typography masters and editing intermediates.

**Not in the 2.1 pipeline:** `guidance_scale` (use `true_cfg_scale`), `strength` / denoise, reference-strength scalars, `mask_image` argument (mask/annotation editing is via marked images in supported workflows), duration, fps, motion, camera path.

## Official Native 2K Presets

| Ratio | width × height | Typical use |
|---|---|---|
| 1:1 | 2048 × 2048 | Products, icons, album art, RGBA assets |
| 4:3 | 2400 × 1792 | Editorial landscape, slides |
| 3:4 | 1792 × 2400 | Editorial portrait, magazine pages |
| 3:2 | 2528 × 1696 | Photography, group scenes |
| 2:3 | 1696 × 2528 | Posters, full-body portraits |
| 16:9 | 2752 × 1536 | Cinematic frames, storyboards, thumbnails |
| 9:16 | 1536 × 2752 | Vertical stories, phone wallpapers |

Keep custom sizes divisible by 32. Qwen's T2I enhancer also emits ratios such as 1:2, 2:1, 21:9, 4:5, 5:4, 3:1 (defaults 3:2 / 2:3) — map them to the nearest ~4 MP size divisible by 32 and validate. ComfyUI notes that targets well above 2K (e.g. 4K) lose prompt adherence.

## CFG and Negative Prompts

| Setting | Effect |
|---|---|
| `true_cfg_scale=1.0` (default) | No guidance; negative prompt skipped. Fastest, the published setting. |
| `1.5–2.0` + negative | Experiment only. ComfyUI: cfg 2 follows dense text more closely but can over-sharpen edges. |
| `≥5` | Badly degraded quality (ComfyUI). Community reports anatomy/appearance shifts above ~3. |
| `<1` (e.g. 0.5) | Breaks the image (ComfyUI). |

## Recommended Combinations

| Goal | Size | Steps | CFG | Refs | Notes |
|---|---|---|---|---|---|
| Fast ideation | ~1 MP, target ratio | 25–40 (validate lower) | 1.0 | 0–1 | Fixed seed |
| Final still | 2K preset | 40 | 1.0 | as needed | KV cache on |
| Poster / typography / infographic | 2K preset (2:3, 3:4, 16:9) | 40 | 1.0 (try 2.0 for dense text) | 0–2 | PNG |
| Identity-preserving edit | match source ratio | 40 | 1.0 | 1 identity ref | Same seed + config |
| Multi-reference composite | canvas ratio | 40 | 1.0 | ordered, roles | KV cache on |
| Transparent asset | 1:1 2048² | 40 | 1.0 | 0 | RGBA wrapper, PNG |
| Simple local edit | match source | 8–25 acceptable in ComfyUI | 1.0 | 1 marked image | Whole-frame rewrites need ~25+ |

## ComfyUI (native workflow)

- Nodes: `Text Encode Qwen Image 2.1` (slots `image_1`…`image_16`; templates wire 1–10 — `image_1` is the image being edited), Resolution Selector (megapixels: 1.0 ≈ 1024², **≈4.0 MP for 2048²**), Image Edit subgraph `resolution` (0–4096 step 32; `0` keeps each reference's size), `Qwen Image 2.1 Cache` (experimental), `SplitImageWithAlpha` / `JoinImageWithAlpha` for RGBA.
- Files: `qwen_image_2.1_bf16` / `int8_convrot` diffusion, `qwen3vl_8b` text encoder, `qwen_image_2.1_vae_bf16`, PE models `qwen3.5_9b_qwen_image_2.1_pe_t2i` / `_pe_i2i`.
- Sampler: base template **25 steps, cfg 1, euler, simple** (published pipeline uses 40; hands/fine detail improve ~30+, 40 reduces fizzle). A "Turbo" checkpoint (8 steps, fixed ManualSigmas) and a Lightning LoRA (4 steps) are distributed in the ComfyUI template — *not listed on the official model card (unverified provenance — confirm on your platform)*.
- Negative prompt has no effect at cfg 1.
- Mask editing: paint on `image_1` in Mask Editor — strokes become part of the RGB image, so **name the mark colour in the prompt** and say what colour the result should be.

## Prompt Enhancers (official)

`Qwen/Qwen-Image-2.1-PE-T2I` and `Qwen/Qwen-Image-2.1-PE-I2I` (fine-tuned Qwen3.5-VL 9B; `--task t2i` / `--task edit`).
- T2I returns `{"rewritten_prompt", "wh_ratio"}` — one English paragraph, ~400–500 words, ratio separate.
- Edit returns `{"rewritten_prompt", "wh_ratio", "ratio_follow"}` — mutually exclusive; single-image edits default to `ratio_follow: "<image1>"`.
- ComfyUI exposes them as `refine_prompt` / `thinking_mode` (off by default).

## Hosted: `qwen-image-2.1-pro`

Alibaba Cloud Model Studio lists **qwen-image-2.1-pro** (text + image in, image out, up to 10 reference images, 20 RPM, **0.25 CNY per image** in most regions). Its native request schema was not published on the overview page — *(unverified — confirm field names on your platform)*.

Runware schema (`alibaba:qwen-image@2.1-pro`), as one verified wrapper example:

| Field | Values |
|---|---|
| `positivePrompt` | 2–3,000 characters |
| `width` + `height` | 192–4,096 px each, sent together; area 0.26–4.19 MP; ratio 1:8 to 8:1 |
| `referenceImages` | 1–10 (URL, UUID, data URI, base64) |
| `seed` | 0–2,147,483,647 |
| `numberResults` | 1–20 |
| `promptExtend` | default **true** (LLM rewrite; hurts reproducibility) · `promptExtendMode` `direct` / `agent` (refs require `direct`) · `thinking` requires `promptExtend` |
| `outputFormat` | `JPG` (default) / `PNG` / `WEBP` · `outputQuality` 20–99 |
| Price | ~$0.075 / image |

No steps, CFG or negative prompt fields. Other wrappers will differ — treat their fields as platform features, not model syntax.

## Specs

| Area | Spec |
|---|---|
| Generator | 7B, 32-layer single-stream DiT, block-causal mixed-granularity attention |
| Encoder | Qwen3-VL 8B (text + vision context for references) |
| VAE | 64-channel RGBA, 16× spatial compression |
| Scheduler | Flow Matching, Euler discrete, dynamic shifting |
| Output | Native ~2K (up to 2752×1536 / 1536×2752), RGB or RGBA |
| References | Up to 10 |
| Prompt length | No published hard limit for open weights (Runware pro: 3,000 chars) |
| Video | Not supported |

Performance: 2K + several references is memory-heavy → CPU offload or fewer refs. `QwenImage21FlexAttnProcessor` is faster **only when the transformer is compiled** (`pipe.transformer.compile()`); uncompiled it can OOM at high resolution.

## Migration From Older Qwen-Image

| Old habit | Qwen-Image-2.1 |
|---|---|
| `QwenImagePipeline` + separate `QwenImageEdit(Plus)Pipeline` | One `QwenImage21Pipeline`, pass `image=` to edit |
| Qwen-Image (20B MMDiT) checkpoint | `Qwen/Qwen-Image-2.1` (7B DiT) |
| Edit recipes `true_cfg_scale=4.0`, 50 steps | `1.0`, 40 steps |
| Negative prompt always on | Only with CFG > 1 |
| "the first image" / "图1" in prose | `<image1>`, `<image2>` tags |
| Ratio in prompt text | `width` / `height` arguments |
| Separate Qwen-Image-Layered for alpha | Native RGBA via wrapper sentence |
| Seed-only reproducibility | Seed + size + steps + CFG + precision + ref order + `use_kv_cache` |
| Generic prompt enhancer | PE-T2I / PE-I2I with different contracts |
