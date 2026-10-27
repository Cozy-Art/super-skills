# World Labs Atlas — Best Practices

## 1. Divide every intent by channel

| Intent | Channel | Why |
|---|---|---|
| Environment, materials, light, weather, style | Prompt text | Semantic appearance |
| Exact framing and movement | `targetCameras` | Pose is first-class state, not language to decode |
| Layout and geometry | Posed depth / RGBD context | Depth fixes surfaces and scale |
| Character or prop identity | Posed reference views | Visible evidence beats repeated adjectives |
| Replace or remove an object | `atlasMasked` masks + instruction | Mask says where; text says what |
| Long continuity | Accepted RGBD keyframes + `promptUsed` + seed | Scene state outlasts a paragraph |

If a sentence in the prompt is doing a camera's job ("the camera slowly orbits…"), move it to the camera plan.

## 2. Prompt a world

- **One place.** A coherent, navigable environment — not unrelated subjects arranged like a poster.
- **Layout first.** Enclosures, openings, paths, levels, adjacency, left/right, foreground/midground/background.
- **Surfaces.** Ground or floor, walls, ceiling or sky, vegetation — and their condition (wet, worn, cracked, polished).
- **Depth cues.** Receding paths, overlapping structures, visible corners, near geometry for parallax, a distant boundary.
- **Light.** Source, direction, time of day, colour temperature, weather; volumetrics only where meaningful.
- **Scale.** Dimensions or familiar anchors — "a thirty-meter ribbed-concrete hall", "knee-high wet grass" — so the model doesn't default to room scale.
- **Viewpoint (text-to-image only).** Wide or medium, eye/waist/aerial height, sightline. For posed tasks the camera is geometry, not words.

World Labs' own guidance: "Higher detail prompts lead to better generations." Detail means detail that changes geometry or material behaviour — not adjectives.

**Translate mood into visible controls.** "Epic" → monumental scale, low horizon, hard backlight, haze, sparse human scale cues, long sightline. "Cozy" → low ceiling, warm practicals, soft fabric, close walls.

## 3. What to avoid

- **Close-up people, character-only seeds, crowds** — models are "not yet as strong on humans or dynamic objects." Use a figure as a small scale/story anchor.
- **Motion in the seed.** "Crowds, close-up people, articulated motion, vehicles in motion" are weak. Imply action through *state*: steam, debris direction, wet surfaces, beacons.
- **Prominent text, logos, UI, borders, split screens, collages.**
- **Weak images:** blur, heavy compression, darkness, blown highlights, mixed exposure or white balance, heavy occlusion, unrelated locations in one request.
- **Bad capture:** zooming, auto-exposure shifts, shaky handheld, things moving during capture.
- **Overlapping frusta between independently posed creative images** — "Independently posed creative images must have non-overlapping camera views." Overlap is only allowed for views reconstructed together from one real place, or views Atlas generated.

## 4. Seed-image composition

A good seed is a wide or medium view with a readable ground plane, vertical structures, clear corners and at least three depth layers. Put something near the camera for parallax and keep travel corridors open — the camera will need somewhere to go. Avoid filling the frame with one close object.

## 5. Camera moves as pose recipes

Start from the posed source camera, keep intrinsics constant, and move in small steps inside observed space. World Labs' quickstart moves 0.25 m along world X; its guide shows a 20° right yaw with −0.25 X. These are examples, not limits. Metric scale is *predicted*, so treat metres as approximate.

| Move | Pose recipe |
|---|---|
| **Truck** | Translate along camera right; orientation fixed (or re-aimed at a fixed look-at point). |
| **Dolly / push-in** | Translate along the viewing direction; keep the first move short. |
| **Pedestal / crane** | Translate up/down; adjust pitch to hold the subject. |
| **Pan / tilt** | Rotation only — fine for views, but add a little translation if you want depth back. |
| **Orbit** | Targets on a constant-radius arc, every camera aimed at one look-at point. |
| **Reveal** | Start behind near occlusion, translate sideways/up into a clear sightline, then yaw toward the subject. |
| **Parallax pass** | Modest lateral translation with strong near foreground and a distant subject. |
| **Establishing → detail** | Validate a wide first, then move closer using accepted RGBD outputs as added context. |

**Smoothness = more targets with smaller deltas**, not prose. **Speed** = distance per target. There is no `motionIntensity`.

## 6. Lens → intrinsics

The frame grid is 1280 × 720 on current tasks, so a lens choice becomes `fx`/`fy`:

`fx = focal_mm × 1280 / sensor_width_mm` · `fy = fx` (square pixels) · `cx = 640` · `cy = 360`

| Lens (36 mm-wide sensor) | fx ≈ | Horizontal FOV ≈ |
|---|---|---|
| 18 mm | 640 | 90° |
| 24 mm | 853 | 74° |
| 35 mm | 1244 | 54° |
| 50 mm | 1778 | 40° |
| 85 mm | 3022 | 24° |

For other sensors, use the sensor's width in the formula. Keep intrinsics constant across a move unless you intend a zoom; a zoom with no translation adds no parallax.

## 7. Enhancement strategy

| Situation | `enhancePrompt` | Write |
|---|---|---|
| New concept, ordinary prose | `true` | the 6-layer description |
| Continuing the same scene | `false` | the earlier `promptUsed`, verbatim |
| Exact wording matters / reproducible set | `false` | a complete caption of the finished scene |
| `atlasMasked`, enhancement on | `true` | an instruction: add / remove / replace / restyle, located by visible landmarks |
| `atlasMasked`, enhancement off | `false` | the whole finished scene as a caption |

Always read `promptUsed` — it shows how Atlas interpreted you. If it drops something load-bearing, add it to your text.

## 8. Common mistakes

| Mistake | Symptom | Fix |
|---|---|---|
| Camera verbs in prose | Path ignored or approximate | Encode the path as target poses |
| Object list, no relationships | Right ingredients, incoherent space | Add layers, adjacency, paths, boundaries |
| Mood-only prompt | Generic scene | Convert to scale, palette, light, weather, materials |
| Resize with old intrinsics | Warped geometry, misregistered depth | Transform RGB, depth, masks and intrinsics together |
| Pure rotation + `returnDepth` | Rejected, or depth scale 0 / NaN | Add translated camera centres |
| Big first move | Invented, smeared regions | Small deltas inside observed coverage |
| Flawed view promoted to context | Errors compound | Review every view before reuse |
| Prompt rewritten per shot | Style/material drift | Reuse `promptUsed`, enhancement off |
| Too many weak references | Conflicting geometry/appearance | Fewer, sharper, consistently lit views |
| Removal not stated in masked edit | Object returns | "Remove the …", mask fully covers it + margin |
| `numSamples: 16` | 422 | 1–4 |
| v1 `world_prompt` on v2 | 422 | Rebuild for the task schema |
