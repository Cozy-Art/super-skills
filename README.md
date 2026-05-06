# super-skills

A growing collection of [agent skills](https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills/overview) you can drop into your workflow—shared here under the **MIT License** so you can adopt, adapt, and ship them in your own projects.

## Why this repo exists

Skills are a practical way to keep tooling and conventions consistent across repos and teammates. This project is a home for skills that have proven useful in real development—starting with patterns that make **AI-assisted coding** cheaper in tokens and clearer in intent.

## Featured skill: code documentation standards

The first skill in this collection is **code documentation standards** (see `.claude/code-documentation-standards/`). It was built to document *while* you build, not after the fact.

**The idea:** put a small, structured “map” at the top of each file and use consistent section markers inside the file. A model (or a human) can skim headers and grep for sections instead of loading entire files to guess what they do. That preserves context, cuts redundant explanation across chat turns, and makes handoffs easier—without turning every file into an essay.

If you want predictable file overviews, greppable structure, and less context burn per session, start there.

## License

MIT — see [LICENSE](LICENSE).
