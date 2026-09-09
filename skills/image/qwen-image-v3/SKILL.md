---
name: qwen-image-3-prompts
description: Generate optimized prompts for Alibaba's Qwen-Image-3.0 — a unified text-to-image and image-editing model with genuine negative-prompt support, multi-image fusion from up to three references, and a prompt-expansion stage that is on by default. Use this skill whenever a user mentions Qwen-Image-3.0, Qwen Image 3, or wants an image prompt targeting Alibaba Model Studio for this model. Also trigger for workflows involving multilingual text rendering, poster and layout design, image editing from references, or reproducible generation with a fixed seed. Always use this skill instead of guessing at Qwen-Image-3.0 prompt structure from general knowledge — the model accepts exactly one prose field and errors on more than one, its prompt-expansion default silently breaks seed reproducibility, and most parameter documentation circulating for it describes a third-party aggregator's API rather than Alibaba's.
---

# Qwen-Image-3.0 Prompt Generator

Generate optimized prompts for Alibaba's Qwen-Image-3.0 — a unified model where text-to-image and image
editing run through the same endpoint, distinguished only by whether reference images are supplied.

One thing worth knowing up front: **it has a real negative-prompt parameter.**

> ⚠️ **This skill is provisional.** Qwen-Image-3.0 is in limited preview with no open weights, no
> technical report, no model card and no third-party benchmarks. Several widely-quoted capability
> figures are vendor launch marketing relayed through third parties and could not be confirmed. See
> [README.md](README.md) for exactly which claims are unverified.

**This skill produces prompt text, not API calls.** The output goes to a person, who pastes it into
whatever tool they are generating with. Every result ships as two clearly separated pieces: the
**prompt** and a short **suggested settings** line. Never merge the two.

## The One Rule That Overrides Everything

**Settings do not belong in the prompt text.** Size, seed, watermark, output count — all have their own
fields.

## One Prose Field, and Only One

A hard constraint with a real failure mode.

> Alibaba: *"Contains only one `{"text": "..."}` object. … **Only one text object is allowed. Omitting
> it or providing multiple text objects will result in an error.**"*

Everything — subject, composition, style, text content, layout — goes into **a single string**. Any
structural convention you use inside it (`LAYOUT:`, `HEADER:`, `COLUMN:`) is a **writing style, not a
schema**. It is still one string.

## Reference Markers

**Numbers in the prompt correspond to array position**, and Alibaba documents addressing them directly:

> *"Image numbers in prompts correspond to array position: the first image is 'image 1', the second is
> 'image 2'. **You can also use markers like '[image 1]' and '[image 2]'**."*

Two documented forms, both fine:

```
The girl in Image 1 wears the black dress from Image 2 and sits in the pose from Image 3.
Place the alarm clock from [image 1] next to the vase on the dining table in [image 2].
```

Casing is not load-bearing — Alibaba's own examples use both `image 1` and `Image 1`.

**Role assignment across images is the intended use**, not something to avoid. Alibaba's worked examples
assign a different contribution to each reference — subject from one, wardrobe from another, pose from a
third.

**Order is the binding.** The marker number *is* the array index, so reordering the array changes what
each marker refers to. Alibaba demonstrates this directly with a before/after pair: `"Move image 1 onto
image 2"` versus `"Move image 2 onto image 1"` produce opposite results from the same two assets.

**Maximum three reference images.**

⚠️ This is documented in Alibaba's **editing guide**, not the API reference — the API reference describes
only positional array binding and never mentions markers. The two pages differ in completeness rather
than contradicting each other, which is worth knowing if someone checks only the API reference and
concludes markers don't exist.

## Prompt Expansion Is On By Default — and it breaks reproducibility

The single most consequential behaviour on this model.

**`prompt_extend` defaults to `true`.** Your prompt is rewritten and expanded by a language model before
generation. What you wrote is not what the model renders.

Two consequences:

**1. A fixed seed does not give you a fixed image.** Seed reproducibility only works if the prompt
reaching the model is identical each time — and with expansion on, it is regenerated each run. **For
reproducible output, expansion must be off.**

**2. Everything you leave unstated, the expander decides.** Specificity is a constraint on the rewrite,
not verbosity for its own sake.

When to turn it off:

| Expansion | Use for |
|---|---|
| **On** (default) | Short prompts, exploration, letting the model fill in a sparse brief |
| **Off** | Reproducible output, precise briefs, anything where you wrote exactly what you meant |

## Negative Prompts Actually Work Here

`negative_prompt` is a real, documented parameter. Use it rather than working around it.

Use it for what negatives are good at: suppressing recurring artefacts and unwanted content.

```
negative_prompt: blurry, distorted hands, watermark, text artifacts, oversaturated
```

Keep the main prompt positive and descriptive; put exclusions in the field where they belong rather than
negating inside the prose.

## Text Rendering

Qwen-Image is positioned around text rendering, and the family's reputation for it is well established.

**The convention of wrapping on-image copy in double quotes is widely used** — but note that for 3.0
specifically it is **documented by a third-party platform, not by Alibaba.** It works, and it is the
right technique; it is just not vendor-stated. Treat it as a strong convention rather than a guarantee:

```
A hand-painted shop sign reading "COLD BEER" above a doorway.
```

**Multilingual rendering claims** — a specific language count, font count, and minimum legible text size
circulate widely. All come from launch materials relayed through third parties and are unconfirmed. The
capability is real; the specific numbers should not be quoted as spec.

## Mode Selection

One endpoint, two behaviours:

| Mode | Trigger |
|---|---|
| **Text-to-image** | One `text` object, no images |
| **Image editing / fusion** | One `text` object plus 1–3 `image` objects |

The mode is determined by what you supply, not by a parameter.

## Suggested Settings

- **Size:** a `width*height` string. **Total pixels between 512×512 and 2048×2048** — the same range for
  both text-to-image and editing. **No fixed default** — unspecified, the model recommends a resolution
  from the prompt
- **Prompt expansion:** on by default. **Turn off for reproducibility**
- **Negative prompt:** available, and worth using
- **Seed:** 0 – 2,147,483,647. **Only meaningful with expansion off**
- **Output count:** 1–6, default 1
- **Watermark:** off by default
- **Output:** PNG, download URL valid 24 hours

## Reference Files

- **[parameters.md](parameters.md)** — The real Alibaba field names and shapes (most published parameter tables for
  this model describe a different vendor's API), pixel budgets, input formats, and an explicit list of
  parameters that do not exist.

- **[best-practices.md](best-practices.md)** — Writing for the expander, when to disable it, negative-prompt use, text
  rendering, layout briefs inside a single string, and a mistakes/fixes table.

- **[continuity-and-references.md](continuity-and-references.md)** — Positional reference binding, the seed-and-expansion interaction,
  holding a look without an identity mechanism, and editing workflows.

- **[examples.md](examples.md)** — Annotated examples across both modes, including a text-rendering poster, a
  reproducible generation, and a multi-image fusion.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
