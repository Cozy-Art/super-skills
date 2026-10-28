---
name: grok-imagine-video-1-5-prompts
description: "Generate optimized prompts for xAI's Grok Imagine Video 1.5 — native audio with lip-synced speech, zero-based angle-bracket reference tokens for visual identity (up to 14 images), a separate voice token system (up to 3 voices), first/last-frame pinning and up to 4 keyframes. Use whenever a user mentions Grok Imagine Video or Grok video generation, or wants a prompt for text-to-video, image-to-video, reference-to-video, pinned frames, or scripted dialogue on this model — and to route editing or extension to classic grok-imagine-video. Also trigger for binding a character, product or wardrobe from reference images, assigning a voice to an on-screen speaker, or looping a clip. Never guess Grok Imagine Video prompt structure from general knowledge — its tokens use angle brackets, not the @-syntax repeated online, they start at zero, its audio tokens bind voices rather than identities, and several defaults differ from third-party guides."
---

# Grok Imagine Video 1.5 Prompt Generator

Generate optimized prompts for xAI's Grok Imagine Video 1.5 — a video model with native audio and
lip-synced speech, angle-bracket reference tokens, and an unusually clean separation between *who
appears* and *what they sound like*.

**This skill produces prompt text, not API calls.** The output goes to a person, who pastes it into
whatever tool they are generating with. Every result ships as two clearly separated pieces: the
**prompt** and a short **suggested settings** line. Never merge the two. When the user's interface
rejects or contradicts a value given here, **the interface wins** — adjust and say so.

## The One Rule That Overrides Everything

**Settings do not belong in the prompt text.** Aspect ratio, resolution, duration — none of it goes in
the sentence. They are controls with their own fields.

## Reference Tokens — angle brackets, not `@`, starting at zero

**xAI uses `<IMAGE_0>`, `<IMAGE_1>`, …** — *"Refer to reference images in the prompt by their position
in the list, starting at `<IMAGE_0>` for the first image, then `<IMAGE_1>`, and so on."* Written inline,
at the point in the sentence where the reference applies. From xAI's own showcase prompt:

```
the model from <IMAGE_0> walks in from the back of the shot … they wear the
shirt from <IMAGE_1> and black flared jeans
```

> **The `@Image1` form does not exist on this model.** It circulates widely in third-party guides and
> video tutorials, appears nowhere in xAI's documentation, and will be read as ordinary text.

**Placement carries meaning.** `the model from <IMAGE_0>` binds identity; `the shirt from <IMAGE_1>`
binds wardrobe. Collecting the tags at the front of the prompt loses that scoping — put each token
beside the thing it governs.

### Index base — zero, with one shift

xAI now states the base explicitly: the first reference image is `<IMAGE_0>`. **One exception:** if a
first frame is also pinned with `image`, *"it takes `<IMAGE_0>` and your reference images start at
`<IMAGE_1>`."* Number the tokens by what is actually attached, in order.

(Earlier versions of xAI's pages mixed `<IMAGE_1>`-first examples with zero-based instructions; the
current reference-to-video page is consistent. If a wrapper documents its own numbering, follow it.)

### How many references

**Up to 14 reference images** per request on 1.5 (classic `grok-imagine-video` takes 7). xAI's own
showcase uses 14 at once — a model, a room and 12 catalog products. Some hosted routes cap lower and
restrict references further; the interface is the source of truth.

## Voice Tokens Are Not Identity Tokens

The distinction this model draws cleanly, and the one most easily collapsed.

| Token | Binds | Supplied via |
|---|---|---|
| `<IMAGE_N>` | **Visual identity** — who/what appears, what they wear, where | Reference images (and a pinned first frame) |
| `<AUDIO_N>` | **Voice timbre** — what they sound like | A preset `voice_id`, or an audio clip ≤ 15 s where enabled |

xAI's own example uses both at once:

```
The person from <IMAGE_0> presents the product from <IMAGE_1> on the set from
<IMAGE_2>, speaking with the voice from <AUDIO_0>. A second speaker with the
voice from <AUDIO_1> replies.
```

`<AUDIO_0>` through `<AUDIO_2>` — **up to three** — are their own zero-based list, independent of the
image numbering. Preset voices come from xAI's TTS roster. The request schema also accepts an uploaded
clip (≤ 15 s) per voice, but xAI's guide says *"voice references with your own audio files are
available to trusted partners"* — treat uploads as access-dependent.

**Why this matters:** an `<AUDIO_N>` token looks like a reference and is not one. It carries no
likeness and no visual information. Only `<IMAGE_N>` holds identity.

## Dialogue — write the lines in quotes

Grok generates an audio track by default, and 1.5 *"generates lip-synced speech."* xAI's own examples
script it the plain way — the speaker, then the line in double quotes:

```
Sam: "I took the job in Berlin. We could leave in March."
Lena: "We? You didn't even ask me."
```

```
She says: "Welcome to my dream living room."
```

`<AUDIO_N>` chooses *how* a speaker sounds; the quoted line says *what* they say. Name or place each
speaker so the line lands on the right face, and keep lines short — xAI's four-line exchange fills a
15-second clip. xAI publishes this as example usage, not a formal rule; there is no tag syntax.

## Prompt Length — write for the scene, not for brevity

A widely repeated claim that this model wants "10–20 words" is **not from xAI** and is contradicted by
two things:

1. **xAI's own showcase reference-to-video prompt runs about 90 words**
2. **The API passes prompts through a documented prompt-rewriting (upsampler) LLM before generation**

That upsampler is the important detail. A short prompt is not fed to the model as written — it is
expanded first, by something making its own choices. **A more specific prompt gives the upsampler less
to invent**, which is the opposite of what a short-prompt optimum would imply.

Write enough to specify the shot: subject, action, camera, setting, light, sound.

**There is a length ceiling** — xAI's error table covers "a prompt that is too long" — but **no number
is published.** Don't write to a budget; do stay inside a paragraph or two.

## Mode Selection

The mode follows from which inputs are attached. On 1.5 they **combine**: `image` alone is
image-to-video; `image` plus `reference_images`, `reference_audios`, `last_frame` or `keyframes` is
reference-to-video with that image pinned as the first frame.

| Mode | Use when | Notes |
|---|---|---|
| **Text-to-video** | Fully imagined scene | Native 1080p available |
| **Image-to-video** | An opening image is fixed | Native 1080p available. Output takes the image's aspect ratio |
| **Reference-to-video** | Identity, product, wardrobe or set carried from images; assigned voices | **Capped at 720p**, up to 15 s |
| **First / last frame** | The clip must start and/or land on exact images | Counts as reference-to-video. Same image both ends = a loop |
| **Keyframes** | Exact images must appear at set moments mid-clip | Up to 4. Counts as reference-to-video |
| **Edit / Extend** | Changing or continuing an existing clip | **Not on 1.5** — classic `grok-imagine-video` |

## Pinned frames — first, last, keyframes

`image` pins the first frame, `last_frame` the last, and up to **four** `keyframes` pin images at
exact timestamps strictly inside the clip (on a 1/3-second grid). The model generates everything
between. A prompt is optional once a frame is pinned — but write one: it is the only place to say
**how** the clip travels between pins (the action, the camera path, the sound).

Don't re-describe the pinned images; describe the transition. To loop, pin the same image at both
ends and write motion that returns to it.

## Extension — the duration is the *addition*

Extension runs on classic `grok-imagine-video`, not 1.5 — a 1.5 clip can be the source.

> xAI: *"if your input video is 10 seconds and you set `duration` to 5, the returned video will be 15
> seconds."*

Extension duration is **what gets added**, not the total. And it has **its own range — 2 to 10 seconds,
default 6** — which is narrower than the 1–15 range for generation. The source must be 2–15 seconds.

Extension continues **from the last frame** of the input. There is no frame-selection option; claims to
the contrary are unsupported.

## Editing — inherit, then cap

Video edit does not produce a fixed-length output. It **retains the source's duration, capped at 8.7
seconds**, and **matches the source's resolution, capped at 720p**. A 4-second input yields a 4-second
output; a 1080p input is downsized to 720p.

Note that editing runs on the non-1.5 `grok-imagine-video` model, so 1.5-specific improvements do not
apply to it.

## Negation

**There is no negative-prompt parameter.** Whether the model responds to in-prompt negation is
**undocumented** — a widely repeated claim that negation is "explicitly ignored" has no first-party
basis either way.

Prefer positive description. If negation is used, treat it as untested rather than as technique.

## Reproducibility

**There is no `seed` parameter.** Seed-locked consistency — a standard technique elsewhere — is simply
unavailable. Plan continuity around reference images and pinned frames instead.

## Suggested Settings

- **Duration:** 1–15 seconds, **default 8**
- **Resolution:** 480p (**default**), 720p, 1080p. **Native 1080p is text-to-video and image-to-video
  only**; anything with references, voices, a last frame or keyframes caps at 720p
- **Aspect ratio:** 1:1, 16:9 (default), 9:16, 4:3, 3:4, 3:2, 2:3, 21:9, 5:2. Image-to-video ignores
  `aspect_ratio` — the output always matches the source image
- **Audio:** on by default; switch it off in settings for a silent clip
- **Cost:** priced per second **by resolution** — $0.08 (480p) / $0.14 (720p) / $0.25 (1080p), plus
  $0.01 per input image
- **Extension (classic model):** 2–10 seconds, default 6 — the *added* portion

## Reference Files

- **[parameters.md](parameters.md)** — Model ID and aliases, the full option set with real defaults, how
  inputs combine into modes, pinned frames, the edit and extension rules, pricing by resolution, and what
  xAI does not publish.

- **[best-practices.md](best-practices.md)** — Writing for the upsampler, token placement, camera and action language,
  the audio and dialogue layer, pinned-frame prompts, and a mistakes/fixes table.

- **[continuity-and-references.md](continuity-and-references.md)** — Reference tokens in depth, the identity-versus-voice
  distinction, holding a character without a seed, pinned frames as continuity, and the resolution
  trade-off that reference mode imposes.

- **[examples.md](examples.md)** — Eight annotated examples across the modes, including a reference-bound character
  with an assigned voice and scripted line, a keyframed clip, an extension, and an edit.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
