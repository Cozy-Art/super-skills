# fish-audio-v2 — build notes

Human-facing build notes. Not loaded as part of the skill.

**Built:** 2026-10-18 · **Skill version:** 1.0 · **Model:** Fish Audio S2.1-Pro + Drama 3 (Fish Audio)

---

## Research verification

- **Slug:** fish-audio-prompts (platform-general: covers s2.1-pro, s2.1-pro-free, drama-3, s2-pro, legacy s1, voice-design-1)
- **Model:** Fish Audio TTS — S2.1-Pro (`s2.1-pro`) as production default; Drama 3 (`drama-3`, released Oct 13, 2026) for directed performance

## Corrections to the research
- Research omits Drama 3 entirely → `drama-3` is a valid `model` header value (released Oct 13, 2026), adds scoped tags `<whisper> <emphasis> <soft> <fast> <slow> <stress> <forceful>`, experimental language tags (`<french>…</french>`), phoneme tags `<|phoneme_start|>…<|phoneme_end|>` → https://docs.fish.audio/features/text-to-speech/drama-3.md, https://docs.fish.audio/api-reference/endpoint/openapi-v1/text-to-speech
- Missing/unrecognized `model` header → silently falls back to `s2.1-pro` (no error); JS SDK defaults to `s1`, Python SDK to `s2-pro` → https://docs.fish.audio/features/text-to-speech
- `opus_bitrate` values are in **bps** (-1000, 24000, 32000, 48000, 64000), not kbps; schema default -1000 vs prose "32 kbps default" (flagged) → TTS API reference
- `latency: low` is in the main schema enum (research said "some schemas") → TTS API reference
- `repetition_penalty` has **no effect on S2.1-Pro**; `normalize_loudness` defaults true and has no effect on s1 → https://docs.fish.audio/developer-guide/models-pricing/migrate-from-s1.md
- Research missed fields `language`, `features` (`quality-guard`), `pronunciation_dictionary` (≤3, inline ≤5000 items, unresolvable refs dropped silently); `early_stop_threshold` range 0–1 → TTS API reference
- Inline `references` items require both `audio` and `text` (transcript); zero-shot multi-speaker uses a 2-D array → TTS API reference
- Official pause cues are `[break]` and `[long-break]`; official sound tags include `[sighing]`, `[clear throat]`, `[panting]` etc. (49 listed emotions) → https://docs.fish.audio/developer-guide/core-features/emotions
- Languages: S2.1-Pro is 83 (research "80+") → https://docs.fish.audio/developer-guide/models-pricing/models-overview
- Cloning guidance: ≥10 s, ideally 2–3 clips of 15–20 s, 30–60 s if robotic (research said 10–30 s); up to 20 voice files per model; `POST /model` requires `type: tts`, `title`, `train_mode: fast`, `voices` → https://docs.fish.audio/developer-guide/best-practices/voice-cloning.md, https://docs.fish.audio/api-reference/endpoint/model/create-model.md
- Research omits Voice Design: `POST /v1/voice-design`, header `model: voice-design-1`, `instruction` 1–2000 chars, `n` 1–4 (default 2), $0.01/request → https://docs.fish.audio/api-reference/endpoint/openapi-v1/voice-design.md
- Pricing: $15 / M UTF-8 bytes for s2.1-pro, s2-pro, s1; s2.1-pro-free $0; concurrency 5/15/50 by prepaid tier, 429 without Retry-After → https://docs.fish.audio/developer-guide/models-pricing/pricing-and-rate-limits.md
- Note: Fish's own real-time streaming doc still uses S1 `(emotion)` parentheses in example code — skill uses brackets for S2 family.

## Unverified / flagged in skill
- Drama 3 pricing (not on official pricing page; third-party sources conflict: $50/M chars list vs $10/M bytes list, both with launch discounts)
- Drama 3 max speakers per text (third-party "up to 16")
- How Voice Design candidates map to `voice_design_signatures` in Create Model (candidate schema shows no signature field)
- Voice Design `reference_text` max: API ref 150 chars vs feature page 300 — skill says stay ≤150
- Phoneme tags on S2.1-Pro (documented on Drama 3 page only)
- Text length caps: no official per-request max; 30,000-char web counter and Runware 3,000-char cap are platform rules
- Sampling/chunk/speed preset ranges are practical guidance, not official

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
