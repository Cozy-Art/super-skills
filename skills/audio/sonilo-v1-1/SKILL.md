---
name: sonilo-v1-1-prompts
description: Generate optimized prompts, segment timelines and API payloads for Sonilo (sonilo.com) — the footage-first audio model (music v1.1 + Sound Effects 1.0) that scores video. Use whenever a user mentions Sonilo, Sonilo v1.1, Sonilo v1.0, sonilo-mcp, or Sonilo on fal.ai / ComfyUI / Scenario, or wants video-to-music, text-to-music, video-to-SFX / Foley, text-to-SFX, combined music+SFX scoring (video-to-sound), scored-video MP4 delivery, speech-preserving soundtracks, dialogue ducking, or per-segment score direction. Also use when writing segments JSON, choosing prompt_influence, or deciding between Sonilo endpoints. Sonilo is instrumental-score and SFX focused — no documented lyrics or sung vocals. Do not guess Sonilo field names or limits from general knowledge or other music models (Suno, Udio, ElevenLabs) — use the reference files.
---

# Sonilo v1.1 — Prompt Generation Skill

Sonilo is an audio platform whose core model reads an edited video's pacing, motion, cuts and emotion and generates a fitted instrumental score (v1.1, June 2026) or synchronized Foley/ambience/action SFX (Sound Effects 1.0, July 2026). Text-only music and SFX endpoints exist too. All generation is natural-language prompts over `multipart/form-data` at `https://api.sonilo.com/v1/...`.

**Scope:** instrumental music and sound effects only. No documented lyrics, sung vocals, voice cloning, TTS, seed, negative prompt or audio-reference input. Picture controls (aspect ratio, camera, lens) do not exist — the source video supplies them.

## The Three Rules That Override Everything

1. **Footage leads; the prompt steers.** For video endpoints, write a short direction (10–35 words) covering only what pixels can't say: brand tone, instrumentation, emotional reading, exclusions. Don't re-narrate the edit. Text-only endpoints get the full brief.
2. **Pick the endpoint before writing a word.** Music and SFX are separate models with separate prompts. Video-to-music won't make Foley; text-to-SFX won't sync to picture. Combined jobs use `video-to-sound` with `music_prompt` + `sfx_prompt`.
3. **Continuity lives in your text and your archive, not the model.** No seed (ComfyUI's seed is ignored), no "continue this track", no audio reference. Consistency = a verbatim sonic identity block + a locked cut + saved selected outputs.

## Prompt Order

**Music** (text-to-music: all layers; video-to-music: keep 1, 2, 4, 7, 8):

| # | Layer | Example |
|---|---|---|
| 1 | Purpose / scene | "Instrumental underscore for a premium product reveal" |
| 2 | Mood (precise) | "confident and restrained, not triumphant" |
| 3 | Genre / sonic language | "minimal electronic", "hybrid orchestral" |
| 4 | 2–4 defining instruments / timbres | "warm analog bass, glassy synth plucks" |
| 5 | Tempo / energy | "mid-tempo, ~96 BPM pulse" |
| 6 | Structural arc | "build gradually, open up for the final reveal, clean cadence" |
| 7 | Mix / vocal constraints | "instrumental, leave space for narration" |
| 8 | Exclusions | "no vocals, no aggressive drops" |

**SFX:** `source/action → material → environment → distance/perspective → intensity → envelope/decay → realism vs. stylization → exclusions`

**Length targets (practical):** text-to-music 25–80 words (portable max 1,000 chars) · video-to-music 10–35 words · text-to-SFX 10–50 words · video-to-SFX: none or one-line policy, then segments.

## Decide the Endpoint First

| User wants | Endpoint | Prompt field(s) |
|---|---|---|
| Music from a description, no picture | `POST /v1/text-to-music` | `prompt` (required) + `duration` |
| Score fitted to a cut (audio file back) | `POST /v1/video-to-music` | `prompt` optional, `prompt_influence` |
| Scored MP4 back, picture untouched | `POST /v1/video-to-video-music` | same; `keep_original_sound` |
| One isolated effect / library sound | `POST /v1/text-to-sfx` | `prompt` + `duration` (1–180 s) |
| Foley + ambience synced to picture | `POST /v1/video-to-sfx` (or `video-to-video-sfx`) | `prompt` optional + `segments` |
| Music **and** SFX in one synced mix | `POST /v1/video-to-sound` (or `video-to-video-sound`) | `music_prompt` + `sfx_prompt` |
| Narration over existing music | `POST /v1/audio-ducking` | no prompt — voice + music inputs |
| Not sure what the cut needs | `POST /v1/video-analysis` | returns a music/sound brief |

## Special Syntax (Quick Reference)

- **No inline syntax.** No weights, brackets, `[Verse]` tags, `--params` or negative field. Exclusions go in plain words ("no vocals").
- **Segments** = a JSON array **serialized as a string** in the `segments` form field. Numeric seconds, `start >= 0`, `end > start`, optional `prompt`:
  `[{"start":0,"end":8,"prompt":"intro: sparse piano, low pulse"},{"start":8,"end":20,"prompt":"build: add percussion"}]`
- **Section labels** (intro / verse / chorus / bridge / drop / outro) go **inside** the segment prompt — there is no `label` field.
- **Video input:** exactly one of `video` (upload) or `video_url`. Must contain a real video stream — audio-only or cover-art files return 422.
- **`audio_format`** (SFX) vs **`output_format`** (music/sound) — different names, snake_case only.

Full field tables and limits → [parameters.md](parameters.md).

## Output Format (always two parts)

1. **Prompt** — in a code block, prompt text only. For `video-to-sound`, give two labeled code blocks (`music_prompt`, `sfx_prompt`). If segments are used, give the segments JSON as its own code block.
2. **Suggested settings** — one line, e.g. `endpoint: video-to-music · mode: async · output_format: wav · prompt_influence: 0.5 · variants_num: 2 · preserve_speech: true`

Never put duration, format, BPM-as-a-setting or influence values inside prompt text (BPM as musical description is fine). If the user is building a call, also give a `curl -F` example with only valid fields.

## Things That Will Break the Request

- Both `video` and `video_url`, or neither, on a video endpoint.
- `wav`/`mp3`, `variants_num > 1`, `preserve_speech`, `ducking` or `stems` with `mode=stream` (default) — set `mode=async`.
- `segments` sent as a nested form array instead of a JSON string; non-numeric times; `end <= start`.
- Inventing fields: `seed`, `negative_prompt`, `lyrics`, `bpm`, `key`, `label`, `ducking_ratio`, `attack_ms`, `release_ms`, `audioFormat`, `aspect_ratio`, `/v1/vocal-isolation`.
- `prompt_influence` on endpoints other than `video-to-music` / `video-to-video-music`.
- Exceeding limits: text-to-music 5–360 s · text-to-SFX 1–180 s · video-to-music 360 s · SFX/sound video 480 s · 300 MB default upload.
- Wrapper platforms rename fields (fal.ai uses `num_samples`, `start_offset`) — don't mix vocabularies.

## Iteration Workflow

1. **Lock the cut.** Any retime after generation breaks the conditioning — regenerate, don't stretch.
2. **First pass footage-led:** video-to-music with no prompt or one line, `prompt_influence` 0.5, `variants_num` 2–3, async M4A.
3. **Diagnose one variable:** poor sync → lower influence / shorten prompt; wrong genre or tone → add a sonic identity phrase, raise influence to 0.65–0.8.
4. **Add 2–5 broad segments** only at structural turns (hook, turn, reveal, CTA, end). Keep the instrument family constant across neighbours; change energy or density first.
5. **Dialogue:** `preserve_speech=true` + `ducking=true` (async), or score first then `audio-ducking`.
6. **Final:** async WAV, single chosen variant. Review against picture (open, first cut, turn, reveal, last frame); trim frame-critical hits in the editor.
7. **Archive** prompt, segments JSON, params, source-cut hash, `task_id`, date, chosen file, license tier. Download on success — don't rely on re-generating.

## Reference Files

- **[parameters.md](parameters.md)** — every endpoint and field, valid values/defaults, async rules, limits, output formats, credit pricing, wrapper differences, v1.0 → v1.1 notes.
- **[best-practices.md](best-practices.md)** — detail level, music vs. SFX vocabulary, camera/edit → auditory interpretation, segment design, prompt_influence tuning, common-mistakes table.
- **[continuity-and-references.md](continuity-and-references.md)** — sonic identity blocks, series/campaign consistency, multi-shot timelines, speech/stem handling, archive protocol, handoffs between endpoints.
- **[examples.md](examples.md)** — annotated prompts: character theme, landscape, chase with segments, camera-move interpretation, isolated SFX, Foley pass, combined product film, social short, brand series, UI sounds.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
