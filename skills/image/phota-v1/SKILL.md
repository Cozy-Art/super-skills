---
name: phota-prompts
description: Generate optimized prompts for PhotaLabs Phota, an identity-preserving AI photo generation and editing system. It uses trained personal profiles ([[profile_id]]) to preserve exact facial bone structure, expressions, and features across every generation and edit. Supports Generate (text-to-photo), Edit (image modification with identity lock), and Enhance (zero-prompt quality improvement) modes. Use when users need portrait photography, headshots, expression fixes, group shot compositing, or any scenario requiring a real person's likeness to be preserved accurately.
---

# Phota — Identity-Preserving Photo Generation Skill

## Model Overview

Phota is an identity-preserving AI photo generation and editing system built by PhotaLabs (founded by former Adobe researchers, backed by a16z). Unlike general-purpose image models that produce "someone who looks like you," Phota trains a **private personal model (profile)** from 30–50 of your photos, then preserves your exact bone structure, expressions, and features across every edit and generation.

This is the rare image skill where the prompt does NOT describe what the person looks like. The profile carries identity; every word of the prompt is freed for creative direction — lighting, framing, expression, setting.

**Platforms:** Phota Studio (studio.photalabs.com), PhotaLabs API, fal.ai (`fal-ai/phota`), WaveSpeed AI, GenAIntel  
**Technology:** Identity-preserving diffusion model with private per-person profile training  
**Profile Training:** 30–50 photos → ~15 minutes → permanent reusable `profile_id`  
**Backed By:** Andreessen Horowitz ($5.6M seed)

---

You are a prompt engineer specializing in PhotaLabs Phota, an identity-preserving AI photo generation system. Your role is to craft prompts that read like a portrait photographer's creative brief — specifying lighting setup, lens feel, framing, expression, and setting — while NEVER describing what the person looks like. The trained profile (`[[profile_id]]`) carries all identity information; your prompt handles everything else.

### Core Principles

1. **Never describe the person's appearance when using a profile** — The profile preserves bone structure, features, and expression range far more accurately than any text description. Every word spent on hair color or eye shape is wasted.
2. **Prompt like a photographer's brief** — Lighting direction, lens feel, framing, expression, and setting. "Soft key light from upper left, 85mm lens look, shallow depth of field" is the language Phota responds to best.
3. **`[[profile_id]]` must be explicitly referenced** — Uploading a profile does NOT activate it. You must include `[[profile_id]]` in every prompt text.
4. **One change per pass** — Stacking 12 simultaneous edits introduces compounding errors. Change one element per generation and iterate.
5. **Edit mode: declare what stays, then what changes** — "Keep identity/pose/framing unchanged. Change only [this specific thing]."
6. **Generate mode: photographic language over abstract style words** — "Chiaroscuro lighting from camera right" outperforms "cinematic" or "professional."

### Three Operating Modes

**Generate Mode:**
- Text prompt + profile references → new photograph
- Full creative brief: subject identity, setting, lighting, style
- Use for: new headshots, portraits, creative scenes, character concepts

**Edit Mode:**
- 1+ input images + text prompt → modified photograph
- Prompt describes what to change ONLY; what to preserve is explicit
- Use for: expression fixes, lighting adjustments, adding/removing people, compositing

**Enhance Mode:**
- Image only → automatically improved photograph
- NO prompt required
- Use for: quality improvement (light, noise, sharpness, color grading consistency)

---

## Phota-Specific Capabilities

### The `[[profile_id]]` System
- Train a private model from 30–50 photos of a person (or pet)
- ~15 minutes training time, ~$2.90 per training run (fal.ai)
- Profile preserves exact bone structure, expressions, and features
- One profile per person — works across all scenes, styles, and conditions
- Profiles are permanent, private, and reusable indefinitely
- Multi-profile generations: `[[abc123]] and [[def456]]` for group shots

### Identity Lock Phrases
These phrases consistently improve identity fidelity in both Generate and Edit modes:

| Situation | Phrase to Add |
|-----------|--------------|
| Prevent face drift | "Preserve identity and facial features exactly" |
| Lock pose/framing | "Keep camera angle and crop the same" |
| Prevent composition changes | "Preserve the original framing and background" |
| Maintain expression baseline | "Keep the same expression, modify only [X]" |
| Preserve clothing | "Clothing and hairstyle unchanged" |

### Multi-Person Group Shots
1. Ensure both subjects have trained profiles
2. Collect 1–2 reference photos of each person
3. Upload as input images
4. Reference both profiles: `[[id1]] and [[id2]]`
5. Describe composition, spatial relationship, and lighting match
6. Add: "appears as if photographed together in the same moment"

### Memory Rescue Workflow
Phota uniquely restores old, damaged, or technically poor photos:
- Supply a degraded reference image AND a `[[profile_id]]`
- Phota uses the profile to lock identity even from blurry/poorly lit source
- Edit prompt fixes quality while preserving the person's likeness

### Enhance Mode (Zero-Prompt)
- No prompt required — automatic quality improvement
- Corrects: lighting, exposure, noise, blur, color grading, compression artifacts
- Ideal for making an entire photo album visually consistent
- No risk of identity drift from prompt errors

---

## Best Practices Summary

### DO:
- ✅ Reference `[[profile_id]]` explicitly in every prompt
- ✅ Write prompts like a photographer's brief (lighting, lens, framing, expression, setting)
- ✅ Specify expression explicitly ("warm natural smile," "confident direct gaze," "introspective, slightly off-camera")
- ✅ Use photographic lighting language ("soft key light from upper left," "chiaroscuro," "rim light on hair")
- ✅ Include camera/lens feel ("85mm lens look, shallow depth of field," "medium format feel")
- ✅ Describe background/setting clearly ("clean neutral gray," "blurred office environment," "soft outdoor bokeh")
- ✅ Use identity lock phrases when editing ("Preserve identity and facial features exactly")
- ✅ Change one element per pass and iterate
- ✅ Train profiles with varied angles, lighting, and expressions (30–50 photos)
- ✅ Add "Photoreal, no plastic smoothing, no over-retouching" for natural output

### DON'T:
- ❌ Don't describe the person's physical appearance — the profile handles this
- ❌ Don't use vague style words alone ("cinematic," "professional," "beautiful") — follow with specifics
- ❌ Don't stack multiple changes in one edit prompt
- ❌ Don't forget to include `[[profile_id]]` — uploading alone doesn't activate it
- ❌ Don't use negative prompt syntax — Phota doesn't document this parameter
- ❌ Don't train profiles with sunglasses, heavy filters, or face-obscuring accessories
- ❌ Don't train from identical poses — variety in training photos is critical

---

## Prompt Formula by Mode

The formula is the prompt text itself. Everything else — mode, resolution, aspect ratio, image count,
output format — is a setting the director sets in their own tool, and belongs nowhere in the prose.

**Generate:**
```
[Portrait style] + [[profile_id]] + [framing] + [expression/pose] +
[lighting] + [background/setting] + [technical/lens look]
```

**Edit** — one change per pass, and say explicitly what is locked:
```
Keep [what stays unchanged]. [What changes — one change per pass].
```

**Enhance:** no prompt required. The pass operates on the source image alone.

---

## Important Notes

**Phota is fundamentally different from every other image generation SKILL.**

The core difference: identity is solved by the profile, not the prompt. This inverts the prompting paradigm:

| Other Image Models | Phota |
|--------------------|-------|
| Describe person's appearance in prompt | Profile handles identity — never describe appearance |
| Character consistency via locked description + seed | Character consistency via `[[profile_id]]` — guaranteed |
| Prompt carries ALL visual information | Prompt carries lighting, framing, expression, setting ONLY |
| One-shot generation | Profile-based: train once, generate infinitely |
| No real-person fidelity | Exact bone structure, expression range preservation |

**Key Differences from Competitors:**

**vs Seedream 5.0 / Grok Aurora / Freepik Mystic:**
- ✅ **Guaranteed identity preservation** — No character drift between shots
- ✅ **Real-person photography** — Not "someone who looks like you" but actually you
- ✅ **Multi-person group compositing** — Multiple profiles in one generation
- ✅ **Memory rescue** — Restore degraded photos with identity lock
- ❌ **Portrait/people only** — Not for landscapes, products, fantasy, or abstract art
- ❌ **Requires profile training** — 30–50 photos + 15 min setup per person
- ❌ **No negative prompts** — Positive constraint language only
- ❌ **No JSON structured prompts or HEX color control**

**vs Hunyuan3D V3:**
- Completely different domains — Phota is 2D portrait photography; Hunyuan3D is 3D mesh generation

**Common Issues:**
- **Output doesn't look like the person:** Profile not referenced in prompt — add `[[profile_id]]`
- **Wrong person generated:** Group photos in training — retrain with solo photos only
- **Identity drift between edits:** Too many changes in one prompt — one change per pass
- **Generic look:** Vague style words — replace with specific lighting recipe
- **Awkward expression:** Expression not specified — add "warm natural smile" or "confident, direct gaze"
- **Group shot looks composited:** Missing lighting match — add "Match lighting and perspective of Image 1"

**Technology:**
- Identity-preserving diffusion model
- Private per-person profile training
- Built on Nano Banana / Gemini 3 Pro Image foundation
- Founded by former Adobe researchers

## Reference Files

Load these when you need depth on a specific topic:

- [parameters.json](parameters.json) — Complete API specs, profile training requirements (30–50 photos), operating-mode definitions, and platform access tiers.
- [best-practices.md](best-practices.md) — The inverted prompt paradigm (the profile carries identity, so the prompt carries the photographer's brief), profile training optimization, edit workflows, and identity-lock techniques.
- [examples-generate.md](examples-generate.md) — 14 annotated Generate-mode examples across the recurring example projects, each spending zero words describing the subject's appearance.
- [examples-edit-enhance.md](examples-edit-enhance.md) — 10 annotated examples for Edit mode (expression fixes, lighting adjustment, group compositing, memory rescue) and zero-prompt Enhance mode.
- [schema.json](schema.json) — Output validation schema for Generate, Edit, and Enhance output, with the `mode` enum and identity-preserving profile references.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
