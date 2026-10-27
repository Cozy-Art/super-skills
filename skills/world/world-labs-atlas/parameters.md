# World Labs Atlas — Parameters

Marble Developer API v2 beta · base path `/api/v2` · tasks are `POST /api/v2/tasks:<taskName>` and return an **Operation** (poll `GET /api/v2/operations/{id}` or `POST …:wait`). Assets live under `/api/v2/assets`.

*Verified against the Atlas announcement (worldlabs.ai/blog/atlas), the Marble 2 beta docs and API reference (atlas-beta.worldlabs.ai/docs), and docs.worldlabs.ai, October 2026.*

**The live schema is the authority.** Task access depends on your account, and beta requests can change. Validate against the live reference before shipping, and if your account or interface rejects a value below, follow it.

## Surfaces

| Surface | Status (Oct 2026) | Notes |
|---|---|---|
| Atlas partner system | Early access, select partners (request form) | Camera-controlled video from 1–6 images, "up to 1 minute of video at 1440p"; reconstruction from "one to dozens" of images (research examples use 100+); outputs incl. point clouds and 3D Gaussian splats. **No public request schema.** |
| Marble Developer API v2 beta | Account-dependent beta | The six tasks below. |
| World API v1 / Marble 1.x | Public | `POST /v1/worlds/generate`, `world_prompt` objects, `marble-1.x` IDs. Different contract — see migration. |

## Shared request controls (all tasks)

| Field | Where | Values | Notes |
|---|---|---|---|
| `wait` | query | bool, default `false` | Block until done, up to a server cap. |
| `Idempotency-Key` | header | string ≤ 128 | Use one per logical request. |
| `webhookUrl` | body | HTTPS :443, ≤ 2048, no IP literals | One signed `task.succeeded` / `task.failed` event. Not with `?wait=true`. |
| `purgeContentOnOperationCompletion` | body | bool / null | Purges outputs + consumed uploads 1 h after completion; omitted = account setting. |

## `atlasTextToImage`

| Field | Req | Values | Default / notes |
|---|---|---|---|
| `prompt` | ✅ | string, min length 1 | No published maximum. |
| `aspectRatio` | — | `16:9` `9:16` `4:3` `3:4` `1:1` | Falls back to `1:1` when omitted. |
| `enhancePrompt` | — | bool | `true` |
| `seed` | — | integer | Sample *i* uses `seed + i`. With enhancement off, repeating the request reproduces the set. |
| `numSteps` | — | 1–100 | No default published — omit. |
| `numSamples` | — | 1–4 | The guide's `"numSamples": 16` example contradicts the schema; use ≤ 4. |
| `returnDepth` | — | bool | `false`; true adds a depth buffer and the camera it was estimated under. |

Response: `promptUsed`, `aspectRatio`, `frames[]` (`imageAsset`, `camera`, optional `depth` with `logDepthAsset`, `confidenceAsset`, `zMin`, `zMax`).

## `images2PosedRGBD`

| Field | Req | Values | Default / notes |
|---|---|---|---|
| `frames` | ✅ | 1+ images | Each `imageAsset`: project asset ID, public HTTPS URL, or inline base64 < 10 MiB. |
| `targetResolution` | — | `[w, h]` or null | `[1280, 720]` |
| `refinePoses` | — | bool | `false`; needs 2+ frames; adds a matching pass + solve. |
| `canonicalizeToFirstFrame` | — | bool | Shown `false` in the example; behaviour not documented *(unverified)*. |
| `base64Outputs` | — | bool | `false` |

Outputs: posed RGB, linear-depth EXR in world units (half-float), confidence PNG. Metric scale is predicted, so distances are approximate.

## `atlasGenerate` (posed RGBD → new views)

| Field | Req | Values | Default / notes |
|---|---|---|---|
| `contextFrames` | ✅ | posed RGBD: `imageAsset` + `depth` + `camera`, all required | All context cameras share one width/height. No public max — check the live limits. |
| `targetCameras` | ✅ | pinhole cameras, output order | Must use the 1280 × 720 grid. One frame per target. |
| `prompt` | — | string / null | Omit and the enhancer captions the context images. |
| `enhancePrompt` | — | bool | `true` |
| `returnDepth` | — | bool | `false`; rejected when all camera origins are identical. |
| `model` | — | string | Unset = routed by context/target counts. Pin only after evaluating a checkpoint. |
| `modelParameters.seed` | — | integer | Default not published *(research's "42" unverified)*. |
| `modelParameters.numSteps` | — | integer | Omit to use the model's recipe; "the current distilled models use eight denoising steps with guidance baked into their weights." |
| `base64Outputs` | — | bool | `false` |

Outputs: submission-time frames JPEG + half-float EXR depth; later frames PNG + float32 EXR.

## `atlasChisel` (depth-guided)

| Field | Req | Values | Default / notes |
|---|---|---|---|
| `targetCameras` | ✅ | ≤ 32, each 1280 × 720 | |
| `prompt` | ✅ | string, min length 1 | Required even with depth present. |
| `contextFrames` | — | depth-only (`camera` + `depthAsset`/`logDepthAsset`) | Zero, or exactly one per target in target order; 1280 × 720 rasters. Empty = prompt alone. Never send `imageAsset`/`maskAsset`/`confidenceAsset`. |
| `sourceFrames` | — | posed RGB (`imageAsset` + `camera`) | Any size (cover-resized, center-cropped to 1280 × 720); same coordinate convention and scale as targets. |
| rollout cap | — | context + source + targets ≤ 64 views | With depth per target, 4 photos leave room for 30 targets. |
| `enhancePrompt` | — | bool | `true` |
| `voxelSize` | — | ≥ 0; recommended 0–0.4 | Omit/0 keeps raw depth; 0.05–0.15 for blockouts. |
| `voxelGridOrientation` | — | `world` / `gauge` | `world`; ignored unless `voxelSize` set. |
| `modelParameters` | — | object | Reference lists `returnDepth` (bool, default `false`, needs 2+ targets with distinct centres); the guide also mentions optional `seed` / `numSteps` overrides. Place `returnDepth` where your live schema shows it. |

## `atlasMasked` (multiview inpainting — account-gated)

Requires task access; "not part of the default external beta surface yet."

| Field | Req | Values | Default / notes |
|---|---|---|---|
| `contextFrames` | ✅ | image + mask + camera, output order | Practical target 1–16 well-overlapped views. |
| `targetCameras` | ✅ | one per context frame, same index | Mismatched counts/poses accepted but degrade. Exactly 1280 × 720. |
| `prompt` | — | string / null | Enhancement on: an edit instruction. Off: a caption of the whole finished scene. Empty prompts tend to restore masked objects. |
| `enhancePrompt` | — | bool | `true`; result returned as `promptUsed`. |
| `returnDepth` | — | bool | `false`; needs 2+ targets, distinct centres. |
| `modelParameters` | — | object | Properties not published *(research's seed 42 / numSteps 50 unverified)*. |
| mask | ✅ | 8-bit grayscale PNG, same pixel grid | Keep = 255 (reference wording: "1 is kept"), fill = 0, gray = soft transition. RGB/RGBA rejected even if gray-looking. |

## `splats2Mesh`

Converts an existing Gaussian splat scene to a GLB mesh, optionally textured or vertex-coloured. No prompt.

## Cameras

| Part | Fields | Rule |
|---|---|---|
| Intrinsics | `fx` `fy` `cx` `cy` `width` `height` | Pixels, not normalized. |
| Extrinsics | `position`, `quaternion` (XYZW, unit), `coordinateSystem` | **Camera-to-world**. `rub` = right/up/back, looks −Z (OpenGL/Three.js/Blender camera); `rdf` = right/down/forward, looks +Z (OpenCV). Changing the string does not convert a pose. Marble outputs `rub` unless the schema says otherwise. |
| Frame | — | One world frame, one distance unit per request. |
| Resize/crop | — | Scale `fx`,`cx` by the width ratio and `fy`,`cy` by the height ratio; subtract crop offsets from `cx`,`cy`; apply the same transform to depth and masks. |

## Operations

- Operation, trace and terminal response are kept **30 days** after acceptance; output assets stay in the project library until deleted (unless purge is on — then 1 hour).
- `done` is the only completion signal. Poll with capped exponential backoff + jitter.
- `expiresAtSecs` is a task deadline, not a URL expiry.

## Recommended Combinations

| Goal | Configuration |
|---|---|
| Fast concept | `atlasTextToImage` · `16:9` · enhancement on · 2–4 samples · default steps · no depth |
| Reproducible variants | same prompt · `enhancePrompt: false` · fixed seed · change one clause |
| Single-image camera move | `images2PosedRGBD` → `atlasGenerate` · small translated targets · `returnDepth` only if outputs become context |
| Faithful place | several sharp overlapping translated photos · stable exposure · `refinePoses: true` · targets inside coverage |
| Blockout → environment | `atlasChisel` · depth per target · `voxelSize` 0.05–0.15 · `world` grid · posed source photos for appearance |
| Object replacement | `atlasMasked` · edited anchor first with all-white mask · 1–16 views · paired cameras |

## Migration from World API v1 / Marble 1.x

| v1 | v2 beta |
|---|---|
| `POST /v1/worlds/generate`, one persistent world | composable tasks: pose → generate views → (depth) → edit |
| `world_prompt: {type: "text", text_prompt}` | top-level `prompt` per task |
| `model: marble-1.1` (omitted = `marble-1.0` today) | `atlasGenerate` routes automatically; `atlasChisel` has no selector |
| `disable_recaption` | `enhancePrompt: false` |

"Older World API v1 and Marble 4 examples are not compatible contracts." Rebuild requests per task schema; don't rename fields.
