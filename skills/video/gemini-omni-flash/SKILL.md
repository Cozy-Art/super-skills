---
name: gemini-omni-flash-prompts
description: Generate optimized prompts for Google's Gemini Omni Flash — an any-to-any model that takes text, image and video and returns short video with natively synchronized audio, and supports conversational multi-turn editing of previously generated clips. Use this skill whenever a user mentions Gemini Omni Flash, Omni Flash, or wants a prompt for text-to-video, image-to-video, reference-to-video, or video editing on this model. Also trigger for workflows involving in-prompt timecode blocking, explicit single-take requests, tagged image roles for first frame and style references, or iterative conversational refinement of a clip. Always use this skill instead of guessing at Omni Flash prompt structure from general knowledge — it defaults to a multi-shot edit rather than a single take, its reference tags are zero-indexed, and several capabilities that appear in its API schema are documented as not working.
---

# Gemini Omni Flash Prompt Generator

Generate optimized prompts for Google's Gemini Omni Flash — an any-to-any model that takes text, image
and video and returns short video with natively synchronized sound. Its distinctive strength is
**conversational editing**: a generated clip can be refined across turns, each edit building on the
last, without re-specifying the whole scene.

Its output envelope is tight and fixed: **3 to 10 seconds, 720p, 24 fps,
landscape or portrait only.** Those limits are not settings to negotiate — they are the model.

**This skill produces prompt text, not API calls.** The output goes to a person, who pastes it into
whatever tool they are generating with. Every result ships as two clearly separated pieces: the
**prompt** and a short **suggested settings** line. Never merge the two.

## The One Rule That Overrides Everything

**Settings do not belong in the prompt text.** Aspect ratio, resolution, duration — none of it goes in
the sentence. With only two aspect ratios and one resolution available, there is very little to say
anyway, and words spent on it are words not spent on the shot.

## The Default Is Multi-Shot — Say So If You Don't Want It

The single most important behaviour on this model, and the one that surprises people.

> Google: *"By default Omni Flash will try to create a video with a few different shots."*

Ask for a scene and you will get an **edited sequence** — several angles, cut together — not a single
continuous take. Inside a 3–10 second clip, that means very short shots.

**If you want one take, request it explicitly:**

```
A single continuous take, no cuts.
```

This is not a nudge; it is a required instruction whenever a single shot is wanted. Conversely, if a
mini-sequence is what you want, the default is already working for you and you can shape it with
timecodes rather than fighting it.

## Timecode Blocking

Omni Flash reads explicit time ranges, which is how you control a multi-shot result rather than
accepting whatever cut it chooses:

```
[0-3s] Wide establishing shot of the platform, rain blowing across it.
[3-6s] Tight on the departure board as the letters roll over.
[6-10s] The board settles. Platform lights come up.
```

Natural-language timing also works — "after two seconds," "at the halfway point" — but bracketed ranges
are more reliable when there is more than one beat.

**Keep the ranges continuous and inside the duration.** A clip is 3–10 seconds; three beats is a
comfortable ceiling and four is pushing it.

## Image Role Tags

Google documents two in-prompt tags for assigning roles to uploaded images.

| Tag | Role |
|---|---|
| `<FIRST_FRAME>` | Use this image as the video's opening frame |
| `<IMAGE_REF_N>` | Use this image as a reference — **numbering starts at 0** |

Written inline, in the position where the reference applies:

```
<FIRST_FRAME> a woman is walking

in the style of <IMAGE_REF_0> a woman <IMAGE_REF_1> is walking
```

**Image references start from 0.** `<IMAGE_REF_0>` is the first reference image. Numbered references
elsewhere start at 1.

### Declaration blocks

For clarity with several assets, roles can be declared up front, with `@ImageN` pointing at the Nth
uploaded image:

```
[# Sources <FIRST_FRAME>@Image1] [# References <IMAGE_REF_0>@Image2]
```

Note the mixed bases — `@Image1` is the first upload, while `<IMAGE_REF_0>` is the first reference.
That is Google's own convention, not a typo.

## Editing — the model's real strength

Omni Flash edits conversationally. Each turn builds on the previous result, so an edit prompt should
describe **only the change**.

**Simple beats verbose.** Google's guidance is explicit that short edit instructions outperform
elaborate ones. Do not restate the scene.

```
✅ Make it night.
❌ The same woman in the same coat walking down the same street, but now it
   is night, with streetlights on and the sky dark…
```

**Preserve the rest explicitly** when an edit risks collateral change:

```
Make it night. Keep everything else the same.
```

That phrasing is Google's own documented preserve instruction.

**Editing requires the prior result to have been retained.** If a clip was generated without being
stored, it cannot be edited afterwards — the conversational chain is broken. Worth knowing before a
session rather than after.

## Audio

Native and synchronized, generated with the frames. Direct it in prose alongside the picture.

**But scripted dialogue is not available.** Google documents no mechanism for putting specific words in
a character's mouth, voice editing is unsupported, and the model card states that speech-changing
capability is currently restricted. `No dialogue` works as a *suppression* instruction; there is no
corresponding way to specify a line.

**Practical consequence:** treat Omni Flash as picture-plus-atmosphere. For a scene that needs specific
spoken words, either generate the audio separately and lay it against this picture, or route to a model
with documented dialogue support — see [README.md](README.md).

## Negation

**There is no negative-prompt field, and Google explicitly lists negative-prompt parameters as
unsupported.** Exclusions go in the prompt text instead, which Google's own guidance directs:

```
No dialogue.
No on-screen text.
```

Positive description first; keep exclusions short and specific.

## Mode Selection

| Mode | Use when |
|---|---|
| **Text-to-video** | Fully imagined scene |
| **Image-to-video** | An opening frame is fixed — tag it `<FIRST_FRAME>` |
| **Reference-to-video** | Style or subject carried from images — tag them `<IMAGE_REF_N>` |
| **Edit** | Refining a previously generated clip conversationally |

The mode is inferred from what you supply if not stated.

## What This Model Cannot Do

Worth knowing before planning around it. All documented by Google as unsupported:

- **Video extension** — no continuation of a clip beyond its generated length
- **Interpolation** — no first-and-last-frame in-betweening
- **Multi-video referencing** — *"Referencing or reasoning across multiple videos is not supported"*
- **Video references in practice** — accepted by the API schema, but *"not correctly processed by the
  model at this time"*
- **Audio reference uploads** — *"unsupported in the current version"*
- **Voice editing**
- **System instructions, temperature, top-p, stop sequences**

**Regional restrictions** apply and are easy to trip over: editing *uploaded* videos is unavailable in
the EEA, Switzerland and the UK — editing model-generated videos is fine. Uploading or editing images
containing minors is blocked in the same regions. Only English has been evaluated.

## Suggested Settings

Very little to choose here, which is itself the point.

- **Duration:** 3–10 seconds
- **Resolution:** 720p — the only option
- **Aspect ratio:** 16:9 (default) or 9:16 — the only two
- **Frame rate:** 24 fps, fixed
- **Audio:** native, generated with the picture
- **Watermark:** SynthID on all outputs, non-optional

## Reference Files

- **[parameters.md](parameters.md)** — Model ID, the full option set, the retention behaviour that gates editing,
  pricing, regional restrictions, and an explicit list of documented non-capabilities.

- **[best-practices.md](best-practices.md)** — Single-take versus default multi-shot, timecode discipline, the six
  descriptive dimensions Google's guidance implies, edit-prompt brevity, and a mistakes/fixes table.

- **[continuity-and-references.md](continuity-and-references.md)** — Image role tags in depth, the zero-indexing trap, declaration
  blocks, what conversational editing can and cannot carry, and holding a look across separate
  generations without a reference mechanism that persists.

- **[examples.md](examples.md)** — Annotated examples across all four modes, including a timecoded mini-sequence, a
  single-take request, and a multi-turn conversational edit chain.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
