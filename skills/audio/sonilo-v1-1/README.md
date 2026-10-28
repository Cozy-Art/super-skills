# sonilo-v1-1 — build notes

Human-facing build notes. Not loaded as part of the skill.

**Built:** 2026-10-18 · **Skill version:** 1.0 · **Model:** Sonilo v1.1 + Sound Effects 1.0 (Sonilo)

---

## Research verification

Medium: instrumental music (text/video-to-music) + SFX (text/video-to-sfx) + combined video-to-sound; continuity adapted to sonic identity blocks, locked-cut timelines, speech preservation, archive (no seed / no audio reference).

Corrections:
- Text-to-music prompt max 1,000 chars → native API allows 1–2,000; 1,000 is a ComfyUI node limit (kept ≤1,000 as portable advice) — sonilo.com/openapi.json; github.com/Comfy-Org/ComfyUI nodes_sonilo.py
- Audio ducking has `ducking_ratio`, `attack_ms`, `release_ms` → no tuning fields exist; only voice_file/voice_url + music_file/music_url — platform.sonilo.com/openapi.json
- Text-to-SFX duration 0.5–180 per MCP → MCP README says 1–180; API is integer 1–180 — github.com/sonilo-ai/sonilo-mcp; sonilo.com/openapi.json
- `preserve_speech`/`keep_original_sound` scope: `keep_original_sound` exists only on video-to-video-music / video-to-video-sound; `isolate_vocals` is a legacy alias ORed with preserve_speech — platform.sonilo.com/openapi.json
- `prompt_influence` is only on video-to-music and video-to-video-music (research implied broader) — platform.sonilo.com/openapi.json
- video-to-sound `ducking` is ignored when `preserve_speech` is used; output_format default `wav` — platform.sonilo.com/openapi.json
- Added endpoints missing from research: video-to-video-sfx, video-to-video-sound, video-analysis, account/services, account/usage — platform.sonilo.com/openapi.json
- Added `stems` boolean (async) on text/video-to-music — platform.sonilo.com/openapi.json (conflicts with sonilo.com/docs; marked unverified)
- Added pricing: credits/output-second V2M 18, V2SFX 18, T2M 5, T2SFX 4; 15 s / 200-credit minimum; plans Free/Pro $11.99/Premium $23.99 — sonilo.com/pricing
- fal.ai wrapper uses `num_samples`, `start_offset`, `duration` (not variants_num/segments) — fal.ai/models/sonilo/v1.1/video-to-music/api
- Vocals/lyrics: none documented (v1.1 announcement mentions only speech preservation) — sonilo.com/news/sonilo-v1-1

Unverified:
- `stems` field availability (platform OpenAPI lists it; docs say stems not offered)
- Task terminal states `completed`/`canceled` (agent guide only; schema lists processing/succeeded/failed)
- `/v1/vocal-isolation` unavailability (from research citing agent reference; not contradicted)
- Whether Sonilo can produce sung vocals if asked (undocumented; skill treats it as instrumental-only)
- 600 s platform-level video length (v1.1 announcement) vs 360/480 s endpoint caps — skill trusts endpoint caps

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
