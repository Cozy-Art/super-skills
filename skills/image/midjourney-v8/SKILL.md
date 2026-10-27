---
name: midjourney-v8-prompts
description: "Generate optimized prompts for Midjourney V8 (V8.1 and the current default V8.2), including the V8.2 Edit model and image-to-video handoff. Use whenever a user mentions Midjourney, MJ, V8, V8.1, V8.2, --v 8.2, /imagine, the Midjourney web Imagine bar or Discord, or wants Midjourney stills, style references (--sref, codes, moodboards, --p profiles), HD 2K renders, seamless tiles, editing/inpainting/outpainting with up to 4 reference images, character continuity across shots, or animating a Midjourney image (--motion, --loop, --end). Also use when migrating V6/V7 prompts, since --q, --oref, --cref, :: multi-prompts, Draft and Turbo do not work on V8.1/V8.2. Do not guess Midjourney V8 syntax from general knowledge or older versions."
---

# Midjourney V8 — Prompt Generation Skill

Midjourney V8.2 (default since July 24, 2026) is a still-image model that rewards longer, specific natural-language prompts. V8.1 remains selectable; V8.0 alpha is gone. Editing, multi-image references, inpaint/outpaint and retexture all live in the **V8.2 Edit model**. Video is a separate image-to-video step.

**Midjourney is the exception to "settings outside the prompt":** its controls are inline `--parameters` typed at the end of the prompt string. That is correct, required syntax — keep them in the prompt block. Still give the separate settings summary line (see Output Format).

## The Three Rules That Override Everything

1. **Describe the picture, not its quality.** Subject → action → setting → framing → light → medium. No "masterpiece", "8K", "ultra detailed" — spend words on things the camera sees.
2. **Parameters go last, cleanly.** Space before every `--`, two unbroken hyphens, no commas or periods inside or after parameters, no description text after them.
3. **V8 is not V7 with a new number.** `--q`, `--oref`/`--ow`, `--cref`/`--cw`, `::` multi-prompts, Draft mode, Turbo and Niji are **incompatible** with V8.1/V8.2. Use `--hd`, the Edit model and plain-language priority instead.

## Prompt Order

| # | Layer | Example |
|---|---|---|
| 1 | Subject + defining traits | "a retired watchmaker, late seventies, silver buzz cut, tortoiseshell glasses" |
| 2 | Action / relationship | "leans over a scarred bench, loupe raised to his right eye" |
| 3 | Setting | foreground / midground / background, era, weather |
| 4 | Composition + camera | shot size, angle, lens, depth of field, subject placement |
| 5 | Light + palette | source, direction, hardness, 2–4 colour families |
| 6 | Medium / style / mood | "documentary photograph", "two-colour risograph" |
| 7 | Exact text | `the headline "NIGHT SIGNAL" across the top` |
| 8 | Parameters | `--ar 4:5 --raw --s 100 --v 8.2` |

```
[subject + traits], [action], [setting], [composition + lens], [light + palette], [medium + mood] --ar W:H [--raw] --s N [--c N] [--hd] --v 8.2
```

**Length (practical, no official max):** simple 10–30 words · editorial 40–90 · complex multi-subject 80–150. Keep descriptive text under ~1,024 characters — some API resellers enforce that limit upstream.

## Decide the Operation First

| User wants | Tool / syntax | Prompt pattern |
|---|---|---|
| New image from text | Imagine bar / `/imagine` | Full layered description + params |
| Same *look* as an image or code | `--sref URL\|code` (+ `--sw`) | Describe content; sref carries colour/medium/light |
| Personal aesthetic | `--p` / `--p code` (profile or moodboard) | Normal prompt; raise `--s` to feel it |
| Composition/colour influence | Image prompt URL(s) first + `--iw 0–3` | URL, then text, then params |
| Same person/object in a new scene | **V8.2 Edit** with 1–4 references | "Use the woman from the reference…" + identity clause |
| Change one thing in an image | Edit → instruction or inpaint region | Change / Keep / Look |
| Extend the canvas | Edit → outpaint (Pan/Zoom Out route through Edit) | Describe what fills the new area |
| Seamless pattern | `--tile` | Describe a surface motif, not a scene |
| Final 2K still | `--hd` (or HD toggle) | Same prompt; HD is a re-render |
| Animate a still | Video (`--video` on Discord, Animate on web) | Describe motion only + video params |

## Quick Syntax Reference

- **Version:** `--v 8.2` (or `--v 8.1`). Lock it when reproducibility across default changes matters.
- **Aspect:** `--ar 16:9` integers only (`139:100`, not `1.39:1`). Max 14:1 in SD, 4:1 in HD.
- **Core dials:** `--s 0–1000` (100) · `--c 0–100` (0) · `--w 0–3000` (0) · `--exp 0–100` (0) · `--raw` · `--seed 0–4294967295`.
- **Resolution:** `--sd` (1024px, default) / `--hd` (2048px native). HD ≈1.3 GPU-min vs 0.8 for SD.
- **Exclusions:** `--no cars text crowds` — a parameter, not prose.
- **Text:** put the exact words in double quotes; keep copy short.
- **Style:** `--sref URL1::2 URL2::1` (weights inside sref are fine), `--sref random`, `--sw 0–1000` (100).
- **Edit (Discord):** `--edit URL` · web: drag images to the prompt bar or click **Edit** in the lightbox.
- **Video:** `--motion low|high` · `--raw` · `--loop` · `--end URL` · `--bs 1|2|4`.

Full table, presets and migration → [parameters.md](parameters.md).

## Output Format (always two parts)

1. **Prompt** — one code block containing the prompt text **with its inline parameters at the end**, exactly as it should be pasted. For image prompts, put image URLs first.
2. **Suggested settings** — one line summarising the parameters *and* anything that lives outside the string: e.g. `Settings: V8.2 · 4:5 · Raw · stylize 100 · chaos 3 · SD for drafts, --hd for final · personalization off · attach: none`.

For Edit jobs, give the instruction text in the code block and list the attached references (in order, with roles) on the settings line. For video, give the motion prompt + video params in the block and name the start frame on the settings line.

## Things That Will Break the Request

- Parameters mid-prompt, punctuation on parameters (`--ar 16:9,`), spaced dashes (`- - ar`), decimal ratios.
- On V8.1/V8.2: `--q`/`--quality`, `--oref`, `--ow`, `--cref`, `--cw`, `::` multi-prompt weights, `--draft`, `--turbo`, `--niji` (switches model). These error or silently do nothing — remove them.
- Image-gen parameters on a video job (only `--motion --raw --loop --end --bs` apply); sref, image prompts and Edit references with video.
- Image-only prompts (no text) with `--s` or `--w`.
- `--sw`/`--sv` together with moodboards.
- Non-public URLs for `--sref`, `--end`, image prompts.

## Iteration Workflow

1. Draft in SD with `--c 0–10`, moderate `--s`. Change one dial at a time.
2. Explore wording with `{a, b}` permutations or `--r` (plan-dependent), not by rewriting everything.
3. Pick a keeper → Vary / Remix rather than re-rolling.
4. Lock style with **one** system (one sref set, one profile or one moodboard).
5. Lock identity with the Edit model + a verbatim identity clause; seed is only a noise start.
6. Fix local defects with inpaint; extend with outpaint.
7. Final: `--hd` (or "Run batch as HD") for 2K; upscalers work on SD images only.
8. Animate only approved stills; start `--motion low --raw --bs 1`.
9. Log prompt, version, params, sref/profile codes, seed, references and parent job.

## Reference Files

- **[parameters.md](parameters.md)** — every parameter with ranges/defaults, V8 compatibility matrix, aspect/HD specs, video specs and GPU costs, presets, V7→V8 migration.
- **[best-practices.md](best-practices.md)** — detail level, hierarchy, composition, camera language for stills, typography, `--no`, style systems, common-mistakes table.
- **[continuity-and-references.md](continuity-and-references.md)** — character bibles, Edit-model reference workflow, style locks, storyboard/multi-shot sequencing, seed use, video handoff.
- **[examples.md](examples.md)** — 11 annotated prompts: portrait, keyframe, landscape, action, product, poster, tile, sref exploration, edit, continuity shot, video.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
