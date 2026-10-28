---
name: kling-4-prompts
description: Generate optimized prompts for Kling 4.0 and Kling 4.0 Flash, Kuaishou's video model with 3–30 s native generation, up to 10 keyframes, Omni Reference (up to 15 assets — 10 images, 5 videos totalling 30 s, 7 elements, 3 voice profiles), 8,000-token prompts, two-channel stereo audio with multilingual lip-sync, 21:9 ultrawide and prompt-driven video editing. Use whenever a user mentions Kling 4, Kling 4.0, Kling 4 Flash, kling-v4, Kling Omni Reference or Multiple Keyframes on klingai.com / kling.ai, or wants @Image1 / @Video1 / @Element1 reference prompts, edit prompts ("Edit @Video1…"), long multi-shot sequences, keyframe storyboards or dialogue scenes on Kling — including on fal or other hosts. Also use when migrating Kling 3.x prompts, since @Character lip-sync tokens, CFG, face-adherence sliders and heavy negative prompts are not part of the 4.0 workflow. Do not guess Kling 4 syntax from general knowledge or Kling 3.x habits.
---

# Kling 4.0 — Prompt Generation Skill

Kling 4.0 (Kuaishou, general rollout mid-October 2026) generates **3–30 s video with native two-channel stereo audio** in one pass, from text plus up to 15 reference assets, or from up to 10 keyframe images. **4.0 Flash** is the faster, cheaper tier. It is an expansion of the Kling 3.x craft, not a new prompt language — what changed is *control*: role-assigned references, keyframe timelines, longer prompts and in-place editing.

## The Three Rules That Override Everything

1. **Every reference gets a job, in words.** Assets are numbered by upload order (`@Image1`, `@Image2`, `@Video1`, `@Element1`). Open the prompt with one line per asset saying what it defines and what to preserve — and what *not* to inherit ("@Video1 supplies camera movement only; do not inherit its actor or location"). Unassigned references make results unpredictable.
2. **Describe what you want; keep negatives to two.** Kling's own guide: negative instructions can increase errors — the only two that are truly necessary are **no subtitles** and **no background music**. Everything else, state positively.
3. **Settings live in the interface, not the prose.** Mode, duration, aspect ratio, resolution and Flash vs. full model are chosen in the UI/API; the prose must agree with them (don't write "a 30-second 16:9 video" on a 10 s 9:16 job). **When the user's interface or API rejects or contradicts a value in this skill, the interface wins — adjust and say so.**

## Prompt Order (Kling's four-part template)

| # | Section | What goes in it |
|---|---|---|
| 1 | **Asset roles** | `@Image1 defines ___; preserve its ___.` One line per asset. Skip if no assets. |
| 2 | **Overall settings** | Scene and texture; visual style; camera tone; light direction; continuity invariants (props, handedness, screen direction) |
| 3 | **Sequence of events** | Chronological beats, optionally timecoded: `0–4s: …` `4–8s: …` `8s–end: …` — visuals + action + emotion, then camera movement, then the closing frame |
| 4 | **Audio** | Dialogue/voice-over in quotes (in the spoken language) + ambience + music (or none) + effects; then `No subtitles.` if needed |

```
@Image1 defines [subject]; preserve its [face / outfit / shape].
@Image2 defines [location]; preserve its [layout / light].
[Scene and texture]. [Visual style]. [Camera tone]. [Continuity invariants].
0–Xs: [visuals + action + emotion]. X–Ys: [camera move + detail]. Ys–end: [closing shot].
Audio: [speaker description] says, "[line]". [Ambience]. [Effects]. [Music or "no music"]. No subtitles.
```

**Length:** up to 8,000 **tokens** (not characters). Simple prompts work — Kling fills in blocking and camera — but a clear, detailed prompt is followed without reinterpretation. Add a line only if it controls something (identity, prop, camera path, sound timing). Longer clips need more *beats*, not more adjectives.

## Decide the Mode First

| User wants | Entry point | Inputs | Prompt describes |
|---|---|---|---|
| New clip from text | Omni Reference (default) | text only | the whole shot/sequence |
| Same character/location/product | Omni Reference | images, elements (+ voice profiles) | roles, then action |
| Copy camera move, choreography or pacing | Omni Reference | `@Video1` as motion/camera reference | what to take from it and what not to inherit |
| Animate a still from frame one | Keyframes | `@Image1` as first frame | "Use @Image1 as the first frame, then…" |
| Hit fixed milestones / transformation | Keyframes | 2–10 images (first, middle, last) | the process between frames |
| Change an existing clip, keep the rest | Omni Reference, edit | `@Video1` (+ images/elements) | `Edit @Video1. [change]. Keep everything else unchanged.` |
| Fast/cheap ideation | 4.0 Flash, if your plan offers it | as above | same prompt |

Keyframes mode **does not accept reference assets** — identity there comes from the keyframes themselves.

## Quick Syntax Reference

- **Reference tokens:** `@Image1` `@Video1` `@Element1`, numbered by upload order (Kling's guide also shows `@Image 1` with a space). Example: `Reference the facial features of the characters in @Image1, @Image2, and @Image3, keeping them strictly consistent.`
- **Edit:** start with `Edit @Video1.` — writing only "Reference @Video1" may be read as reference-based generation, not an edit. Add `Keep everything else unchanged.` / `Preserve the original composition, shots, and actions.`
- **Continuous take vs. cuts:** multi-shot is **on by default** (Kling splits shots automatically). For one take write `one continuous shot with no cuts, angle changes, or scene changes`; for cuts write labelled shots `Shot 1 (0–5s): …` with hard cuts.
- **Dialogue:** quoted, in the language to be spoken; describe the speaker's age, tone, speed and emotion. Languages: Chinese, English, Japanese, Korean, Spanish, Portuguese, German, French, Hindi (+ Sichuanese/Cantonese dialects; American/British/Indian English accents).
- **Stereo:** place sound sources in space ("wind crossing from left to right", "a door slams off frame-right").
- **On-screen text:** quote it exactly; for subtitles give font size, alignment and timing; otherwise say `No subtitles`.

## Output Format (always two parts)

1. **Prompt** — in a code block. Asset roles → settings → timed events → audio. No mode, duration, aspect ratio, resolution or model name in the text.
2. **Suggested settings** — one line, e.g. `mode: Omni Reference · model: Kling 4.0 · duration: 12 s · aspect ratio: 16:9 · resolution: 1080p (4K if your plan/interface offers it) · uploads in order: @Image1 character, @Image2 location, @Video1 camera ref`

Always list the **upload order** so the token numbers resolve to the right files.

## Things That Will Break the Request

- Over the limits: >15 assets total, >10 images, >5 videos or >30 s of video combined, >7 elements (>3 video elements), >3 voice profiles, >10 keyframes; images >30 MB or outside 2:5–5:2; videos outside 3–30 s each or >300 MB; element source footage outside 3–8 s; voice audio outside 5–30 s.
- Reference assets uploaded in **Keyframes** mode (not supported there).
- A token for an asset that isn't uploaded, or numbering that doesn't match upload order.
- "Reference @Video1" when you meant **Edit @Video1**.
- Asking for "one continuous move" and "cut to…" in the same prompt.
- Assuming 10-bit HDR, 2-minute extension, or (at launch) 4K are live — Kling marks HDR and extension "coming soon"; check your interface.
- Kling 3.x carry-overs: `@Character says` lip-sync tokens, CFG scale, face-adherence values, "Fun/Spicy" modes, long negative-prompt lists. None are documented for 4.0.

## Iteration Workflow

1. Draft on **4.0 Flash** (if available) or 720p at the target duration — check blocking, references and sound.
2. Change one variable per pass: roles → action beats → camera → audio.
3. When a clip is mostly right, **edit it** (`Edit @Video1 …`) instead of re-rolling.
4. Lock milestones with Keyframes (extract frames from approved takes) when free generation drifts.
5. Final at 1080p (or 4K where offered) with the same prompt and identical reference files in the same order.

## Reference Files

- [best-practices.md](best-practices.md) — the four-part template in depth, role manifests, timed beats, continuous vs. multi-shot, camera and action craft, audio/stereo/dialogue/languages, text rendering, negative-instruction policy, long-clip pacing, common-mistakes table.
- [continuity-and-references.md](continuity-and-references.md) — reference budget planning, identity packages, elements and voice profiles, keyframe storyboards, edit-first revisions, shot-to-shot continuity, carrying results between generations, migrating from Kling 3.x.
- [examples.md](examples.md) — 10 annotated prompts: character performance, landscape, action with motion reference, camera transfer product spot, keyframe style transition, first/last-frame process, 30 s multi-shot narrative, bilingual dialogue, remove/replace edit, add-element edit.
- [parameters.md](parameters.md) — entry points, every documented limit, duration/aspect/resolution options and defaults, Flash vs. full, rollout status, host notes, open uncertainties.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
