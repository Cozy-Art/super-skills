# tripo-p1 — build notes

Human-facing build notes. Not loaded as part of the skill.

**Built:** 2026-10-18 · **Skill version:** 1.0 · **Model:** Tripo Smart Mesh P1.0 (Tripo)

---

## Research verification


Corrections / clarifications vs research:
- Image-to-model and multiview-to-model have NO prompt / negative_prompt / image_seed fields → skill routes prompt craft into the reference-image brief — developers.tripo3d.ai/en/docs/generation-image-to-model/p , /generation-multiview-to-model/p
- `quad=true` on P1 returns HTTP 400 specifically (research said only "an error") — developers.tripo3d.ai/en/docs/changelog
- P2-20260801 is marked "Preview" on endpoint pages (research presented it as plain successor) — /generation-text-to-model/p
- face_limit lower bound: endpoint pages consistently 50; P1 model page's parameter section says 48 (overview 50) → used 50 — /models/p1
- On /v3/models/texture the texture version field is `model` (default v3.0-20250812), not `texture_version`; texture_prompt is {text|image|images(exactly 4)} + style_image only with text — /models-texture
- Rig: added model versions v1.0-20240301 (default, biped only), v2.5-20260210 (creatures), v3.0-20260909 (humanoid, `others`); rig_type list, spec values (tripo/mixamo/actorcore/unity/unreal/vrm) — /animations-rig
- Retarget preset IDs are `preset:walk` etc. (rig v2.5) or `preset:biped:*` (rig v1.0); `animation` vs `animations` mutually exclusive; `bake_animation` deprecated — /animations-retarget
- Rig check path confirmed `POST /v3/animations/rig-check`, returns riggable + rig_type — developers.tripo3d.com/en/docs/animations-rig-check
- Segmentation path `POST /v3/mesh/segment` (research only cited "smart segmentation"); v2.0-20260430 Beta semantic — /mesh-segment
- Convert parameters fully listed (quad forces FBX, fbx_preset, pivot_to_center_bottom, etc.) — /models-convert
- Pricing added: P1 30/40/50 (text) and 40/50/60 (image/multiview) for none/standard/detailed; P2 100/110/120/130 — /models/p1, /changelog
- credits_consumed is decimal (changelog doc correction)
- Retopology `POST /v3/mesh/decimate` and `POST /v3/mesh/uv` exist (Oct 2026 changelog)

Unverified / flagged in skill:
- Pricing units on P1 model page unlabelled (assumed credits)
- Retarget preset set for rig v3.0-20260909
- Smart Segmentation and Mesh Complete endpoint paths (omitted); decimate parameters (only path given)
- Emoji/Unicode warning (legacy P1 doc only)
- Result URL expiry duration (not documented; skill just says download promptly)
- `tripo-p1` alias: appears in models/versions guidance, but requests use `P1-20260311`

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
