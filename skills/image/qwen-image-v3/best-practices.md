# Qwen-Image-3.0 — Best Practices

Depth on prompt construction. The hard rules live in `SKILL.md`.

---

## Everything goes in one string

Alibaba's constraint is explicit and it errors rather than degrading:

> *"Only one text object is allowed. Omitting it or providing multiple text objects will result in an
> error."*

Subject, composition, style, on-image copy, layout — one string.

**Structural conventions inside that string are a writing style, not a schema.** This is legitimate and
useful for dense layout briefs:

```
LAYOUT: three-column poster, portrait orientation.
HEADER: large serif type reading "HARVEST FESTIVAL" across the top third.
COLUMN 1: an illustrated wheat sheaf, ink line-work.
COLUMN 2: body text block, small type, left-aligned.
COLUMN 3: a woodcut-style apple.
PALETTE: ochre, deep green, cream ground.
```

That is still a single string. The labels help the model parse a complex brief; they are not fields.

---

## Write for the expander

**`prompt_extend` is `true` by default.** Your prompt is rewritten and expanded by a language model
before generation. What you wrote is not what gets rendered.

This is the same structural situation as Grok Imagine Video's upsampler, and it has the same
implication: **specificity is a constraint on the rewrite**, not verbosity for its own sake. Every
element you leave unstated is one the expander chooses.

### When to turn it off

| Expansion | Use for |
|---|---|
| **On** (default) | Short prompts, exploration, sparse briefs you want filled in |
| **Off** | Reproducible output, precise briefs, layout work, anything specified exactly |

**Two situations demand it off:**

1. **Reproducibility.** A fixed seed only reproduces a fixed prompt. With expansion on, the prompt is
   regenerated each run, so the seed cannot do its job. **Seed plus expansion is a contradiction.**
2. **Precise layout or copy.** If you wrote a structured brief with exact text strings and column
   positions, an expander rewriting it is working against you.

---

## Use the negative prompt — it actually exists

`negative_prompt` is a real, documented parameter. There is no need to phrase artefact suppression
positively here.

**What belongs in it:**

```
blurry, distorted hands, extra fingers, watermark, text artifacts,
oversaturated, low resolution
```

**What does not:** subject matter you simply didn't ask for. Negative prompts are best at suppressing
*artefacts and tendencies*, not at excluding objects. "No people" in a negative prompt is less reliable
than describing an empty scene in the positive one.

**Keep the main prompt positive.** Put exclusions in the field built for them rather than negating
inside the prose — that way the expander has nothing to misread.

---

## Text rendering

Wrap exact on-image copy in double quotes:

```
A hand-painted shop sign reading "COLD BEER" above a doorway.
```

**Note the sourcing:** for 3.0 this convention is documented by a **third-party platform, not by
Alibaba.** It works and it is the right technique — it just isn't vendor-stated here, unlike
Krea 2, where it is.

**Working notes:**

- **Quote the exact string including capitalisation.** `"COLD BEER"` and `"Cold Beer"` are different
  requests
- **Describe the surface and treatment** around the quoted text. Quotes fix the words; prose fixes the
  look
- **Turn expansion off** for anything where the copy must be exact — an expander is free to rewrite your
  wording
- **Multilingual rendering works**, but do not quote a specific language count, font count, or minimum
  pixel size as spec. Those figures are unconfirmed launch marketing

---

## Reference images

**1–3 images, addressed by number in the prompt.** Alibaba documents two forms — bare prose (`image 1`)
and bracketed (`[image 1]`) — with the number matching array position.

**Assign a role to each reference.** This is the intended use, and Alibaba's own examples do it:

```
✅ The girl in Image 1 wears the black dress from Image 2 and sits in the
   pose from Image 3.
```

Don't borrow syntax from other models — `@Image1` and `<IMAGE_1>` have no effect here.

**Order is the binding**, so reordering the array changes what each number points at. Alibaba shows this
with `"Move image 1 onto image 2"` versus `"Move image 2 onto image 1"` — same assets, opposite results.

---

## Sizing

`size` is a `"width*height"` **string**, and **there is no default** — unspecified, the model recommends
a resolution from the prompt, which is a reasonable behaviour to lean on for exploration and a bad one
to rely on for a deliverable.

**Total pixels: 512×512 to 2048×2048.** The same range for text-to-image and editing — supplying
references does not reduce the budget, despite claims otherwise.

---

## Mistakes and fixes

| Symptom | Cause | Fix |
|---|---|---|
| Request errors immediately | More than one `text` object | Exactly one is allowed |
| Request errors on `prompt` | No field of that name exists | It is `{"text": "…"}` in the content array |
| Same seed, different image | `prompt_extend` on | Turn it off — expansion regenerates the prompt |
| Output doesn't match a precise brief | Expander rewrote it | Turn expansion off for exact work |
| On-image copy reworded | Expander rewrote the string | Turn expansion off, quote the exact text |
| CFG / steps parameters rejected | They do not exist on this API | Those come from open-weight Qwen guides |
| Size rejected | Sent as integers | `size` is a `"width*height"` string |
| Unexpected output resolution | No default; model chose | Set `size` explicitly for deliverables |
| Reference number points at the wrong asset | Array reordered after writing the prompt | The number IS the array index — keep them in sync |
| More than 3 references rejected | Ceiling is 3 | — |
| Artefacts persisting | Negative prompt unused | **Use it — this model has a real one** |
| Model unavailable | Limited preview | Access requires Model Gallery application |

---

## Iterating

**Explore with expansion on, finish with it off.** The default is genuinely good for finding a
direction from a sparse prompt — it fills in what you didn't specify. Once the direction is right, turn
it off, write the fuller prompt yourself, and fix a seed.

**That two-phase workflow is the model's natural shape**, and it follows directly from the expansion
default rather than being a workaround.

**Use `n` for variation** — 1 to 6 outputs per call — rather than re-running with different seeds. It is
one request.

**Provisional-model caution:** this is a limited preview with no published technical documentation
beyond the API reference. Behaviour may change without notice. Do not build a production pipeline
around observed quirks without re-testing; this skill is flagged for a follow-up research pass.
