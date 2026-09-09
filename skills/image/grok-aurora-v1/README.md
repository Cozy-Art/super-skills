# grok-aurora-v1 — build notes

Human-facing build notes.

---

## Version Information

- **Skill Version:** 1.0
- **Model:** Grok Aurora (`grok-imagine-image`)
- **Last Updated:** 2026-04-18

## Resources

This skill includes comprehensive documentation and examples:

- `parameters.json` — Complete API specifications, aspect ratios, rate limits, pricing
- `best-practices.md` — Advanced optimization, style control, iterative refinement, troubleshooting
- `examples-text-to-image.md` — 16 examples across the recurring example projects for text-to-image generation
- `examples-editing.md` — 10 examples for image-to-image editing, multi-image compositing, and iterative refinement
- `schema.json` — JSON validation schema for prompt output format

---

## Output Format

Generate prompts as natural language descriptions with supporting parameters:

```
Prompt: [2-5 sentence natural language description following 
Subject + Style/Medium + Environment + Lighting + Mood + Technical Details]

Negative Guidance: [Inline "avoid:" list, if needed — included at end of prompt or as separate line]

Model: grok-imagine-image
Resolution: [1k | 2k]
Aspect Ratio: [ratio from supported list]
N: [number of images, 1-10]
Seed: [integer for reproducibility, or null]
Reference Images: [URLs if image-to-image editing, or null]

Director's Notes: [Brief explanation of prompt decisions]
```

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
