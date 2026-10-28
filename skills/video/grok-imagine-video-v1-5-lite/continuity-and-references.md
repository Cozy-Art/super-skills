# Grok Imagine Video 1.5 Lite — Continuity and References

Lite has **no reference-image input, no voice reference, no pinned last frame, no keyframes and no seed.**
Its only conditioning input is one starting image. Continuity therefore comes from production discipline,
and knowing when to hand a shot to a model that has the mechanism.

---

## 1. What Lite gives you

| Mechanism | On Lite? | Where it lives instead |
|---|---|---|
| One starting image (frame 1) | ✅ `image` | — |
| Reference images for identity/product/style | ❌ | Full 1.5 (up to 14) · classic Grok Video (up to 7) |
| Voice references (preset or uploaded) | ❌ | Full 1.5 (up to 3) |
| First + last frame interpolation | ❌ | Full 1.5 |
| Mid-clip keyframes | ❌ | Full 1.5 (up to 4) |
| Extend a clip | ❌ | Classic Grok Video (+2–10 s) |
| Edit a clip | ❌ | Classic Grok Video (source ≤ 8.7 s) |
| Seed | ❌ | Nowhere natively — Grok Video is nondeterministic |

There is **no in-prompt token** on Lite. `<IMAGE_1>`, `<AUDIO_0>` and `@Image1` are read as plain text.

## 2. Canonical stills → image-to-video

The strongest continuity tool on Lite. For each recurring character, product or set:

1. Make or approve **one canonical still per shot** (same character design, wardrobe, light direction, grade).
2. Animate it with **image-to-video**; the still is frame 1, so identity starts locked.
3. Keep the **same crop and aspect ratio** across stills — image-to-video inherits the source ratio.
4. Prompt **only the change** and state what holds ("her face, braid and green scarf unchanged").

Drift resumes as the clip runs and as the camera reveals unseen areas — keep moves modest on identity-critical
shots, and keep clips short.

## 3. Identity anchors in prose (text-to-video)

When there is no still, the description is the only link between shots:

- Write **one identity anchor** per character — age range, build, hair, wardrobe, one signature detail — and
  reuse it **verbatim** in every prompt. "The woman in the oxblood coat" in shot 1 is the same phrase in shot 6.
- Same for products: geometry, material, colour, label wording.
- Keep **camera vocabulary and lens feel** consistent across a sequence ("50 mm portrait perspective").
- Keep **light direction and palette** fixed ("cool window light from camera-left, warm tungsten rim").

Expect variation — prose is a description, not a lock. For a hero character who must match across a sequence,
route to full 1.5 reference-to-video.

## 4. Last-frame handoff

To continue action across clips on Lite:

1. Download the accepted clip; extract its **last frame** yourself.
2. Use that frame as the next clip's `image`.
3. Prompt the next beat only, continuing screen direction, light and sound bed.

This gives a pixel-continuous join without extension — but each handoff compounds softness, and audio does
not carry over (describe the same bed again). For a true continuation, classic Grok Video's extend
(+2–10 s from the last frame) is the documented tool; for an exact end composition, full 1.5's `last_frame`.

## 5. Audio and voice continuity

- **Ambient bed:** describe the same bed in the same words across a scene ("soft refrigerator hum, rain on
  glass") so cuts don't jump.
- **Voices:** Lite chooses timbre from your description. Reuse the same voice description for a character
  ("a low, unhurried baritone") — consistency is likely but not guaranteed.
- **When a voice must match exactly** across a production, route those shots to full 1.5 with a preset
  `voice_id` or an uploaded voice clip, or generate the dialogue with a dedicated voice model and lay it in.

## 6. Session discipline (no seed)

Record, per accepted take: prompt, source image, model ID, duration, resolution, aspect ratio, audio setting,
date, and the downloaded file (output URLs are temporary). Re-running the same prompt gives a new take; the
record is how you recreate the conditions, not the result. A wrapper's "seed" control (e.g. ComfyUI) only
forces a re-run.

## 7. When to leave Lite

Move the shot to **full Grok Imagine Video 1.5** when:

- identity, wardrobe, product or location must be bound from reference images,
- a specific preset or uploaded voice is required,
- the clip must land on an exact end frame, or hit frames at set moments,
- native 1080p detail matters.

Move it to **classic `grok-imagine-video`** when an existing clip needs editing or extending.

Stay on Lite for everything else — it is the cheapest way to iterate a simple shot with sound and speech.
