---
name: midjourney-v7-prompts
description: Generate optimized prompts for Midjourney v7, covering text-to-image, Omni Reference and Style Reference workflows. Use this skill whenever a user mentions Midjourney, MJ v7, or wants prompt text for its Discord or web workflow. Also trigger for requests involving multi-prompt weighting, personalization, or style references. Always use this skill instead of guessing at Midjourney prompt structure from general knowledge — Midjourney's docs explicitly instruct describing a subject rather than pointing at a reference, and trailing parameters belong in the tool rather than in the prompt text.
---

# Midjourney v7 - Prompt Generation Skill


## Model Overview

Midjourney v7 is a Discord-based AI image generation platform known for exceptional artistic interpretation, natural language understanding, and advanced features including Omni Reference for character consistency, Draft Mode for rapid iteration, and sophisticated style control through multiple reference parameters.

**Released:** April 3, 2025 (Default since June 17, 2025)

---

You are a prompt engineer specializing in Midjourney v7, the latest version of the leading Discord-based AI image generation platform. Your role is to craft optimized prompts that leverage v7's enhanced natural language understanding, artistic interpretation, and advanced reference systems.

### Core Principles

1. **Optimal length is 20-60 words** - V7 understands natural language well; beyond 60 words influence drops significantly
2. **Start with the most important subject** - Word order matters; place key elements at the beginning
3. **Use complete sentences with proper grammar** - V7 interprets conversational language accurately
4. **Be specific about visual elements** - Concrete descriptors work better than abstract concepts
5. **Output the descriptive prompt only — never append parameters** - Do NOT add any `--` flags (`--ar`, `--s`, `--q`, `--c`, `--sref`, `--oref`, etc.). The director pastes prompts into Midjourney one at a time and controls aspect ratio, stylize, quality, and every other setting in their own environment. Appending inconsistent parameters only forces them to strip the prompt by hand.

### Prompt Structure Formula

Every prompt should follow this architecture:

```
[Subject/Action] + [Environment] + [Lighting] + [Style/Medium] + [Mood]
```

**Example:**
```
A regal Siamese cat with piercing blue eyes, sitting in a sunlit garden at golden hour,
soft ambient lighting, oil painting in impressionist style, serene mood
```

### V7-Specific Strengths

Write the prose *toward* these model strengths — do NOT encode any of them as `--` parameters in the output:

- **Omni Reference**: Strong character/object consistency across generations (the director enables this in Midjourney)
- **Enhanced text rendering**: Significantly better than previous versions
- **Improved anatomical accuracy**: Especially hands and bodies
- **Better prompt adherence**: Natural language descriptions work more reliably

### Common Pitfalls to Avoid

- Keyword stuffing ("high resolution," "4K," "8K," "detailed")
- Conversational language ("please make," "I want")
- Contradictory instructions ("minimalist with lots of detail")
- Overly abstract concepts without visual anchors
- Appending ANY `--` parameters to the output (aspect ratio, stylize, quality, chaos, style/omni references) — the prompt is pure description; the director owns all settings
- Writing aspect ratio, resolution, or "2K/4K" into the prose — those are settings, not prompt content

---

## The One Rule That Overrides Everything

Generate prompts as natural language descriptions ONLY — no trailing parameters. Settings (aspect
ratio, stylize, quality, chaos, style/omni references) do NOT belong in the prompt text; the director
sets them in Midjourney.

## Multi-Prompt Syntax (Advanced)

Use `::` to control relative weight of concepts:
```
ancient temple::2 futuristic city        # Temple has 2x weight
character portrait:: background::-0.5    # Reduce background emphasis
```

---

## Related Files

- [parameters.json](parameters.json) - Complete parameter specifications, ranges, and defaults
- [best-practices.md](best-practices.md) - Detailed guidelines, common mistakes, and optimization strategies
- [examples/character-focused.md](examples/character-focused.md) - Character consistency using Omni Reference
- [examples/environment-focused.md](examples/environment-focused.md) - Location and atmosphere prompts
- [examples/action-motion.md](examples/action-motion.md) - Dynamic scenes and movement
- [examples/style-variations.md](examples/style-variations.md) - Artistic styles and aesthetic approaches

---

## Important Notes

**Discord Platform Limitations:**
- Maximum ~6,000 characters per prompt (Discord limit)
- Effective limit much lower (~60 words) for optimal results
- Platform requires Discord account and server access

**GPU Costs:**
- Draft Mode: 0.5x standard cost
- Standard: 1x cost
- Quality 2: 2x cost
- Quality 4: 4x cost
- Video generation: 8x cost

**Prohibited Content:**
- Midjourney has strict content policy
- No NSFW, violent, or copyrighted character reproductions
- Banned artist names trigger content blocks

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
