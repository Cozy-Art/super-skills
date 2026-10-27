# ltx-v2-3 — build notes

Human-facing build notes. Not loaded as part of the skill.

**Built:** 2026-10-18 · **Skill version:** 1.0 · **Model:** LTX-2.3 Fast & Pro (Lightricks)

---

## Research verification


Corrections:
- Resolution tiers 1080p/1440p/4K only → a 720p tier (1280x720 / 720x1280) was added 2 Aug 2026 for T2V/I2V on both Pro and Fast — https://docs.ltx.io/models/ltx-2-3, https://docs.ltx.io/api-changelog
- Fast 12–20 s "at 1080p only" → 12–20 s at 720p and 1080p, 24/25 fps only; 48/50 fps capped at 10 s — https://docs.ltx.io/models/ltx-2-3
- Endpoints: sync V1 was presented as current → V1 video endpoints are deprecated and stop working after 26 Oct 2026 23:59 UTC; use async /v2/* (202 → poll GET /v2/<ep>/{id} → result.video_url), same params/pricing — https://docs.ltx.io/api-changelog, https://docs.ltx.io/api-documentation/api-reference/async-video-generation/submit-text-to-video
- Base URL api.ltx.video → api.ltx.io (old host still works) — https://docs.ltx.io/api-changelog (Jul 21)
- LTX-2.3 positioned as the current model → LTX-2.5 (ltx-2-5-pro/fast) launched 11 Aug 2026; LTX-2.3 is now "previous generation" but remains the ONLY family with retake/extend — https://docs.ltx.io/models
- Extend: added `mode` (end/start, default end), input ≥ 73 frames, 16:9/9:16 only, ≤ 100 MB; `duration` 2–20 s, `context` 1–20 s, 505-frame cap confirmed — https://docs.ltx.io/api-documentation/api-reference/async-video-generation/submit-extend, https://docs.ltx.io/input-formats
- Retake: added resolution limited to 1920x1080/1080x1920, input ≥ 73 frames, mode enum replace_audio / replace_video / replace_audio_and_video — https://docs.ltx.io/api-documentation/api-reference/async-video-generation/submit-retake
- Audio-to-video was mentioned but not specified → added full schema: audio_uri required, image_uri/prompt one-of, fps, last_frame_uri, camera_motion (added 19 Aug 2026); max audio 20 s @720p/1080p, 10 s @1440p/4K on ltx-2-3-pro — https://docs.ltx.io/api-documentation/api-reference/async-video-generation/submit-audio-to-video
- Input size limits: video/audio HTTPS 32 MB, data URI 15 MB, cloud 200 MB (research said cloud 100 MB for all) — https://docs.ltx.io/input-formats
- Prompt enhancement "some hosted surfaces provide it" → official guide: enhancer applies only to local open-source paths, not direct API requests — https://docs.ltx.io/api-documentation/implementation-guides/prompting-guide
- Prompt length "under ~200 words" → official API guide gives no word cap ("match length to complexity"), 4–8 sentences; 5,000-char field limit confirmed — same source
- stg_blocks example "[^29]" (citation artifact) → `[28]` — https://docs.ltx.io/open-source-model/integration-tools/pytorch-api
- Added pricing (per second): Fast $0.03/0.06/0.12/0.24, Pro $0.04/0.08/0.16/0.32 (720p/1080p/1440p/4K); A2V Pro $0.06–0.34; retake/extend $0.10 @1080p — https://docs.ltx.io/pricing
- Replicate wrapper: fps default 25 (native default 24), resolution enums 1080p/2k/4k, `camera_motion` default `none`, task-based field names — https://replicate.com/lightricks/ltx-2.3-pro/llms.txt
- Confirmed: camera_motion 8 values (dolly_in/out/left/right, jib_up/down, static, focus_shift) — https://docs.ltx.io/api-changelog/2026/1/1; LTX-2 IDs removed 16 Aug 2026; width/height ÷32, frames 8n+1, distilled 8 steps CFG 1 — https://huggingface.co/Lightricks/LTX-2.3

Unverified (marked in skill or kept as plausible):
- Leonardo, Runware, MachGen field names/grids (marked "unverified — confirm on your platform").
- Official ComfyUI two-stage template specifics (960×544 → x2, 8+3 steps) and default local negative prompt text — from research, not re-fetched.
- Result URL expiry on V2 (not documented; skill says download immediately).
- LTX-2 → 2.3 LoRA incompatibility (stated on ltx.io model page per research + community guide; not re-fetched).

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
