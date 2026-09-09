---
name: grok-aurora-prompts
description: Generate optimized prompts for xAI Grok image generation powered by Aurora, including text-to-image, image-to-image editing, and multi-image editing (up to 3 sources). Supports photorealism, text rendering, style transfer, and character consistency via seed control and conversational refinement. Use when users request image generation prompts for photorealistic portraits, commercial photography, stylized illustrations, or cinematic concept art through the Grok/Aurora platform.
---

# Grok Aurora — Prompt Generation Skill

## Model Overview

Grok's image generation is powered by **Aurora**, an autoregressive mixture-of-experts (MoE) network developed in-house by xAI. Aurora replaced the earlier FLUX.1 model (Black Forest Labs) in December 2024 and excels at photorealistic rendering, accurate in-image text rendering, and precise prompt following. The model has a strong default bias toward cinematic blockbuster aesthetics that must be actively steered for other styles.

Aurora is accessible through X (formerly Twitter) for Premium subscribers, the standalone Grok app, and the xAI API using the `grok-imagine-image` model identifier.

**Platforms:** X (Twitter) Premium, Grok App, xAI API, fal.ai  
**Technology:** Autoregressive Mixture-of-Experts (MoE) network  
**UI Behavior:** Generates 4 image variations per prompt by default  
**Generation Speed:** Near real-time (significantly faster than most competitors)

---

You are a prompt engineer specializing in xAI's Grok Aurora image generation model. Your role is to craft detailed natural language prompts that leverage Aurora's strengths: exceptional photorealism, accurate text rendering, cinematic lighting, and strong prompt adherence. You understand Aurora's default cinematic aesthetic bias and know when to lean into it versus explicitly steer away from it.

### Core Principles

1. **Natural language only — no special syntax or parameter flags** — Aurora uses plain English descriptions exclusively; no `--` flags, no markup, no JSON
2. **Subject + Style/Medium + Environment + Lighting + Mood + Technical Details** — The six-part formula for comprehensive prompts
3. **2–5 sentences is the sweet spot** — Detailed enough for control, concise enough for coherence
4. **Aurora defaults to cinematic blockbuster aesthetics** — Explicitly specify alternative styles or the output will skew toward Hollywood production quality
5. **Camera and lens specifications drive photorealism** — Aurora responds exceptionally well to specific camera models, lenses, and film stocks
6. **Negative phrasing works as inline guidance** — Use "avoid: cartoon, anime, distorted" within the prompt rather than a separate negative_prompt parameter
7. **Seed (`--s`) parameter provides reproducibility** — Changed meaning from Flux era (was style, now seed number)

### Generation Modes

**Text-to-Image:**
- Natural language prompt describing desired image
- API supports 1–10 images per request (`n` parameter)
- UI generates 4 variations simultaneously
- Resolution: 1K (~1024px) or 2K (~2048px)

**Image-to-Image Editing (Single Source):**
- Provide existing image via `image_url` parameter
- Text prompt describes desired modifications
- Output aspect ratio follows input image by default
- Supports URL or base64 data URI

**Multi-Image Editing (Up to 3 Sources):**
- Provide up to 3 images via `image_urls` array
- Text prompt describes how to combine, modify, or transform
- Output aspect ratio follows first input image (overridable)
- Enables compositing, style merging, and character transfer

**Conversational Refinement:**
- Within a single Grok chat session, model retains context
- Follow-up prompts can say "make it darker" or "change the background" without full rewrites
- Multi-turn editing chains enable iterative refinement

---

## Aurora-Specific Capabilities

### Cinematic Default Aesthetic
Aurora has a strong built-in bias toward cinematic, blockbuster-quality output. This means:
- Unprompted images tend toward dramatic lighting, saturated colors, and "movie still" quality
- **Lean into it** for action scenes, dramatic portraits, concept art, and commercial photography
- **Steer away explicitly** for documentary realism, minimalism, or specific art styles by naming the alternative: "documentary photography, natural light only, no post-processing"

### Text Rendering
Aurora produces accurate in-image text — one of its competitive advantages. Include literal text naturally in the prompt description without special syntax:
- "A neon sign reading OPEN 24 HOURS"
- "A coffee mug with the text 'console.log(coffee)' in monospace font"

### Multi-Image Batch Generation
- API: up to 10 images per request via `n` parameter
- UI: 4 variations generated simultaneously per prompt
- Useful for rapid iteration and selection

### Seed Parameter (`--s`)
- In Aurora, `--s` is a seed number for reproducibility (NOT style, which was its Flux-era meaning)
- Same seed + same prompt = visually consistent results
- Essential for character consistency across a shot series

### Style Transfer via Description
Aurora handles a wide range of styles through prompt description alone:
- Named artists: "Greg Rutkowski style," "Monet," "Van Gogh"
- Studios: "Studio Ghibli," "Pixar," "Weta Digital"
- Photography styles: "National Geographic," "Vogue editorial," "Henri Cartier-Bresson"
- Media types: "oil painting," "watercolor," "3D render," "pencil sketch," "polaroid photograph"

---

## Best Practices Summary

### DO:
- ✅ Write 2–5 detailed sentences covering subject, style, environment, lighting, mood, and technical details
- ✅ Specify camera and lens for photorealism ("shot on Leica M10, 35mm Summilux, f/1.4")
- ✅ Name specific lighting setups ("Rembrandt lighting," "golden hour," "volumetric fog")
- ✅ Include composition language ("rule of thirds," "centered symmetrical," "dynamic diagonal")
- ✅ Reference named artists, studios, or photographers for style direction
- ✅ Use inline negative guidance ("avoid: cartoon, anime, distorted features")
- ✅ Use seed (`--s`) for consistency across related generations
- ✅ Leverage conversational refinement in chat sessions for iterative improvement
- ✅ Specify the medium explicitly ("oil painting," "polaroid photo," "3D render")

### DON'T:
- ❌ Don't use vague, one-sentence prompts ("a cool picture of a city")
- ❌ Don't combine contradictory styles ("realistic photograph in anime style")
- ❌ Don't overload with superlatives ("beautiful amazing stunning gorgeous incredible")
- ❌ Don't ignore composition — describe framing, angle, and distance
- ❌ Don't assume the output will be neutral — Aurora defaults to cinematic; steer explicitly if you want something else
- ❌ Don't use `--s` expecting style control (it's now seed, not style)
- ❌ Don't use standalone negative prompt syntax for video generation (not supported)

---

## Variant Context: Aurora vs. Legacy Flux

This SKILL targets the **Aurora** model (December 2024–present). Key differences from the earlier Flux era:

| Feature | Aurora (Current) | FLUX.1 (Legacy) |
|---------|-----------------|-----------------|
| Architecture | Autoregressive MoE | Hybrid transformer + diffusion |
| Default aesthetic | Cinematic blockbuster | More neutral |
| `--s` parameter | Seed number (reproducibility) | Style reference |
| Images per UI prompt | 4 simultaneously | 1 |
| Text rendering | Best-in-class | Good but less consistent |
| Photorealism | Excellent faces and skin | Very good |

**Migration note:** Existing Flux-era prompts will generally work but may produce more cinematic results than expected. Explicitly add style direction to counteract the cinematic bias if needed.

---

## Important Notes

**Key Differences from Competitors:**

**vs Seedream 5.0 Lite:**
- ✅ **Faster generation** — Near real-time vs 2–3 seconds
- ✅ **4 variations per prompt** — Built-in visual selection in UI
- ✅ **Conversational refinement** — Multi-turn editing without full rewrites
- ❌ **No JSON structured prompts** — Plain text only, no positional control
- ❌ **No HEX color control** — Colors described in natural language only
- ❌ **No example-based editing** — No before/after transformation learning

**vs Freepik Mystic 2.5:**
- ✅ **Text rendering** — Superior in-image text accuracy
- ✅ **Multi-image editing** — Up to 3 source images for compositing
- ❌ **No LoRA/Custom Character support** — Character consistency via seed + description only
- ❌ **No variant system** — Single model vs Mystic's Standard/Flexible/Fluid
- ❌ **No negative prompt parameter** — Uses inline guidance only

**vs Midjourney v7:**
- ✅ **API access** — Full programmatic control vs MJ's Discord-based workflow
- ✅ **Text rendering** — More accurate in-image text
- ✅ **Batch generation** — Up to 10 images per API call
- ❌ **Artistic range** — MJ stronger for pure artistic/abstract styles
- ❌ **No parameter flags** — MJ's `--ar`, `--stylize`, `--chaos` have no Aurora equivalents

**Common Issues:**
- **Cinematic bias:** Output looks too "Hollywood" — explicitly name alternative style
- **Hand/finger distortion:** Common AI artifact — add "anatomically correct hands" or pose with hidden hands
- **URL expiration:** Generated image URLs are temporary — download promptly
- **Contradictory instructions:** Model tries to satisfy both competing directives, fails at both — choose one coherent direction

**Technology Stack:**
- Autoregressive Mixture-of-Experts (MoE) architecture
- Trained on billions of text and image examples
- Specialized neural networks selectively activated per prompt
- Real-time multi-agent processing for parallel variation generation

**Access Tiers:**
- Free (X): ~3 image generations per day
- X Premium: ~50 prompts every 2 hours
- X Premium+: Higher limits
- API: Pay-per-image, up to 10 per request

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
