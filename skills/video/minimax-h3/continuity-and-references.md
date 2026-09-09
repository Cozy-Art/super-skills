# MiniMax H3 — Continuity and References

H3 has the most capable reference system in the video catalogue. It is also the one most easily used
wrong, because three separate mechanisms look alike.

---

## The three layers, applied

| Layer | Tokens | Binds | Fails how |
|---|---|---|---|
| Visual identity | `<Subject N>`, `<Picture N>` | Who appears, what they look like | Character drifts or is replaced |
| Speech attribution | `(S1)`, `(S2)` + `<d>…</d>` | Which character speaks which line | Right voice, wrong mouth |
| Voice timbre | `<Audio N>` | What a voice sounds like | Correct speaker, wrong voice |

MiniMax states it directly: *"`<Subject N>` identifies the referenced subject, while `(Sx)` identifies
the actual speaker."*

A single character can occupy all three simultaneously. They compose; they do not substitute.

**Diagnostic:** when something is wrong, the layer tells you where to look. Wrong-looking person →
`<Subject N>` definition. Wrong mouth moving → `(Sx)` assignment. Right person, wrong voice →
`<Audio N>` binding or its retention marker.

---

## Defining subjects

A `<Subject N>` token means nothing until it is bound. Define it once, at the top of the prompt, in
`subject_definitions`.

```
<Subject 1> is the young woman in <Picture 1>, with long dark hair, a blue
cardigan, and a thin silver necklace.
```

**What makes a good definition:**

- **Bind to a source.** `<Picture N>` or `<Video N>`. An unbound subject is just a phrase.
- **Three to five identifying details**, chosen for specificity rather than completeness. "A thin
  silver necklace" reproduces; "nice jewellery" does not.
- **Define once.** Redefining a subject mid-prompt produces two people.
- **Keep the wording stable across generations.** Same subject, same words, every time.

### Split-source subjects

The most distinctive thing H3 does. A subject can draw different attributes from different assets:

```
<Subject 1> is the woman whose appearance comes from <Picture 1> and whose
walking motion comes from <Video 1>.
```

This separates *who someone is* from *how they move*, cleanly. Production uses:

- **Identity from a still, performance from a clip** — cast from a photo, move from a reference take
- **Identity from a still, voice from an audio clip** — pair with `<Audio N>`
- **Camera behaviour from a clip without carrying its subject** — see the retention note below

---

## Retention markers

A fixed vocabulary. The words are not interchangeable with ordinary adjectives.

**Visual:** `fully_preserved` · `partially_preserved` · `attribute_transfer` · `weak_reference`
**Audio:** `fully_copy` · `partially_copy` · `reference` · `weak_reference`

| Marker | Use when |
|---|---|
| `fully_preserved` | A face, a product, a logo — anything that must reproduce exactly |
| `partially_preserved` | Identity holds, wardrobe or setting may vary |
| `attribute_transfer` | Characteristics move **to a different identifiable target subject** |
| `weak_reference` | Loose guidance — camera behaviour, pacing, general feel |

**The common error is `attribute_transfer`.** It does not mean "loosely inspired by." It means taking
characteristics from one asset and applying them to a *different* subject. If you want a reference
video to guide only the camera, that is `weak_reference` on the `<Video N>`, and it is worth saying
explicitly in `retention_analysis` that the video's subject and setting are not to be carried:

```
Camera behaviour follows <Video 1> as a weak_reference only — do not carry
its subject, wardrobe or location.
```

Without that line, a video reference tends to bring its whole scene with it.

---

## Holding identity across generations

H3 is one of the few models where this works reliably, because the reference is a real mechanism rather
than a description.

**The workflow:**

1. **Establish the asset.** Generate or select a hero image of the character. This becomes `<Picture 1>`
   for every subsequent shot.
2. **Write the subject definition once** and store it as a fixed string. Paste it identically into
   every prompt — not paraphrased.
3. **Use `fully_preserved`** for the face and any signature item.
4. **Reuse the same `<Picture N>` asset** across the sequence. A different photo of the same person is
   a different reference and will drift.
5. **Add angles as you get them.** Up to 9 images; extracting a good profile or three-quarter frame
   from an approved generation and adding it strengthens the lock.

**Budget note:** the first five input images are free, then $0.04 each. A nine-image identity lock is
cheap in absolute terms but adds up across an iteration loop — see `parameters.md`.

### Locations, props and brand objects

Same mechanism, same discipline. A location gets a `<Subject N>` and a `<Picture N>` exactly as a
character does. For a brand object, `fully_preserved` is almost always correct — a logo that is
"partially preserved" is a wrong logo.

---

## Voice continuity

`<Audio N>` carries voice timbre, and its retention vocabulary is separate:

| Marker | Effect |
|---|---|
| `fully_copy` | Reproduce the voice as closely as possible |
| `partially_copy` | Keep the character of the voice, allow variation |
| `reference` | Guided by it |
| `weak_reference` | Loose |

**Constraints worth knowing before you plan around it:**

- Audio **cannot be the sole input** — it must be paired with an image or video
- Max 3 audio clips, 2–15 s each, combined ≤15 s
- Audio assets are billed free, unlike images

A recurring character with a consistent voice across a production means keeping one approved audio
clip and binding it every time, exactly as with the identity photo.

**Routing note:** for a *lead* character whose voice must be identical across dozens of shots, a
dedicated voice model with a real identity lock is still the better tool, and the audio should be laid
against H3's picture. H3's native audio is excellent for one-off and background lines. This is the same
distinction the audio skill set draws between a recurring character voice and an incidental one.

---

## Multi-shot within a generation

Shot markers let one generation carry several beats:

```
[Shot 1] … [Shot 2] …
```

Continuity holds across the markers, which makes this the cheapest way to keep two beats matching.
Realistic ceiling is two or three shots inside the 15-second duration cap.

**There is no Extend endpoint.** Claims that H3 output extends to ~30 seconds via a separate tool
circulate widely and are unsupported by the API surface. The documented ceiling is 15 seconds per
generation. For longer sequences, plan a multi-clip workflow with a locked identity rather than
expecting extension.

---

## Frame conditioning versus reference conditioning

These are **mutually exclusive**. `first_frame` and `last_frame` cannot be combined with any
`reference_*` role.

| You want | Use |
|---|---|
| A fixed opening image | `first_frame` |
| A fixed ending | `last_frame` |
| Both ends fixed | Both |
| A character carried from a photo | `reference_*` |
| A fixed opening **and** a referenced character | **Not possible in one call** |

That last row is a real constraint and worth planning around. The usual resolution is to put the
identity work into the reference pass and accept a generated opening, or to generate the opening frame
separately from a reference-conditioned still and then use it as `first_frame`.

---

## When to route elsewhere

H3's reference system is strong; it is not always the right answer.

- **Cross-shot identity over a long sequence with many angles** — H3 is a good choice, and among the
  best available.
- **A lead character's voice across a whole production** — use a dedicated voice model and lay the
  audio against H3's picture.
- **Sequences longer than 15 s in one generation** — `seedance-v2-5` generates 30 s single-pass and
  extends twice.
- **More than 12 reference files** — `seedance-v2-5` accepts up to 30 images, 10 videos and 10 audio
  clips.
- **Cheap exploration** — 768P at $0.08/s is reasonable, but a draft-tier model may be cheaper for
  pure ideation.

Recommending a different model where it genuinely fits is expected, not a failure of this skill.
