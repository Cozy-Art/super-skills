# YuE2 — Parameters

Four common surfaces: the **native `yue2` pipeline** (HF wheel), **ComfyUI core nodes**, **DiffSynth-Studio**, and **MachGen hosted T2M**. They name and expose different controls — pick the interface first, then use only its fields.

*Verified against the m-a-p/YuE2-3B model card and LICENSE, the multimodal-art-projection/YuE covers guide, ComfyUI `nodes_yue2.py` + embedded docs, DiffSynth-Studio YuE2 docs, and MachGen models / API reference / pricing pages, October 2026.*

## Native Pipeline (`m-a-p/YuE2-3B`)

Install (Linux, Python 3.10+):
```bash
python -m pip install huggingface-hub==0.36.2
hf download m-a-p/YuE2-3B yue2_infer-0.1.5-py3-none-any.whl --local-dir .
python -m pip install ./yue2_infer-0.1.5-py3-none-any.whl
```

```python
from yue2 import YuE2Pipeline
pipe = YuE2Pipeline.from_pretrained("m-a-p/YuE2-3B", device="cuda")   # vae="m-a-p/YuE2-Vae-legacy" optional
song = pipe(style="...", lyrics="...", cot="full", seed=831001)
song.save("song.flac"); song.save_artifacts("outputs/song")
pipe.close()
```

| Argument | Type | Values | Default | Notes |
|---|---|---|---|---|
| `style` | str | free text | — | Musical direction. No published character max; shares context with everything else. |
| `lyrics` | str | sectioned text | — | Singable words + `[Section]` tags. |
| `cot` | str | `full` `melody` `off` | `full` | `full` = melody + chords plan · `melody` = melody-only (covers) · `off` = no symbolic plan. |
| `abc` | str | ABC score | none | Supplied/edited score. Requires `cot="full"` or `"melody"`. |
| `seed` | int | integer | — | Hold fixed for A/B. Not bit-identical across GPUs/runtimes/revisions. |
| `cfg_scale` | float | ≥ 0 | 1.0 (`full`/`melody`), 1.01 (`off`) | 1.0 = semantic CFG off. Model card suggests trying `1.2` for stronger text adherence. ABC sampling uses no CFG. |
| `progress` | bool (loader) | `False` | on | Silences progress output. |
| `vae` | str (loader) | `m-a-p/YuE2-Vae` / `m-a-p/YuE2-Vae-legacy` | `YuE2-Vae` | Default = better perceptual quality; legacy = paper benchmark protocol. |

Staged API for editing: `pipe.plan(...)` → `plan.save(dir)` → `pipe.generate_semantic(plan)` → `pipe.synthesize(semantic)` → `pipe.decode(latents)`.
CLI in the package: `yue2 generate`, `yue2 batch`. Repo example: `python examples/generate.py --request song.json --abc-file score.abc --cot melody --output outputs/x` (`song.json` holds `style`, `lyrics`, `cot`, `seed`).
Sampling and duration are **not** documented as native call arguments — use the ComfyUI values below only where your runtime exposes them.

## ComfyUI Core Nodes

Checkpoint `yue2.safetensors` (all-in-one). Graph: **YuE2 Generate ABC** → **YuE2 Generate Music** → (`seconds`) → **Empty YuE2 Latent Audio** → sampler → decode.

**YuE2 Generate ABC** → outputs `abc` string

| Input | Default | Range / Options |
|---|---|---|
| `style`, `lyrics` | — | multiline, dynamic prompts |
| `seed` | 0 | 0 – 18,446,744,073,709,551,615 |
| `mode` | `full` | `full`, `melody` |
| `max_abc_tokens` | 8192 | 1 – 20,000 (advanced) |

ABC sampling is fixed internally (temperature 0.7, top_p 0.9, top_k 30, repetition penalty 1.005) — not user inputs.

**YuE2 Generate Music** → outputs CONDITIONING + `seconds`

| Input | Default | Range | Notes |
|---|---|---|---|
| `abc` | `""` | string | **Empty/whitespace forces `off` mode**, overriding `mode`. |
| `seed` | 0 | 0 – 2⁶⁴−1 | |
| `mode` | `full` | `full`, `melody` | `off` is not in the dropdown. |
| `max_duration` | 360 s | 0.04 – 900 s, step 0.04 | Ceiling, auto-reduced for long prompts; may finish earlier. Builds before ComfyUI PR #16292 cap at 360. |
| `temperature` | 1.0 | 0.0 – 5.0 | Lower = predictable, higher = varied. |
| `top_p` | 0.95 | 0.01 – 1.0 | |
| `top_k` | 100 | 1 – 32,768 | |
| `repetition_penalty` | 1.2 | 0.01 – 10.0 | Too high breaks musically necessary repetition (choruses). |
| `cfg_scale` | 1.0 | 0.0 – 100.0 | Optional/advanced; 1.01 = original off-mode value. May be absent in older builds. |

**Empty YuE2 Latent Audio:** `seconds` 120 default (0.04–1000) — wire from Generate Music's `seconds`; `batch_size` 1–4096.

## DiffSynth-Studio

`pipe(prompt=..., lyrics=..., cot="full", seed=831001)` — **style field is `prompt`** here. Extra: `num_inference_steps` (default 30, acoustic flow-matching ODE steps), `vae_core_frames` (decode tiling), `abc`, `cfg_scale` (same defaults). Install `pip install -e ".[yue2,audio]"`; supports CPU offload / `vram_limit` for smaller GPUs. Saves 48 kHz audio.

## MachGen Hosted (`YuE2-3B`, task `T2M`)

`POST https://api.machgen.ai/api/v0/generate` → poll `GET /api/v0/tasks/{task_id}` (PENDING / RUNNING / COMPLETED / FAILED).

| Field | Required | Values | Notes |
|---|---|---|---|
| `model` | ✅ | `YuE2-3B` | Account needs access. |
| `task_type` | ✅ | `T2M` | |
| `prompt` | ✅ | style text | Genre, instruments, mood, voice, tempo. Not lyrics. |
| `audio_config.lyrics` | ✅ vocal | 400 – 10,000 chars | Out-of-range rejected pre-generation. Instrumental: 0 – 10,000; blank = default sections. |
| `audio_config.force_instrumental` | — | bool | UI: Generate → Advanced → *Instrumental only*. Humming/vocals can still appear. |
| `audio_config.output_format` | — | `flac` only | Default `flac`. |
| `seed` | — | int | General platform field; random if omitted. YuE2-specific behaviour undocumented. |

Do **not** send: `duration_secs` (docs: omit for YuE2), `composition_plan`, `voice_id`, `cot`, `abc`, `cfg_scale`, sampling fields.
Output: stereo FLAC, capped ≈ 6 min (over-long songs are truncated, still "successful"). Score-limit failure → `FAILED`, `error_msg`: *"Score limit reached. Try a different music style or lyrics to shorten the generated score."*
Price: **$0.10 per generation** (MachGen pricing page; subject to change).

## Technical Specs

| Spec | Value |
|---|---|
| Model | YuE2-3B (~3.6B params reported by third parties — unverified), 28-layer AR–NAR Mixture-of-Transformers; symbolic + semantic AR, acoustic flow matching |
| Context | 24,576 positions shared by style, lyrics, ABC and music tokens |
| Semantic / latent rate | 25 Hz; 64-dim acoustic latents |
| Audio | 48 kHz stereo; FLAC in examples |
| Languages | English and Chinese confirmed (model tags + examples); others unverified — confirm on your platform |
| Hardware | 24 GB BF16 NVIDIA GPU + 24 GB host RAM recommended; reported peak ~11 GiB (≤14.1 GiB at max context). 3.6-min song ≈ 71 s on RTX 4090 (full CoT). One song at a time; separate vLLM server for concurrency. |
| Licence | Weights (YuE2-3B, YuE2-Vae, YuE2-Vae-legacy): **CC BY-NC 4.0**, attribution to YuE2 + source repo. Output-licensing terms not stated — check before commercial use. |

## Recommended Combinations

| Goal | `cot` | `abc` | CFG | Sampling | Notes |
|---|---|---|---|---|---|
| Reliable original | `full` | — | 1.0 | defaults | 4–6 sections, moderate density |
| Weak style adherence | `full` | — | try 1.2 | defaults | One change at a time |
| Fast ideation | `off` | — | 1.01 | defaults, vary seed | No score produced |
| Restyle cover | `melody` | `--melody-only` score | 1.0 | defaults | Lyrics aligned to score |
| Harmony-locked cover | `full` | score with chords | 1.0 | defaults | |
| Score edit | baseline | edited `score.abc` | baseline | baseline | Same seed & revisions |
| More predictable takes | `full` | saved | 1.0 | temperature below 1.0 (heuristic, untested values) | ComfyUI only |
| Hosted demo | MachGen | — | — | — | `$0.10`, FLAC, ≤ 6 min |

## YuE v1 → YuE2 Migration

| YuE v1 | YuE2 |
|---|---|
| Stage-1 7B + stage-2 1B + upsampler | One ~3B model + VAE decoder |
| `genre.txt` with ~5 space-separated tags | One `style` line (comma-separated, can be descriptive) |
| `lyrics.txt`, each section ≈ one 30 s session | Sections are form, not session boundaries |
| `--run_n_segments`, `--max_new_tokens` | Whole song in 24,576-position context (`max_duration` in ComfyUI) |
| CoT vs ICL checkpoints | One checkpoint; choose `cot` |
| Audio ICL (`--use_audio_prompt`, dual-track) | SheetSage2 → reviewed ABC → `cot="melody"` |
| Apache 2.0 weights | CC BY-NC 4.0 weights |
| v1 seeds | Not transferable — re-baseline |
