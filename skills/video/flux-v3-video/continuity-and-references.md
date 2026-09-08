# FLUX 3 Video — Continuity and References

The most important thing to understand about FLUX 3 continuity, stated once and plainly:

> **FLUX 3 has no cross-generation identity mechanism.** There is no reference token, no attachment
> slot, nothing to point a character at. BFL: *"Video editing and Omni Reference with images and videos
> will be available soon."* Soon is not shipped.

Everything below follows from that.

---

## What `keyframes` actually is

`keyframes` accepts up to 10 images. On most models an array like that is a reference-image slot. Here
it is not, and the difference is total.

BFL's own description: *"Your images become frames of the video… one starts the video, two start and
end it, with more the first starts it, the last ends it, and the rest fall evenly in between."*

| | Reference images (other models) | FLUX 3 `keyframes` |
|---|---|---|
| What the image supplies | An identity or style to apply throughout | A literal frame at a point in time |
| Where it appears | Diffused across the whole clip | At one moment on the timeline |
| How the prompt addresses it | A token (`@Image 1`, `<Subject 1>`) or role prose | Not addressed at all |
| Effect of adding more | Stronger identity lock | More fixed points, tighter pacing control |

**Practical consequence:** phrasings like *"the character from the first reference image"* or *"match
the style of the reference"* have nothing to bind to. They are borrowed from image-editing models and
will be read as ordinary description, competing with the actual conditioning.

**What to write instead:** describe the motion between the frames. The images already carry their
content; the prompt supplies what happens in the gaps.

### Timed placement

Even spacing is the default. To control pacing, place frames explicitly as `[seconds, image]` pairs:

```
[[0, "..."], [3.5, "..."], [9, "..."]]
```

This is the real lever — a beat landing at 3.5s rather than at the midpoint is a directorial choice, and
FLUX 3 is one of the few models that lets you make it.

---

## Holding a character without a reference mechanism

Three techniques, in descending order of reliability.

### 1. One generation, multiple shots — the only real guarantee

Continuity holds **within** a generation, including across hard cuts. Character, look, and a single
audio bed carry through. This is not a workaround; it is the model's actual continuity feature.

```
SHOT ONE — [description]. HARD CUT. SHOT TWO — [description].
```

**If two shots must match, put them in one generation.** Two separate generations of the same character
will drift, and there is no parameter to prevent it.

Realistic ceiling: two or three shots inside the duration cap. Beyond that, the beats get too short to
read.

### 2. A locked character block, reused verbatim

When shots genuinely must be separate generations, write the character description **once** and paste
it identically into every prompt. Not paraphrased — identically.

```
A stooped archivist in his sixties, close-cropped grey beard, round wire
spectacles, a moth-eaten charcoal cardigan buttoned wrong at the collar.
```

Rules that make this work:

- **Three to five fixed, unusual details.** "Buttoned wrong at the collar" does more work than "old
  cardigan" because it is specific enough to be reproduced.
- **Never rewrite it between shots.** Any rewording is a new description and will produce a new person.
- **Keep it in the same position** in every prompt — front-loaded, before the action.
- **Accept that this reduces drift; it does not eliminate it.** Two takes will look like the same
  *character description*, not the same *performer*.

The same discipline applies to locations, props and brand objects. A location block and a prop block,
each locked and reused, are what hold a sequence together.

### 3. Last frame becomes the next first frame

Extract the final frame of an approved clip and pass it as the opening keyframe of the next generation,
with `v2v` continuation or as a single keyframe at position 0.

This is the strongest cross-generation link available, because it is pixel-exact at the join. Its
limits: it constrains only the *opening* of the new clip, and drift resumes from there. Good for a
continuous action carried across two clips; weak for two shots separated in time.

---

## Style and look continuity

Same problem, same shape of answer. There is no style reference.

Build a **look block** and reuse it verbatim alongside the character block:

```
Overcast north light, desaturated except for the lamp warmth, fine grain,
shallow focus with the background dissolved.
```

Keep it short — three or four elements. A long look block starts competing with the action for the
model's attention, and the elements at the end get dropped.

**Do not stack style labels.** "Cinematic, film noir, moody, atmospheric, dramatic" reads as five
competing instructions. One coherent look description beats a pile of adjectives.

---

## What to do until Omni Reference ships

A practical production stance:

1. **Plan sequences as multi-shot single generations** wherever possible. Design around the model's
   actual strength rather than fighting its gap.
2. **Lock character, location and look blocks** at the start of a project and treat them as fixed
   strings. Store them where they can be pasted, not retyped.
3. **Chain via last frames** for continuous action.
4. **Route elsewhere when identity is non-negotiable.** If a named character must appear across a dozen
   shots and be recognisably the same person, FLUX 3 is the wrong tool today. `minimax-h3` has typed
   `<Subject N>` reference tokens with explicit retention markers; `seedance-v2-5` has `@Image 1`
   tokens and accepts up to 30 reference images; `veo-v3` has numbered reference images. Recommending a
   different model is the right answer here, not a failure of this one.
5. **Revisit when Omni Reference lands.** At that point this file, the the reference-token convention capability, and
   the "no cross-generation identity mechanism" section in `SKILL.md` all change together.

---

## Audio continuity

Easy to overlook and cheap to get right.

Within a generation, one audio bed carries across hard cuts — which is much of what makes a multi-shot
generation feel like a single scene rather than two clips glued together. **Keep the ambience
description constant across shots** unless the location actually changes.

Across generations, ambience drifts like everything else. Lock the ambience phrasing the same way you
lock the character block:

```
Low wind across open moorland, distant rooks.
```

Reused verbatim, this does a surprising amount of work in making separate clips feel like one place.
