# grok-imagine-video-v1-5-lite — build notes

Human-facing build notes. Not loaded as part of the skill.

**Built:** 2026-10-19 · **Skill version:** 1.0 · **Model:** Grok Imagine Video 1.5 Lite (xAI)

---

## Research verification

Base structure from the `video/grok-imagine-video-v1-5` skill (upsampler framing, positive-description
stance, no-seed discipline), reduced to Lite's two modes and re-verified rather than inherited.

Corrections:
- Prompt template and example prompts put duration and format inside the prompt text ("8-second…", "9:16 vertical…") → removed everywhere; duration, aspect ratio and resolution live only on the settings line (skill convention; xAI exposes them as request fields) — https://docs.x.ai/developers/model-capabilities/video/generation
- Quoted dialogue attributed to "community tutorials" → xAI's own Video Overview shows the convention first-party: `Sam: "I took the job in Berlin…"` and `She says: "Welcome to my dream living room."` (shown on full 1.5; Lite is documented with lip-synced speech) — https://docs.x.ai/developers/model-capabilities/video/overview
- `generate_audio` listed as a native REST field with default `true` → audio-on-by-default and `generate_audio=False` are documented in the generation guide (SDK usage), but the field does not appear in the REST request schema reviewed; skill says "audio off in settings" and flags the REST name as unverified — https://docs.x.ai/developers/model-capabilities/video/generation, https://docs.x.ai/developers/rest-api-reference/inference/videos
- `aspect_ratio` "default 16:9" → stated in the generation guide; the REST schema lists the nine values with no default. Kept 16:9 as the guide default — same sources
- Prompt structure presented as a free ordering → xAI documents that Lite text-to-video *"uses text-to-image then image-to-video under the hood: the model generates a first frame from your prompt"*; prompt order now opens with the first-frame composition — https://docs.x.ai/developers/model-capabilities/video/generation
- Upsampler not mentioned → the shared REST usage schema documents a *"prompt-rewriting (upsampler) LLM"*; added, with its implication for prompt specificity — https://docs.x.ai/developers/rest-api-reference/inference/videos
- Timecodes recommended as technique → community-only; xAI documents none for Lite. Skill prefers ordered prose ("first… then… finally") and marks timecodes untested — https://docs.x.ai/developers/model-capabilities/video/generation (no timecode guidance)
- Full-1.5 voice references described as preset voices only (and the base 1.5 skill says `voice_id` only) → the REST schema now also accepts an uploaded audio `url` (≤ 15 s) in `reference_audios` — https://docs.x.ai/developers/rest-api-reference/inference/videos
- Video Overview price cells render as "$0.027 / $0.031" in some fetches → run-together cell text ("480p $0.02720p $0.031080p $0.14"); the pricing page confirms $0.02 / $0.03 / $0.14 per second + $0.01 per input image — https://docs.x.ai/developers/pricing
- Confirmed: model ID, T2V + single-image I2V only, 1–15 s default 8, 480p default, 1080p *"by upscaling 720p"*, nine aspect ratios incl. 21:9 and 5:2, I2V ignores `aspect_ratio`, no reference images / voice references / first-last frame / keyframes / edit / extend on Lite, full 1.5 up to 14 references and 4 keyframes, classic Grok Video edit ≤ 8.7 s and extend +2–10 s, 10 rps, regions us-east-1/us-west-2, full 1.5 pricing $0.08/$0.14/$0.25 — https://docs.x.ai/developers/model-capabilities/video/overview, https://docs.x.ai/developers/models/grok-imagine-video-1.5-lite, https://docs.x.ai/developers/pricing
- Confirmed wrapper: ComfyUI GrokVideoNode default model Lite, duration default 6, seven ratios + `auto` (no 21:9 / 5:2), seed is a re-run trigger only ("actual results are nondeterministic regardless of seed") — https://docs.comfy.org/built-in-nodes/GrokVideoNode

Drift in the base `grok-imagine-video-v1-5` skill found while verifying (not changed here; that skill is a separate folder):
- It states xAI documents no way to script speech → xAI's overview now shows quoted dialogue lines and says 1.5 *"generates lip-synced speech"*.
- It states no numeric reference cap → overview: up to 14 reference images on 1.5.
- It states $0.08/s at every resolution → $0.08 / $0.14 / $0.25 by resolution.
- It describes edit/extend as 1.5 modes → overview lists edit/extend on classic `grok-imagine-video` only (the base skill does note edit runs on the non-1.5 model).
- It lacks `last_frame` and `keyframes`, which full 1.5 now documents.

Unverified (marked in skill or kept as plausible):
- REST field name for audio on/off (`generate_audio` per SDK usage; not in the reviewed REST schema).
- Wrapper IDs for Vercel AI Gateway (`spacexai/…`), OpenRouter (`x-ai/…`) and Runware (`xai:grok-imagine@video-1.5-lite`, 6 s default, 64,000-char prompt cap) — from research, not re-fetched.
- Whether in-prompt negation and audio/text exclusions ("no subtitles") work — community practice only.
- Whether broad timecodes are honoured on Lite.
- Exact launch date (xAI overview "Last updated: October 8, 2026"; no xAI announcement found).
- Polling status values and output URL lifetime (not re-fetched; skill says download promptly).
- Whether the upsampler can be bypassed.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
