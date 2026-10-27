# Fish Audio Drama 3 — Parameters

*Verified against docs.fish.audio (Drama 3 feature page, Text to Speech API reference, Pricing & Rate Limits), speech.fish.audio (overview, Installation, Inference), huggingface.co/fishaudio/drama-3, github.com/fishaudio/fish-speech (README, chunking source), the Drama 3 technical report (arXiv 2610.18010), docs.comfy.org (Fish Audio Drama 3 tutorial), recipes.vllm.ai and openrouter.ai, October 2026.*

Drama 3 is labelled **preview** by Fish Audio and "will keep updating" — re-check field behaviour when a new checkpoint or runtime revision lands.

## Model Facts

| Item | Value |
|---|---|
| Architecture | 35B-A3B MoE (3B active per token), hybrid full + linear attention, codebook-MTP audio decoder (10 codebooks) |
| Weights | `fishaudio/drama-3` — FP8 MoE experts, rest bf16 |
| Quantized checkpoint | `fishaudio/drama-3-int4` (unverified — not named on first-party pages; community quantizations exist) |
| Output | 44.1 kHz mono; 2,048 samples per acoustic frame ≈ 21.53 frames/s |
| Speaker IDs | `<|speaker:0|>` … `<|speaker:15|>` — up to 16 characters in one text (model card). Hosted docs state no maximum; ComfyUI node exposes 5 voices |
| Languages | 83 listed in model-card metadata; technical report says "about 80 languages and dialects" |
| Licence | README: Fish Audio Community License (model-card header metadata says research licence — check the `LICENSE` file of your exact revision) |

## Fish API — `POST https://api.fish.audio/v1/tts`

Headers: `Authorization: Bearer <key>`, `Content-Type: application/json` (or `application/msgpack`), **`model: drama-3`**. A missing or misspelled header does not fail — it falls back to `s2.1-pro`.

| Field | Type | Values | Default | Drama 3 notes |
|---|---|---|---|---|
| `text` | string | script | **required** | Speaker tags, brackets, paired/language/phoneme tags + words |
| `reference_id` | string \| string[] | voice model ID(s) | `null` | Array index = `<|speaker:N|>` |
| `references` | `{audio, text}`[] or 2-D | inline clip + exact transcript | `null` | **MessagePack only**; 2-D array for zero-shot multi-speaker, inner array index = speaker. No `speaker` field on the hosted schema |
| `temperature` | number | 0–1 | 0.7 | |
| `top_p` | number | 0–1 | 0.7 | |
| `prosody` | object | `speed` 0.5–2.0 (1), `volume` dB (0), `normalize_loudness` (true) | `null` | Global only — use `<fast>`/`<slow>` for local pace |
| `chunk_length` | int | 100–300 | 300 | |
| `min_chunk_length` | int | 0–100 | 50 | |
| `condition_on_previous_chunks` | bool | | `true` | Keep on for long scenes |
| `normalize` | bool | | `true` | Number/symbol normalization |
| `language` | string | BCP-47, ≤35 chars | `null` | Normalization only, not the voice |
| `format` | enum | `mp3` `wav` `pcm` `opus` | `mp3` | |
| `sample_rate` | int | wav/pcm 8k–44.1k · mp3 32k/44.1k · opus 48k | `null` | |
| `mp3_bitrate` | enum | 64, 128, 192 | 128 | |
| `opus_bitrate` | enum | -1000, 24000, 32000, 48000, 64000 (bps) | -1000 | |
| `latency` | enum | `low` `balanced` `normal` | `normal` | `normal` for rendered drama |
| `max_new_tokens` | int | frames per chunk | 1024 | ≈ 47.6 s |
| `repetition_penalty` | number | | 1.2 | Ignored by Drama 3 |
| `early_stop_threshold` | number | 0–1 | 1 | Leave default |
| `features` | string[] | e.g. `quality-guard` | `[]` | |
| `pronunciation_dictionary` | array | ≤3 entries | `null` | Unresolvable refs dropped silently |

**Not on the hosted schema:** `seed`, `top_k`, `single_chunk`, `previous_takes` or any history/edit/infill field, `duration`, `emotion`, `voice_id`. Revision and infilling are therefore **not** available through the public hosted endpoint as of October 2026.

**Pricing:** `drama-3` is not listed on Fish's pricing page (it lists s2.1-pro / s2-pro / s1 at $15 per M UTF-8 bytes). Platform listings differ — ComfyUI: ≈ $14.30 per M bytes launch offer, $35.75 from November 13, 2026; third-party: $50 per M chars list, $10 launch (unverified — confirm on your platform). Concurrency follows the account tier (5 / 15 / 50 by prepaid total; 429 without `Retry-After`).

## Fish Speech Open Runtime

Server: `python tools/api_server.py --llama-checkpoint-path checkpoints/drama-3 --device cuda:0` (options `--half`, `--api-key`, `--workers`, `--max-text-length`). Docker: `fishaudio/fish-speech:server-cuda` with `LLAMA_CHECKPOINT_PATH=checkpoints/drama-3`. The model is the checkpoint loaded at startup — there is **no per-request model field**.

| Endpoint | Purpose |
|---|---|
| `POST /v1/tts` | Generate — **MessagePack** body |
| `GET /v1/tts/defaults` | Loaded model's sampling defaults — query it rather than trusting a table |
| `GET /v1/health` | Health |
| `POST /v1/vqgan/encode` · `/decode` | Audio ↔ VQ tokens |
| `POST /v1/references/add` · `GET /list` · `POST /update` · `DELETE /delete` | Saved reference voices (`reference_id`) |
| `GET /ui` | Web UI |

| Field / flag | Default | Range | Notes |
|---|---|---|---|
| `text` | required | | |
| `format` | `wav` | `wav` `pcm` `mp3` `opus` | |
| `streaming` | `false` | | Per-chunk streaming |
| `references` | `[]` | `{audio, text}` | Exact transcript required |
| `reference_id` | `null` | saved ID | From `/v1/references/add` |
| reference speaker | 0 | 0–15 | Client `--reference_speaker N` per reference, written as a `<|speaker:N|>` prefix; a reference with no speaker is speaker 0 (body field name unverified — confirm on your revision) |
| single chunk | `false` | | Client `--single_chunk`: whole text in one pass, bypassing Drama 3 chunking (body field name unverified) |
| `max_new_tokens` | 1024 | int; `0` = model cap | `0` → 600 frames per chunk, or 2,048 with single chunk |
| `temperature` | 0.7 (resolved via defaults) | 0.1–1.0 | Schema file default may read 0.8 on some revisions — check `/v1/tts/defaults` |
| `top_p` | 0.7 (resolved) | 0.1–1.0 | Same caveat |
| `top_k` | 30 | | Not a documented request field; fixed in defaults |
| `seed` | `null` | int | Controls sampling RNG; does not guarantee identical timbre or waveforms across hardware/revisions |
| `normalize` | `true` | | Stabilizes English/Chinese numbers |
| `latency` | `normal` | `normal` `balanced` | |
| `use_memory_cache` | `off` | `on` `off` | Reference cache |
| `chunk_length` | 200 | 100–1000 | **No effect on Drama 3** |
| `repetition_penalty` | — | 0.9–2.0 accepted | **Ignored** (compatibility only) |

CLI: `python fish_speech/models/text2semantic/inference.py --checkpoint-path checkpoints/drama-3 --text '…' --prompt-audio ref.wav --prompt-text '<exact transcript>' --output out.wav --device cuda:0`.

## Frame Budget

| Frames | ≈ Audio |
|---:|---:|
| 600 (auto-chunk cap with `max_new_tokens=0`) | 27.9 s |
| 1,024 (default per pass) | 47.6 s |
| 2,048 (single-chunk cap with `0`) | 95.1 s |
| 10,240 minus prompt length (hard total cap, Fish Speech) | < 475 s |

Cap `max_new_tokens` near the expected length of short lines — runaway silence to the cap is a reported failure on some stacks.

## Drama 3 Chunker (Fish Speech source)

| Constant | Value | Behaviour |
|---|---|---|
| `DRAMA3_CHUNK_BYTES` | 300 | Target UTF-8 bytes per chunk (threshold — a protected span longer than this stays whole) |
| `DRAMA3_CHUNK_MAX_SPEAKERS` | 3 | Distinct speakers per chunk (A-B-A can share one) |
| `DRAMA3_CHUNK_MAX_NEW_TOKENS` | 600 | Frames per chunk when `max_new_tokens ≤ 0` |
| `DRAMA3_HISTORY_RECENT_TURNS` | 1 | Recent chunks kept besides the pinned first chunk |

Split order: sentence ends (`. ! ? ; 。 ！ ？ ； …` newline) → clause marks (`, : ， ： 、`) → spaces → raw characters, then re-merge to target. `3.14` is never split. `<|…|>` tokens, paired `<tag>…</tag>` spans and `[brackets]` are never split. Text before the first speaker tag = speaker 0. History: first chunk pinned for the run + latest chunk, falling back to shorter history if context is tight.

## Other Serving Paths

| Surface | Request shape | Notes |
|---|---|---|
| SGLang-Omni (`sgl-omni serve --model-path fishaudio/drama-3 --port 8000`) | `/v1/tts` JSON: `text`, `references: [{audio_path, text}]`, `previous_takes` for editing as continuation | Fish's recommended efficient path; exact `previous_takes` item shape — follow the model card / cookbook for your revision |
| vLLM-Omni (`vllm serve fishaudio/drama-3 --omni`) | `/v1/audio/speech`: `model`, `input`, `voice`, `ref_audio` + `ref_text`, `response_format`, `stream` | `previous_takes` and long-text chunking **not exposed yet**; ≥48 GB GPU; event tags mid-sentence are more reliable than at line start |
| ComfyUI Fish Audio TTS node (ComfyUI ≥ 0.39.3) | `model: drama-3`; growable `voices` input, ≤5 | One voice → passed as `reference_id`, no labels. Two+ → `@Voice1`… in text, every connected voice must appear or the node errors |
| OpenRouter | `/api/v1/audio/speech`: `model: fish-audio/drama-3`, `input`, `voice`, `response_format` `mp3`/`pcm` (default `pcm`) | No sampling or history fields |

## Hardware (open weights)

- NVIDIA CUDA only — no CPU, Apple MPS or AMD ROCm; no `torch.compile` / `--compile`.
- At least 48 GB VRAM for the FP8 path; Linux or WSL; CUDA builds cu126 / cu128 / cu129.
- Pre-SM80 GPUs fall back to fp16 with fp32 residuals — marked untested.
- Multi-GPU: `--device cuda:0,cuda:1,…`; the **last** device hosts the audio decoder and codec; plain `cuda` uses up to four GPUs.
- `FISH_DRAMA3_FP8_EXPERTS=0|1` (force dequantized / FP8 experts), `FISH_DRAMA3_CUDA_GRAPH=0` (disable CUDA-graph decoding).
- If the checkpoint folder lacks `codec.pth`, the S2-Pro codec is also needed.

## Sampling Starting Points (practical, not official)

| Goal | `temperature` | `top_p` |
|---|---:|---:|
| Stable narration | 0.5–0.6 | 0.6–0.7 |
| Balanced default | 0.7 | 0.7 |
| Emotional performance | 0.8–0.9 | 0.8–0.9 |
| Revision with minimal drift | match or slightly below the accepted take | match |

Higher sampling buys variation, not better acting — fix the direction first.
