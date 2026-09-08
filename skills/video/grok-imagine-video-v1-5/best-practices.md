# Grok Imagine Video 1.5 — Best Practices

Depth on prompt construction. The hard rules live in `SKILL.md`.

---

## Write for the upsampler

The single most useful thing to understand about this model.

xAI's API documentation describes a **prompt-rewriting (upsampler) LLM** that processes every prompt
before generation. What you write is not what the model sees — it is expanded first, by something that
makes its own choices about anything you left out.

**Two consequences:**

**1. Specificity is leverage, not verbosity.** Every element you leave unstated is an element the
upsampler decides. If you don't say where the light comes from, it picks. If you don't say how the
camera behaves, it picks. The prompt is a set of constraints on that expansion.

**2. The "10–20 words" advice is wrong.** It circulates widely, comes from a third-party fan site, and
is contradicted by xAI's own showcase reference-to-video prompt, which runs about **90 words**. A
short prompt does not produce a focused result here; it produces an upsampled result you did not
specify.

**Practical target:** a paragraph or two. Enough to cover subject, action, camera, setting, light and
sound. Stop when you have specified the shot, not when you hit a word count.

---

## Token placement

Put each reference token beside the thing it governs. xAI's own example:

```
the model from <IMAGE_1> walks in from the back of the shot … they wear the
shirt from <IMAGE_2> and black flared jeans
```

`<IMAGE_1>` scopes to the person. `<IMAGE_2>` scopes to the shirt. Collecting both at the front —
`using <IMAGE_1> and <IMAGE_2>, a model walks in wearing a shirt` — loses the scoping and leaves the
upsampler to guess which image governs which element.

**Angle brackets, not `@`.** The `@Image1` form appears nowhere in xAI's documentation and will be read
as ordinary text. See `README.md` for where that claim came from.

---

## Camera and action

Standard cinematography terms work. Be concrete:

| ❌ Vague | ✅ Concrete |
|---|---|
| "cinematic shot" | "low-angle tracking shot, following at waist height" |
| "dramatic lighting" | "hard side light from camera-left, deep falloff" |
| "she moves through the space" | "she crosses from the doorway to the window and stops" |
| "beautiful atmosphere" | "low sun through haze, long shadows toward camera" |

**One primary action per clip.** At the 8-second default there is room for one beat, or one beat and a
settle. Chaining four actions gives the upsampler licence to compress or drop them.

**State the camera explicitly.** Left unspecified, the upsampler chooses — and its choice is generic.
Even "locked off" is a real instruction.

### What not to use

Two camera terms circulate for this model with **zero first-party support**: `camera switch` for hard
cuts, and `fixed lens` / `unfixed lens` as a toggle. Neither appears in xAI's documentation, and the
lens toggle implies a control that exists in neither the API schema nor any documented UI. Do not build
prompts around them.

---

## Audio

Native and on by default. Describe it in prose alongside the picture — ambience, effects, texture.

```
Rain on asphalt, a transformer buzz cutting out, a distant bassline
continuing under it.
```

### Voice, but not script

`<AUDIO_0>` through `<AUDIO_2>` select **preset voices** from xAI's roster, supplied as
`reference_audios: [{"voice_id": "…"}]`. They control *how a speaker sounds*.

```
The person from <IMAGE_1> speaks to camera with the voice from <AUDIO_0>.
```

**There is no documented way to specify what they say.** No quoted-line convention, no scripting
syntax. Assigning a voice does not assign words.

**Handle it one of two ways:**

- Describe the *manner* of speech and accept unspecified content — works for background presence,
  a figure talking at a distance, someone mid-sentence as the shot begins
- Generate the audio elsewhere and lay it against this picture

Do not write a line in quotes expecting it to be spoken. That convention belongs to other models.

---

## Negation — genuinely unknown

**No `negative_prompt` parameter exists.** Whether the model responds to in-prompt negation is
**undocumented** — and a widely repeated claim that negation is "explicitly ignored" has no first-party
basis in either direction.

**Prefer positive replacement:**

| ❌ Negation | ✅ Positive |
|---|---|
| "no camera movement" | "locked off" |
| "not a crowded street" | "an empty street, no traffic in frame" |
| "no smiling" | "expression flat, mouth closed" |

If negation is used, flag it in `notes` as untested rather than presenting it as technique. This is
weaker guidance than the FLUX 3 skill (where BFL endorses negation) and matches `minimax-h3` (where it
is equally undocumented).

---

## No seed

There is **no `seed` parameter**. Seed-locked reproducibility — a standard technique on most models — is
unavailable here.

Continuity has to come from reference images instead. Do not promise a director repeatable output from
a fixed seed on this model; it does not exist.

---

## Resolution trade-off

Worth deciding deliberately, because it is unusual:

- **Text-to-video and image-to-video reach 1080p**
- **Reference-to-video caps at 720p**

So binding a character from reference images **costs you the top resolution tier.** For a hero shot
where identity is already well-described in prose, text-to-video at 1080p may beat reference-to-video
at 720p. For a shot where identity must match, reference mode wins regardless.

There is no cost argument either way — pricing is $0.08/second at every resolution.

---

## Mistakes and fixes

| Symptom | Cause | Fix |
|---|---|---|
| Reference tokens ignored | `@Image1` form used | Angle brackets: `<IMAGE_1>` |
| Wrong image governs wrong element | Tokens collected at the front | Place each token beside what it governs |
| References not binding at all | Index base | Try `<IMAGE_0>` — xAI's docs are inconsistent |
| Result generic despite a short prompt | Upsampler filling gaps | Specify camera, light, setting explicitly |
| Actions compressed or dropped | Too many beats | One primary action per clip |
| Request returns 400 | `image` and `reference_images` both sent | Modes are mutually exclusive |
| Output lower resolution than expected | Reference mode caps at 720p | Use text-to-video or image-to-video for 1080p |
| Image stretched in image-to-video | Aspect ratio overridden | Inherit the source image's ratio |
| Extension came out longer than expected | `duration` is the **added** portion | 10s source + `duration: 5` = 15s total |
| Extension rejected at 12 seconds | Extension range is 2–10, not 1–15 | Different range from generation |
| Edit output shorter than expected | Edit inherits source duration | 4s in, 4s out — capped at 8.7s |
| Spoken words don't match the script | No scripting mechanism exists | Voice tokens select timbre only |
| Cannot reproduce a result | No `seed` parameter | Use reference images for continuity |

---

## Iterating

**Iterate at 480p for speed, not cost** — pricing is per second regardless of resolution, so the only
saving is time-to-result.

**Change one element at a time.** With an upsampler between your prompt and the model, changing three
things at once makes attribution impossible — you cannot tell whether the improvement came from your
edit or from the rewrite.

**Test reference bindings early and short.** Confirm identities land before committing to a
15-second generation. And confirm the index base on the first attempt — that one ambiguity accounts for
most "the reference did nothing" reports.
