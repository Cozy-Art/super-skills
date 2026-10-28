---
name: meshy-v7-prompts
description: "Generate optimized prompts and API payloads for Meshy 7 / Meshy 7.1 (ai_model meshy-7.1, latest), Meshy's AI 3D asset generator. Use whenever a user mentions Meshy, Meshy 7, Meshy 7.1, Meshy Ultra 2K/4K, or wants text-to-3D, image-to-3D, multi-view image-to-3D, AI texturing or retexturing, remeshing to a polycount, auto-rigging, preset animations or Text to Motion clips for a generated 3D model — game props, characters, environment modules, collectibles, 3D-print parts or consistent asset libraries. Also use when migrating Meshy 6 / Meshy 7 payloads (ultra_mode, hd_texture, is_a_t_pose, art_style, lowpoly) to 7.1. Meshy makes 3D assets, not video: no aspect ratio, duration or camera fields on geometry. Do not guess Meshy syntax from general knowledge or older versions — use these references."
---

# Meshy 7.1 — Prompt Generation Skill

Meshy 7.1 is a 3D asset model: text, one image, or up to four views in → a textured mesh (GLB/FBX/OBJ/STL/USDZ/3MF) out. Texturing, remeshing, rigging and animation are **separate task endpoints chained by task ID**. `ai_model: "latest"` resolves to `meshy-7.1`; `meshy-7` is deprecated but still runs.

**Scope:** one asset per task. Scenes, cameras, lenses, lighting setups and shot timing belong in your DCC/engine, not in Meshy prompts.

## The Three Rules That Override Everything

1. **One object, subject first.** Name a single asset and its silhouette in the first words — early terms carry the most weight. Scenes, crowds and "a set of…" fuse into one blob. Generate parts separately and assemble downstream.
2. **Shape and surface are different prompts.** The geometry `prompt` describes form, proportions and construction; the `texture_prompt` (or texture image) describes materials, colour and wear. Don't spend geometry words on paint or lighting.
3. **Continuity lives in task IDs and files, not seeds.** There is no seed, no weighting syntax and no working `negative_prompt`. To keep an asset, chain its task ID (`preview_task_id`, `input_task_id`) or re-feed the downloaded GLB — and download within 3 days (API retention for non-Enterprise).

## Prompt Order

| # | Layer | Example |
|---|---|---|
| 1 | Singular subject | "A medieval wooden treasure chest", "A full-body desert courier android" |
| 2 | Silhouette + proportions | "compact rectangular", "oversized head, short sturdy limbs" |
| 3 | 2–4 defining features | "two side valves, wide circular visor" |
| 4 | Construction material (geometry-relevant) | "thick oak planks", "layered ceramic armour plates" |
| 5 | One coherent style | "grounded dieselpunk realism", "hand-painted stylized game art" |
| 6 | Pose (characters) | "symmetrical A-pose, separated arms and legs" |
| 7 | Technical intent | "single unified object", "watertight", "game-ready", "clean edges" |

```
[SUBJECT], [SILHOUETTE/PROPORTIONS], [DEFINING FEATURES],
[MATERIAL CONSTRUCTION], [ONE STYLE], [POSE], [TECHNICAL INTENT].
```

**Limits:** `prompt` ≤ 800 chars · `texture_prompt` ≤ 800 chars · Text to Motion `prompt` ≤ 400 chars. **Practical targets:** geometry 20–60 words · texture 10–40 words · motion one action, 1–2 sentences.

## Decide the Operation First

| User wants | Endpoint / mode | Key fields |
|---|---|---|
| New asset from text | `POST /openapi/v2/text-to-3d` `mode: preview` → `mode: refine` | `prompt`, `geometry_resolution`, then `preview_task_id` + `texture_prompt` |
| Asset from one concept image | `POST /openapi/v1/image-to-3d` | `image_url` or `input_task_id`, `texture_prompt` optional |
| Accurate asset from front/side/back | `POST /openapi/v1/multi-image-to-3d` | `image_urls` (1–4, front first), max `geometry_resolution: 2k` |
| New look on an existing mesh | `POST /openapi/v1/retexture` | `input_task_id`/`model_url` + `text_style_prompt` or `image_style_url` |
| Controlled polycount / quads / format | `POST /openapi/v1/remesh` | `topology`, `target_polycount` or `decimation_mode` |
| Clean game topology from the start | text/image-to-3d `model_type: smart-topology` | `ai_model: meshy-t2.5` (default) or `meshy-t2` |
| Skeleton on a humanoid | `POST /openapi/v1/rigging` | textured biped, ≤300k faces, `height_meters` |
| Preset moves | `POST /openapi/v1/animations` | `rig_task_id` + `action_id` / `action_ids` (≤10) |
| Custom move from text | `POST /openapi/v1/text-to-motion` → animations | `prompt`, `duration` 2–10 s, then `motion_task_id` |

## Quick Syntax Reference

- **Auth:** `Authorization: Bearer <MESHY_API_KEY>`; create returns `{"result": "<task id>"}`; poll `GET …/:id` or stream `…/:id/stream` until `SUCCEEDED`.
- **Geometry tiers:** `geometry_resolution: standard | 2k | 4k` (+5 credits for Ultra). `4k` only on Text to 3D Preview and single Image to 3D; Multi-Image caps at `2k`.
- **Texture tiers:** `texture_resolution: 2k | 4k | 8k` — independent of geometry resolution. 8K costs more.
- **Pose:** `pose_mode: "a-pose" | "t-pose" | ""`. Use the field, and echo it in the prompt.
- **Exclusions:** describe what you want ("single unified watertight form"). Short structural phrases like "no floating parts" are fine; long "no X, no Y" lists are not.
- **Text vs image texture:** if both `texture_prompt` and `texture_image_url` are sent, the text wins. Send one.

Full field tables, defaults and credits → [parameters.md](parameters.md).

## Output Format (always two parts)

1. **Prompt** — in a code block, prompt text only. For texture work give the **geometry prompt** and the **texture prompt** as separate code blocks, labelled. For motion, the motion prompt in its own block.
2. **Suggested settings** — one line, e.g. `endpoint: text-to-3d preview→refine · ai_model: meshy-7.1 · geometry_resolution: 2k · pose_mode: a-pose · texture_resolution: 4k · enable_pbr: true · target_formats: [glb, fbx]`

Never put polycount, resolution, format or pose *values* inside prompt text as a substitute for the fields. If the user is building an API call, also give the JSON body with only documented fields.

## Things That Will Break the Request

- `prompt` > 800 chars, motion `prompt` > 400 chars or blank → **400**.
- `geometry_resolution: "4k"` on Multi-Image, or any Ultra tier with a non-7.1 model → error.
- `topology: "quad"` with `smart-topology` → error. `image_enhancement`/`remove_lighting` with `meshy-6-lite` or `smart-topology` → error.
- `texture_image_urls` combined with `texture_prompt` or `texture_image_url` → rejected.
- Rigging a non-humanoid, untextured, >300k-face, or non-+Z-facing mesh → fails (422 on pose estimation).
- Re-sending an expired signed download URL as `model_url` → `400 failed to download model file`. Use `input_task_id` while retained, else your local copy.
- Deprecated, no effect: `negative_prompt`, `art_style`, `symmetry_mode`, `surface_mode`. Deprecated but mapped: `ultra_mode` → `2k`, `hd_texture` → `4k`, `is_a_t_pose` → `pose_mode`. `model_type: "lowpoly"` retires 30 Oct 2026. Legacy `/v2/text-to-3d` path → `/openapi/v2/text-to-3d`.

## Iteration Workflow

1. **Shape first:** Preview at `standard`, `should_remesh: false`, mesh only, `target_formats: ["glb"]`. Run 2–4 variants.
2. **Diagnose one category** — identity, silhouette, construction, material, topology — and change one or two phrases per pass.
3. **Lock geometry** before paying for Ultra or 8K: re-run the winner's prompt at `2k`/`4k` only if fine detail must be real geometry.
4. **Texture** the locked mesh via `refine` (`preview_task_id`) or Retexture — never by regenerating the mesh.
5. **Optimize** with Remesh (keep the un-remeshed GLB as master; `save_pre_remeshed_model: true` when remeshing inline).
6. **Rig → animate** only the approved, textured A/T-pose character. Download every stage immediately.

## Reference Files

- **[parameters.md](parameters.md)** — every endpoint and field, valid values, defaults, credit costs, formats, recommended combinations, Meshy 7 → 7.1 migration.
- **[best-practices.md](best-practices.md)** — geometry vs texture prompting, asset-type templates, image/multi-view reference prep, motion prompts, common mistakes table.
- **[continuity-and-references.md](continuity-and-references.md)** — task-ID chaining, canonical masters, consistent asset libraries (style, topology, texel density, scale), character rig/animation pipelines, versioning.
- **[examples.md](examples.md)** — 10 annotated prompts + payloads: prop, hero prop with texture prompt, rig-ready character, stylized character, environment module, display sculpture, multi-view, retexture variant set, game-ready remesh, motion pipeline.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
