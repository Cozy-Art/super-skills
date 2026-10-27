---
name: flux-3-image-prompts
description: Generate optimized prompts and API payloads for Black Forest Labs' FLUX 3 Image model (endpoint /v1/flux-3-image). Use whenever a user mentions FLUX 3, Flux 3, flux-3-image, or BFL's newest image model, or wants text-to-image, multi-reference compositing (up to 10 images), natural-language editing, prompt-embedded bounding-box layouts, exact typography, or 4K stills from Black Forest Labs — including on fal.ai or Replicate. Also use when migrating FLUX.2 / FLUX.1 payloads to FLUX 3, since seed, guidance, steps, width/height and negative_prompt no longer exist and will be rejected. Do not guess FLUX 3 syntax from FLUX.2 habits.
---

# FLUX 3 Image — Prompt Generation Skill

FLUX 3 Image is one endpoint that generates, edits, restyles and composites. There is **no mode field**: what you send in `images` plus what the prompt says determines the operation. It is not a renamed FLUX.2 — the control surface is different.

**Scope:** stills only. Duration, audio, keyframes and camera paths belong to FLUX 3 Video (separate model).

## The Three Rules That Override Everything

1. **Describe the finished image in sentences.** Connected prose that states relationships beats keyword soup. No "masterpiece", "8K", "best quality" — describe visible evidence instead.
2. **Say what IS there, never what isn't.** There is no `negative_prompt`. "An empty promenade" — not "no crowds".
3. **Continuity lives in images, not seeds.** There is no `seed`. To keep anything (a face, a composition, a draft you liked) feed the approved image back in `images` and assign it a role.

## Prompt Order

Most important constraint first. Default order:

| # | Layer | Example |
|---|---|---|
| 1 | Image type / medium | "A 35mm film still", "A two-color lithograph poster" |
| 2 | Subject + action | identity traits, pose, expression, relationships |
| 3 | Setting | foreground / mid / background, weather, spatial layers |
| 4 | Lighting | source, direction, quality, colour, what it lands on |
| 5 | Framing + camera | shot size, angle, lens, depth of field, focus plane |
| 6 | Style, palette, effects | era, film stock, palette (hex OK), grain, blur |
| 7 | Exact text / layout | quoted copy + placement; bounding-box JSON if needed |

```
[IMAGE TYPE]. [SUBJECT + ACTION]. [SETTING + RELATIONSHIPS].
[LIGHT SOURCE + EFFECT]. [SHOT SIZE + ANGLE + LENS + FOCUS].
[STYLE + PALETTE + MATERIALS + EFFECTS]. [QUOTED TEXT + PLACEMENT].
```

For portraits, put shot size and identity first so the model doesn't pull back to a wide.

**Length targets (practical, not official — no documented max):** simple object 15–50 words · directed scene 50–120 · multi-subject 100–220 · poster/typography 100–300 + copy · bbox layouts: caption + JSON.

## Decide the Operation First

| User wants | `images` | Prompt pattern |
|---|---|---|
| New image from text | none | Full 7-layer description |
| New image, consistent character/style | 1–10 refs | "Use the person from image 1, the coat from image 2…" + roles |
| Edit an existing image | that image first | One conceptual change + preserve list |
| Place things precisely | optional | Caption with `<id>` tags + JSON box array |
| Move/remove/replace one element | source image | Edit rows with `from`/`src_bbox`/`tgt_bbox` |
| Factual place/product/event | optional | Keep `grounding: true` |

## Special Syntax (Quick Reference)

- **Visible text:** quote it — `a sign reads "NIGHT MARKET" in condensed cream sans-serif`. Keep copy short, state placement, type character, colour.
- **References in prose are 1-based:** "image 1", "image 2". Put the base scene/identity master first — `aspect_ratio: "auto"` follows image 1.
- **References in boxes are 0-based:** `ref_image_0`, `ref_image_1`.
- **Bounding boxes:** `[top, left, bottom, right]`, integers 0–1000 from top-left, grid stretches with aspect ratio. Tag elements inline as `<name_N>`.

Full syntax, edit-row operations and the `kind` field → [best-practices.md](best-practices.md).

## Output Format (always two parts)

When producing a prompt for the user, return:

1. **Prompt** — in a code block, prompt text only. Never put aspect ratio, resolution or other API settings inside the prompt text.
2. **Suggested settings** — one line, e.g. `aspect_ratio: 4:5 · resolution: 2k · grounding: false · images: [identity master]`

If the user is building an API call, also give the JSON payload with only valid fields (`prompt`, `images`, `aspect_ratio`, `resolution`, `safety_tolerance`, `grounding`, `version`).

## Fields That Will Break the Request

The native schema rejects unknown fields (HTTP 422). Never send: `negative_prompt`, `seed`, `guidance`, `steps`, `width`, `height`, `input_image`, `input_image_2…`, `mode`, `output_format`, `output_quality`, `prompt_upsampling`. Wrappers (fal, Replicate) may add their own — those are platform-specific, not BFL.

## Iteration Workflow

1. Draft at `768sq` or `1k`, `grounding: false` for fiction.
2. Read `result.prompt` in the response — it shows how FLUX 3 expanded your prompt; fix the wording gap it reveals.
3. Lock the approved draft by **downloading it** (result URLs expire after ~1 hour).
4. Final at `2k`/`4k` with the approved draft as image 1 — changing resolution alone is a new roll and composition may shift.
5. Edits: one conceptual change per request; branch from the cleanest master, not a long chain of edits.

## Reference Files

- **[parameters.md](parameters.md)** — every native API field, aspect ratios, resolution tiers, recommended combinations, response/polling, FLUX.2 migration table.
- **[best-practices.md](best-practices.md)** — detail level, positive language, composition by shot type, camera language for stills, typography, bounding-box layouts and edit rows, common mistakes table.
- **[continuity-and-references.md](continuity-and-references.md)** — identity masters, multi-reference role assignment, style lock blocks, storyboard/multi-shot sequencing, handoff to FLUX 3 Video.
- **[examples.md](examples.md)** — annotated prompts: portrait, environment, frozen action, motion aesthetic, poster/typography, character continuity, boxed layout, local edit, migration payload.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
