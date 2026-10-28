# yue-v2 — build notes

Human-facing build notes. Not loaded as part of the skill.

**Built:** 2026-10-18 · **Skill version:** 1.0 · **Model:** YuE2 (M-A-P)

---

## Research verification


Corrections:
- Licence "CC BY-NC 4.0 plus additional individual-creator permission" → LICENSE and model card state CC BY-NC 4.0 for weights only; no individual-creator grant; output licensing not addressed — https://huggingface.co/m-a-p/YuE2-3B/blob/main/LICENSE
- ComfyUI ABC sampling (temperature 0.7 / top_p 0.9 / top_k 30 / rep 1.005) listed as tunable → fixed internally in YuE2 Generate ABC, not inputs; `penalty_window` not found — https://github.com/Comfy-Org/ComfyUI/blob/master/comfy_extras/nodes_yue2.py
- ComfyUI `cot` "full/melody/off" → `mode` dropdown is only full/melody; empty ABC silently forces off — same source + embedded docs
- ComfyUI `max_duration` 0.04–900 s → build-dependent: 900 after PR #16292, 360 cap in earlier node source — https://comfyui-wiki.com/news/2026-09-11-yue2-3b , embedded docs
- Covers: "remove chord symbols during review" → SheetSage2 `--melody-only` flag already omits chords (manual strip only needed if a chorded score is used with melody mode) — https://github.com/multimodal-art-projection/YuE/blob/main/docs/covers.md
- ABC voices named `Vocal` / `Ins` → not stated in covers guide or model card; marked unverified — same
- MachGen: added verified details missing from research — out-of-range vocal lyrics rejected pre-generation; blank instrumental lyrics use default sections; `duration_secs` explicitly "omit for YuE2"; `output_format` only `flac`; score-limit FAILED error text; truncated >6 min tracks still return success — https://www.machgen.ai/docs/reference , https://www.machgen.ai/docs/models
- MachGen seed: research implied supported for YuE2 → model page says seed "not documented for this model"; only the general platform field exists — same
- DiffSynth-Studio uses `prompt` (not `style`) and adds `num_inference_steps` (default 30) — https://github.com/modelscope/DiffSynth-Studio/blob/main/docs/en/Model_Details/YuE2.md
- Native install/CLI added: wheel `yue2_infer-0.1.5`, `yue2 generate`/`yue2 batch`, staged plan→semantic→synthesize→decode API, `progress`/`vae` loader args; hardware 24 GB GPU + 24 GB host RAM, ~11 GiB peak — https://huggingface.co/m-a-p/YuE2-3B
- Verified as correct: cot defaults/semantics, cfg 1.0/1.01 defaults and 1.2 suggestion, 48 kHz stereo, 24,576 context, 25 Hz/64-dim latents, best-of-8 6.96 vs 6.73, VAE default vs legacy, $0.10/generation, MachGen 400–10,000 char lyric range, ~6 min cap.

Unverified (marked in skill):
- Parameter count ~3.58B (third-party/paper figure not confirmed from fetched pages)
- Languages beyond English/Chinese
- ABC dialect voice labels
- Native sampling/duration call arguments (only ComfyUI exposes them)
- Output (generated audio) licensing terms
- v1-era claim that `[Intro]` as first section is unstable — flagged as needing re-test on YuE2

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
