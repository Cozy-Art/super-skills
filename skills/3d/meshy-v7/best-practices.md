# Meshy 7.1 — Best Practices

## 1. What a Geometry Prompt Is For

Meshy reads the `prompt` as a description of **one physical object's shape**. Everything that isn't form — camera, lens, lighting, mood, background — is either ignored or leaks in as unwanted geometry (a "dramatic sunset" can become a base plate). Official formula: **subject → material/texture → art style → technical constraints**, most important first.

Spend words on:
- **Identity:** object type, function, era.
- **Silhouette:** overall proportions, major volumes, thick vs thin parts, openings.
- **Signature features:** 2–4, concrete and countable ("two side valves", "four short thrusters").
- **Construction materials** that change shape: planks, plates, rivets, stitching, scales.
- **One style:** "grounded dieselpunk realism", "chibi vinyl toy", "low-poly stylized" — never three.
- **Technical intent:** "single unified object", "watertight", "game-ready", "clean edges", "A-pose".

## 2. Geometry Prompt vs Texture Prompt

| Put in geometry `prompt` | Put in `texture_prompt` |
|---|---|
| "thick oak planks with iron bands" (the bands are raised) | "dark weathered oak, rust bleeding from bolts" |
| "layered ceramic armour plates over mechanical joints" | "glossy white ceramic, scuffed edges, graphite joints" |
| "flattened oval hull, folded manipulator arms" | "matte safety-yellow paint, white serial markings, salt crust" |

Texture prompt pattern (10–40 words):
```
[BASE MATERIAL + COLOUR], [SECONDARY MATERIALS], [MARKINGS/PATTERN],
[WEAR + WHERE IT SITS], [ROUGHNESS/FINISH].
```
State hex colours or named paint finishes when matching an existing library. Don't describe scene lighting — with `enable_pbr` the renderer lights it.

## 3. Templates by Asset Type

| Asset | Template |
|---|---|
| Prop | `A [object], [shape], [2–3 features], [material construction], [style], single unified object.` |
| Hard-surface vehicle/device | `A [vehicle], [hull shape], [count + parts], [panelling], hard-surface [genre] design, single watertight asset.` |
| Rig-ready character | `A full-body [character], [body proportions], [head/face feature], [costume construction], [style], symmetrical A-pose, separated arms and legs, rig-ready.` |
| Stylized character | `A [creature/character], [exaggerated proportions], [silhouette feature], [accessory ≤2], [shading style], T-pose, clean readable silhouette.` |
| Environment module | `A single [module], [footprint + height], [structural parts], [surface carving/wear], [style], modular environment asset, solid unified construction.` |
| Display sculpture | `A [subject] captured [moment], [stance], [key limb positions], [material], collectible-statue composition, sturdy connected forms.` |
| Print part | `A [object], [dimensions/proportions], solid watertight construction, thick walls, no thin overhangs, single printable piece.` |

## 4. Geometry Resolution Choice

| Tier | When |
|---|---|
| `standard` | Ideation, distant/background assets, anything that will be remeshed hard |
| `2k` (Ultra) | Production balance; ceiling for Multi-Image |
| `4k` (Ultra) | Detail that must exist as geometry: engraving, scales, stitching, wrinkles, reliefs; sculpt/print work. Raw meshes can be very heavy (up to ~80M tris before simplification per Meshy) — budget for decimation |

Lock the shape at `standard` before paying for Ultra.

## 5. Preparing Image References

Single image (Image to 3D):
- One subject, 70–90% of frame, plain or transparent background, ≥1024×1024 (512 minimum).
- Front or three-quarter view, near-orthographic/telephoto — wide-angle distorts proportions.
- Even diffuse light; no hard cast shadows, watermarks, text overlays, motion blur.
- Avoid transparent, mirror-chrome and effect-heavy subjects.
- Clean renders → `image_enhancement: false`; ordinary photos → leave `true`.

Multi-view (Multi-Image to 3D):
- Same object, pose, proportions, scale and lighting in every view.
- Image 1 = front. Others: side, back, opposite side or three-quarter.
- Fixed camera height and distance; rotate the object, not the camera.
- Three consistent views beat four inconsistent ones — a bad view lowers coherence.

When generating a 2D concept for conversion (in any image model), prompt for: "front view, orthographic, neutral even lighting, plain white background, full object in frame, 1:1". Those words belong in the **image** prompt, not the Meshy prompt.

## 6. Characters & Rig-Readiness

- Use `pose_mode: "a-pose"` (or `t-pose`) **and** say it in the prompt.
- Separated limbs, visible hands and feet, no capes/long coats fused to legs, no weapons in hand.
- Hair as sculpted volume ("short swept-back sculpted hair"), not strands.
- Accessories ≤2 and attached ("backpack integrated into the torso"); add the rest as separate props.
- Rigging needs a **textured** humanoid ≤300k faces facing +Z — remesh before rigging.

## 7. Motion Prompts (Text to Motion)

One action, body mechanics, sequence, ending state. ≤400 chars.
```
The character [ACTION 1], [weight shift / limb detail], [ACTION 2],
[landing or recovery], and [ends in STATE].
```
- Set `duration` to fit the action (2–10 s). Too long → padding/idle; too short → rushed.
- No camera, no environment props beyond implied contact ("waist-high obstacle" is fine as a mime target).
- Describe energy in verbs ("shambles", "springs") — there is no intensity field.

## 8. Retexture Prompts

`text_style_prompt` is a full surface brief for an existing mesh. Name the material system and palette; say what changes and what each region becomes ("helmet shell becomes oxidised copper, visor smoked glass, straps black leather"). For skin variants of one asset, keep the structure of the prompt identical and swap only palette/material nouns.

## 9. Things Meshy Can't Do Well

Smoke, fire, fog, energy wisps, individual hair strands, thin wires/chains, glass interiors, text/logos as geometry, multiple separate objects, full scenes, terrain. Fake effects in the engine; model chains/wires by hand; add decals in texturing.

## 10. Common Mistakes

| Mistake | Result | Fix |
|---|---|---|
| Scene prompt ("a knight in a castle courtyard") | Fused base/blob | One asset; build the scene downstream |
| Multiple subjects or "a set of" | Merged characters/props | One task per asset |
| Camera/lens/lighting words in geometry | Wasted tokens, odd bases | Move to renderer; surface info to texture prompt |
| Vague praise ("epic", "highly detailed") | Generic mesh | Concrete silhouette + countable features |
| Key feature late in prompt | Feature missing | Move right after the subject |
| Contradictory styles | Incoherent surfaces | One geometry language, one material system |
| Long "no X, no Y" lists | Ignored or inverted | Positive construction: "single unified watertight form" |
| Many loose accessories | Floating parts | Fewer, attached accessories; separate props |
| Dynamic pose for a rig | Rigging fails / bad weights | A/T-pose master; pose via animation |
| Texture image of a different shape | Mismatched texture | Texture ref must match geometry |
| `texture_prompt` + `texture_image_url` together | Image silently ignored | Send one |
| Ultra 4K on Multi-Image | Error | Max `2k` there |
| Remeshing the only copy | Fine detail lost | Keep un-remeshed GLB master |
| Waiting to download | Assets gone after 3 days | Download on `SUCCEEDED` |
| Expecting seeds/negative_prompt | No effect | Chain task IDs; positive phrasing |
