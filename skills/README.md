# Model prompting skills

Agent Skills that teach a model how to write prompts for a specific image, video or audio
generation model — the syntax it actually parses, the parameters it actually exposes, and the
traps that look like features.

Each skill is researched against **first-party vendor documentation**. Where a widely repeated
claim turned out to be wrong, the correction is recorded in that skill's `README.md` with the
source. That file is the receipts, not filler — several of these models are surrounded by
confident third-party guidance that is simply invented.

## Video (16)

| Skill | Model | Vendor |
|---|---|---|
| [`veo-v3`](video/veo-v3) | Veo 3.1 | Google DeepMind |
| [`sora-v2`](video/sora-v2) | Sora 2 (Standard + Pro) | OpenAI |
| [`kling-v3`](video/kling-v3) | Kling 3.0 | Kuaishou |
| [`seedance-v2`](video/seedance-v2) | Seedance 2.0 | ByteDance |
| [`seedance-v2-5`](video/seedance-v2-5) | Seedance 2.5 | ByteDance |
| [`ltx-v2`](video/ltx-v2) | LTX-2 Fast & Pro | Lightricks |
| [`minimax-h3`](video/minimax-h3) | MiniMax H3 | MiniMax |
| [`hailuo-v2`](video/hailuo-v2) | Hailuo 2.3 | MiniMax |
| [`flux-v3-video`](video/flux-v3-video) | FLUX 3 Video | Black Forest Labs |
| [`gemini-omni-flash`](video/gemini-omni-flash) | Gemini Omni Flash | Google |
| [`grok-imagine-video-v1-5`](video/grok-imagine-video-v1-5) | Grok Imagine Video 1.5 | xAI |
| [`luma-ray-v3`](video/luma-ray-v3) | Ray 3 (Dream Machine) | Luma AI |
| [`pixverse-v5`](video/pixverse-v5) | PixVerse V5.5 | PixVerse |
| [`pixverse-v6`](video/pixverse-v6) | PixVerse V6 | PixVerse |
| [`wan-v2`](video/wan-v2) | WAN 2.5 | Alibaba |
| [`happyhorse-v1`](video/happyhorse-v1) | HappyHorse 1.0 | HappyHorse |

## Image (15)

| Skill | Model | Vendor |
|---|---|---|
| [`midjourney-v7`](image/midjourney-v7) | Midjourney v7 | Midjourney |
| [`gpt-image-v2`](image/gpt-image-v2) | GPT Image 2 | OpenAI |
| [`gemini-v3-pro`](image/gemini-v3-pro) | Gemini 3 Pro Image (Nano Banana Pro) | Google |
| [`flux-v2`](image/flux-v2) | FLUX.2 (Pro, Max, Flex, Klein, Kontext) | Black Forest Labs |
| [`ideogram-v3`](image/ideogram-v3) | Ideogram 3.0 | Ideogram |
| [`seedream-v5`](image/seedream-v5) | Seedream 5.0 Lite | ByteDance |
| [`seedream-v4`](image/seedream-v4) | Seedream 4.5 | ByteDance |
| [`qwen-image-v3`](image/qwen-image-v3) | Qwen-Image 3.0 | Alibaba |
| [`qwen-image-v2`](image/qwen-image-v2) | Qwen-Image 2.0 | Alibaba |
| [`stable-diffusion-v3-5`](image/stable-diffusion-v3-5) | Stable Diffusion 3.5 | Stability AI |
| [`luma-uni-v1`](image/luma-uni-v1) | Uni-1.1 | Luma AI |
| [`krea-v2`](image/krea-v2) | Krea 2 | Krea AI |
| [`grok-aurora-v1`](image/grok-aurora-v1) | Grok Image (Aurora) | xAI |
| [`mystic-v2`](image/mystic-v2) | Mystic 2.5 | Freepik |
| [`phota-v1`](image/phota-v1) | Phota | PhotaLabs |

Audio and 3D skills follow.

## Installing

Copy any skill folder into your project's or user's skills directory:

```bash
# project-level
cp -r skills/video/veo-v3 .claude/skills/

# or user-level, available in every project
cp -r skills/video/veo-v3 ~/.claude/skills/
```

The skill triggers on its own `description` — mention the model by name and it loads. Nothing
else to wire up.

## What's in a skill

| File | Role |
|---|---|
| `SKILL.md` | The prompt-craft itself. Frontmatter + body; the body is the instruction set. |
| `best-practices.md` | Longer-form craft guidance, loaded on demand. |
| `examples.md` / `examples.json` / `examples/` | Worked prompts with annotations, sometimes split by mode. |
| `parameters.md` / `parameters.json` | The model's real API surface — enums, ceilings, defaults. |
| `continuity-and-*.md` | How the model holds a character or a look across shots. |
| `schema.json` | Structured-output shape, where the vendor documents one. |
| `README.md` | Build notes: what was researched, what was corrected, what is still open. |

Not every skill has every file — the shape follows what the vendor actually documents.

## A note on scope

These skills deliberately **do not** write output settings into prompt prose — no aspect ratio,
resolution, duration or `--parameters`. Those belong in whatever tool is making the call, not in
the descriptive text. Where a model has meaningful settings, they appear in a separate suggested-
settings section.

---

Maintained by **Visual Horizon Studio**. MIT licensed — see [LICENSE](../LICENSE).
