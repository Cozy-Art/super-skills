# Qwen-Image-3.0 — Example Prompts

Annotated examples across both modes, drawn from the recurring example projects.

Note what is absent from every prompt: in-prompt negation. This model has a real `negative_prompt`
field, so exclusions belong there rather than in the prose.

---

## Example 1 — Text-to-image, exploration

**Project:** *Shadows of Ashford* · **Mode:** text-to-image

**Prompt:**
```
A weathered brass diving helmet resting on wet slate, low winter sun raking
across it from the left.
```

**Negative prompt:** `blurry, distorted, watermark, oversaturated`
**Settings:** `prompt_extend: true` (default) · `n: 4` · `size` unset

**Technique notes:**
- **Short prompt plus expansion is the exploration combination.** The expander fills in what isn't
  specified, which is exactly what you want when finding a direction
- **`n: 4` gives four variations in one request** rather than four calls at different seeds
- **`size` unset deliberately** — the model recommends a resolution from the prompt, which is fine for
  exploration and wrong for a deliverable
- **Negative prompt used from the start.** A working one exists here, so there is no reason to phrase
  artefact suppression positively

---

## Example 2 — The same shot, committed

**Project:** *Shadows of Ashford* · **Mode:** text-to-image

**Prompt:**
```
A weathered brass diving helmet resting on wet slate, seawater pooling in the
grooves around the faceplate glass. Low winter sun rakes across it from the
left, throwing a long shadow to the right of frame. The slate is dark and
uneven, still holding rain. Muted palette, cold light, fine surface detail on
the corroded brass.
```

**Negative prompt:** `blurry, distorted, watermark, oversaturated, plastic texture`
**Settings:** **`prompt_extend: false`** · `seed: 184529` · `size: "1536*1024"` · `n: 1`

**Technique notes:**
- ⚠️ **Expansion off, and that is what makes the seed work.** With `prompt_extend: true` the prompt is
  regenerated each run, so the same seed produces a *different image*. Seed plus expansion is a
  contradiction
- **The prompt is now fuller because you are writing what the expander was writing.** Turning expansion
  off means taking over its job, not just disabling it
- **`size` set explicitly** — no default exists, and an unspecified size can vary between runs of a set
- This pair of examples is the model's natural two-phase workflow: explore with expansion, commit
  without it

---

## Example 3 — Text rendering / poster layout

**Project:** *Forgotten Waters* · **Mode:** text-to-image

**Prompt:**
```
LAYOUT: single-panel portrait poster, generous margins.
HEADER: large condensed serif type reading "HARBOUR MASTER" across the top
third, letterpress texture, slightly uneven inking.
CENTRE: an ink line-work illustration of a brass diving helmet, front-facing,
high contrast.
FOOTER: small caps reading "EST. 1897" centred at the base.
PALETTE: deep navy, salt white, one accent of oxidised copper.
STYLE: vintage maritime print, flat colour, no gradients, visible paper grain.
```

**Negative prompt:** `photorealistic, gradient, drop shadow, blurry text, extra letters`
**Settings:** **`prompt_extend: false`** · `seed: 77120` · `size: "1024*1536"`

**Technique notes:**
- **The labels are a writing style, not a schema.** This is still one `{"text": "…"}` object — Alibaba
  errors if you supply more than one. The structure helps the model parse a dense brief; it is not fields
- **Expansion off is essential for exact copy.** An expander is free to reword `"HARBOUR MASTER"`, which
  defeats the point of quoting it
- **Quote the exact strings including capitalisation.** Note this convention is documented by a
  third-party platform for 3.0, not by Alibaba — it works, but it isn't vendor-stated here (unlike
  Krea 2, where it is)
- **Two text strings is a reasonable ceiling.** More competing elements is where text rendering starts
  to fail
- Negative prompt targets the specific failure modes of text work — extra letters, blurred type

---

## Example 4 — Image editing

**Project:** *Aurelia* · **Mode:** editing
**References:** approved bottle render, brushed-brass surface swatch (in that array order)

**Prompt:**
```
The perfume bottle from image 1, standing on the brushed brass surface from
image 2. A single hard key light from above-right draws a clean highlight
down the glass edge, soft fill from the left. Seamless dark gradient
background, the label crisp and centred.
```

**Negative prompt:** `blurry, distorted label, duplicate bottle, harsh reflections`
**Settings:** **`prompt_extend: false`** · `seed: 4410` · `size: "1024*1024"`

**Technique notes:**
- **Each reference given an explicit role** — `image 1` supplies the bottle, `image 2` the surface. This
  is Alibaba's documented pattern, and their own examples do the same: *"The girl in Image 1 wears the
  black dress from Image 2 and sits in the pose from Image 3"*
- **The number is the array index**, so reordering the array changes what each marker points at. Keep
  the prompt and the array in sync
- Brackets are equally valid: `[image 1]`, `[image 2]`
- **The prompt describes the whole intended result**, not the change. This differs from video edit
  models where the prompt is only the delta, and it differs from what "editing" implies
- **Same endpoint as text-to-image.** The mode is set by supplying image objects, not by a parameter
- **Same pixel budget as generation** — 512×512 to 2048×2048. Claims that references reduce the budget
  describe a third-party platform's limits
- Expansion off because this is a precise brief

---

## Example 5 — Multi-image fusion

**Project:** *Iron Crown* · **Mode:** editing
**References:** stone chamber plate, torch-sconce detail, parchment texture (array order)

**Prompt:**
```
The stone council chamber from image 1, lit by the torch sconces from
image 2, with the parchment texture from image 3 spread across a long map
table at its centre. Warm light falls short of the far end, which stays in
shadow. Heavy carved stone, worn flagstones, cold air.
```

**Negative prompt:** `modern furniture, electric lighting, people, blurry`
**Settings:** `prompt_extend: false` · `seed: 9082` · `size: "1536*1024"`

**Technique notes:**
- **Three references, three explicit roles** — room, lighting, surface texture. This is the pattern
  Alibaba demonstrates, and it does more work than ordering the array and hoping
- **Three references is the ceiling** on this model
- **Expansion off matters here specifically.** With three role assignments in play, an expander free to
  reword the prompt can scramble which marker governs what
- **Negative prompt excluding subject matter** — `people`, `modern furniture`. Note this is the weaker
  use of a negative prompt: it is better at suppressing *artefacts and tendencies* than at excluding
  objects. Describing an empty chamber in the positive prompt does more work
- Seed fixed with expansion off, so this frame is recoverable when the sequence is revisited

---

## Example 6 — Routing away

**Project:** *Iron Crown* · **Scenario:** the queen across 30 images

**Notes field:**
```
Qwen-Image-3.0 is a strong choice for this production's SIGNAGE, MAPS,
HERALDIC DESIGN and any text-bearing prop — the Qwen Image family's text
rendering is its reason to exist, and it has a working negative_prompt
field.

It is the wrong choice for the QUEEN across 30 images.

No identity mechanism exists. Reference images support editing and fusion;
they do not bind likeness, there is no LoRA path (no open weights to
fine-tune), and the ceiling is three references. She will match the
description, not herself.

Two further cautions for anything load-bearing:

1. Limited preview. No open weights, no technical report, no model card, no
   independent benchmarks. Behaviour may change without notice.

2. Seed reproducibility only works with prompt_extend disabled — and it is
   ON by default. A pipeline that fixes a seed without disabling expansion
   will appear reproducible and silently is not.

Recommend: route character work to GPT Image 2 (16 references) or
Phota (trained identity profiles). Keep Qwen-Image-3.0 for the
text-bearing and design assets, with expansion off and seeds fixed.
```

**Technique notes:**
- Following the D5 precedent — `notes` carries the real recommendation, including the model's
  provisional status
- The seed/expansion interaction is the kind of thing that fails silently, so it belongs in `notes`
  rather than only in the reference files

---

## Quick reference

| Situation | Approach |
|---|---|
| Exploring a direction | Short prompt, expansion **on**, `n: 4` |
| Committing a result | Full prompt, expansion **off**, seed fixed, size set |
| Exact on-image copy | Quote the string, expansion **off** |
| Dense layout brief | Labelled sections inside **one** text string |
| Suppressing artefacts | **Use `negative_prompt`** — a real one exists here |
| Excluding an object | Describe the scene without it; negatives are weaker at this |
| Editing from references | 1–3 images, addressed as `image 1` / `[image 1]`, numbers matching array order |
| Reproducible output | **Expansion off** — otherwise the seed does nothing |
| A recurring named character | **Route elsewhere** — no identity mechanism |
| More than 3 references | **Route elsewhere** — three is the ceiling |
| Production-critical work | **Consider routing elsewhere** — limited preview |
