# world-labs-atlas — build notes

Human-facing build notes. Not loaded as part of the skill.

**Built:** 2026-10-19 · **Skill version:** 1.0 · **Model:** World Labs Atlas + Atlas-family Marble Developer API v2 beta tasks (World Labs)

---

## Research verification

First-party sources: https://www.worldlabs.ai/blog/atlas (launch) · https://atlas-beta.worldlabs.ai/docs (beta guides + API reference) · https://docs.worldlabs.ai/api (World API v1). Note the beta docs live on `atlas-beta.worldlabs.ai`, not `docs.worldlabs.ai`; the latter documents only Marble 1.x and mentions neither Atlas nor Marble 2.

Confirmed: Sept 1 2026 announcement, "early access with select partners"; "one to six input images with manually designed camera paths"; "up to 1 minute of video at 1440p"; inputs "text, images, camera poses, and 3D depth maps"; six v2 tasks incl. `splats2Mesh`; `numSamples` 1–4 vs guide example 16; aspect ratios and `1:1` fallback; `seed + i`; 1280 × 720 targets; 8-step distilled `atlasGenerate`; Chisel 1–32 targets, 64-view rollout, voxelSize 0–0.4 / 0.05–0.15; mask format; camera-to-world XYZW, `rub`/`rdf`; 30-day operation retention; non-overlapping frusta for separately posed images; "not yet as strong on humans or dynamic objects"; v1/Marble 4 examples "not compatible contracts".

Corrections:
- `atlasMasked` "access-dependent" → stronger: "requires access to this task on your account" and "is not part of the default external beta surface yet" — https://atlas-beta.worldlabs.ai/docs/inpainting
- "Do not assume a model selector" for `atlasGenerate` → an optional `model` field exists; unset = routed by context/target counts; pin only after evaluation — https://atlas-beta.worldlabs.ai/docs/atlas-generate
- `atlasChisel` `returnDepth` shown top-level → API reference lists it inside `modelParameters` (the only property listed there); skill says to follow the live schema — https://atlas-beta.worldlabs.ai/docs/api-reference/atlas-chisel
- `atlasChisel` contextFrames → may be left empty to generate from the prompt alone; `imageAsset`/`maskAsset`/`confidenceAsset` are rejected; source photos any size, cover-resized and center-cropped — same reference + https://atlas-beta.worldlabs.ai/docs/depth-guided-generation
- Mask keep value "255" → docs say 255 in the guide and "1 is kept" in the reference; skill teaches 255 for an 8-bit PNG and notes the wording — https://atlas-beta.worldlabs.ai/docs/api-reference/atlas-masked
- Quickstart "0.25-unit X" → "0.25 metres along world X in the estimated scene", with metric scale predicted (approximate) — https://atlas-beta.worldlabs.ai/docs/web-quickstart
- "2–3 images can often give faithful reconstruction" → not found on the launch page; it says "one to dozens", "over a hundred", and video reframing from "as few as three cameras". Replaced.
- World API v1 default → `marble-1.0` when omitted today, changing to `marble-1.1` later — https://docs.worldlabs.ai/api/models

Unverified (marked in the skill): `modelParameters.seed` default 42 (all tasks) and `atlasMasked` `numSteps` default 50 — the reference pages list `modelParameters` with no properties; `canonicalizeToFirstFrame` behaviour (appears only in an example); any `contextFrames` maximum for `atlasGenerate`; all Atlas partner video controls (duration, FPS, codec, aspect ratio) — none are public; the fx/FOV lens table is derived pinhole math, not a World Labs table.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
