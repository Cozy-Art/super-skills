---
name: ltx-2-prompts
description: Generate optimized prompts for Lightricks LTX-2 Fast and Pro — the open-source production video model (19B parameters, 14B video + 5B audio) that generates synchronized video and audio in a single pass. Use this skill whenever a user mentions LTX-2, LTX Video, LTX-2.3, Lightricks video generation, or asks for prompts targeting ltx.io, fal.ai, WaveSpeed AI, or Runware with LTX models. Also trigger for workflows involving native audio generation (ambient, SFX, dialogue in quotes), Fast vs. Pro mode selection, sequential phase prompting for clips up to 20 seconds, image-to-video with first/last frame interpolation, video chaining for longer sequences, seed locking for style continuity, or LoRA character fine-tuning. Always use this skill — LTX-2 requires a single flowing paragraph format (not keyword lists), present-tense verbs, physical cues over emotional labels, explicit negative-space animation, and temporal distribution of motion across the clip duration.
---

# LTX-2 Fast & Pro Prompt Generator

Generate optimized prompts for LTX-2 — the only production model with **native single-pass audio-video generation**. Released January 2026; covers versions 2.0, 2.1, and 2.3 (identical prompting principles across all).

## The One Rule That Overrides Everything

**Write a single flowing paragraph.** This is not aesthetic preference — it is a functional requirement. LTX-2's language model architecture is optimized for narrative flow, not keyword grids. Fragmented or bullet-style prompts produce measurably lower fidelity output.

## The First Decision: Fast or Pro?

| Scenario | Mode |
|----------|------|
| First draft, concept exploration | **Fast** |
| Batch-testing 3–5 prompt variations | **Fast** |
| Social content, short-form | **Fast** |
| Duration > 10 seconds required | **Fast** (only option) |
| Hero shot, client deliverable | **Pro** |
| Character close-up with facial nuance | **Pro** |
| Product demo for marketing | **Pro** |
| Found direction with Fast, now need polish | **Pro** |

> "There is a much bigger disparity between LTX-2 Pro and LTX-2 Fast compared to the difference between competing models' standard and fast variants." — Independent benchmark. Plan credit budget accordingly.

## T2V vs. I2V Prompt Strategy

| Mode | Prompt must describe | What to omit |
|------|---------------------|-------------|
| **Text to Video** | All 6 elements — scene, character, action, camera, style, audio | Nothing — build the complete world |
| **Image to Video** | Motion only — what changes, camera behavior, light shifts | Subject appearance (already in image) |

**Redundant description is the #1 I2V mistake.** Restating what's visible in the reference image wastes the model's token budget on information it already has.

❌ `"A red car parked on a cobblestone street in the rain"`  
✅ `"The camera pans slowly across the car's profile as reflections shift across the polished surface."`

## The Official Six-Element Structure (T2V)

```
1. Establish the Shot   → genre, shot scale, visual category
2. Set the Scene        → lighting, color palette, textures, atmosphere
3. Describe the Action  → core action as a natural sequence, beginning to end
4. Define Character(s)  → age, hair, clothing, features, emotion via PHYSICAL CUES
5. Camera Movement(s)   → how and when camera moves, what appears after motion
6. Describe Audio       → ambient, SFX, music, or spoken dialogue in "quotes"
```

**All six elements combined into one flowing paragraph.**

## Critical Rules

**1. Physical cues only — never emotional labels.**
❌ `"She is sad"` → ✅ `"Eyes downcast, lips pressed together, shoulders slightly hunched"`
❌ `"Beautiful lighting"` → ✅ `"Side lighting from a single practical source, warm 3200K, deep shadow on one side"`

**2. Animate negative space — always.**
Static regions (sky, water, plain backgrounds) freeze if not explicitly animated:
- `"clouds drift slowly overhead"` — prevents frozen sky
- `"ripples spread across the water surface"` — prevents frozen water
- `"curtains sway gently in a slight breeze"` — prevents frozen background

**3. Distribute motion across the full duration.**
Front-loaded prompts produce all motion in the first 2–3 seconds, then drift. Use sequential phase language:
```
"Initially, the camera holds steady. After a moment, it begins a slow dolly.
As the sequence continues, the subject turns toward the light."
```

**4. Dialogue goes in quotation marks.**
`She says quietly: "This one."` — triggers synchronized lip-sync. Specify language/accent if needed.

**5. No negative prompts** — use artifact-targeting positive language instead:
❌ `"no frozen background"` → ✅ `"clouds drift overhead throughout the scene"`

## Prompt Length

| Use case | Target |
|----------|--------|
| Simple character moment | 4–6 sentences |
| Standard production clip | 6–8 sentences |
| Complex 20-second sequence | 8–12 sentences with phase markers |

10,000-character limit — practical maximum before diminishing returns is ~8 sentences.

## Reference Files

Load these when you need depth on a specific topic:

- **`parameters.md`** — Complete API parameter table, Fast vs. Pro spec comparison, all resolution and aspect ratio options, audio generation behavior, FPS options, output formats, credit costs, and Fast vs. Pro decision framework with scenario table.

- **`best-practices.md`** — Single paragraph format discipline, physical cues deep-dive with conversion table, camera vocabulary with intensity qualifiers, negative space rule, detail-to-scale matching, strengths and known limitations, iteration workflow (6-step), sequential phase prompting for extended clips, style anchoring, and troubleshooting table.

- **`continuity-and-references.md`** — I2V as primary consistency tool (supported formats, resolution by mode), first/last frame interpolation (2.3 Fast only), video chaining workflow for sequences beyond max duration, seed locking for cross-shot style continuity, LoRA fine-tuning (recommended config: size 16, lr 0.0002, 960×576@24fps), and the Grid Method for character consistency without LoRA training.

- **`examples.md`** — 5 fully annotated example prompts: simple character moment (T2V), breaking news broadcast with dialogue (T2V), product orbit (I2V), atmospheric walkthrough with negative space, and multi-phase 20-second complex sequence. Includes quick-start templates by use case and a pre-generation checklist.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
