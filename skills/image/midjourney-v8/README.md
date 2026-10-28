# midjourney-v8 — build notes

Human-facing build notes. Not loaded as part of the skill.

**Built:** 2026-10-18 · **Skill version:** 1.0 · **Model:** Midjourney V8 (8.1 / 8.2) (Midjourney)

---

## Research verification


Corrections:
- `--q 1/2/4` recommended for V8 (incl. `--q 4` product preset) → Quality parameter is listed as INCOMPATIBLE with V8.1/V8.2 (q4 existed only in V8.0 alpha); replaced with `--hd` — https://docs.midjourney.com/docs/models
- V7 Omni Reference "still available while V8 replacement matures" → Omni Reference (`--oref`/`--ow`) is not supported on V8.1/V8.2; Edit model replaces Omni Reference, Character Reference and Retexture — https://docs.midjourney.com/docs/models , https://updates.midjourney.com/edit-model-for-v8/
- `--draft` / Draft mode (24 images) listed as V8 parameter → Draft mode is listed as incompatible with V8.1/V8.2 in the current Version doc (Parameter List says `--draft` is V7-only); the June V8.1 draft post is superseded — docs.midjourney.com/docs/models, Parameter List
- `--turbo` listed as a V8 speed option → Turbo incompatible with V8.1/V8.2 — docs.midjourney.com/docs/models
- HD described loosely ("about 2K", no syntax) → explicit `--hd` / `--sd` params; HD = 2048px, SD = 1024px; HD ≈1.3 GPU-min vs SD 0.8; max aspect 14:1 SD / 4:1 HD; upscalers SD-only; Pan/Zoom/Vary Region downscale HD to SD — docs.midjourney.com/docs/models, Parameter List
- Multi-prompts "not officially listed" → explicitly incompatible with V8.1/V8.2 — docs.midjourney.com/docs/models
- Added `--exp` (missing from research) — listed as compatible with V8.1/8.2 in Version doc and in V8 alpha post
- `--iw` "V8 range unverified" → Image Prompts doc lists V8.1: 0–3, default 1 — docs.midjourney.com Image Prompts article
- Seed: added "V8 reruns ~99% identical" — docs.midjourney.com/docs/models
- Video incompatibilities: research said "Omni Reference" → doc says Edit Model references, Style Reference and Image Prompts; added GPU cost table (bs4 SD 8 min / HD 26 min etc.) and HD = Fast only — https://docs.midjourney.com/hc/en-us/articles/37460773864589-Video
- Edit model: dated public test Aug 27, 2026; targeted edits change only selected pixels (Sept 24 update) — updates.midjourney.com/edit-model-for-v8/, /edit-updates-thumbnail-previews-and-more/
- Moodboards incompatible with `--sw` and `--sv` (added) — Style Reference doc

Unverified:
- `--exp` range 0–100 / default 0 (from V7-era docs and evolink reseller, not a V8 official page)
- `--sv` values for V8.x (only V7/V6 documented)
- `--iw` range for V8.2 specifically (doc lists 8.1)
- 1,024-character descriptive limit (reseller-enforced; no official MJ limit)
- Edit-model reference ordering semantics (only "up to 4" documented)
- `--stealth` plan requirement (Pro/Mega) taken from general knowledge

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
