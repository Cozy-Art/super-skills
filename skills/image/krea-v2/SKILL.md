---
name: krea-2-prompts
description: Generate optimized prompts for Krea AI's Krea 2 — a text-to-image and image-to-image model with three hosted tiers, aesthetic sliders for intensity, complexity and movement, a creativity control spanning raw to high, moodboards, style references and trained LoRA styles. Use this skill whenever a user mentions Krea, Krea 2, K2, or wants an image prompt targeting this model. Also trigger for workflows involving text rendering inside an image, style transfer from reference images, taste-driven generation from a moodboard, or image-to-image refinement from a source. Always use this skill instead of guessing at Krea 2 prompt structure from general knowledge — it has no in-prompt reference syntax at all, three of its request fields are required with no defaults, and several of its documented parameter ranges conflict between Krea's own pages.
---

# Krea 2 Prompt Generator

Generate optimized prompts for Krea AI's Krea 2 — a text-to-image and image-to-image model built around
**taste controls rather than prompt syntax**. Its distinguishing features are a set of aesthetic sliders,
a creativity dial spanning raw to high, and moodboards that carry a look no prompt could describe.

**This skill produces prompt text, not API calls.** The output goes to a person, who pastes it into
whatever tool they are generating with. Every result ships as two clearly separated pieces: the
**prompt** and a short **suggested settings** line for the controls beside it. Never merge the two.

## The One Rule That Overrides Everything

**Settings do not belong in the prompt text.** Aspect ratio, resolution, the sliders, the creativity
level — all of these are controls with their own fields. Writing "1:1" or "high creativity" into the
sentence spends words on something the model reads as description.

## There Is No Reference Syntax — At All

The most important structural fact about this model, and the one that most often produces a broken
prompt carried over from elsewhere.

**Krea 2 has no in-prompt way to point at a reference.** No `@Image1`, no `<IMAGE_1>`, no bracket form,
no "Image 1 is the product" role-assignment convention. Nothing in Krea's prompting guide, user guide
or API schema addresses a reference from prompt text.

Every reference is a **separate attachment**, bound outside the prompt with a numeric strength:

| Attachment | What it carries | Bound by |
|---|---|---|
| **Style references** | The look of one or more images | URL + strength |
| **Moodboard** | A saved taste profile | UUID + strength |
| **Styles** | Trained LoRAs | UUID + strength |

**Consequence for prompting:** write the prompt as if the references did not exist. Do not write "in
the style of the reference image" or "the character from image 1" — there is nothing for those phrases
to bind to, and they will be read as literal description of an image that isn't in the frame.

The prompt describes the subject. The attachments carry the look. Keep them separate.

## Prose, Not Tags

Krea's own guidance: *"long detailed prompts yield best results, but the model is capable of generating
high quality images with minimal prompt engineering."*

Write **flowing natural language**, not comma-separated tag stacks. Both extremes work — a short prompt
produces a good image, a long one produces a specific image — but the long version should read as
description, not as a keyword grid.

```
✅ A weathered brass diving helmet resting on wet slate, seawater pooling in
   the grooves, low sun raking across it from the left, deep shadows.

❌ diving helmet, brass, weathered, wet slate, seawater, low sun, dramatic
   lighting, 8k, masterpiece, highly detailed
```

## Text Rendering — the quote convention is real

Krea documents this explicitly: *"For text rendering, we recommend putting quotes around the words to be
rendered."*

```
A hand-painted shop sign reading "COLD BEER" above a doorway.
```

The quoting convention is first-party documented: Krea states it outright, rather than it circulating
as community folklore.

## The Controls That Do the Work

More of Krea 2's character lives in its controls than in its prompt. Worth choosing deliberately rather
than defaulting.

### Creativity

`raw` · `low` · `medium` · `high`

How far the model may depart from a literal reading of the prompt. `raw` is the most literal; `high`
gives it licence to interpret.

> ⚠️ **The default is disputed.** Krea's user guide and developer overview both say `medium`; the API
> schema on all three endpoints says `low`. Do not assume — set it explicitly.

### Sliders

`intensity` · `complexity` · `movement` — each an integer from **−100 to 100**, default **0**.

These are aesthetic dials, not prompt content. Reaching for a slider is usually better than adding
adjectives: raising `complexity` beats writing "highly detailed, intricate, ornate."

### Style references and moodboards

- **Style references** — up to **10** via the API (the UI shows 4). Strength **0–1**, default **0.5**
- **Moodboard** — **exactly one** per request. Strength **0–1**, default **0.23**

**Moodboard and style reference strength do not stack** — using both does not compound their influence.

## Mode Selection

| Mode | Use when | Available on |
|---|---|---|
| **Text-to-image** | Generating from nothing | All three tiers |
| **Image-to-image** | Starting from an existing image | **Medium and Large only** |

**Image-to-image is not available on Medium Turbo.** Supply a source image plus a `strength` value:
**0 keeps the input, 1 fully replaces it**, default **0.99** — which is very nearly a full replacement,
so lower it deliberately if you want the source to survive.

## Tier Selection

| Tier | Use for | Speed |
|---|---|---|
| **Medium** | General work, image-to-image | Standard |
| **Large** | Highest quality, image-to-image | Slower |
| **Medium Turbo** | Fast iteration, text-to-image only | **~4 seconds** |

## Suggested Settings

**Three fields are required with no defaults** — this catches people out:

- **Prompt** — required
- **Aspect ratio** — **required.** 8 options including `2.35:1` (1568×672)
- **Resolution** — **required.** Hosted API offers **`1K` only**

Then, optionally:

- **Creativity:** `raw` / `low` / `medium` / `high` — set it explicitly, the default is disputed
- **Sliders:** intensity, complexity, movement — −100 to 100, default 0
- **Style references:** up to 10, strength 0–1 (default 0.5)
- **Moodboard:** one, strength 0–1 (default 0.23)
- **Image-to-image strength:** 0–1, default 0.99 (Medium and Large only)

**There is no negative-prompt field and no batch parameter.** The "4 images per generation" figure is a
UI behaviour, not an API option.

## Reference Files

- **`parameters.md`** — Every documented field with its real enum and default, the two places Krea's
  own pages conflict, tier pricing, aspect-ratio pixel dimensions, and the open-weight checkpoints.

- **`best-practices.md`** — Prose construction, when to reach for a slider instead of an adjective,
  creativity-level selection, text rendering, image-to-image strength, and a mistakes/fixes table.

- **`continuity-and-references.md`** — How to hold a look without any in-prompt reference mechanism,
  the three attachment types compared, moodboards versus style references, and LoRA styles.

- **`examples.md`** — Annotated examples across both modes and all three tiers, including text
  rendering, style-reference work, and an image-to-image refinement.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
