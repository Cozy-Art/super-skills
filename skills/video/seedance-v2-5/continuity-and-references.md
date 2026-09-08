# Seedance 2.5 — Continuity and References

Seedance 2.5 has the largest reference budget in the video catalogue — **50 assets** in one request:
30 images, 10 videos, 10 audio clips. Using it well is mostly discipline.

---

## The binding rule

**Number by upload order. Bind explicitly in the prompt text.**

> ByteDance: *"The numbering should correspond to the upload order of the assets, such as Image 1 /
> Video 1 / Audio 1, and each asset should be explicitly bound in the text prompt."*

**The delimiter does not matter.** ByteDance's own first-party documentation uses at least five forms
interchangeably across its examples:

| Form | Where it appears |
|---|---|
| `@Image1` | Published API curl examples |
| `@Image 1` | Keyframe reference example |
| `@video1` / `@image1` | Task-instruction examples |
| `[Video 1]` / `[Image 1]` | 3D clay-model examples |
| `<video1>` / `<2pic>` | Coarse-grained clay-model example |
| `Image 1:` (bare) | Multi-panel storyboard example |

All work. **Pick one and stay consistent within a prompt.** This skill uses `@Image 1`.

What is load-bearing is the **number matching upload order** and an **explicit binding sentence**.

---

## Never bind inside the asset

The single most common cause of character confusion and duplication.

> Avoid writing "John" on the protagonist's image and then simply saying "John is at school." That
> causes character confusion or duplication.

State the mapping in the prompt instead:

```
Image 1 depicts the protagonist John and uses the voice timbre from Audio 1.
```

**For many subjects, use a list** rather than prose:

```
Images 1-2 are Character 1 and correspond to Audio 1; Images 3-4 are
Character 2 and correspond to Audio 2.
```

---

## Say what each asset is a reference *for*

Every asset gets a stated job. Partial references are supported and should be scoped:

```
Refer to the action of casting the spell in Video 1 and the wrap-around
camera movement in Video 2.

Refer to Image 1 for lighting and filters.
```

**When an asset is already accurate, point at it and stop:**

```
Strictly refer to the actions and camera movements in Video 1, and keep the
sequence consistent with the video.
```

There is no need to also describe raising a hand, turning around, or the camera orbiting. Re-describing
an accurate reference makes the prose compete with the asset.

---

## Reference types

Seedance 2.5 supports a genuinely broad taxonomy. Each can be combined with the others.

| Type | Carries |
|---|---|
| **Subject reference** | Appearance identity and/or voice — person, object, scene, virtual character |
| **Motion reference** | Action, expression, camera movement, effects, from video |
| **3D clay-model reference** | Motion and camera from a coarse or fine white-model pass, rendered into the target style |
| **Style reference** | Visual style of an image or video |
| **Audio reference** | Music, melody, dialogue, voice, tone, timbre |
| **Storyboard reference** | Subjects, composition, actions, plot, scene progression |
| **Keyframe reference** | One or more images used as literal keyframes |

**Audio reference standalone is 2.5-exclusive.** On Seedance 2.0, 2.0 fast and 2.0 mini, an audio
reference must be accompanied by an image or video. On 2.5 it stands alone.

---

## Subject counts — ByteDance's own stability guidance

Not hard caps. Exceeding them works but may need retries.

| | Reliable | Possible, less stable |
|---|---|---|
| Subjects via **image** reference | **1–8** | 9–12 |
| Subjects via **audio/video** reference | **1–5** | 6–10 |

**Reference clip duration:** 5–10 seconds works better for subject audio/video references. Longer
reduces stability.

### Viewpoints

- **1–5 subjects:** single-view and multi-view both supported
- **Above 5 subjects:** single-view is more stable. If multiple viewpoints are needed, **split them
  into separate images per view** rather than one image containing several viewpoints

Multi-view subject reference is another 2.5 addition — Seedance 2.0 does not recommend it.

---

## 3D clay-model reference

The most distinctive capability here, and the one with no equivalent on any other model in the
catalogue. A previz pass supplies motion and camera; the look comes from references and prose.

**State exactly which elements to take:**

```
Refer to the camera movement and motion in [Video 1]…
```

If the clay pass contains lighting changes you also want, say so explicitly. If it doesn't, don't ask.

**Map references onto the models by name:**

```
Map the man in gray clothing from [Image 1] to the red model in [Video 1],
and replace the green model 2 in [Video 1] with the red-haired girl from
[Video 2].
```

**Still describe the target fully.** A clay reference does not replace description. Describe the
intended result in detail, keep it consistent with the clay video, and for any subject lacking its own
image or video reference, describe its appearance and key features.

**Coarse-grained beats fine-grained** for motion reference — simple geometric primitives representing
people, objects and animals. Fine-grained clay is for re-rendering ("colouring" a complete model), and
should be supplied clean: no trajectory lines, coordinate grids or camera cones.

**Why it matters in production:** blocking and dressing become separable decisions. A shot can be
blocked and timed in previz, approved, and only then dressed — with the blocking surviving exactly.

---

## Storyboard vs keyframe

The distinction that decides which to use.

| | Storyboard | Keyframe |
|---|---|---|
| Input | Multi-panel board as one image | Independent images, in order |
| Alignment | **Loose** — high-level plot reference | **Strict** — visuals align closely |
| Use when | The plot matters, the framing doesn't | The framing matters |
| Opening line | Describe the plot per panel | `Use Images 1 to 7 in order as keyframes.` |

**Storyboards will not be followed frame-for-frame.** If that is unacceptable, use keyframes.

Storyboard hygiene: ≤15 panels, stick-figure or line-art, no text on the board, nothing cluttered or
over-sharpened, no contradictions between board and prompt.

---

## Holding identity across generations

Within a request, references hold. Across requests the same assets do the work — with discipline.

1. **Fix the asset.** One approved image per identity, reused in the same slot every time. A different
   photo of the same character is a different reference and will drift
2. **Keep the binding sentence identical.** If `@Image 2` is "the pianist" in shot one, it is "the
   pianist" in shot four — not "the piano player"
3. **Keep slot numbers stable** across a sequence. Costs nothing, makes prompts diffable
4. **Add viewpoints as they accumulate** — but respect the single-view guidance above five subjects

### Return last frame

Seedance returns the last frame of a generation. That frame becomes the next generation's `first_frame`
— pixel-exact at the join, and the strongest cross-generation link available.

Its limit is the usual one: it constrains the *opening* and drift resumes from there. Good for
continuous action, weaker for shots separated in time.

---

## Editing

**Locked task.** `ratio` must be `adaptive`; `duration` must be `-1`. Requires a trigger word.

```
Only edit the man's dialogue in Video 1: change it to "Don't come over here,"
and adjust the accent to an American English accent.

Change the man's action from drinking coffee to mopping the floor from 4-6
seconds in Video 1, and leave the rest of the content unchanged.

Editing task: Replace the Asian woman on the right in Video 1 with the
Latina woman from Image 1.
```

**Describe the change as A → B.** "Change X from A to B" outperforms "make it B."

**Timestamps scope the edit** — `from 4-6 seconds` confines the change to that window and leaves the
rest untouched. This is the feature that makes editing practical on an approved clip.

**What can be edited:** subjects, costumes, camera movements, effects, style, background, colour,
lighting, material, motion, camera position; removal of subjects, subtitles and watermarks; and audio —
vocals, music and sound effects can each be added, modified or removed.

**Practical limits:** input videos ≤20 s produce better results; 1–5 reference images when editing with
references. Use `mov`.

**Duration tolerance:** output may differ from input by up to ~0.3 s, compressing transition frames
only. **No difference at all when the input was itself generated by Seedance 2.5.**

---

## Extension

**Locked task** for aspect ratio; duration is the director's choice. Requires a trigger word.

**Forward or backward** — 2.5 can extend in either direction:

```
Extend @Video 1 backward: the character from @Image 1 falls from the sky…
Continue the first 5 seconds of @Video 1: the woman from @Video 2 enters
the frame and says…
Extend @Video 1 by 5 seconds. A bee flies in and lands on the flower…
```

**Use `mov` for both input and output.** Volume may differ slightly between input and generated
segment; that difference is smallest when the source was itself generated by Seedance 2.5.

Reference assets can be combined with extension — a new character entering an extended clip can carry
their identity from an image.

---

## When to route elsewhere

- **1080p or 4K output** — **Seedance 2.5 tops out at 720p.** Seedance 2.0 offers 1080p and 4K, as do
  other models in the catalogue. This is the most likely reason to route away, and it is
  counter-intuitive
- **Per-attribute reference control** — `minimax-h3` draws appearance from one asset and motion from
  another *within a single subject definition*, with explicit retention markers. Seedance scopes
  references by sentence instead
- **Keyframe timing at specific seconds with a fast preview loop** — `flux-v3-video` has timed
  keyframes and a draft/enhance workflow. Seedance has no draft mode
- **A lead's voice across a production** — a dedicated voice model with a real identity lock, laid
  against Seedance's picture

**Reach for Seedance 2.5 when the scene is long, crowded, previz'd, or needs editing and extension with
clean joins.** Those are what it does better than anything else here.
