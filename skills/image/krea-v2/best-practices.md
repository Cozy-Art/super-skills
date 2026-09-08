# Krea 2 — Best Practices

Depth on prompt construction. The hard rules live in `SKILL.md`.

---

## Write prose, not tags

Krea 2's text encoder is a vision-language model (Qwen 3 VL), and it reads sentences better than
keyword grids.

```
✅ A weathered brass diving helmet resting on wet slate, seawater pooling in
   the grooves, low sun raking across it from the left, deep shadows behind.

❌ diving helmet, brass, weathered, wet slate, seawater, low sun, dramatic
   lighting, 8k, masterpiece, highly detailed
```

The tag version is not merely less elegant — the quality boosters at the end (`8k`, `masterpiece`,
`highly detailed`) are doing nothing, and the comma-separated fragments give the encoder no relational
information. "Seawater pooling *in the grooves*" tells the model where the water is. "seawater" does not.

**Both lengths work.** Krea: *"long detailed prompts yield best results, but the model is capable of
generating high quality images with minimal prompt engineering."* A short prompt gives a good image; a
long one gives a specific image. Choose based on how much you care about the specifics.

---

## Reach for a slider before an adjective

The highest-leverage habit on this model, and the one that distinguishes it from most image models.

Krea 2 exposes three aesthetic dials — `intensity`, `complexity`, `movement`, each −100 to 100,
defaulting to 0. They do work that adjectives do badly.

| Instead of writing | Move this |
|---|---|
| "highly detailed, intricate, ornate, busy" | `complexity` up |
| "minimal, clean, sparse, simple" | `complexity` down |
| "dramatic, bold, striking, high contrast" | `intensity` up |
| "subtle, muted, understated, soft" | `intensity` down |
| "dynamic, energetic, in motion, action" | `movement` up |
| "still, calm, static, frozen" | `movement` down |

**Why this is better:** adjectives compete with the subject for the encoder's attention, and stacked
synonyms compound the problem. A slider changes the aesthetic without spending prompt on it.

Leave the prompt for *what is in the picture*. Let the sliders handle *how it feels*.

---

## Choosing a creativity level

`raw` · `low` · `medium` · `high` — how far the model may depart from a literal reading.

| Level | Use when |
|---|---|
| `raw` | You have specified exactly what you want and want it back |
| `low` | Product, brand, or anything where the brief is the spec |
| `medium` | General work — a prompt with room to breathe |
| `high` | Exploration, mood-finding, when the prompt is a starting point |

> ⚠️ **Set it explicitly.** Krea's user guide says the default is `medium`; the API schema says `low`.
> Since the two disagree, an unset value is genuinely unpredictable. Choosing removes the problem.

**Pair creativity with prompt length.** A long, specific prompt at `high` creativity works against
itself — you specified carefully and then gave the model licence to reinterpret. Long prompt → lower
creativity. Short prompt → higher creativity, if you want it filled in interestingly.

---

## Text rendering

Krea documents the quote convention explicitly: *"For text rendering, we recommend putting quotes
around the words to be rendered."*

```
A hand-painted shop sign reading "COLD BEER" above a doorway.
```

**This is genuinely first-party.** Most models where this technique circulates have no vendor statement
behind it — here there is one, so it can be taught as guidance rather than as folklore.

**Working notes:**

- **Quote the exact string**, including capitalisation. `"COLD BEER"` and `"Cold Beer"` are different
  requests
- **Describe the surface and treatment** around the quoted text — hand-painted, embossed, neon,
  chalked. The quotes fix the words; the prose fixes the look
- **Keep strings short.** Long passages degrade in every image model, and Krea publishes no claim to
  the contrary
- **One or two strings per image.** Several competing text elements is where failure starts

---

## Image-to-image

Available on **Medium and Large only** — not Medium Turbo.

The `strength` value controls how much survives: **0 keeps the input, 1 fully replaces it.**

**The default is 0.99**, which is very nearly a total replacement. If the point is to keep something of
the source, that value has to come down deliberately — leaving it at default will feel like the source
was ignored, because it nearly was.

| Strength | Effect |
|---|---|
| 0.2–0.4 | Refinement — the source clearly survives |
| 0.5–0.7 | Substantial reinterpretation, composition roughly held |
| 0.8–0.99 | Essentially a new image with a nudge from the source |

**Write the prompt for the result you want, not for the change.** Unlike video models where an edit
prompt describes only the delta, image-to-image here re-renders from the prompt — so the prompt should
describe the whole intended image.

---

## Prompting around attachments

**There is no in-prompt way to reference an attachment**, so do not try.

```
❌ In the style of the reference image, a brass diving helmet…
❌ The helmet from image 1, on wet slate…
❌ Using the moodboard's palette, a coastal scene…
```

Each of these is read as literal description of something not in the frame — at best wasted, at worst
actively confusing the composition.

```
✅ A weathered brass diving helmet resting on wet slate.
   [style reference attached at strength 0.5]
```

**The prompt describes the subject. The attachments carry the look.** Keeping them separate is the
whole technique.

---

## Negation

**There is no negative-prompt field**, and `additionalProperties: false` means adding one is rejected
rather than ignored.

Exclusions must be phrased positively as description of what *is* there:

| ❌ | ✅ |
|---|---|
| "no people" | "an empty street at dawn, no traffic" → better: "a deserted street at dawn" |
| "not cluttered" | "a bare room, one chair, nothing on the walls" |
| "no text" | describe the surface as blank or unmarked |

In-prompt negation on a model with no negative field is unreliable in general and undocumented here
specifically. Describe the desired state instead.

---

## Mistakes and fixes

| Symptom | Cause | Fix |
|---|---|---|
| Request returns 400 | `aspect_ratio` or `resolution` omitted | **All three fields are required** — no defaults |
| Request returns 400 on legacy tooling | camelCase field aliases | `presetStyles` / `imageStyleRefs` expired 2026-06-19 |
| Reference seems ignored | Prompt tried to point at it | There is no in-prompt reference syntax |
| Result unpredictable between runs | `creativity` unset, default disputed | Set it explicitly |
| Prompt fighting itself | Long specific prompt at `high` creativity | Long prompt → lower creativity |
| Adjective stack not landing | Aesthetic written as description | Move it to `intensity` / `complexity` / `movement` |
| Source image seems ignored in i2i | `strength` left at 0.99 default | Lower it — 0.2–0.4 to refine |
| Image-to-image unavailable | Using Medium Turbo | Only Medium and Large support it |
| Text garbled | Words not quoted | Quote the exact string |
| Output capped at 1K | Hosted API offers 1K only | Open-source Turbo reaches 2K; hosted does not |
| Only one image returned | No batch parameter exists | The "4 per generation" figure is UI-only |
| Style references above 4 rejected in UI | UI limit is 4; API allows 10 | Different surfaces, different ceilings |

---

## Iterating

**Iterate on Medium Turbo, finish on Medium or Large.** At ~4 seconds and $0.015–0.02, Turbo is the
cheap loop — but remember it cannot do image-to-image, so a workflow that starts from a source has to
begin on Medium.

**Change one thing at a time**, and prefer changing a *control* over changing the prompt. If the image
is right but too busy, drop `complexity` and regenerate — that isolates the variable in a way that
rewriting the prompt does not.

**Strength values are the second dial to try.** If a style reference is overwhelming the subject, lower
its strength before rewriting either. Default 0.5 is a middle position, not a recommendation.
