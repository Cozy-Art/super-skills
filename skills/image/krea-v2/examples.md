# Krea 2 — Example Prompts

Annotated examples across both modes and all three tiers, drawn from the recurring example
projects.

Note what is *absent* from every prompt: any mention of a reference, a style, or a moodboard. Those live
in the attachments, never in the text.

---

## Example 1 — Text-to-image, prose over tags

**Project:** *Shadows of Ashford* · **Tier:** Medium

**Prompt:**
```
A weathered brass diving helmet resting on wet slate, seawater pooling in the
grooves around the faceplate glass. Low winter sun rakes across it from the
left, throwing a long shadow to the right of frame. The slate is dark and
uneven, still holding rain.
```

**Settings:** `aspect_ratio: 2.35:1` · `resolution: 1K` · `creativity: low` · `complexity: +20`

**Technique notes:**
- **Prose with relational detail.** "Seawater pooling *in the grooves around the faceplate glass*" tells
  the model where the water sits — "seawater, brass, wet" does not
- **No quality boosters.** `8k`, `masterpiece`, `highly detailed` do nothing here and compete with the
  subject for the encoder's attention
- **`complexity: +20` instead of adjectives.** The alternative was writing "intricate, detailed,
  ornate" — a slider does that work without spending prompt on it
- **`creativity: low`** because the brief is specific. Pairing a detailed prompt with `high` creativity
  works against itself
- `2.35:1` is a genuine anamorphic ratio

---

## Example 2 — Text rendering

**Project:** *Forgotten Waters* · **Tier:** Medium

**Prompt:**
```
A hand-painted wooden sign reading "HARBOUR MASTER" mounted above a weathered
door, the paint cracked and flaking at the edges, salt-bleached. Overcast
flat light, the door frame damp.
```

**Settings:** `aspect_ratio: 4:5` · `resolution: 1K` · `creativity: raw`

**Technique notes:**
- **The quote convention is first-party here** — Krea documents it: *"For text rendering, we recommend
  putting quotes around the words to be rendered."* Most models where this technique circulates have no
  vendor statement behind it
- **Quote the exact string including capitalisation.** `"HARBOUR MASTER"` and `"Harbour Master"` are
  different requests
- **Quotes fix the words; prose fixes the look.** "Hand-painted," "cracked and flaking," "salt-bleached"
  all describe the treatment of the lettering
- **One text string.** Several competing text elements is where text rendering starts to fail
- `creativity: raw` — for legible text you want the most literal reading available

---

## Example 3 — Style reference, no mention in the prompt

**Project:** *Neon Pulse* · **Tier:** Large
**Attachments:** 3 style references at strength 0.5

**Prompt:**
```
A dancer standing under a dead neon sign on wet asphalt, one hand still
raised from the end of a turn. Light spills from an open doorway to the
right, the only source. Rain has stopped but the ground is still holding it.
```

**Settings:** `aspect_ratio: 9:16` · `resolution: 1K` · `creativity: medium` · `intensity: +30`

**Technique notes:**
- ⚠️ **The prompt never mentions the references.** There is no in-prompt reference syntax on this model
  — writing "in the style of the reference images" would be read as literal description of something not
  in the frame
- **The prompt describes the subject; the attachments carry the look.** That separation is the whole
  technique
- Up to **10 style references** via the API — the 4-image limit belongs to the UI
- **Strength 0.5 is the default, not a recommendation.** If the references overwhelm the dancer, lower
  it before rewriting anything
- `intensity: +30` for the contrast, rather than writing "dramatic, high contrast, bold"

---

## Example 4 — Moodboard for project-wide identity

**Project:** *Iron Crown* · **Tier:** Medium
**Attachments:** 1 moodboard at strength 0.23 (default)

**Prompt:**
```
A stone council chamber at night, a long map table at its centre with
parchment spread across it. Torches burn in sconces along both walls. The far
end of the room is lost in shadow.
```

**Settings:** `aspect_ratio: 21:9` · `resolution: 1K` · `creativity: medium` · `complexity: +15` · `movement: −20`

**Technique notes:**
- **Exactly one moodboard per request** — a hard schema limit, not a guideline
- **A moodboard carries what a prompt cannot**: an accumulated sense of the project's visual identity.
  For a production with a consistent look, this is the strongest continuity tool Krea 2 offers, because
  it applies to every generation without occupying any prompt
- **Default strength 0.23 is a light touch** — deliberately lower than style references. Raise it if the
  identity isn't coming through
- **Moodboard and style-reference influence do not stack.** Using both does not compound, and the
  pricing does not either. Pick the one that fits
- `movement: −20` for stillness, rather than writing "static, calm, still"

---

## Example 5 — Image-to-image refinement

**Project:** *Aurelia* · **Tier:** Medium
**Source:** approved bottle render

**Prompt:**
```
A tall rectangular glass perfume bottle with a gold cap and amber liquid,
standing on brushed brass. A single key light from above-right draws a clean
highlight down the glass edge, soft fill from the left. Seamless dark
gradient background.
```

**Settings:** `strength: 0.3` · `aspect_ratio: 1:1` · `resolution: 1K` · `creativity: raw`

**Technique notes:**
- ⚠️ **`strength: 0.3`, not the 0.99 default.** At 0.99 the source barely survives — which is why
  image-to-image on this model often feels like the input was ignored. It nearly was. Lower it
  deliberately
- **The prompt describes the whole intended image**, not just the change. This differs from video edit
  models where the prompt describes only the delta — here the image is re-rendered from the prompt
- **Image-to-image is Medium and Large only.** Medium Turbo cannot do this
- `creativity: raw` — a refinement pass wants the most literal reading available

---

## Example 6 — Fast iteration on Turbo

**Project:** *Stellar Drift* · **Tier:** Medium Turbo

**Prompt:**
```
A narrow spacecraft service corridor lit by recessed strips at knee height,
everything beyond ten metres falling into darkness. Bare structural ribbing
along the walls, a junction panel open on the right.
```

**Settings:** `aspect_ratio: 21:9` · `resolution: 1K` · `creativity: high` · `complexity: +40`

**Technique notes:**
- **~4 seconds and $0.015–0.02** — the cheap exploration loop. The "~2 seconds" figure circulating for
  Turbo is not Krea's
- **`creativity: high` paired with a shorter prompt.** Short prompt plus high creativity is the
  exploration combination; long prompt plus low creativity is the specification combination
- ⚠️ **Turbo cannot do image-to-image.** A workflow starting from a source has to begin on Medium
- Iterate here, then re-run the winner on Medium or Large for the finish

---

## Example 7 — Routing away

**Project:** *Iron Crown* · **Scenario:** the queen across 30 images

**Notes field:**
```
Krea 2 is a strong choice for this production's LOOK — a moodboard would
carry the candlelit stone-and-torchlight identity across every image, and the
sliders hold the treatment consistent in a way prose cannot.

It is the wrong choice for the QUEEN.

Krea 2 has no character identity mechanism. Style references transfer look,
not likeness; a moodboard carries taste, not a face. There is no IP-Adapter
equivalent and no per-subject binding. Across 30 images she will look like
the same description, not the same person.

Options:

1. Route character work to GPT Image 2 (up to 16 reference images),
   Gemini 3 Pro Image (14 references with prose role assignment), or
   Phota (trained identity profiles). Keep Krea 2 for environments,
   props and establishing images.

2. Train a LoRA style for the queen and attach it via `styles`. This is the
   only real identity mechanism available on Krea 2, and it lives entirely
   outside the prompt. Justified only if she is central enough to warrant
   the training cost.

Recommend option 1 for the character, Krea 2 for everything around her.
```

**Technique notes:**
- Following the D5 precedent — `notes` carries the real recommendation, including using a different
  model for part of the work
- Note the split: routing away from a *subject* is not routing away from the model. Krea 2 remains right
  for the rest of this production

---

## Quick reference

| Situation | Approach |
|---|---|
| Specific brief, want it back literally | Long prompt + `creativity: raw` or `low` |
| Exploring a look | Short prompt + `creativity: high`, on Turbo |
| Aesthetic adjustment | **Move a slider**, don't add adjectives |
| Text in the image | Quote the exact string — first-party documented |
| Specific look from images | Style references, up to 10, **never mentioned in the prompt** |
| Project-wide visual identity | One moodboard, reused across every generation |
| Refining an approved image | Image-to-image at `strength: 0.2–0.4` — **not the 0.99 default** |
| Fast iteration | Medium Turbo — but it cannot do image-to-image |
| A recurring named character | **Route elsewhere** — no identity mechanism |
| Output above 1K | **Route elsewhere** — hosted API is 1K only |
| Excluding something | Describe what *is* there — no negative field exists |
