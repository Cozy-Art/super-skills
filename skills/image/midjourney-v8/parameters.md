# Midjourney V8 — Parameters

Interfaces: midjourney.com Imagine bar (pills + settings panel), alpha.midjourney.com, Discord `/imagine`. Parameters are typed **inline at the end of the prompt**; most also exist as UI toggles/pills. The settings panel (web) or `/settings` (Discord) sets defaults that apply when a parameter is omitted.

*Verified against docs.midjourney.com (Version, Parameter List, Quality, Image Prompts, Style Reference, Video, Multi-Prompts) and updates.midjourney.com (V8 Alpha, V8.1 default, Version 8.2, Edit Model for V8, Sept 24 edit updates, Aug 20 changelog), October 2026.*

## Versions

| Version | Status (Oct 2026) | Notes |
|---|---|---|
| V8.2 | **Default** since Jul 24, 2026 | Stronger aesthetics, fewer low-quality results, better personalization taste modelling |
| V8.2 Edit model | Public test since Aug 27, 2026 | Instruction edits, up to 4 image references, inpaint/outpaint; replaces Omni Reference, Character Reference and Retexture |
| V8.1 | Selectable (default Jun 10 – Jul 23) | Introduced HD/SD; ~4 s SD, ~12 s HD at launch |
| V8.0 alpha | Removed | Images remain in gallery |
| V7 | Selectable | Only place Omni Reference (`--oref`), `--q` and Draft still work |

## Formatting Rules

- Parameters after all descriptive text; space before each `--`; no space between the dashes.
- No commas, periods or other punctuation inside or after parameters.
- Image-prompt URLs go **first**, before text. `--sref`, `--end`, `--edit` take URLs after the flag. URLs must be publicly reachable.
- Aliases are interchangeable: `--ar/--aspect`, `--s/--stylize`, `--c/--chaos`, `--w/--weird`, `--v/--version`, `--p/--profile`, `--r/--repeat`.

## Still-Image Parameters (V8.1 / V8.2)

| Parameter | Syntax | Range / values | Default | Notes |
|---|---|---|---|---|
| Version | `--v 8.2` | `8.2`, `8.1` (also `7`, `6.1`…) | settings | Lock for reproducibility |
| Aspect ratio | `--ar W:H` | integers only | `1:1` | Max **14:1** in SD, **4:1** in HD |
| SD / HD | `--sd` / `--hd` | flag | SD | SD = 1024px class; HD = 2048px native (no upscale). HD ≈1.3 GPU-min, SD ≈0.8 |
| Stylize | `--s N` | 0–1000 | 100 | Higher = more Midjourney aesthetic, less literal |
| Raw | `--raw` | flag | off | Strips default styling → better adherence; best for photo/product |
| Chaos | `--c N` | 0–100 | 0 | Variety across the grid |
| Weird | `--w N` | 0–3000 | 0 | Unconventional aesthetics; not fully seed-stable |
| Experimental | `--exp N` | 0–100 | 0 | Extra detail/dynamism; values above ~25 can override prompt and sref (range from V7 docs/resellers — confirm on your platform) |
| Seed | `--seed N` | 0–4294967295 | random | Testing tool; V8 seed reruns are ~99% identical. Not an identity lock |
| No | `--no a b c` | text list | — | Visible exclusions |
| Style reference | `--sref URL\|code\|random` | one or more, space-separated; weights `URL::2` | — | Style only (colour, medium, texture, light) — not people/objects |
| Style weight | `--sw N` | 0–1000 | 100 | Not compatible with moodboards |
| Style version | `--sv N` | V7: 1–6 (default 6) | — | V8 values not documented (unverified — confirm on your platform). Not compatible with moodboards |
| Personalization | `--p` / `--p CODE` | profile or moodboard codes | settings | V8 may require unlocking your Global V7/V8 profile |
| Image prompt | `URL [URL] text…` | `.png .gif .webp .jpg .jpeg` | — | Needs text + 1 image, or 2+ images. Crop to target ratio |
| Image weight | `--iw N` | 0–3 | 1 | V8.1 documented; assume same for 8.2 |
| Tile | `--tile` | flag | off | Seamless repeat; seam blending improved Sept 2026 |
| Repeat | `--r N` | plan-dependent | 1 | Multiple grids from one prompt |
| Permutations | `{a, b, c}` | plan/job-limit dependent | — | Batch prompt variants |
| Speed | `--fast` / `--relax` | — | settings | Relax is supported on V8.1/8.2 |
| Visibility | `--stealth` / `--public` | — | plan | Stealth requires Pro/Mega |
| Edit | `--edit URL [URL…]` | up to 4 references | — | Discord form; web uses attach/Edit tab |
| Preview | `--preview` | flag | — | Tests early model versions; not stable over time |

## Incompatible With V8.1 / V8.2

| Parameter / feature | What to do instead |
|---|---|
| `--q` / `--quality` (1/2/4) | `--hd` for detail; Raw + clearer prompt for coherence. (V8.0 alpha had `--q 4`; it's gone) |
| `--oref`, `--ow` (Omni Reference) | V8.2 Edit model references |
| `--cref`, `--cw` (Character Reference) | V8.2 Edit model references |
| `::` multi-prompts / weights | Plain-language priority, order, `--no` |
| Draft mode / `--draft` | SD + low stylize; permutations. (A V8.1 Draft mode was announced in June; the current Version doc lists Draft as incompatible — treat as unavailable) |
| `--turbo` | `--fast` |
| `--niji` | Separate model — switches you off V8 |
| Retexture tool | Edit model |
| Upscalers on HD images | Upscalers apply to SD images only; HD is already 2K |

Pan, Zoom Out and Vary Region run through the Edit model and **downscale HD results to SD** — Upscale to return to HD.

## Aspect Ratio Guide

| Ratio | Best for |
|---|---|
| `1:1` | Icons, album art, tiles |
| `4:5` / `4:3` | Portraits, editorial, product |
| `3:2` | Photography, cinematic stills |
| `2:3` | Posters, covers, fashion |
| `16:9` | Storyboards, keyframes, landscapes |
| `9:16` | Vertical social, character frames |
| `21:9` | Panoramic establishing — validate at 16:9 first; within HD's 4:1 cap |

## Stylize / Chaos / Weird Starting Points

| Intent | `--s` | `--c` | `--w` | Raw |
|---|---|---|---|---|
| Product / UI / literal | 0–50 | 0 | 0 | yes |
| Controlled photo / continuity | 50–125 | 0–5 | 0 | yes |
| Editorial finish | 150–300 | 0–10 | 0 | optional |
| Concept exploration | 300–600 | 10–25 | 0–250 | no |
| Style discovery / profile-led | 600–1000 | 25–60 | 250–1000 | no |

Raise one dial at a time.

## Presets

```
Photoreal portrait     --ar 4:5 --raw --s 75 --c 2 --v 8.2
Cinematic storyboard   --ar 16:9 --raw --s 125 --c 5 --v 8.2
Editorial illustration --ar 3:2 --s 300 --c 12 --v 8.2
Style exploration      --ar 1:1 --s 600 --c 35 --w 500 --v 8.2
Product fidelity       --ar 4:3 --raw --s 25 --c 0 --hd --v 8.2
Continuity keyframe    --ar 16:9 --raw --s 75 --c 0 --w 0 --v 8.2
Directed video         --motion low --raw --bs 1
```

## Video (Image-to-Video)

Every video starts from an image (Midjourney or uploaded). Text prompt is optional and should describe motion only.

| Parameter | Values | Default |
|---|---|---|
| `--video` | flag — Discord: image URL first, then text | — |
| `--motion` | `low` / `high` | `low` |
| `--raw` | flag | off |
| `--loop` | flag — start frame = end frame | off |
| `--end URL` | public image URL as last frame | — |
| `--bs N` | `1`, `2`, `4` | `4` |

- **Duration:** 5 s initial; Extend adds 4 s, up to 4 times → 21 s max. Extend Auto reuses the prompt; Extend Manual lets you edit it. Each extension costs the same as a new job.
- **Resolution:** SD 480p (all plans, default) · HD 720p (Standard/Pro/Mega, Fast only). Relax = Pro/Mega, SD only.

| Start ratio | SD | HD |
|---|---|---|
| 1:1 | 624×624 | 960×960 |
| 4:3 | 720×544 | 1104×832 |
| 2:3 | 512×768 | 784×1168 |
| 16:9 | 832×464 | 1280×720 |
| 1:2 | 448×880 | 672×1360 |

- **GPU cost:** `--bs 4` SD 8 min / HD 26 min · `--bs 2` 4 / 13 · `--bs 1` 2 / 7.
- **Incompatible:** Edit Model references, `--sref`, image prompts, all still-image params (stripped on animate).
- **Downloads:** Social MP4, Raw MP4, GIF.

## V7 → V8 Migration

| V7 habit | V8.1 / V8.2 |
|---|---|
| `--v 7` | `--v 8.2` |
| `--q 2` / `--q 4` | Remove; use `--hd` for finals |
| `--oref URL --ow 100` | Edit model with the image attached as a reference |
| `--cref URL --cw` | Edit model references + identity clause |
| `part one:: part two::2` | One prose sentence, most important first |
| Draft mode for ideation | SD at low stylize, permutations, `--r` |
| Retexture | Edit model |
| Upscale for 2K | `--hd` native 2K (upscalers still work on SD images) |
| V7 srefs, moodboards, profiles | Carry over; re-check — V8.2 profile model changed |
| Same seed across versions | Expect different results; rebaseline |
| Short keyword prompts | Longer, specific sentences; V8 follows more detail and literalizes more |
