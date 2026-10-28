# drama-v3 — build notes

Human-facing build notes. Not loaded as part of the skill.

**Built:** 2026-10-19 · **Skill version:** 1.0 · **Model:** Fish Audio Drama 3 (Fish Audio)

---

## Research verification

Dedicated Drama 3 skill (frontmatter name `drama-3-prompts`). The general Fish Audio skill (`fish-audio-v2`, name `fish-audio-prompts`) still covers S2.1-Pro, Voice Design and S1 migration; hosted-API facts here (model header and silent fallback, MessagePack references, field ranges, pricing-page status, concurrency) are kept consistent with it.

### Corrections and additions (claim → verified fact → source)

- Revision/infilling presented as generally usable "at the model level" with `speaker` on references → the hosted `/v1/tts` schema has **no** history, edit, infill, `seed`, `top_k`, `single_chunk` or reference-`speaker` field; ReferenceAudio is `audio` + `text` only, multi-speaker zero-shot is a 2-D `references` array → https://docs.fish.audio/api-reference/endpoint/openapi-v1/text-to-speech
- Revision mechanism → SGLang-Omni path: "editing as continuation" with `previous_takes` (model card example: `by noon` → `by five` with earlier takes in context); vLLM-Omni: `previous_takes` and long-text chunking "not exposed through the speech API yet" → https://huggingface.co/fishaudio/drama-3, https://recipes.vllm.ai/fishaudio/drama-3
- Revision notes → technical report: earlier takes stay in context as audio, the note arrives relative to a prior take (e.g. "[softer and warmer versus previous]") → https://arxiv.org/html/2610.18010
- Long-form limits → research omitted the hard total cap: 10,240 frames minus prompt length; 1,024 frames per pass default; `0` → 600 / 2,048 → https://speech.fish.audio/inference/
- Chunker constants confirmed and extended: `DRAMA3_CHUNK_BYTES` 300 (threshold), `DRAMA3_CHUNK_MAX_SPEAKERS` 3, `DRAMA3_HISTORY_RECENT_TURNS` 1, untagged text = speaker 0, raw-character fallback split → https://github.com/fishaudio/fish-speech/blob/main/fish_speech/models/text2semantic/fish_omni/chunking.py
- Reference-to-speaker mapping on Fish Speech → client `--reference_speaker` (0–15) "written as a `<|speaker:N|>` prefix"; `--single_chunk` spelled with underscore; temperature/top-p resolve to 0.7 when unset, top-k 30 → https://speech.fish.audio/inference/
- ComfyUI → node exposes up to **5** voice slots; one voice is passed as `reference_id` with no labels; two or more need `@Voice1…`, every connected voice must appear or the node errors; requires ComfyUI ≥ 0.39.3 → https://docs.comfy.org/tutorials/partner-nodes/fishaudio/drama-3
- Direction persistence ("until replaced") → confirmed: directions "apply from that point until the next direction" → same ComfyUI page
- Language tags → Fish shows `<french> <spanish> <german> <japanese> <chinese> <korean> <italian>`, "not guaranteed for every language or voice" → https://docs.fish.audio/features/text-to-speech/drama-3.md
- Speakers → model card: `<|speaker:0|>` … `<|speaker:15|>`, up to 16 characters; hosted Drama 3 page states no maximum (three-speaker example) → model card + Drama 3 page
- Hardware → ≥48 GB VRAM (FP8), Linux/WSL, NVIDIA only, no `--compile`, pre-SM80 fp16 fallback untested, last listed device hosts the audio decoder/codec, plain `cuda` uses up to four GPUs, S2-Pro codec needed if `codec.pth` absent → https://speech.fish.audio/install/, https://speech.fish.audio/inference/
- Licence → README: Fish Audio Community License for the codebase and associated weights; model-card header metadata says `fish-audio-research-license` — conflict flagged → https://github.com/fishaudio/fish-speech, model card
- Languages → model-card metadata lists 83; technical report says "about 80 languages and dialects" → model card, arXiv 2610.18010
- Preview status → Fish's landing page labels Drama 3 a preview: "Results vary between takes, so generate a few and pick the best" → https://fish.audio/drama-3/
- Event-tag placement → vLLM-Omni recipe: mid-sentence tags more reliable than line-start; takes opening with fillers/event tags can emit silence to `max_new_tokens` → https://recipes.vllm.ai/fishaudio/drama-3
- OpenRouter → `fish-audio/drama-3`, `/api/v1/audio/speech`, `input` + `voice`, `response_format` `mp3`/`pcm` (default pcm) → https://openrouter.ai/fish-audio/drama-3/llms.txt

### Unverified / flagged in the skill

- `fishaudio/drama-3-int4` checkpoint — not named on any first-party page checked
- Body field names for single-chunk and reference speaker on the Fish Speech server (`single_chunk`, `speaker`): docs give the client flags; the schema file fetched still showed the pre-Drama-3 shape (temperature/top_p default 0.8, no such fields) — skill tells users to query `GET /v1/tts/defaults` and their installed revision
- Exact `previous_takes` item shape on SGLang-Omni (text vs audio/VQ) — model card wording and examples differ
- Hosted Drama 3 price — not on Fish's pricing page; ComfyUI ≈ $14.30 / M bytes launch → $35.75 from 2026-11-13; third-party $50 / M chars list, $10 launch
- Fish's own editing/inpainting interface being invite-only (third-party report)
- Sampling ranges per goal are practical guidance, not official presets

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
