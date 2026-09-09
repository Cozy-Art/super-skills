---
name: stable-diffusion-3-5-prompts
description: Generate optimized prompts for Stable Diffusion 3.5 (SD3.5) — Stability AI's open-weight image generation family including SD3.5 Large (8.1B, maximum quality), SD3.5 Large Turbo (8.1B, 4-step fast generation), and SD3.5 Medium (2.5B, consumer hardware and LoRA fine-tuning). Use this skill whenever a user mentions SD3.5, Stable Diffusion 3.5, stabilityai/stable-diffusion-3.5, or asks for prompts targeting ComfyUI, Automatic1111, Replicate, AWS Bedrock, or the Stability AI API with SD3.5 models. Also trigger for natural language scene composition, text rendering with double-quote syntax, guidance scale tuning, art style prompting without artist names, IP-Adapter reference consistency, ControlNet structural guidance, or LoRA fine-tuning on SD3.5 Medium. Always use this skill — SD3.5 requires CFG 4.4 (not SDXL's 7–9), no prompt weighting syntax, and minimal negative prompts.
---

# Stable Diffusion 3.5 Prompt Generator

Generate optimized prompts for SD3.5's MMDiT architecture — which uses three text encoders (2× CLIP + T5-XXL), understands natural language natively, and requires a fundamentally different parameter approach than SDXL.

## Which Variant Are You Targeting?

| Variant | Params | Use When | Steps | CFG |
|---------|--------|---------|-------|-----|
| **SD3.5 Large** | 8.1B | Maximum quality, complex scenes | 20–35 | **4.4** |
| **SD3.5 Large Turbo** | 8.1B | Speed, batch work, rapid iteration | **4 exactly** | 1.0 |
| **SD3.5 Medium** | 2.5B | Consumer hardware, LoRA fine-tuning | 20–30 | **4.4** |

**Turbo rule:** Use exactly 4 steps and simple prompts. Turbo underperforms with complex, detailed prompts.

## The Official 7-Element Structure

Stability AI's recommended prompt order:

```
[Style/Medium] → [Subject + Action] → [Composition/Framing] → [Lighting/Color] → [Technical/Camera] → ["Text in quotes"] → [Negative Prompt]
```

**Style goes first** — placing the art style/medium at the beginning produces stronger stylistic influence than appending it at the end.

✅ **Stronger:** `"Art Nouveau drawing of a beautiful redhead sitting at an outdoor bar"`  
⚠️ **Weaker:** `"A beautiful redhead sitting at an outdoor bar. In the Vienna Secession style, an Art Nouveau drawing"`

## Natural Language vs. Keywords — Both Work

| Approach | Example | Best For |
|----------|---------|---------|
| **Natural Language** | "A woman stands at the edge of a stormy ocean cliff, beneath a cherry blossom tree. The tree drops countless pink petals into the sea below." | Complex scenes, spatial relationships, narrative |
| **Keywords** | "woman, ocean cliff, cherry blossom tree, pink petals, stormy, oil painting, expressionism" | Quick iterations, simple subjects |

The T5-XXL encoder parses sentence structure — natural language handles spatial relationships and multi-element scenes better than keyword lists.

## Why SD3.5 Needs Its Own Skill

SD3.5's MMDiT + T5-XXL architecture differs fundamentally from SDXL. Three SDXL habits that actively degrade SD3.5 output:
- **Prompt weighting** `(keyword:1.2)` — silently ignored; restructure with positional emphasis instead
- **CFG 7–9** — causes artifacts and illogical details; use **4.4** as default
- **Long negative prompts** — the SDXL boilerplate negative often makes SD3.5 output worse; start with none

## The Three Hard Rules

**1. No prompt weighting.** `(keyword:1.2)` is silently ignored. Emphasize by moving elements earlier, adding descriptive detail, or using natural language: "very detailed fur" not "(fur:1.4)".

**2. Minimal negative prompts.** Less is better. The standard SDXL negative ("deformed, disfigured, ugly, blurry, worst quality...") often hurts in SD3.5. Start with no negative prompt; add only if specific issues appear.

**3. CFG default is 4.4 — not 7–9.** SDXL's CFG range causes artifacts and illogical details in SD3.5. Start at 4.4.

## Text Rendering Syntax

Enclose exact text in **double quotation marks** within the prompt:

```
The neon bar light reads "And So It Was" in red, its light reflects in the water.
```

Keep text short — single words or short phrases. Longer strings may produce spelling errors.

## Token Budget Awareness

The first ~77 tokens carry the most weight (CLIP encoders). T5-XXL processes longer context but with diminishing positional weight. **Critical information must go in the first 77 tokens (~60 words).**

Order of importance:
1. Style/medium (first)
2. Subject and primary action
3. Key composition and lighting
4. Atmosphere and detail
5. Text to render
6. Supporting environmental detail

## Prompt Lengths by Use Case

| Use case | Target length | Notes |
|----------|--------------|-------|
| Turbo quick generation | 5–15 words | Simpler prompts work better on Turbo |
| Standard Large / Medium | 30–80 words | Optimal balance |
| Complex multi-element scenes | 80–200 words | Requires logical spatial ordering |

## Describe Styles, Don't Name Artists

Artist names work unpredictably in SD3.5 — some influence style, others are ignored.

✅ **Reliable:** `"painted in ink wash and watercolor with fine line work"`  
❌ **Unpredictable:** `"in the style of Ivan Bilibin"`

Use visual descriptions of medium, technique, and aesthetic instead.

## Reference Files

Load these when you need depth on a specific topic:

- **[parameters.md](parameters.md)** — Complete API parameter tables for all three variants, CFG deep-dive with value table, inference steps recommendations, all 9 aspect ratios with pixel dimensions, resolution limits per variant, output formats, platform availability (Replicate, AWS Bedrock, ComfyUI, A1111), and SDXL → SD3.5 migration checklist.

- **[best-practices.md](best-practices.md)** — Scene description ordering discipline, what to emphasize (materials/textures, lighting, camera terms, mood), what to avoid (weighting syntax, quality boosters, artist names, long negative prompts), common mistakes table with fixes, consistency strategies (seed locking, "prune it out" rule), style anchoring, and art style + subject compatibility notes.

- **[continuity-and-references.md](continuity-and-references.md)** — Seed-based reproducibility workflow, image-to-image mode with `prompt_strength` guidance, IP-Adapter for reference-image consistency (ipadapter_scale, style/character/object modes), ControlNet modules (Canny, Tile, Pose), LoRA fine-tuning on SD3.5 Medium, and multi-shot consistency strategies combining all tools.

- **[examples.md](examples.md)** — 7 fully annotated examples: text rendering, environmental portrait with neon text, dynamic action/cyberpunk, Art Nouveau illustration, complex fantasy portrait, caricature/3D cartoon, and product still life. Includes quick-start templates by content type and a pre-generation checklist.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
