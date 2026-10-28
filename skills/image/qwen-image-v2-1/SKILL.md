---
name: qwen-image-2-1-prompts
description: Generate optimized prompts and pipeline/API settings for Alibaba's Qwen-Image-2.1 — the open-weight 7B unified text-to-image + image-editing model (QwenImage21Pipeline, checkpoint Qwen/Qwen-Image-2.1) and its hosted sibling qwen-image-2.1-pro (Alibaba Cloud Model Studio, Runware and other APIs). Use whenever a user mentions Qwen-Image 2.1, Qwen Image 2.1, Qwen-Image-2.1-Pro, QwenImage21Pipeline, or wants native 2K stills, exact typography/posters/infographics, native RGBA transparent assets, multi-reference compositing (up to 10 images with <image1> tags), identity/product-preserving edits, or circle/paint/mask-guided local edits — in Diffusers, ComfyUI or a hosted API. Also use when migrating from Qwen-Image, Qwen-Image-Edit/Edit-Plus or Qwen-Image-2.0, since 2.1 is one pipeline with 40 steps and CFG off by default. Do not guess Qwen-Image-2.1 syntax from older Qwen-Image versions or general knowledge.
---

# Qwen-Image-2.1 — Prompt Generation Skill

Qwen-Image-2.1 is **one pipeline** that generates and edits: no `image` = text-to-image; one image or an ordered list (up to 10) = editing / compositing. 7B single-stream DiT conditioned by Qwen3-VL 8B, with a 64-channel **RGBA** VAE — transparency is native. Stills only: no duration, FPS, motion or camera-path controls.

## The Three Rules That Override Everything

1. **Two grammars.** Text-to-image prompts *describe the finished frame as an observer* (present tense, declarative, spatial). Edit prompts are *imperative and surgical*: operation → target → result → one broad preservation clause.
2. **CFG is off, so negatives are dead.** Default `true_cfg_scale=1.0` ignores `negative_prompt` entirely. Write positive descriptions of what fills the space; only enable CFG (>1) as a tested experiment.
3. **Multi-image = `<image1>`, `<image2>`… with a role for every image.** List order is the order the model reads. Point to the reference for identity instead of redescribing a face in words.

## Prompt Order (text-to-image)

| # | Layer | Example |
|---|---|---|
| 1 | Medium + orientation + shot | "A vertical cinematic portrait photograph", "A modernist screen-printed poster" |
| 2 | Hero subject + action | who/what, pose, expression, wardrobe, key prop |
| 3 | Spatial walk | foreground / middle / background; upper-left, lower third, right edge |
| 4 | Camera | height, angle, lens character, depth of field, focus target |
| 5 | Lighting | source, direction, hardness, colour temperature, shadows |
| 6 | Materials + palette | named colours, surfaces, wear, translucency |
| 7 | Exact text | every string in straight double quotes + position, size, weight, colour |
| 8 | Closing sentence | "The overall composition…" — balance, palette, style, mood |

```
A [orientation] [medium/style] [shot] of [subject + action] in [setting].
[Position, pose, clothing, props]. [Foreground / middle / background].
The camera is [height, angle, lens]; [depth of field]. The lighting is [source,
direction, quality, colour]. [Quoted text + placement]. The overall composition
[balance, palette, mood].
```

**Length (practical, no documented max):** simple subject / small edit 20–80 words · scene 100–250 · poster/infographic/storyboard/UI 250–500 (region by region, every string spelled out). Qwen's official T2I enhancer writes ~20 sentences / 400–500 words — a strategy, not a requirement.

## Decide the Operation First

| User wants | `image` | Prompt pattern |
|---|---|---|
| New still from text | none | Observational paragraph, layers 1–8 |
| Transparent asset (sticker, icon, game sprite) | none | Official RGBA wrapper (below); save PNG |
| Edit one image | that image | "Replace/remove/add/change [target] … Preserve [everything else]." Say "the image", no tags |
| Composite / outfit swap / product placement | ordered list, ≤10 | `<imageN>` tags, one role each, name the canvas |
| Local edit in a marked region | image with circle/paint mark (or mask in supported workflows) | Name the mark + colour, the operation, "remove the annotation", preserve outside |
| Identity-preserving new shot | identity ref first | "The person from <image1>…" + what changes + what holds |
| Outpaint / background swap | source image + new `width`/`height` | Describe the new area; preserve the original subject |

## Special Syntax (Quick Reference)

- **Visible text:** `a large condensed cream headline reads "SIGNAL LOST"` — straight double quotes, exact spelling/case/script; describe a line break as "on a second line". Chart ticks, legends and cell values count as text.
- **Multi-image tags:** `<image1>`, `<image2>` … 1-based, matching list order. Mandatory in Qwen's official edit enhancer. Single image → "the image", no tag.
- **Transparency wrapper (use verbatim):**
  `This is an RGBA image with transparency. <description>. The image has alpha channel and the background is transparent.`
- **No inline syntax:** no weights, brackets, `--ar`, or headings. Ratio, seed, steps, CFG are call arguments.

Full grammar, edit patterns, typography and mistakes table → [best-practices.md](best-practices.md).

## Output Format (always two parts)

1. **Prompt** — in a code block, prompt text only. Never put resolution, aspect ratio, steps or seed inside the prompt (Qwen's own enhancers strip them; "4K" in prose reads as quality intent, not size).
2. **Suggested settings** — one line, e.g.
   `2:3 · width 1696 × height 2528 · steps 40 · true_cfg_scale 1.0 · seed 42 · use_kv_cache on · image: [identity, outfit, scene]`

For Diffusers users also give the `pipe(...)` call; for hosted users (`qwen-image-2.1-pro`) give only that platform's fields.

## Things That Will Break the Request

- **Omitting `width`/`height`** — they fall back to the condition image's ratio at `output_resolution=1024` (≈1 MP), not native 2K. Always pass both from the preset table.
- **`negative_prompt` at CFG 1.0** — silently ignored. **`guidance_scale`** is not the 2.1 keyword (`true_cfg_scale` is). No `strength` argument exists.
- **More than 10 references** — official limit (ComfyUI's encoder node exposes 16 slots; stay at 10).
- **Old pipeline classes** (`QwenImagePipeline`, `QwenImageEditPipeline`, `QwenImageEditPlusPipeline`) or old recipes (`true_cfg_scale=4.0`, 50 steps).
- **Saving RGBA output as JPEG** — alpha is discarded. ComfyUI nodes built for 3-channel images may fail on RGBA; split alpha first.
- **Duration / FPS / camera-path / motion fields** — none exist.
- **Hosted APIs:** `qwen-image-2.1-pro` wrappers typically expose no steps/CFG/negative fields and run prompt extension **on by default** — turn it off when you need your exact wording or reproducibility.

## Iteration Workflow

1. Draft: subject-first prompt, target preset ratio, fixed seed. (Lower steps or ~1 MP only for drafts, after visual check.)
2. Lock the recipe: seed, `width`/`height`, steps, CFG, precision, backend, reference order **and `use_kv_cache`** — toggling the cache changes the sample even with the same seed.
3. Change one variable per run (one prompt clause, one reference, one setting).
4. Final at the official 2K preset, 40 steps, CFG 1.0. Pushing well past 2K (e.g. 4K) loses prompt adherence.
5. Edits: one operation per pass, edit the saved approved frame (PNG), not a fresh text regen. After 3–4 chained edits, rebuild from the master.
6. Optional: run Qwen's PE-T2I / PE-I2I rewriter and read its output to see what the model "wants" — then keep or trim.

## Reference Files

- **[parameters.md](parameters.md)** — full `QwenImage21Pipeline` signature, defaults, official 2K presets, CFG/negative behaviour, ComfyUI settings, hosted `qwen-image-2.1-pro` fields and pricing, specs, migration from older Qwen-Image.
- **[best-practices.md](best-practices.md)** — observational T2I grammar, edit grammar, multi-image roles, typography and layouts, transparency, local/mask edits, action and camera language for stills, common-mistakes table.
- **[continuity-and-references.md](continuity-and-references.md)** — reference ordering, identity packs, style frames, recipe locking, shot manifests, edit chains, video keyframe handoff.
- **[examples.md](examples.md)** — 11 annotated prompts: portrait, environment, action, tracking-shot keyframe, poster, infographic, RGBA asset, single edit, multi-reference composite, marked local edit, API call.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
