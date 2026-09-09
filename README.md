
<img width="1344" height="768" alt="video-frame3-2 83s" src="https://github.com/user-attachments/assets/218ab474-8145-4f9d-8eac-fba11b423d96" />


# super-skills


A growing collection of [agent skills](https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills/overview) you can drop into your workflow—shared here under the **MIT License** so you can adopt, adapt, and use them in your own projects.

## Why this repo exists

Skills are a practical way to keep tooling and conventions consistent across repos and teammates. This project is a home for skills that have proven useful in real development—starting with patterns that make **AI-assisted coding** cheaper in tokens and clearer in intent.

## What's here

### [Model prompting skills](skills/) — 16 video + 15 image models

Prompt-generation skills for Veo 3.1, Sora 2, Kling 3.0, Seedance, LTX-2, MiniMax H3, FLUX 3 Video and nine more video models—plus Midjourney v7, GPT Image 2, Gemini 3 Pro Image, FLUX.2, Ideogram 3.0, Seedream, Qwen-Image, Stable Diffusion 3.5 and seven more on the image side. Each one teaches the syntax a given model actually parses, the parameters it actually exposes, and the traps that look like features.

They are researched against **first-party vendor documentation**. Where a widely repeated claim turned out to be wrong, the correction is recorded with its source in that skill's build notes—because several of these models are surrounded by confident third-party guidance that is simply invented.

Audio and 3D skills follow. → **[Browse the collection](skills/)**

### Code documentation standards

**Code documentation standards** (see `.claude/skills/code-documentation-standards/`) was built to document *while* you build, not after the fact.

**The idea:** put a small, structured “map” at the top of each file and use consistent section markers inside the file. A model (or a human) can skim headers and grep for sections instead of loading entire files to guess what they do. That preserves context, cuts redundant explanation across chat turns, and makes handoffs easier—without turning every file into an essay.

If you want predictable file overviews, greppable structure, and less context burn per session, start there.

### AI agent readiness

**AI agent readiness** (see `.claude/skills/ai-agent-readiness/`) audits and fixes how a site is read by AI agents and answer engines—`llms.txt`, per-bot `robots.txt` policy, CDN and WAF bot gates, markdown mirrors, JSON-LD, SSR verification, and plain content extractability.

**The idea:** two audiences get conflated. Answer engines that cite you (ChatGPT, Claude, Perplexity, Gemini) and working agents that have to read and act on the page want different things, and a site can be invisible to both for reasons that never show up in a browser. The skill works in layers—can the bot reach the page, can it parse what's there, can it find the rest—and ships a runnable audit script, per-crawler reference tables, and `llms.txt` / `robots.txt` templates.

Run it before launching a marketing site, docs site or landing page—the output is a checked list of fixes, not a vibe.

### Decision capture

**ADR capture** (see `.claude/skills/adr-capture/`) writes lightweight architecture decision records as the decisions actually happen—when you say "let's go with X over Y", at phase close, or retroactively from a commit or changelog note. It exists because the reasoning behind a trade-off is the part that evaporates first.

## Installing

A skill is a **folder** containing `SKILL.md`. There is no `.skill` file format—every tool below reads the same folder. Claude's web and desktop apps are the one exception: they want that folder **zipped**. Nothing here needs a second copy of the tree.

One catch shapes everything: **Claude Code and Codex only look one level deep.** `.claude/skills/veo-v3/SKILL.md` loads; `.claude/skills/video/veo-v3/SKILL.md` does not. So skills get flattened on install, which is what `scripts/install.sh` is for.

| Tool | Reads skills from | Install |
|---|---|---|
| **Claude Code** | `~/.claude/skills/<name>/`, `.claude/skills/<name>/` | `./scripts/install.sh veo-v3` |
| **Claude** (web, desktop) | an uploaded `.zip` | `./scripts/package.sh veo-v3`, then upload |
| **Cursor** | `~/.cursor/skills/`, `.cursor/skills/`, `.agents/skills/` | `./scripts/install.sh veo-v3 --cursor` |
| **Codex** | `~/.agents/skills/`, `.agents/skills/` | `./scripts/install.sh veo-v3 --codex` |
| **ChatGPT** | the Skills picker | `./scripts/package.sh veo-v3`, then upload |
| **Anything else** | its own skills directory | `./scripts/install.sh veo-v3 --target <dir>` |

### Claude Code

```bash
./scripts/install.sh veo-v3              # one skill, available in every project
./scripts/install.sh --all               # all 34
./scripts/install.sh veo-v3 --claude-code-project   # this repo only
```

Or by hand, since the folder is the whole unit:

```bash
cp -r skills/video/veo-v3 ~/.claude/skills/    # every project
cp -r skills/video/veo-v3 .claude/skills/      # this project
```

### Claude (web and desktop apps)

Build a zip, then upload it:

```bash
./scripts/package.sh veo-v3      # → dist/veo-v3.zip
./scripts/package.sh --all       # → one zip per skill
```

**Settings → Capabilities → Skills → Add**, and pick the `.zip`. The archive has the skill folder at its root (`veo-v3.zip` → `veo-v3/SKILL.md`), which is the layout Claude expects. Custom skills need **code execution** enabled, and are available on the Free, Pro, Max, Team and Enterprise plans.

### Cursor

```bash
./scripts/install.sh veo-v3 --cursor            # ~/.cursor/skills/
./scripts/install.sh veo-v3 --cursor-project    # ./.cursor/skills/
```

Cursor also reads `.agents/skills/`, and unlike Claude Code it *does* walk category subfolders—so you can point it at a copy of the whole `skills/` tree if you prefer. The script flattens anyway, so both tools behave the same.

### Codex / ChatGPT

```bash
./scripts/install.sh veo-v3 --codex             # ~/.agents/skills/
./scripts/install.sh veo-v3 --codex-project     # ./.agents/skills/ in a repo
```

Codex scans `.agents/skills` from the working directory up to the repo root, plus `~/.agents/skills`. For ChatGPT itself, use the zip from `scripts/package.sh` with the Skills picker.

### Notes

- Skills trigger on their own `description`—name the model ("write me a Veo 3.1 prompt") and the skill loads. Nothing to wire up.
- **Custom skills don't sync across Claude surfaces.** A skill uploaded to claude.ai isn't available in the API or in Claude Code, and vice versa. Install it wherever you want it.
- `./scripts/install.sh --list` shows every installable skill; `--dry-run` shows what would happen; `--force` replaces an existing copy.
- Skills are instructions a model will follow. Read one before installing it—that goes for these and for anyone else's.

## License

MIT — see [LICENSE](LICENSE).

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
