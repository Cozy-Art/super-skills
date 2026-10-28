# qwen-image-v2-1 — build notes

Human-facing build notes. Not loaded as part of the skill.

**Built:** 2026-10-18 · **Skill version:** 1.0 · **Model:** Qwen-Image 2.1 (Alibaba)

---

## Research verification

- **Model:** Qwen-Image-2.1 (Alibaba / Qwen), open weights `Qwen/Qwen-Image-2.1`, Diffusers `QwenImage21Pipeline`, released 2026-09-20; hosted sibling `qwen-image-2.1-pro`.

## Verified as stated in research
Release date, 7B/32-layer single-stream DiT, Qwen3-VL 8B encoder, 64-ch RGBA VAE 16x, 10 refs, 7 official 2K presets, 40 steps, true_cfg_scale=1.0 default, negative ignored unless CFG>1, full __call__ signature incl. output_resolution=1024 and use_kv_cache, KV-cache determinism note, flex-attention compile requirement, RGBA wrapper text, <imageN> tag mandate, install requirements, Qwen Research License, PE-T2I/PE-I2I (Qwen3.5-VL 9B).

## Corrections / additions
- "Official examples use 2048x2048" as width/height default → pipeline default is None; omitted dims are derived from the condition image ratio at output_resolution=1024 (~1 MP), so explicit width/height is required for 2K. — https://huggingface.co/docs/diffusers/main/api/pipelines/qwenimage21
- Edit enhancer output contains only wh_ratio → it returns rewritten_prompt + wh_ratio + ratio_follow (mutually exclusive; single-image edits default ratio_follow "<image1>"). — https://github.com/QwenLM/Qwen-Image-2.1/blob/main/prompt_rewrite/prompts/system_prompt_edit.txt
- Research said the edit rewriter removes quality boosters → that ban is in the T2I prompt; the edit prompt instead mandates affirmative phrasing. — system_prompt_t2i.txt / system_prompt_edit.txt
- T2I enhancer ratios limited to the 7 presets → it defaults to 3:2 / 2:3 and also emits 1:2, 2:1, 21:9, 9:21, 4:5, 5:4, 3:1, 1:3 etc. — system_prompt_t2i.txt
- Max refs 10 → official is 10, but ComfyUI's Text Encode node exposes 16 slots (templates wire 10). — https://docs.comfy.org/tutorials/image/qwen/qwen-image-2-1
- Added ComfyUI facts: base template 25 steps/cfg 1/euler/simple; cfg 2 helps dense text but oversharpens; cfg 5 degrades, 0.5 breaks; targets well above 2K lose adherence; painted marks become RGB pixels, name mark colour; split alpha for 3-channel nodes; 4.0 MP ≈ 2048². — docs.comfy.org
- Research had no hosted API section → added qwen-image-2.1-pro: Model Studio lists 10 refs, 20 RPM, 0.25 CNY/image (https://help.aliyun.com/en/model-studio/qwen-image-2-1-pro); Runware schema: prompt 2–3000 chars, 192–4096 px, 0.26–4.19 MP, 1:8–8:1, promptExtend default true, no CFG/steps/negative, ~$0.075/image (https://runware.ai/docs/models/alibaba-qwen-image-2-1-pro).

## Unverified
- Native Alibaba Model Studio / DashScope request field names for qwen-image-2.1-pro (overview page has no API reference) — marked unverified.
- ComfyUI "Turbo" checkpoint (8 steps) and Lightning LoRA — in ComfyUI template but not on the official model card; marked unverified provenance.
- Community claim that CFG ~3 improves negative-prompt responsiveness (Reddit) — kept only as "community reports".
- Divisible-by-32 sizing comes from NVIDIA NeMo / ComfyUI step-32 control, not the model card.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
