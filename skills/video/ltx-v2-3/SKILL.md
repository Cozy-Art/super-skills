---
name: ltx-2-3-prompts
description: Generate optimized prompts and API payloads for Lightricks' LTX-2.3 joint audio-video model (ltx-2-3-pro, ltx-2-3-fast). Use whenever a user mentions LTX-2.3, LTX 2.3, LTXV 2.3, ltx-2-3-pro/fast, Lightricks video, or the LTX API (api.ltx.io / api.ltx.video), or wants text-to-video, image-to-video, first/last-frame interpolation, audio-to-video, retake (replace a section) or extend on LTX — including via Replicate, fal, Runware, Leonardo, MachGen, ComfyUI or the open 22B weights. Also use when migrating removed LTX-2 model IDs (ltx-2-pro/fast) or V1 endpoints to V2, or when choosing between LTX-2.3 and LTX-2.5 for retake/extend work. Covers synchronized audio and dialogue prompting, camera_motion presets, the fixed resolution/fps/duration grid, and local CFG/STG/frame-count rules. Do not guess LTX-2.3 syntax from general knowledge, LTX-Video 0.9 or LTX-2 habits.
---

# LTX-2.3 — Prompt Generation Skill

LTX-2.3 is Lightricks' 22B DiT model that generates **video and synchronized audio in one pass** (ambience, effects, music, quoted dialogue). Hosted as `ltx-2-3-pro` (quality, all endpoints) and `ltx-2-3-fast` (iteration, T2V/I2V only), plus open weights for local pipelines.

**Status (Oct 2026):** LTX-2.5 is the newer family, but **retake and extend exist only on `ltx-2-3-pro`** — LTX-2.3 remains the model for surgical edits and continuations.

## The Three Rules That Override Everything

1. **One shot, told chronologically, in present tense.** A single flowing paragraph of ~4–8 sentences from opening frame to landing frame. Every sentence carries a verb. No keyword soup, no tag weights, no timestamps.
2. **Write the sound.** Audio is on by default (`generate_audio: true`). If you don't describe ambience, effects, music, dialogue — or explicitly "no music, no speech" — the model invents them. Dialogue goes in quotation marks with language/accent.
3. **Prose and settings must agree.** Resolution, fps, duration and `camera_motion` are request fields, never prompt text. If you set `camera_motion: "static"`, the prose must not describe an orbit.

## Prompt Order

| # | Layer | Example |
|---|---|---|
| 1 | Primary action | "A courier sprints across a wet rooftop…" |
| 2 | Character / object identity + movement detail | age range, hair, wardrobe, signature accessory; gestures, gait |
| 3 | Setting + atmosphere | foreground/background, weather, environmental motion |
| 4 | Shot + camera | shot size, angle, ONE movement relative to subject, landing composition |
| 5 | Lighting + look | key source, palette, texture, lens/grain |
| 6 | Change / event | what is revealed, breaks, appears by the end |
| 7 | Audio | ambience, synced effects, music, `"quoted dialogue"`, or explicit silence |

```
[PRIMARY ACTION]. [IDENTITY + MOVEMENT]. [SETTING + ATMOSPHERE].
[SHOT SIZE + CAMERA MOVE + WHERE IT LANDS]. [LIGHT + PALETTE + TEXTURE].
[WHAT CHANGES BY THE END]. [SOUND: ambience, effects, music, "dialogue"].
```

**Length:** API hard limit 5,000 characters. Practical sweet spot 60–180 words; match length to complexity. For **image-to-video**, spend the words on motion, camera and sound — the image already supplies appearance.

## Decide the Operation First

| User wants | Endpoint (V2 async) | Model | Key inputs |
|---|---|---|---|
| New clip from text | `/v2/text-to-video` | Fast (drafts) / Pro (final) | prompt |
| Animate a still / lock identity | `/v2/image-to-video` | Fast or Pro | `image_uri` + motion prompt |
| Hit an exact end composition | `/v2/image-to-video` | Fast or Pro | `image_uri` + `last_frame_uri` |
| Picture cut to a song / VO | `/v2/audio-to-video` | **Pro only** | `audio_uri` (+ `image_uri` and/or prompt) |
| Fix 2+ s of a clip, keep the rest | `/v2/retake` | **Pro only** | `video_uri`, `start_time`, `duration`, `mode` |
| Continue a clip forward/backward | `/v2/extend` | **Pro only** | `video_uri`, `duration`, `mode: end/start` |
| Clip longer than 10 s in one go | `/v2/text-` or `image-to-video` | **Fast only**, 720p/1080p @ 24/25 fps | duration 12–20 |
| Local control, LoRAs, IC-LoRA | open weights | dev / distilled | see parameters.md |

## Quick Syntax Reference

- **Dialogue:** `she says in a quiet Scottish accent, "Not tonight."` Short lines; leave time for action.
- **Silence:** "no music, no voices" — say it, or the model may score the shot.
- **Multi-beat single take:** "The shot begins… As she reaches the door… The camera then… By the final moment…"
- **Camera presets (`camera_motion`):** `dolly_in` `dolly_out` `dolly_left` `dolly_right` `jib_up` `jib_down` `static` `focus_shift`. Discrete — no strength value. Pans, orbits, handheld, tracking → describe in prose and omit the field.
- **Emotion:** physical cues ("her jaw tightens, eyes drop"), never labels alone.
- **Grid:** 16:9 or 9:16 only · 720p/1080p/1440p/4K · 24/25/48/50 fps · 6/8/10 s (Fast up to 20 s). Full matrix → [parameters.md](parameters.md).

## Output Format (always two parts)

1. **Prompt** — in a code block, prose only. No resolution, fps, duration, model or preset inside the text.
2. **Suggested settings** — one line, e.g. `model: ltx-2-3-pro · resolution: 1920x1080 · fps: 24 · duration: 8 · generate_audio: true · camera_motion: dolly_in · image_uri: [approved first frame]`

If the user is building an API call, also give the JSON body with only valid fields for that endpoint. On a wrapper (Replicate, fal, Runware, Leonardo, MachGen), translate to that platform's field names — they differ (see parameters.md).

## Things That Will Break the Request

- **Removed model IDs:** `ltx-2-pro`, `ltx-2-fast` (removed Aug 2026) → error.
- **V1 endpoints** (`/v1/text-to-video` etc.) stop working after **26 Oct 2026 23:59 UTC** → use `/v2/...` (same params and pricing, async job + poll).
- **Off-grid values:** 1:1 or 4:5 sizes, 30 fps, 5 or 7 s durations, 4K at 20 s, Fast at 48 fps beyond 10 s.
- **Fast on Pro-only endpoints:** audio-to-video, retake, extend with `ltx-2-3-fast`.
- **`last_frame_uri` with `duration: null`** (null is an LTX-2.5 feature anyway).
- **Fields not in the native schema:** `negative_prompt`, `seed`, `aspect_ratio`, `cfg_scale`, `steps`, `enhance_prompt`, `motion_intensity`. (Some wrappers or local pipelines have them — native API does not.)
- **Retake/extend inputs** under 73 frames (~3 s at 24 fps); retake output is 1080p only.

## Iteration Workflow

1. Draft on `ltx-2-3-fast` at 720p or 1080p, 24 fps, 6 s — validate action, blocking, camera, sound.
2. Change one thing per pass: action → camera → light → audio.
3. Save the approved draft's prompt and a clean frame from it (download the result — store the file, not the URL).
4. Final on `ltx-2-3-pro` at 1440p/4K with the same prompt; use the saved frame as `image_uri` if composition must survive (a resolution change is a new roll).
5. Small defect → `retake` that section. Needs more time → `extend`. New angle → new I2V shot from a continuity frame.

## Reference Files

- **[parameters.md](parameters.md)** — every endpoint and field, full resolution/fps/duration matrix, pricing, input formats/limits, wrapper field maps, open-weight controls, LTX-2 and V1 migration.
- **[best-practices.md](best-practices.md)** — detail budget, chronology, camera language and presets, audio/dialogue craft, shot-size rules, I2V prompting, common-mistakes table.
- **[continuity-and-references.md](continuity-and-references.md)** — character anchors, first/last frames, shot-to-shot continuity frames, extend/retake strategy, audio continuity, style lock, LoRAs.
- **[examples.md](examples.md)** — 10 annotated prompts: close-up dialogue, landscape, action, reveal, product, noir, first/last frame, audio-to-video, retake, extend.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
