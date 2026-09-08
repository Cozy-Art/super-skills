# Seedance 2.0 — Continuity, References, Editing & Extension

Seedance 2.0 has no persistent "character ID" or seed-lock system that guarantees identity across separate generations. Continuity is achieved entirely through **Reference-to-Video mode plus disciplined, repeated prompt text.** This file covers how, and how it maps onto a shot-chain / continuity-anchor production workflow.

---

## The Three Continuity Mechanisms

### 1. Reuse the exact subject description

The most basic and most reliable technique. Lock a canonical description — age, hair, clothing, distinguishing features — the first time a character appears, then paste that exact wording into every subsequent prompt for that character. Small wording drift ("grey wool coat" becoming "gray coat" three prompts later) is enough to introduce visible inconsistency. Treat the description as a fixed string, not something to paraphrase per shot.

This is the text equivalent of a **Continuity Anchor**: the canonical description *is* the anchor, and every downstream prompt should quote it rather than re-derive it.

### 2. Image-to-Video from a hero frame

Once a strong frame exists — a generated still, a concept image, an approved character turnaround — switch to Image-to-Video and use it as the first-frame reference. The image anchors identity and look; the prompt then only needs to describe motion, camera, and audio, not the character's appearance all over again.

```
[Motion]. [Camera]. [Audio].
```
Never redescribe the reference image itself — it's already fixed as the first frame.

### 3. Reference-to-Video chaining

The deepest continuity mechanism, and the one that maps most directly onto sequence work: feed a prior clip in as `@Video1` and describe its role explicitly.

```
Keep the camera movement and color grading from @Video1. [New subject
beat, same character as before]. [Setting/lighting continuity note if
the scene continues]. [Audio].
```

**Example — continuing a sequence:**
```
Use the camera movement from @Video1 throughout and keep the color
grading and character appearance from @Image1. The protagonist jogs
along a riverside path and waves at the camera once. Handheld follow
shot, soft morning daylight, light filmic documentary style. Ambient
river sounds and light city noise.
```

This is the pattern to reach for whenever a shot needs to feel like part of the same sequence as the one before it — treating the earlier clip as the camera/motion reference while the new text defines only the new beat.

---

## Reference-to-Video: Combining Modalities

Reference-to-Video accepts up to 9 images, 3 video clips, and 3 audio clips in a single generation (12 files total), each addressed in the prompt by its own token: `@Image1`, `@Image2`, `@Video1`, `@Audio1`, and so on.

Assign each reference a clear **role** in the prompt rather than just listing them:

```
Use @Image1 as the first frame and reference for character appearance.
Use @Video1's camera movement throughout. Use @Audio1 as the
background music.
```

**Common combinations:**

| Goal | References to combine |
|---|---|
| Character consistency in a new scene | 1 image (character look) |
| Camera/motion continuity across a sequence | 1 video (prior shot) |
| Style + camera continuity | 1 image (style/grade reference) + 1 video (camera reference) |
| Music-synced content | 1 image or video (visual) + 1 audio (rhythm/track reference) |
| Outfit or prop change mid-sequence | 1 video (base performance) + 1 image (new outfit/prop) |
| Full multimodal continuity | 1 video (motion) + 1 image (character) + 1 audio (music bed) |

---

## Video Editing (Change One Thing, Keep Everything Else)

Provide a reference video and describe the change plus what must stay the same. This is Reference-to-Video used for a targeted edit rather than a new scene.

```
Recreate the scene from @Video1 but [the one change]. Keep [invariant
A] and [invariant B] exactly as they were.
```

**Examples:**
```
Recreate the scene from @Video1 but replace the perfume bottle with
the face cream from @Image1, keeping all original motion.

Recreate the scene from @Video1 but replace the background with the
environment from @Image1. Keep the subject's motion and camera
movement unchanged.
```

**Guidance:**
- Name the change first, then the invariants — this is the order the model weighs most reliably
- Keep it to **one change per pass.** Multiple simultaneous edits (swap the subject *and* the background *and* the lighting) produce drift; run them as sequential single-change passes instead
- Restating an invariant explicitly ("keep the camera movement unchanged") is more reliable than assuming it will be preserved by omission

---

## Video Extension (Continue a Clip Forward)

Provide a reference video and describe what happens next. The model continues with consistent characters, environment, and style rather than starting a fresh scene.

```
Continue directly from @Video1: [what happens next]. Maintain the
same character, environment, and style throughout.
```

This is the natural tool for extending a shot that's almost — but not quite — long enough, or for building a longer sequence out of several extension passes rather than one long single generation (which trades off quality and control as duration increases).

---

## Building a Longer Sequence Out of Short Clips

For anything beyond a single shot's worth of story, the recommended pattern (consistent with how creators are chaining Seedance 2.0 in practice) is:

1. Generate a short, tight first clip with a locked subject description
2. Feed that clip back in as `@Video1` for the next beat, explicitly asking to preserve camera movement and/or color grading
3. Repeat — each new prompt only needs to describe what's new; everything else rides on the reference
4. Use Video Extension instead of a fresh Reference-to-Video call when the next beat is a direct continuation rather than a new angle or setup

This keeps continuity errors from compounding the way they do when every clip is generated independently and reconciled after the fact.

---

## Style and Brand Consistency

For a recurring style across a project or brand series:

- Fix **one or two** style labels ("clean commercial product style," "gritty documentary") and never mix them within the same series
- Reuse the exact style wording in every prompt, the same way subject descriptions are reused
- Where a strong style reference image exists, feed it in as `@Image1` in Reference-to-Video and describe it as the style source explicitly: `"Match the color grading and lighting style of @Image1."`
