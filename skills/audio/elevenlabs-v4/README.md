# elevenlabs-v4 — build notes

Human-facing build notes. Not loaded as part of the skill.

**Built:** 2026-10-18 · **Skill version:** 1.0 · **Model:** Eleven v4 / v4 Turbo (ElevenLabs)

---

## Research verification


Corrections / additions vs research:
- Dialogue `settings` uses `similarity` (default 0.75), not `similarity_boost` as in research example 6; `similarity_boost` is the TTS voice_settings name — elevenlabs.io/docs/api-reference/text-to-dialogue/convert.md + changelog 2026-09-28
- New `audio_effects` object on TTS + Dialogue (filter_preset_id, distance 0–1, environment_id, send_level 0–1 default 1, background_noise_id, pan −1..1); stereo effects rejected (400) with pcm/ulaw/alaw; catalog GET /v1/audio-effects/catalog; no cost change — absent from research — changelog 2026-10-12, text-to-dialogue/convert.md
- TTD WebSocket API reference still says model_id default `eleven_v3_conversational` / "must be a v3 model"; WebSocket guide says prefix `eleven_v3`/`eleven_v4`, v4 ≤10 voices, Turbo 1 voice — kept guide, told users to set model_id explicitly — elevenlabs.io/docs/api-reference/text-to-dialogue/ttd-websocket, .../websockets/tts-vs-ttd-websockets
- WebSocket details added: 20 s keep_alive timeout, ~40 chars / 8 words buffer, voice_settings & dictionaries only in first message — .../websockets/realtime-tdd
- Languages: "90+" on models/changelog, but v4 page FAQ lists 87 by name — noted both — elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4
- `use_pvc_as_ivc` no longer deprecated; added to Text to Dialogue — changelog 2026-09-28
- `enable_logging: false` disables request stitching (zero retention, enterprise only) — not in research — create speech API ref
- Pricing added: API $0.08/1K chars (v4), $0.04/1K (Turbo); app uses same credits as other TTS models — elevenlabs.io/pricing/api
- Dialogue capability page says "no limit to number of speakers" but API caps 10 unique voice_ids per request — used the API limit — text-to-dialogue/convert
- Agents default TTS model changed to eleven_v4_turbo (2026-10-05); `preserve_voice_settings` for transfers — changelog
- Cloning source specs added (RMS −23 to −18 dB, true peak < −3 dB, IVC 1–2 min, PVC 30 min–2 h+); Voice Design voices may be less performative on v4 — troubleshooting + v4 capability page
- Confirmed (no change): 10,000-char v4 limit, 2,000-char dialogue guidance, 100-char previous/future_text, 3 request IDs (ordering), 3 dictionaries, seed 0–4,294,967,295 best-effort, mp3_44100_128 default + 28-value enum + tier gates, model_id defaults (multilingual_v2 / v3), no Style/Speed/SSML on v4, slash IPA syntax, ordinary TTS WebSocket excludes v3/v4, ~100 ms Turbo latency, launch 2026-09-28.

Unverified / caveats:
- Numeric 0–1 range for stability/similarity (schema shows defaults only) — marked in parameters.md
- Changelog 2026-10-12 says "The seed field is deprecated and has no effect" in the context of agent TTS configuration; Create speech / dialogue refs still document seed as best-effort — kept seed as best-effort
- ~150 ms time-to-first-speech for Turbo (from press coverage) omitted; only the documented ~100 ms median inference kept
- Turbo per-request character ceiling not published
- Stability preset bands are working practice, not official presets

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
