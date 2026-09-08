# flux-v2 — build notes

Human-facing build notes.

---

## Version History

### v1.0.0 (2026-02-25)
- Initial SKILL creation covering the complete Flux 2 family
- Variant selection guide for Pro, Max, Flex, Klein (4B/9B), and Kontext
- JSON structured prompting documentation
- Platform API paths for BFL, Replicate, Fal.ai, Together AI, Freepik, ComfyUI
- 6 example input/output pairs across complexity levels and variants
- Hex color precision and multi-reference workflows

## Platform-Specific API Paths

### Black Forest Labs (Official API)
```
POST https://api.bfl.ai/v1/flux-2-pro
POST https://api.bfl.ai/v1/flux-2-max
POST https://api.bfl.ai/v1/flux-2-flex
POST https://api.bfl.ai/v1/flux-2-klein-9b
POST https://api.bfl.ai/v1/flux-2-klein-4b
Authorization: Bearer {API_KEY}
Content-Type: application/json
```

### Replicate
```
POST https://api.replicate.com/v1/predictions
Model: black-forest-labs/flux-2-pro
Model: black-forest-labs/flux-2-max
Model: black-forest-labs/flux-2-flex
Authorization: Bearer {API_TOKEN}
```

### Fal.ai
```
POST https://fal.run/fal-ai/flux-2-pro
POST https://fal.run/fal-ai/flux-2-max
POST https://fal.run/fal-ai/flux-2-flex
POST https://fal.run/fal-ai/flux-2-klein-4b
POST https://fal.run/fal-ai/flux-2-klein-9b
Authorization: Key {API_KEY}
```

### Together AI
```
POST https://api.together.xyz/v1/images/generations
Model: black-forest-labs/FLUX.2-pro
Model: black-forest-labs/FLUX.2-max
Authorization: Bearer {API_KEY}
```

### Freepik
```
Access via Freepik AI Image Generator
Models menu → Flux.2 Pro or Flux.2 Flex
Supports character/style references via suite
Resolution: 1K or 2K, up to 4 outputs per generation
```

### ComfyUI (Local)
```
Model: flux2-klein-4b (Apache 2.0, ~13GB VRAM)
Model: flux2-klein-9b (FLUX NCL, ~29GB VRAM)
Model: flux2-dev (open weights, ~32B params)
Workflow: Load model → CLIP + T5 encode → Sample → Decode
LoRA support: Klein 4B Base and 9B Base variants
```

---

## Metadata
- **Model:** Black Forest Labs Flux 2
- **Model Family:** Flux 2 (Pro, Max, Flex, Klein, Kontext)
- **SKILL Version:** 1.0.0
- **API Version:** Flux 2 (November 2025 launch; Klein January 2026)
- **Last Updated:** 2026-02-25
- **Status:** production
- **Category:** image-generation
- **Maintainer:** Visual Horizon Studio

---
