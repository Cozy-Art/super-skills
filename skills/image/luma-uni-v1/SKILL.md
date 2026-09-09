---
name: luma-uni-1-prompts
description: Generate optimized prompts for Luma Uni-1.1, the reasoning image model powering the Luma Agents API. Use this skill whenever a user mentions Luma Uni-1, Uni-1.1, Luma image generation, or the Luma Agents API, or asks for prompts involving character consistency across scenes, multi-reference generation (up to 9 references with explicit role assignment), image editing with structure preservation, manga/anime style generation, spatial reasoning for complex multi-constraint scenes, web-grounded real-world locations, text rendering on signs and surfaces, or the Create vs. Modify mode decision. Also trigger for prompts targeting agents.lumalabs.ai, the uni-1 or uni-1-max model tiers, or workflows chaining Create to Modify for iterative production. Always use this skill — Uni-1.1 is an autoregressive reasoning transformer that reasons before it generates, requiring intent-driven natural language and explicit reference role labels unlike diffusion conventions. Positive-only prompting is mandatory.
---

# Luma Uni-1.1 Prompt Generator

Generate optimized prompts for Luma Uni-1.1 — an autoregressive reasoning transformer that **reasons before it generates**, decomposing prompts and resolving visual constraints before producing output. This architecture rewards intent-driven natural language and punishes vague quality boosters.

## The First Decision: Create or Modify?

Everything starts here. Get this wrong and the output will fight you.

| Mode | `type` | When to use |
|------|--------|------------|
| **Create** | `"image"` | Generating something new; references *inspire* but do not constrain |
| **Modify** | `"image_edit"` | Editing an existing image; structure and composition are *preserved* unless explicitly changed |

**Decision rule:** If output should look like a *version* of your input → `image_edit`. If it should feel *inspired but new* → `image`.

## Positive-Only Prompting (MANDATORY)

Luma's official guidance: **negative prompting creates internal conflicts and produces worse results.** The model is built for positive intent-driven language.

Convert exclusions into positive descriptions:

| ❌ Negative | ✅ Positive replacement |
|------------|------------------------|
| "a room, do not add people" | "an empty, minimalist room with natural light" |
| "a landscape, no cars" | "a pristine, untouched natural landscape with a dense forest and tranquil lake" |
| "don't make it blurry or ugly" | "a high-resolution, professional photograph with cinematic lighting" |
| "futuristic city, not too busy" | "a serene futuristic city with empty streets and glowing buildings at night" |

## Reference Role Syntax (Create Mode)

References only work if you explicitly declare their role. The model will guess without labels — guesses are unreliable.

**Single reference:**
```
Use IMAGE1 ([brief description]) as a [ROLE] reference.
```

**Multi-reference:**
```
Use IMAGE1 as a COLOR PALETTE reference, IMAGE2 as LIGHTING, IMAGE3 as COMPOSITION.
Treat each reference as having authority over its assigned layer only.
```

**Available roles:** Style · Character · Composition · Color palette · Lighting · Texture · Mood

**Character consistency template:**
```
Use IMAGE1 (woman with short copper-red hair, freckles, green eyes, late 20s) as a CHARACTER reference.
Preserve her facial features, hair color, and freckle pattern exactly.
New scene: [describe new environment and action].
```

## Modify Mode Syntax

Two required components — both must be present:

```
Change [specific element(s)]. Update [what changes].
Keep [everything that must stay exactly the same].
```

**Example:**
```
Change the time of day to golden hour. Update sky, light direction, shadows, and color temperature.
Keep all subjects and composition unchanged.
```

## What Uni-1.1 Does Best

This model's primary differentiator is **multi-constraint adherence** — it handles complex simultaneous requirements (spatial, stylistic, referential) where diffusion models partially execute or blend constraints incorrectly.

Lean into:
- Named aesthetics with specificity: `"1970s Italian giallo film poster, high-contrast color blocking"`
- Camera and lens language: `"85mm lens, shallow depth of field, anamorphic lens flare"`
- Cultural visual traditions: manga panels, ukiyo-e, film noir, art house cinema framing
- Exact quoted text for signs and surfaces: `reading "OPEN 24 HRS"`
- Lighting direction, quality, temperature, and time of day — all have measurable effects

Avoid:
- Vague quality terms: "beautiful," "amazing," "high quality," "masterpiece"
- Redundant phrasing (repeating the same concept dilutes rather than reinforces)
- Conflicting instructions (the model partially executes both — resolve before submitting)
- Unlabeled references in Create mode

## Model Selection

| Model | Price (T2I, 2K) | When to use |
|-------|----------------|------------|
| `uni-1` | $0.0404/image | Standard quality; ~31s generation; default |
| `uni-1-max` | $0.1000/image | Higher quality; reference-heavy or detail-critical work |

Use `uni-1-max` for: multi-reference generation, text rendering precision, complex character consistency, final production assets.

## Recommended Prompt Lengths

| Use case | Target length |
|----------|--------------|
| Simple T2I | 80–150 words |
| Reference-guided | 100–300 words |
| Modify / edit mode | 30–100 words |
| Multi-panel / storyboard | 150–300 words |

## Seed Strategy

1. Leave seed unset while exploring directions
2. Find a strong result — note the seed
3. Lock that seed — same seed + same prompt = same result
4. Change **one variable at a time** when iterating
5. Save prompt + seed together as a reusable recipe

> Same seed + changed prompt = controlled variation (not the same image)

## API Endpoint

```
Base URL:  https://agents.lumalabs.ai
Generate:  POST /v1/generations
Poll:      GET  /v1/generations/{id}
Auth:      Authorization: Bearer <LUMA_AGENTS_API_KEY>
```

Output URLs expire after **1 hour** — download promptly.

## Reference Files

Load these when you need depth on a specific topic:

- **`parameters.md`** — Complete API parameter table, all 9 aspect ratios, style preset constraints (manga portrait-only rule), model tier pricing with reference image surcharge table, validation rules, output specifications, failure codes, SDK support, web platform credit pricing, and Photon → Uni-1.1 migration guide.

- **`best-practices.md`** — Prompt depth guidance, weak-vs-strong comparison table, what to emphasize (named aesthetics, camera language, cultural visual traditions, lighting specifics), what to avoid, positive prompting deep-dive with conversion examples, seed strategy, web search grounding guidance, multi-constraint discipline, and the Create → Modify workflow chain.

- **`continuity-and-references.md`** — Character consistency workflow (canonical reference creation, reuse pattern, seed locking), multi-reference architecture for series production (up to 9 references with role assignment), Create → Modify chain workflow, image-to-image layered editing with source + image_ref, multi-panel / storyboard generation, board context retention in the Luma App, and reference pricing breakdown.

- **`examples.md`** — 7 fully annotated examples with complete JSON: simple cinematic landscape, character portrait with reference, multi-reference architecture (3 roles), manga style, text rendering on sign/surface, web-grounded real location, image modification. Includes quick-start templates and a pre-flight checklist.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
