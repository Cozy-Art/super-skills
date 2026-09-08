# super-skills

A growing collection of [agent skills](https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills/overview) you can drop into your workflow—shared here under the **MIT License** so you can adopt, adapt, and ship them in your own projects.

## Why this repo exists

Skills are a practical way to keep tooling and conventions consistent across repos and teammates. This project is a home for skills that have proven useful in real development—starting with patterns that make **AI-assisted coding** cheaper in tokens and clearer in intent.

## What's here

### [Model prompting skills](skills/) — 16 video + 15 image models

Prompt-generation skills for Veo 3.1, Sora 2, Kling 3.0, Seedance, LTX-2, MiniMax H3, FLUX 3 Video and nine more video models—plus Midjourney v7, GPT Image 2, Gemini 3 Pro Image, FLUX.2, Ideogram 3.0, Seedream, Qwen-Image, Stable Diffusion 3.5 and seven more on the image side. Each one teaches the syntax a given model actually parses, the parameters it actually exposes, and the traps that look like features.

They are researched against **first-party vendor documentation**. Where a widely repeated claim turned out to be wrong, the correction is recorded with its source in that skill's build notes—because several of these models are surrounded by confident third-party guidance that is simply invented.

Audio and 3D skills follow. → **[Browse the collection](skills/)**

### Code documentation standards

**Code documentation standards** (see `.claude/code-documentation-standards/`) was built to document *while* you build, not after the fact.

**The idea:** put a small, structured “map” at the top of each file and use consistent section markers inside the file. A model (or a human) can skim headers and grep for sections instead of loading entire files to guess what they do. That preserves context, cuts redundant explanation across chat turns, and makes handoffs easier—without turning every file into an essay.

If you want predictable file overviews, greppable structure, and less context burn per session, start there.

## Installing a skill

Copy the folder you want into your project's or user's skills directory:

```bash
cp -r skills/video/veo-v3 .claude/skills/      # this project
cp -r skills/video/veo-v3 ~/.claude/skills/    # every project
```

Each skill triggers on its own `description`—mention the model by name and it loads.

## License

MIT — see [LICENSE](LICENSE).

---

Maintained by **Visual Horizon Studio**.
