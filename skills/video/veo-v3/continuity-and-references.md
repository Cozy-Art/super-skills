# Veo 3.1 — Continuity and References

**Read the first section before writing any prompt that involves a reference image.** Veo binds
references differently from almost every other model in the catalogue, and the difference is the kind
that produces confidently wrong output rather than an error.

---

## There is no in-prompt reference token

Google documents **no token of any kind** for pointing at an attached image. Not `@Image1`, not
`<IMAGE_1>`, not `[Image 1]`, not a bare `image 1` ordinal.

References bind through the `referenceImages[]` API array, and each carries a `referenceType` of
`character` or `asset`. **That API field is where the role assignment lives** — the prompt never
addresses a slot.

What the prompt does instead is **re-describe the subject in prose.** Google's own three-reference
example attaches a person, a dress and a pair of sunglasses, and refers to all three purely by
description:

> "The video opens with a medium, eye-level shot of **a beautiful woman with dark hair and warm brown
> eyes**. She wears **a magnificent, high-fashion flamingo dress**… complemented by **whimsical pink,
> heart-shaped sunglasses**…"

Three images attached. Zero tokens in the prompt.

### Why this matters more than it looks like it should

Writing `@Image1` into a Veo prompt does one of two things, both bad:

1. It renders as **literal text in the video** — the characters "@Image1" burned into the frame, or
   spoken.
2. It is ignored, and the reference silently contributes nothing.

Neither fails loudly. You get a plausible video that quietly did not use the reference you attached.

### Why there is no reference-token convention here, not even a prose one

A prose convention applies to models that document a **role-assignment convention** — Luma's
`IMAGE1 (CHARACTER)`, OpenAI's `"Image 1: product photo… Image 2: style reference…"`, BFL's "subject
from image 1, style from image 2". In those, the ordinal is load-bearing and the model parses it.

Google documents nothing of the kind. What is left is ordinary scene description that happens to
overlap with what is attached, with the real role assignment sitting in `referenceType`. That is not a
prompt-side convention, so no reference-token instruction should be emitted at all.

> **History worth keeping.** This skill previously declared numbered reference tokens with the comment
> "Veo binds up to 3 reference images, addressed positionally (@Image1, @Image2…)". That was wrong, and
> it was live — Veo prompts were carrying
> a reference-token instruction the model has no way to honour. Corrected 2026-08-11.

---

## Holding a character across shots

Veo's identity tools are the three references, the seed, and the words. Use all three.

**1. Lock the description.** Write the character once, word for word, and paste the same block into
every shot. Drift in the *prompt* is the largest single cause of drift in the output.

```
a seasoned detective in his fifties, close-cropped grey hair, a three-day beard,
a charcoal wool overcoat with a frayed left cuff
```

Re-use that string verbatim. Do not paraphrase it, do not "vary it for interest", and do not let a
later shot say "the detective" alone.

**2. Attach the same references.** 1–3 stills, `referenceType: "character"`, front-facing, high
resolution, **identical across every shot in the sequence.** Swapping in a better photo halfway through
a sequence changes the face.

**3. Lock the seed.** Same seed plus the same locked description gives materially tighter consistency
than either alone.

**4. Remember the 8-second floor.** Using reference images forces `durationSeconds: 8`. A sequence of
4-second shots cannot use them, so a character-continuity sequence is a sequence of 8-second shots.

---

## Locations, props and brand objects

Same mechanism, `referenceType: "asset"`. The same rules apply: describe it in prose, attach the same
stills, keep the description byte-identical between shots.

Environments are where locked descriptions pay off most, because a location re-described loosely
("the alley") re-invents itself every generation. Carry the full block:

```
a rain-slicked alley behind a shuttered noodle shop, fire escapes on both walls,
a single sodium vapour lamp at the far end
```

---

## First frame, last frame, and interpolation

Distinct from references, and often the better tool:

| Parameter | What it pins |
|---|---|
| `image` | The literal opening frame |
| `lastFrame` | The literal closing frame |
| both | Interpolation between two fixed states |

**Frame conditioning is stronger than reference conditioning.** If a shot must start exactly where the
previous one ended, extract the last frame and pass it as `image` — that is a pixel-level guarantee,
where a reference image is a suggestion.

The pair is the tool for transformations: a character turning, a room changing time of day, a camera
arriving somewhere specific. Give both ends and let Veo find the path.

⚠️ `image` forces 8-second duration.

---

## Extension versus separate clips

For anything beyond 8 seconds, extension usually beats stitching independent generations, because the
model carries its own state forward rather than re-deriving it from a description.

```
Generate 8s at 720p  →  extend +7s  →  extend +7s  →  … up to 20 times (~148s)
```

Three constraints that decide whether this is available at all:

- **720p only.** A 1080p or 4K sequence cannot be built this way.
- **Veo-generated source only.** An external clip cannot be extended.
- **Two-day storage,** with the timer resetting on each reference. A chain left over a weekend is gone.

Each extension takes its own prompt describing what happens *next* — not a restatement of the whole
scene. Keep the locked character and location blocks; change the action.

---

## When to route elsewhere

- **A recurring character's voice must be identical across a production.** Veo's native speech is
  excellent per-clip but has no voice identity lock. Use a dedicated voice model and lay the audio
  against Veo's picture.
- **A shot needs a reference bound to a specific phrase.** Veo cannot do it — there is no token. If the
  work genuinely depends on "the woman in image 2", use a model with a real reference syntax
  (`seedance-v2-5`, `minimax-h3`, `pixverse-v6`).
- **More than 3 references.** `minimax-h3` takes 12; `seedance-v2-5` takes far more.
- **A single take longer than 8 seconds at above 720p.** Not possible; plan the sequence at 720p.
