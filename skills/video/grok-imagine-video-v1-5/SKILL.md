---
name: grok-imagine-video-1-5-prompts
description: Generate optimized prompts for xAI's Grok Imagine Video 1.5 — a video model with native audio, angle-bracket reference tokens for visual identity, and a separate preset-voice token system for speech attribution. Use this skill whenever a user mentions Grok Imagine Video, Grok video generation, or wants a prompt for text-to-video, image-to-video, reference-to-video, video editing, or video extension on this model. Also trigger for workflows binding a character or wardrobe from reference images, assigning a preset voice to an on-screen speaker, or extending an existing clip. Always use this skill instead of guessing at Grok Imagine Video prompt structure from general knowledge — its reference tokens use angle brackets rather than the @-syntax widely repeated online, its audio tokens bind voices rather than identities, and several of its parameter defaults differ from what circulates in third-party guides.
---

# Grok Imagine Video 1.5 Prompt Generator

Generate optimized prompts for xAI's Grok Imagine Video 1.5 — a video model with native audio,
angle-bracket reference tokens, and an unusually clean separation between *who appears* and *what they
sound like*.

**This skill produces prompt text, not API calls.** The output goes to a person, who pastes it into
whatever tool they are generating with. Every result ships as two clearly separated pieces: the
**prompt** and a short **suggested settings** line. Never merge the two.

## The One Rule That Overrides Everything

**Settings do not belong in the prompt text.** Aspect ratio, resolution, duration — none of it goes in
the sentence. They are controls with their own fields.

## Reference Tokens — angle brackets, not `@`

**xAI uses `<IMAGE_1>`, `<IMAGE_2>`.** Written inline, at the point in the sentence where the reference
applies. From xAI's own showcase prompt:

```
the model from <IMAGE_1> walks in from the back of the shot … they wear the
shirt from <IMAGE_2> and black flared jeans
```

> **The `@Image1` form does not exist on this model.** It circulates widely in third-party guides and
> video tutorials, appears nowhere in xAI's documentation, and will be read as ordinary text.

**Placement carries meaning.** `the model from <IMAGE_1>` binds identity; `the shirt from <IMAGE_2>`
binds wardrobe. Collecting the tags at the front of the prompt loses that scoping — put each token
beside the thing it governs.

### Index base — genuinely ambiguous, so don't assert one

xAI's own documentation is inconsistent. The main worked examples are 1-indexed (`<IMAGE_1>`,
`<IMAGE_2>`), but the reference-audio subsection instructs tagging images `<IMAGE_0>` when audio is
also passed — while that same section's combined example uses `<IMAGE_1>` alongside `<AUDIO_0>`.

**Practical stance:** default to `<IMAGE_1>` (the form in the primary examples). If references are not
binding as expected, try the zero-based form before assuming the prompt is wrong.

### How many references

xAI publishes **no numeric cap**. Their own examples use three. A figure of seven circulates in
third-party guides with no basis in the API schema — do not rely on it.

## Voice Tokens Are Not Identity Tokens

The distinction this model draws cleanly, and the one most easily collapsed.

| Token | Binds | Supplied via |
|---|---|---|
| `<IMAGE_N>` | **Visual identity** — who appears, what they wear | Reference images |
| `<AUDIO_N>` | **Voice timbre** — what they sound like | A preset voice from xAI's roster |

xAI's own example uses both at once:

```
The person from <IMAGE_1> speaks to camera with the voice from <AUDIO_0>.
```

`<AUDIO_0>` through `<AUDIO_2>` — up to three — select **preset voices**, not uploaded audio. Custom
voice cloning is restricted to trusted partners.

**Why this matters:** an `<AUDIO_N>` token looks like a reference and is not one. It carries no
likeness and no visual information. Only `<IMAGE_N>` holds identity.

## Dialogue — voice, but no script

Grok generates an audio track by default, and `<AUDIO_N>` lets you choose *how a speaker sounds*.

**But xAI documents no way to specify what they say.** There is no scripting syntax, no quoted-line
convention, nothing equivalent to the double-quote trigger on other models.

**Practical consequence:** treat this as picture plus atmosphere plus voice *character*. For specific
spoken words, generate the audio separately and lay it against this picture, or route to a model with
documented dialogue support — see `README.md`.

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

Modes are **mutually exclusive.** Passing `image` and `reference_images` together returns an error.

| Mode | Use when | Notes |
|---|---|---|
| **Text-to-video** | Fully imagined scene | 1080p available |
| **Image-to-video** | An opening image is fixed | 1080p available. Inherits the image's aspect ratio |
| **Reference-to-video** | Identity or wardrobe carried from images | **Capped at 720p** |
| **Edit** | Changing an existing clip | Runs on the non-1.5 model. Inherits then caps |
| **Extend** | Continuing a clip | Own duration range — see below |

## Extension — the duration is the *addition*

Easy to get wrong and worth stating plainly.

> xAI: *"if your input video is 10 seconds and you set `duration` to 5, the returned video will be 15
> seconds."*

Extension duration is **what gets added**, not the total. And it has **its own range — 2 to 10 seconds,
default 6** — which is narrower than the 1–15 range for generation.

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
unavailable. Plan continuity around reference images instead.

## Suggested Settings

- **Duration:** 1–15 seconds, **default 8**
- **Resolution:** 480p (**default**), 720p, 1080p. **1080p is text-to-video and image-to-video only**;
  reference-to-video caps at 720p
- **Aspect ratio:** 1:1, 16:9 (default), 9:16, 4:3, 3:4, 3:2, 2:3. Image-to-video inherits the source
  image's ratio — **overriding it stretches the image**
- **Audio:** on by default
- **Extension:** 2–10 seconds, default 6 — the *added* portion

## Reference Files

- **`parameters.md`** — Model ID and aliases, the full option set with real defaults, mode
  exclusivity, the edit and extension rules, pricing, and what xAI does not publish.

- **`best-practices.md`** — Writing for the upsampler, token placement, camera and action language,
  the audio layer, and a mistakes/fixes table.

- **`continuity-and-references.md`** — Reference tokens in depth, the identity-versus-voice
  distinction, holding a character without a seed, and the resolution trade-off that reference mode
  imposes.

- **`examples.md`** — Annotated examples across all five modes, including a reference-bound character
  with an assigned voice, an extension, and an edit.
