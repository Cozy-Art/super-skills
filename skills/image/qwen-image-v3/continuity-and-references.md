# Qwen-Image-3.0 — Continuity and References

Two things determine how continuity works on this model, and the second is easy to miss: references bind
**positionally**, and the default prompt-expansion setting **silently defeats seed reproducibility**.

---

## Positional markers, addressable from the prompt

> Alibaba: *"Image numbers in prompts correspond to array position: the first image is 'image 1', the
> second is 'image 2'. **You can also use markers like '[image 1]' and '[image 2]'**."*

Two documented forms — bare prose and bracketed. Casing is not load-bearing; Alibaba's own examples use
both `image 1` and `Image 1`.

**Assigning a different role to each reference is the intended use.** Alibaba's worked examples do
exactly that:

```
✅ The girl in Image 1 wears the black dress from Image 2 and sits in the
   pose from Image 3.

✅ The girl in Image 1 wears the necklace from Image 2 and carries the bag
   from Image 3 on her left shoulder.

✅ Place the alarm clock from image 1 next to the vase on the dining table
   in image 2.
```

**What does not work** is syntax borrowed from models with a different convention:

```
❌ @Image1 the bottle, @Image2 the background…
❌ <IMAGE_1> …
```

The `@` and angle-bracket forms belong to other models. Qwen uses bare numbers or square brackets.

**Order is the binding.** The number *is* the array index, so reordering the array changes what each
marker points at. Alibaba demonstrates this with a before/after pair: `"Move image 1 onto image 2"`
versus `"Move image 2 onto image 1"` — same two assets, opposite results.

**Ceiling: three reference images.**

⚠️ **Sourcing note.** This is documented in Alibaba's **editing guide**, not the API reference. The API
reference describes only positional array binding and never mentions markers, so checking it alone
leads to the wrong conclusion. The two pages differ in completeness rather than contradicting each
other.

---

## ⚠️ Seed and prompt expansion are in conflict

The most important continuity fact about this model, and it is not obvious.

**`prompt_extend` defaults to `true`.** The prompt is rewritten and expanded by a language model before
generation.

**A seed only reproduces a result if the prompt reaching the model is identical each time.** With
expansion on, it is regenerated every run — so the same seed with the same input prompt produces a
*different image*.

| `prompt_extend` | `seed` | Result |
|---|---|---|
| `true` (default) | set | **Not reproducible** — the expanded prompt differs each run |
| `false` | set | **Reproducible** |
| `false` | unset | Not reproducible, but for the ordinary reason |

**For any workflow depending on reproducibility, expansion must be off.** This includes:

- Regenerating an approved image at a different size
- A/B testing a single prompt change
- Any pipeline where a result must be recoverable later

This is the same structural situation as Grok Imagine Video's upsampler, but with a sharper consequence:
Grok has no seed at all, so nothing is silently broken. Here there *is* a seed, and it appears to do
nothing.

---

## The two-phase workflow

The expansion default is genuinely useful, and the right response is not to disable it permanently but
to use it in the right phase.

**Phase 1 — explore, expansion on.** A short prompt plus expansion is a good way to find a direction.
The expander fills in what you did not specify, and `n` up to 6 gives you variations in one call.

**Phase 2 — commit, expansion off.** Once a direction is right, write the fuller prompt yourself,
disable expansion, and fix a seed. From here the result is reproducible and the prompt is yours.

This follows from how the model is built rather than working around it.

---

## Holding a look across generations

There is **no identity mechanism** — no LoRA binding, no IP-Adapter equivalent, no per-subject
reference. Reference images inform an edit; they do not lock a likeness.

What is available:

1. **Fix the seed, with expansion off.** The only true repeatability on this model. Same prompt, same
   seed, same size, expansion off → same image
2. **Reuse a style description verbatim.** Three or four elements, identical wording every time:

```
Ochre and deep green on a cream ground, ink line-work, flat colour,
no gradients.
```

3. **Reuse the same reference images in the same array position.** A different photo of the same subject
   is a different reference, and a different array position is a different binding
4. **Keep `size` fixed.** Because there is no default, an unspecified size is chosen from the prompt —
   which means it can vary between runs of a set

---

## Character consistency — manage expectations

**Qwen-Image-3.0 cannot hold a character across independent generations.** Reference images support
editing and fusion; they do not bind identity, and there is no training-time personalisation path
(there are no open weights to fine-tune).

**What you can do:**

- Write a detailed fixed character description with three to five reproducible specifics, and reuse it
  verbatim
- Work by **editing** rather than generating — take one approved image and edit it, rather than
  regenerating the character from prose each time. This is the strongest continuity available here
- Fix the seed with expansion off, which at least makes each generation recoverable

**What you cannot do:** expect the same person across separate prompts. They will match the
*description*, not each other.

**Routing consequence:** for a named character recurring across many images, this is not the model. See
below.

---

## Editing workflows

Text-to-image and editing run through the **same endpoint** — the mode is determined by whether image
objects are present, not by a parameter.

**Editing accepts 1–3 references and the same pixel budget as generation** (512×512 to 2048×2048).
Claims that the budget drops when references are supplied describe a third-party platform's limits, not
this model's.

**Write the prompt for the whole intended result**, not for the change. This differs from video editing
models where the prompt describes only the delta — and it differs from what the word "editing" implies.

**Turn expansion off for edits.** An edit is by definition a precise instruction; letting an expander
rewrite it is working against the point.

---

## When to route elsewhere

- **A named character recurring across many images.** No identity mechanism.
  GPT Image 2 (up to 16 reference images), Gemini 3 Pro Image (14 references with prose role
  assignment) or Phota (trained identity profiles) all bind likeness properly
- **More than three references.** Three is the ceiling here; GPT Image 2 takes 16
- **Above 2048×2048.** That is the pixel-budget ceiling
- **Production dependability.** This is a **limited preview** with no open weights, no technical report,
  no model card and no independent benchmarks. For work that must not break, a documented model is the
  safer choice
- **A consistent project-wide aesthetic across many images.** Krea 2's moodboards carry a look
  across every generation without occupying prompt

**Reach for Qwen-Image-3.0 when** the work is text-heavy or layout-heavy — posters, signage,
multi-element design — and when a working negative prompt is worth having. Those are its strengths, and
the negative-prompt support in particular is rare enough to be a reason on its own.
