# Seedance 2.5 — Best Practices

Depth on prompt construction, following ByteDance's own documented guidance. The hard rules live in
`SKILL.md`.

> **Treat Seedance 2.5 as a visual content producer.** Write structured prompts with a visual
> storytelling mindset. This is ByteDance's own framing and it is the right one — the model rewards a
> shot list, not a mood description.

---

## The recommended structure

Four parts, in order:

**1. Asset referencing.** Each asset by upload-order number, with its job.

**2. One-sentence summary.**
```
Subject + Location + Event + Genre/Style + Camera movement
```

**3. Detailed plot description.** Timestamps or `Shot N` — either is acceptable. Each segment gets its
visuals, camera movement, actions, dialogue and sound effects.

**4. Additional notes.** Anything that stays consistent throughout: camera angle, environment, scene
setting, sound, atmosphere.

For long prompts, ByteDance's own examples use bracketed section headers as an organising convention:

```
[Subject settings]   [Overall style]   [Shot list]   [Strictly exclude]
```

And bracketed shot descriptors within a shot list:

```
Shot 1: [Wide shot, locked-off camera, rule-of-thirds composition] …
```

**Long is fine — unstructured is not.** ByteDance's published examples run 400–700 words. What
degrades output is a wall of prose, not word count.

---

## Timestamps

Seedance 2.5 responds to **integer-second** timestamps. Seedance 2.0 does not — it reads only shot
numbers. Use 1-second intervals as the basic unit.

**Three supported forms:**

| Form | Example |
|---|---|
| Intervals | `0-3 seconds… 3-7 seconds… 7-15 seconds` or `[1s-4s]… [4s-8s]` |
| Time point | `Quick left sideways transition at the 5-second mark.` |
| Relative | `After 3 seconds, everyone around him shakes their head.` |

**Rules:**

- **No gaps.** `0-3s… 5-6s…` leaves a hole the model fills unpredictably. Keep the timeline continuous
- **Balance the load.** Too little plot in a range and the model improvises freely; too much and you
  get excessive cuts or dropped beats
- **Not for high-frequency action.** "Shake your head three times per second" will not work

**Allocate realistically.** A 30-second generation supports six to nine shots at 3–5 seconds each.
Twelve shots in 30 seconds gives each beat two seconds, which reads as a montage whether you wanted one
or not.

---

## Camera language

**Write standard terms directly.** The model knows them:

- **Shot size** — extreme wide / wide / medium / medium close-up / close-up
- **Movement** — push in / pull out / pan / track / follow / orbit / dive / pull back / tilt up /
  handheld shake
- **Angle** — low angle / overhead / first-person
- **Techniques** — one-shot / long take, Hitchcock zoom, dolly zoom, aerial, FPV, bullet time,
  handheld, speed ramp

**For niche or technical terms, write `term + explanation`:**

```
Rack focus: the focus shifts smoothly; the trees that were originally clear
in the foreground become blurred, while the character in the background
gradually becomes clear.
```

**For transitions, specify both trigger point and method:**

```
At the 5-second mark, the camera quickly transitions leftward using a left
wipe combined with a natural dissolve.
```

---

## Action and expression

**Actions — prefer general descriptions.** This is counter to the instinct on most models.

```
✅ doing several sets of high-knee raises and somersaults
✅ both sides engaging in close combat
```

Write specific detail only for the few memorable actions that matter, and **avoid repeating the same
action** across a prompt.

**Expressions — use descriptive sentences, reduce idioms.**

```
❌ her heart sank
✅ her eyes lower and her jaw tightens
```

---

## Reference binding

**Number by upload order, bind explicitly in text.** ByteDance's rule:

> *"The numbering should correspond to the upload order of the assets, such as Image 1 / Video 1 /
> Audio 1, and each asset should be explicitly bound in the text prompt."*

**Never rely on information inside the asset.** Writing "John" on a character image and then saying
"John is at school" causes character confusion or duplication. State the mapping in the prompt.

**For many subjects, use a list:**

```
Images 1-2 are Character 1 and correspond to Audio 1; Images 3-4 are
Character 2 and correspond to Audio 2.
```

**Scope partial references explicitly:**

```
Refer to the action of casting the spell in Video 1 and the wrap-around
camera movement in Video 2.
Refer to Image 1 for lighting and filters.
```

**When an asset is accurate, just point at it** — do not re-describe:

```
Strictly refer to the actions and camera movements in Video 1, and keep the
sequence consistent with the video.
```

There is no need to also describe raising a hand, turning around, or the camera orbiting.

---

## Storyboards

**Storyboards are a high-level plot reference and will not be followed frame-for-frame.** The generated
video keeps a degree of autonomy. If strict alignment is needed, use keyframes instead.

**What works:**

- **≤15 panels.** An 18-panel board causes still frames or out-of-order sequences
- **Stick-figure or line-art.** Simple boards outperform detailed ones
- **No text on the board.** Put that information in the prompt
- **Avoid cluttered or over-sharpened AI-generated boards**
- **No contradictions** between the board and the prompt

**Method:**

1. State the asset mappings
2. Write an overall story summary
3. Describe the plot shot by shot, filling in everything the board doesn't show — actions, camera
   movement, style. Timestamps optional

**For a concept board or keyframe design, simplify:**

```
Construct a complete story plot according to the storyboard sequence, and
use the shots in a reasonable and coherent way.
```

---

## Keyframes — when alignment must be strict

Supply each frame as an **independent reference image in order**, and open the prompt with:

```
Use Images 1 to 7 in order as keyframes.
```

Generated visuals align relatively strictly to the supplied images. Duration remains the director's
choice. This is the tool to reach for when a storyboard's looseness is unacceptable.

---

## 3D clay-model reference

The capability with no equivalent elsewhere in the catalogue. A previz pass supplies motion and camera
while the look comes from references and prose.

**State exactly which elements to take from the clay video:**

```
Refer to the camera movement and motion in [Video 1]…
Refer to the lighting changes, camera movement, and motion in [Video 1]…
```

If the clay pass has no lighting changes, don't ask for them.

**Map references onto the models explicitly:**

```
Map the man in gray clothing from [Image 1] to the red model in [Video 1],
and replace the green model 2 in [Video 1] with the red-haired girl from
[Video 2].
```

**Still describe the target content fully.** A clay reference does not replace description — describe
the intended result in detail and keep it consistent with the clay video. For any subject without its
own image or video reference, describe its appearance and key features.

**Coarse-grained beats fine-grained.** Simple geometric primitives work better as motion references.
For fine-grained clay used for re-rendering, supply a clean pass without trajectory lines, coordinate
grids, camera cones or similar visual interference.

---

## Dialogue

Double quotes, behind a speaker label:

```
Dialogue (elderly woman): "Fly safe, my child. Come back to me."
```

For sung or multilingual content, label each line:

```
English: "Hello"   Chinese: "你好"   Japanese: "こんにちは"
```

Native lip-sync covers 10+ languages. Frame the mouth when it matters.

> **Bracket conventions circulating online are not real.** Music-in-parentheses, SFX-in-angle-brackets,
> dialogue-in-braces, subtitles-in-`【 】` appear in no ByteDance source and are contradicted by their
> own examples.

---

## Negative control

**Documented and narrowly scoped.** ByteDance: *"Use positive descriptions whenever possible. Negative
constraints are supported for subtitles and audio control."*

**Inside the guarantee:**

```
No subtitles.
No BGM; generate only environmental sounds and action sounds.
No audio.
```

Audio negation is fine-grained — sound effects, BGM and dialogue can be suppressed independently.

**Outside it but used in ByteDance's own examples:**

```
No subtitles, no text overlays, no dissolve transitions, no duplicated
people, only hard cuts.

[Strictly exclude]
Black-and-white, monochrome, grayscale; hand-drawn, sketch, line art;
storyboard frames; tilt-shift miniature look, plastic CG.
```

These work. Positive description first, exclusions after.

---

## Mistakes and fixes

| Symptom | Cause | Fix |
|---|---|---|
| Task not recognised as an edit | No trigger word in the prompt | Include `edit`, `add`, `remove`, `replace`, `modify`, `change to` |
| Extension not recognised | No trigger word | Include `extend forward/backward`, `continue`, `continue from` |
| Wrong video acted on | Multiple videos, target unnamed | Name the target explicitly in the prompt |
| Request fails on a locked task | `ratio` not `adaptive`, or `duration` not `-1` for editing | Locked tasks force both |
| Last frame stretched | First and last frames have different ratios | Use matching ratios |
| Character confusion or duplication | Mapping only inside the asset | Bind every asset explicitly in text |
| Storyboard not followed | Storyboard is a high-level reference by design | Use independent keyframes for strict alignment |
| Storyboard produces stills or wrong order | Too many panels | ≤15, stick-figure, no text on the board |
| Reference over-described and fighting the prompt | Re-describing an accurate asset | Just point at it |
| Model improvises inside a timestamp range | Too little plot allocated | Balance the load across the timeline |
| Excessive cuts or dropped beats | Too much plot in a range | Fewer beats, or longer duration |
| Unpredictable gap in the video | Timeline gap between timestamp ranges | Keep intervals continuous |
| Clay reference brings its own look | Elements to reference not scoped | State exactly which elements to take |
| Poor continuity across an extension join | mp4 used | Use `mov` for both input and output |
| Output softer than expected | 720p is the ceiling on 2.5 | Route elsewhere for 1080p/4K — see `README.md` |

---

## Iterating

**Change one section at a time.** The structure makes this cheap — if shot four is wrong, revise shot
four.

**Iterate at 480p.** There is no draft mode on any Seedance model, so the low resolution tier is the
cheap loop.

**Test reference bindings short first.** Confirm identities land correctly on a short generation before
committing to 30 seconds with a dozen references.

**Stay inside the stability recommendations** while iterating — 1–5 subjects for audio/video reference,
1–8 for image reference. Push higher only once the prompt itself is working, so you know which variable
caused a failure.
