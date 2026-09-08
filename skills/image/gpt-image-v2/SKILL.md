---
name: gpt-image-2-prompts
description: Generate optimized prompts for OpenAI's GPT Image 2 (gpt-image-2) — the flagship OpenAI image model, released April 2026, with Thinking Mode, multilingual text rendering, resolutions up to 4K, web search grounding, and multi-image editing (up to 16 references). Use this skill whenever a user mentions GPT Image 2, gpt-image-2, ChatGPT Images 2.0, or OpenAI image generation, or asks for image prompts involving text rendering (menus, signage, UI copy, labels), UI/app mockups, infographics, technical diagrams, character consistency across scenes, multi-image compositing, virtual try-on, product photography, or any task targeting the OpenAI API. Also trigger for requests involving the Thinking Mode parameter, flexible aspect ratios, quality tiers (low/medium/high), or edit-over-regenerate workflows. Always use this skill instead of guessing at GPT Image 2 prompt structure from general knowledge — its six-element framework, Thinking Mode triggers, and text rendering rules are model-specific.
---

# GPT Image 2 Prompt Generator

Generate optimized prompts for OpenAI's `gpt-image-2` — the current flagship image model with a reasoning layer (Thinking Mode), near-perfect multilingual text rendering, and flexible resolutions up to 4K.

## The One Rule That Overrides Everything

**Describe the image, not the feeling about it.** Every element in a prompt should be something the model can visually render. Replace vague praise with visual facts.

❌ **Weak:**
```
A stunning ultra-detailed cinematic masterpiece of a woman in a museum, beautiful, photoreal, 8K, award-winning.
```

✅ **Strong:**
```
Scene: A quiet classical museum gallery in soft afternoon light.
Subject: A woman in her 30s standing in front of a large oil painting.
Important details: Natural smile, realistic skin texture, beige knit sweater, dark jeans, eye-level full-body framing, marble floor reflections, shallow depth of field.
Use case: Editorial lifestyle photograph.
Constraints: No watermark, no logos, no heavy retouching.
```

## The Six-Element Framework

For generation prompts, use this ordered structure:

```
Scene:
[Where it happens, time of day, environment, background]

Subject:
[Who or what is the main focus — scale, pose, gaze, action]

Important details:
[Materials, textures, clothing, lighting direction/quality, camera angle, lens feel, composition, mood]

Use case:
[editorial photo / product mockup / poster / UI screen / infographic / concept frame]

Constraints:
[no watermark / no logos / no extra text / preserve face / no heavy retouching]
```

## Edit Prompts (Two-Column Structure)

For the `/v1/images/edits` endpoint with reference images:

```
Change:
[Exactly what should change]

Preserve:
[face, identity, pose, lighting, framing, background, geometry, text, layout]

Constraints:
[no extra objects, no redesign, no logo drift, no watermark]
```

**Three-sentence edit pattern:**
1. What changes: "Replace the parked car with a vintage bicycle."
2. What stays locked: "Preserve the house, fence, driveway, landscaping, lighting direction, and time of day exactly."
3. Physical realism: "Match the bicycle scale and shadow pattern to the existing scene."

## Text Rendering Rules

GPT Image 2 has near-perfect text rendering — but only when formatted correctly:

- Wrap literal text in **quotation marks** or write in **ALL CAPS**
- Specify font style, size, color, and placement explicitly
- Spell out hard-to-spell words letter-by-letter if critical
- Add `"no extra words, no duplicate text"` to Constraints
- Use `quality: "high"` + `thinking: "medium"` for dense text layouts

**Example:**
```
Menu board text — BREAKFAST, GRIDDLE, SANDWICHES, SIDES, DRINKS, and daily special reading "CHICKEN FRIED STEAK 8.25". Type must be 100% readable and physically believable.
```

## Thinking Mode — Quick Decision Rule

**If the prompt contains a number, a label, or a positional constraint → move up one thinking tier.**
**If the prompt is purely atmospheric → drop a tier or use `off`.**

| Level | When to use |
|-------|------------|
| `off` | Creative/loose prompts, landscapes, abstract art |
| `low` | Product shots, hero images, standard portraits |
| `medium` | Infographics, UI mockups, scenes with counted elements, dense text |
| `high` | Complex multilingual layouts, strict technical diagrams |

## Endpoint Summary

| Task | Endpoint | Key parameter |
|------|----------|--------------|
| Generate from text | `POST /v1/images/generations` | `model: "gpt-image-2"` |
| Edit with references | `POST /v1/images/edits` | `image_urls` (1–16 images) |

**Critical:** `background: "transparent"` is **NOT supported** on `gpt-image-2`. Use `"opaque"` or `"auto"`, then post-process for transparency.

## Workflow: Ideation → Production

1. **Draft at `quality: "low"`** — fast and cheap, calibrate composition
2. **Iterate with single-change edits** — never regenerate from scratch (primary source of character/brand drift)
3. **Final at `quality: "high"`** with appropriate `thinking` level
4. **Cache output bytes immediately** — response URLs expire in 1 hour

## Multi-Image Reference Labeling

When using the edit endpoint with multiple images, label each by role:

```
Image 1: base scene to preserve.
Image 2: jacket reference.
Image 3: lighting/style reference.

Dress the subject from Image 1 using the jacket from Image 2. Apply Image 3's lighting approach. Preserve face, pose, background, and framing exactly.
```

## Reference Files

Load these when you need depth on a specific topic:

- **`parameters.md`** — Complete API parameter tables for both generation and edit endpoints, all `size` values, quality/cost matrix, resolution constraints, rate limits, output formats, pricing, and API code examples (Python).

- **`best-practices.md`** — Anti-slop rules, composition techniques by content type (editorial, product, UI, people), common mistakes table with fixes, syntax rules, living artist moderation avoidance, session noise bug workarounds, and the edit-over-regenerate discipline.

- **`continuity-and-consistency.md`** — Character consistency strategy (DNA Template, anchor image workflow, close-up reference technique), image-to-image / reference image workflows, style transfer patterns, seed-based reproducibility, batch generation for coherent variants, iterative editing strategy, and multi-scene storyboard setup.

- **`examples.md`** — 7 fully annotated example prompts covering: photoreal editorial portrait, children's book character consistency, documentary landscape, text rendering (diner menu), UI mockup (mobile app), quiet still life, and multi-image virtual try-on compositing. Includes quick-start templates for the most common use cases.
