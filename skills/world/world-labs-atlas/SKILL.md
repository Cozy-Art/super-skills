---
name: world-labs-atlas-prompts
description: "Generate prompts, camera plans and task pipelines for World Labs Atlas, the omni world model announced September 1 2026 (select-partner early access), and the Atlas-family tasks in the Marble Developer API v2 beta at atlas-beta.worldlabs.ai, namely atlasTextToImage, images2PosedRGBD, atlasGenerate, atlasChisel (depth-guided) and atlasMasked (multiview inpainting, account-gated). Use whenever a user mentions Atlas, World Labs Atlas, Marble 2 beta, posed RGBD, target cameras, novel-view generation, camera-controlled world video, depth-guided blockout-to-environment, multiview object replacement, or migrating World API v1 / Marble 1.x requests to the v2 task API. Atlas is controlled by text plus camera geometry plus depth plus posed reference views, not by camera verbs in prose. Do not guess Atlas fields, limits or video controls from Marble 1.x, the World API v1, or general video-model habits."
---

# World Labs Atlas — Prompt Generation Skill

Atlas is an omni world model: its native context is **text, images, camera poses and depth**, with video represented as image sequences. It is not a text-to-video model that decodes "slow dolly left" from prose. The craft is splitting each intent into the channel that carries it best.

**Two surfaces, different evidence:**
- **Publicly documented (Marble Developer API v2 beta):** `atlasTextToImage`, `images2PosedRGBD`, `atlasGenerate`, `atlasChisel`, `splats2Mesh`, and `atlasMasked` (needs task access on your account; "not part of the default external beta surface yet"). Frames are 1280 × 720.
- **Early-access only (Atlas partner system):** camera-controlled video "up to 1 minute of video at 1440p" from "one to six input images with manually designed camera paths", plus reconstruction and simulation. No public request fields exist for it — no `duration`, `fps`, `motionIntensity` or named moves. Never invent them.

**The interface is the source of truth.** If the user's account, schema or interface rejects or contradicts a value here, the interface wins — adjust and say so.

## The Rules That Override Everything

1. **Text = appearance. Cameras = viewpoint and movement. Depth = known structure. Posed references = identity, materials and light.** Never ask prose to carry what a camera pose or a reference view can carry.
2. **Prompt a place, not a picture.** One coherent navigable environment with explicit layout and spatial relationships — not a collage, split screen, poster or close-up portrait. Atlas/Marble 2 models are strongest on "spaces, environments, architecture, landscapes" and "not yet as strong on humans or dynamic objects."
3. **Continuity lives in scene state.** Reuse accepted RGBD views, cameras, `promptUsed` and seed; don't rewrite a long continuity paragraph per shot.

## Prompt Order (appearance prompt)

| # | Layer | Example |
|---|---|---|
| 1 | Place + layout | "A quiet stone courtyard enclosed by two-story arcades" |
| 2 | Depth layers | foreground path → central fountain → workshop doorway beyond |
| 3 | Materials + condition | damp limestone, oxidized bronze, dark oak, climbing ivy |
| 4 | Light, time, atmosphere | blue hour, warm window light, thin ground mist |
| 5 | Viewpoint (text-to-image only) | wide eye-level view with deep sightlines |
| 6 | Style | photorealistic cinematic naturalism / 1970s period color |

```
[PLACE + LAYOUT]. [FOREGROUND → MIDGROUND → BACKGROUND].
[MATERIALS + SURFACE CONDITION]. [LIGHT + TIME + ATMOSPHERE].
[VIEWPOINT — text-to-image only]. [STYLE].
```

**Length (practical, not official — no maximum is published):** new environment ≈ 60–150 words · continuation view = the earlier `promptUsed` verbatim · edit = one sentence.

## Decide the Task First

| User wants | Task | Text does | Geometry does |
|---|---|---|---|
| A world concept / seed image | `atlasTextToImage` | Full 6-layer description incl. viewpoint | — |
| Pose photos or generated stills | `images2PosedRGBD` | nothing (no prompt) | estimates camera + depth |
| A camera move / new viewpoints from images | `images2PosedRGBD` → `atlasGenerate` | "the same scene…" or `promptUsed` | `targetCameras` = the path |
| Turn a blockout or depth into a styled place | `atlasChisel` | style, materials, light (prompt required) | depth per target + optional posed source photos |
| Replace / remove an object across views | `atlasMasked` *(if your account has it)* | one edit instruction | grayscale masks + paired cameras |
| A mesh from an existing splat scene | `splats2Mesh` | — | — |
| A full minute-long camera-controlled video | Atlas partner system *(early access only)* | appearance prompt | designed camera path in their tool |

## Quick Syntax Reference

- **Prompt text:** plain natural language. No weighting, brackets, shot tags, negative-prompt field or special delimiters are documented. Prefer positive phrasing ("an empty courtyard"); in masked edits, state removals explicitly ("remove the parked car").
- **Enhancement:** `enhancePrompt` is on by default and rewrites your text (with context images) into a scene description returned as `promptUsed`. Off = your text is used verbatim as a caption of the finished scene.
- **Cameras:** pinhole; intrinsics `fx fy cx cy width height` in pixels; extrinsics are **camera-to-world** `position` + unit quaternion in **XYZW** + `coordinateSystem` `rub` (looks along −Z; OpenGL/Three.js) or `rdf` (looks along +Z; OpenCV). One world frame and one distance unit per request.
- **Movement:** express truck/dolly/crane/orbit/reveal as a sequence of target poses — see [best-practices.md](best-practices.md).

## Output Format

Return, in this order:

1. **Prompt** — in a code block, appearance text only. Never put aspect ratio, resolution, task names, seeds, camera numbers or move names like "dolly in" meant as instructions inside it.
2. **Suggested settings** — one line, e.g. `task: atlasTextToImage · aspectRatio: 16:9 · enhancePrompt: true · numSamples: 4 · returnDepth: false`.
3. **Camera plan** — only for posed tasks: a short list of target poses relative to the posed source camera (e.g. "8 targets, +0.05 m X each, yaw constant"), intrinsics policy, and `coordinateSystem`. Keep it out of the prompt.

If the user is building an API call, give JSON with only documented fields for that task.

## Things That Will Break the Request

- `numSamples` above 4 (a guide example shows 16; the schema caps at 4) · `aspectRatio` outside `16:9 9:16 4:3 3:4 1:1`.
- Target cameras that are not 1280 × 720 for `atlasGenerate`, `atlasChisel`, `atlasMasked`; context cameras of mixed sizes in `atlasGenerate`.
- `returnDepth: true` with all cameras sharing one centre (pure rotation) — add translation.
- Resizing or cropping an image without updating its intrinsics (and its depth/mask).
- An RGB/RGBA mask, or a mask off the image's pixel grid.
- Overlapping view frusta between independently posed creative images.
- World API v1 / Marble 1.x shapes (`world_prompt`, `text_prompt`, `marble-1.1`) sent to v2 tasks — rebuild, don't rename.
- Video fields (`duration`, `fps`, `motionIntensity`, `pan`) — not in any public schema.

## Iteration Workflow

1. Concept: `atlasTextToImage`, 2–4 samples, enhancement on. Pick the sample with the clearest ground plane and depth layers.
2. Pose it (`images2PosedRGBD`) and inspect depth/camera registration.
3. Generate a **conservative** first path — small translations inside observed space — with depth if outputs will become context.
4. Reject flawed views before they enter context; errors propagate.
5. Continue with `promptUsed` + `enhancePrompt: false` + fixed seed; widen the path only after geometry holds.
6. Store request, cameras, seed, `promptUsed` and assets — operations are kept 30 days.

## Reference Files

- [parameters.md](parameters.md) — every documented field for the six tasks with values, defaults and what is unconfirmed, camera schema, output formats, operations/retention, recommended combinations, World API v1 migration.
- [best-practices.md](best-practices.md) — world-first prompt craft, what to emphasize/avoid, camera moves as pose recipes, focal-length-to-intrinsics, seed-image composition, enhancement strategy, common-mistakes table.
- [input-modes-and-continuity.md](input-modes-and-continuity.md) — posing photos vs creative images, context curation, `promptUsed` reuse, character/prop consistency, multiview masked edits, blockout-to-environment, multi-shot workflow, early-access video status.
- [examples.md](examples.md) — 10 annotated examples: concept seed, landscape, character-as-scale-anchor, action-as-state, single-image push-in, orbit, reveal, multishot continuity, depth-guided blockout, masked replacement.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
