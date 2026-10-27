# Kling 4.0 — Continuity & References

Kling 4.0 has no documented seed and no memory between generations. **Continuity is carried by the files you feed back in** — the same reference package, in the same upload order, with the same role lines — plus keyframes and edits of approved clips.

## 1. Housekeeping

- Download every approved output. Keep the file, not a link.
- Library: `characters/`, `locations/`, `products/`, `motion-refs/`, `voices/`, `keyframes/`, `approved-shots/`.
- Per shot, archive: prompt, mode, model (4.0 / Flash), duration, aspect, resolution, and the **ordered asset list** (`@Image1 = characters/mara_front.png`, …).
- Extract keyframes losslessly (PNG) from approved takes — first, last and any milestone frame.

## 2. Plan the Reference Budget

15 assets per generation, inside these caps: 10 images · 5 videos (≤ 30 s combined) · 7 elements (≤ 3 video elements) · 3 voice profiles. Video references, edit sources and video elements share the video budget.

| Priority | Typical allocation |
|---|---|
| 1. Identity | 1 image or element per principal character (a turnaround sheet counts as one image) |
| 2. Hero product/prop | 1 image per object whose shape must not drift |
| 3. Location | 1 image (layout and light) |
| 4. Motion / camera | 1 short video, trimmed to the part you want |
| 5. Voice | 1 voice profile per speaking character, if you have one |
| 6. Style | 1 image, only if Palette can't be said in words |

More references are not better. Each extra asset is another authority competing for control; add one only if it fixes a specific failure.

## 3. Identity Packages

- One **authoritative** image per character: clear face, signature wardrobe, even light. A character turnaround or image grid in a single image is allowed and saves budget.
- **Elements** (subjects) bundle identity for reuse; a video element is built from 3–8 s of footage. Up to 7 per generation.
- Reuse the *identical file* across every shot. Re-exporting or cropping it is a new reference.
- Role line: `@Image1 defines Mara's face, short grey hair and green rain jacket; preserve them exactly.` Then, in the action, refer to her by a short consistent description ("Mara", "the woman in the green jacket").
- Restate only invariants per shot — identity, wardrobe state, held props, light direction, screen direction.

## 4. Voice Continuity

- Up to 3 voice profiles per task, each from 5–30 s of clean audio (≤ 50 MB). Profiles can come from different assets.
- How a profile is bound to a specific character or element is set in the interface; Kling's guide shows no in-prompt voice token *(confirm on your platform; fal notes up to 3 elements can carry a voice)*.
- Without a profile, describe the voice identically every time: age, timbre, speed, accent, emotional baseline.
- For a recurring character voice across a long project, a dedicated voice model with a stored voice ID is more stable than re-describing it.

## 5. Keyframe Storyboards

Keyframes mode takes up to 10 images placed as first, middle and last frames anywhere on the timeline. It **does not accept other reference assets**, so identity must already be in the frames.

1. Generate or select milestone stills with the same identity package (image model or extracted frames).
2. Use only the frames you need — every keyframe is a hard constraint the motion must pass through.
3. Prompt the process between frames: `Use @Image1 as the first frame and @Image2 as the last frame, then describe the [process] in between.`
4. Time the beats to the keyframe positions.
5. Aspect ratio follows the first keyframe — make all frames the same aspect.

Best for transformations, craftsmanship, before/after, and style transitions that must return to the original.

## 6. Edit-First Revisions

When a clip is mostly right, edit it rather than re-rolling — composition and performance that already work survive.

- `Edit @Video1. [one change]. Keep everything else unchanged.`
- Replace a character or environment with an asset: `Edit @Video1. Replace the environment and characters throughout the video with the content from @Image1.`
- Add an element at a moment: `Edit @Video1. When the box is opened again at the end, add @Element1 lying inside asleep.`
- Restyle without re-blocking: `Edit @Video1. Replace the video's style with the felt style of @Image1. Preserve the original composition, shots, and actions.`
- Up to 5 clips per editing task, each 3–30 s; the clip being changed is the one you address with `Edit`.

## 7. Shot-to-Shot Continuity

| Need | Tool |
|---|---|
| Same character, new shot | Same identity image/element, same role line, same short description |
| Shot B must start where shot A ended | Last frame of A as `@Image1` first frame in Keyframes mode |
| Matching camera grammar across a sequence | Same camera reference video in each shot |
| Persistent prop / handedness / screen direction | State it in Overall settings every shot: "carries the parcel in her left hand; travels left to right" |
| Fix one shot of a sequence | Edit that clip; don't regenerate the rest |
| Consistent sound bed | Repeat the ambience description verbatim; keep music "none" until the edit |

## 8. Long and Multi-Shot Sequences

- Up to 30 s in one generation lets a whole short scene live in one take with cuts. Lock continuity in Overall settings, then label shots with times.
- Wide → medium → insert → close-up → wider reveal is a reliable 30 s shape.
- Past 30 s: generate scene by scene and bridge with last-frame keyframes. The 2-minute extend is "coming soon" — use it only if your interface offers it.

## 9. Style Lock

- Put style in one Overall-settings sentence and repeat it verbatim across shots.
- Use a style image only when words fail, and say it controls style only: `@Image3 defines the colour grade and texture only; do not inherit its subject or composition.`

## 10. Migrating from Kling 3.x

| 3.x habit | 4.0 practice |
|---|---|
| `@Character says, "…"` for lip-sync | Quote the line, describe the speaker; `@` tokens now address uploaded assets |
| Elements with a face-adherence slider value | Elements/images with explicit role lines; no adherence value is documented |
| CFG scale, Fun/Spicy modes | Not documented — describe the result instead |
| Long negative prompt | Only "no subtitles" / "no background music" when needed |
| 15 s cap, extend to minutes | 30 s native; extension "coming soon" |
| One video ref ≤ 15 s + 4 images | 5 videos / 30 s, 10 images, 7 elements, 15 total |
| First/last frame only | Up to 10 keyframes anywhere on the timeline |
| Storyboard shots with durations | Still works; durations now fit inside 3–30 s |
