# Krea 2 — Continuity and References

Krea 2 has **no in-prompt reference mechanism whatsoever**. That
shapes everything about how continuity works here, and it is worth understanding rather than working
around blindly.

---

## There is no token, and there is no prose convention

No `@Image1`. No `<IMAGE_1>`. No brackets. No "Image 1 is the product, Image 2 sets the style"
role-assignment convention.

Nothing in Krea's prompting guide, user guide, or OpenAPI schema addresses a reference from prompt text.
This is confirmed by absence across every first-party source, not merely undocumented.

**What that means in practice:**

```
❌ In the style of the reference image, a brass diving helmet on wet slate.
❌ The character from image 1, standing at a window.
❌ Match the moodboard's palette.
```

Every one of these is read as **literal description of something that is not in the frame**. At best
the words are wasted; at worst they add a phantom element to the composition.

```
✅ A weathered brass diving helmet resting on wet slate.
   [style reference attached, strength 0.5]
```

**The prompt describes the subject. The attachments carry the look.** That separation is the entire
technique on this model.

---

## The three attachment types

All bound outside the prompt, each with a numeric strength.

| Attachment | Carries | Bound by | Max | Strength |
|---|---|---|---|---|
| **Style references** | The look of specific images | URL | **10** (API) / 4 (UI) | 0–1, default **0.5** |
| **Moodboard** | A saved taste profile | UUID | **1** | 0–1, default **0.23** |
| **Styles** | A trained LoRA | UUID | — | −2 … 2 |

### Style references

The workhorse. Attach one or more images; their look transfers.

- **Up to 10 via the API** — the 4-image limit belongs to the UI, and the two surfaces genuinely differ
- **Strength 0–1, default 0.5.** That default is a middle position, not a recommendation — if a
  reference is overwhelming the subject, lower it before rewriting anything
- Krea's style-transfer prose page quotes a −2…2 range. **That range belongs to `styles` (LoRAs), not
  here.** Trust the schema: 0–1

### Moodboards

A saved taste profile referenced by UUID. **Exactly one per request** — this is a hard schema limit, not
a guideline.

A moodboard carries something a prompt genuinely cannot: an accumulated sense of what you like. For a
project with a consistent visual identity, this is the strongest single continuity tool Krea 2 offers,
because it applies across every generation without occupying any prompt.

**Default strength 0.23** — noticeably lower than style references. Krea's moodboards prose page
suggests starting around 0.35 within a −0.5…1.5 range; the schema says 0–1 with 0.23 default. Trust the
schema, and treat 0.23 as a light touch you can raise.

### Styles (LoRAs)

Trained models bound by UUID, with a wider strength range of −2 to 2. Negative values invert the style's
influence — an unusual capability, and the only place in Krea's parameter set where negative strength is
genuinely available.

### They do not stack

**Moodboard and style-reference influence do not compound.** Using both does not double the effect, and
the pricing reflects this — the cost does not stack either.

Pick the one that fits: a moodboard for project-wide identity, style references for a specific look on a
specific image.

---

## Holding a look across generations

Without an identity mechanism, consistency comes from doing the same things the same way.

1. **Attach the same assets every time.** One approved style reference set, or one moodboard, reused
   across the whole project. A different photo of the same look is a different reference
2. **Keep strength values fixed.** Changing 0.5 to 0.6 between shots is a different treatment. Lock a
   value once it works
3. **Write a look block and reuse it verbatim** — three or four elements, not a list:

```
Overcast north light, desaturated except for the lamp warmth, fine grain,
shallow focus with the background dissolved.
```

4. **Keep the sliders fixed too.** `intensity`, `complexity` and `movement` are as much part of the look
   as the prompt. Varying them between shots in a set undoes the consistency the references bought
5. **Set `creativity` explicitly and keep it.** The default is disputed between Krea's own pages, so an
   unset value is unpredictable — and unpredictable is the opposite of what a set of matching images
   needs

---

## Character consistency — manage expectations

**Krea 2 has no character identity mechanism.** Style references transfer *look*, not *likeness*. A
moodboard carries taste, not a face. There is no IP-Adapter equivalent, no face lock, no per-subject
binding.

**What you can do:**

- Write a detailed, fixed character description and reuse it verbatim. Three to five specific,
  reproducible details — "a healed burn scar across the left jaw" reproduces; "distinctive features"
  does not
- Use a **trained LoRA style** if the character is important enough to justify training one. This is the
  only real identity mechanism available, and it lives outside the prompt entirely
- Use **image-to-image at low strength** to iterate on an approved image rather than regenerating —
  0.2–0.4 keeps the source clearly recognisable

**What you cannot do:** expect a character to survive across independent generations from prose alone.
They will look like the same *description*, not the same *person*.

**Routing consequence:** for work where a named character must recur across many images, this is not the
model. See below.

---

## Image-to-image as a continuity tool

Available on **Medium and Large only** — not Medium Turbo.

`strength` controls survival: **0 keeps the input, 1 fully replaces it. Default 0.99.**

That default matters. At 0.99 the source barely survives, which is why image-to-image on Krea 2 often
feels like it ignored the input — it nearly did. **Lower it deliberately.**

| Strength | Use for |
|---|---|
| 0.2–0.4 | Refining an approved image — the strongest continuity available here |
| 0.5–0.7 | Reinterpreting while roughly holding composition |
| 0.8–0.99 | A new image with a nudge from the source |

**Write the prompt for the whole intended result**, not for the change. This differs from video editing
models where the prompt describes only the delta — here the image is re-rendered from the prompt.

---

## When to route elsewhere

- **A named character recurring across many images.** Krea 2 has no identity mechanism.
  GPT Image 2 (up to 16 reference images), Gemini 3 Pro Image (14 references, prose role
  assignment), or Phota (trained identity profiles) all bind likeness properly
- **Output above 1K.** The hosted API offers 1K only. The open-source Turbo checkpoint reaches 2K, but
  that is self-hosting, not the API
- **Precise per-subject placement or composition control.** Seedream 5.0 supports structured
  positioning; Krea 2 does not
- **Negative prompting.** No field exists, and the schema rejects unknown properties

**Reach for Krea 2 when the look matters more than the likeness** — when a project needs a consistent
aesthetic across many images and a moodboard or style-reference set can carry it. That is what it is
built for, and the taste controls make it unusually good at it.
