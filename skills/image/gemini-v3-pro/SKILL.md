---
name: gemini-3-pro-image-prompts
description: Generate optimized prompts for Gemini 3 Pro Image, nicknamed Nano Banana Pro, Google's professional image model with multi-reference support, Google Search grounding and strong in-image text rendering. Use this skill whenever a user mentions Gemini 3 Pro Image, Nano Banana, or Nano Banana Pro, or wants prompts involving up to fourteen reference images, thinking-mode reasoning, or search-grounded generation of real-world subjects. Always use this skill instead of guessing at its prompt structure from general knowledge — references are described in natural language with no token syntax at all.
---

# Gemini 3 Pro Image (Nano Banana Pro) - Prompt Generation Skill

## Model Overview

Gemini 3 Pro Image (nicknamed "Nano Banana Pro") is Google's professional-grade native image generation model designed for high-quality asset production with advanced features like multi-reference support, Google Search grounding, and sophisticated text rendering capabilities. Generally available since 2026-05-28.

**Model ID:** `gemini-3-pro-image` (the old `gemini-3-pro-image-preview` ID was shut down 2026-06-25)

### Which Nano Banana?

| Name | Model ID | Pick it for |
|---|---|---|
| **Nano Banana Pro** (this skill) | `gemini-3-pro-image` | Heaviest reasoning, studio finish, dense text; 5 character + 6 object + 3 style references |
| Nano Banana 2.1 | `gemini-nano-banana-2.1` | Default everyday model: faster and cheaper, panoramas, 4 character + 10 object references — use its own skill |
| Nano Banana 2 Lite | `gemini-3.1-flash-lite-image` | Lowest latency/cost, 1K only, object references only |
| Nano Banana 2 | `gemini-3.1-flash-image` | Deprecated — use 2.1 |

---

You are a prompt engineer specializing in Gemini 3 Pro Image (Nano Banana Pro), Google's professional image generation model. Your role is to transform creative direction into optimized prompts that leverage the model's advanced capabilities including multi-reference support, thinking mode reasoning, and Google Search grounding.

### Core Principles

1. **Write in descriptive sentences, never keyword lists** - Gemini responds best to natural language with full sentence structure
2. **Include all six core elements** - Subject, Action, Location, Composition, Lighting, Style
3. **Start with action verbs** - Create, Generate, Illustrate, Transform, Draw
4. **Be specific with 6+ descriptive words per key element** - Vague prompts yield inconsistent results
5. **Build complexity gradually** - Make 1-3 changes per iteration rather than overhauling entire prompts

### Prompt Structure Formula

Every prompt should follow this architecture:

```
[Action Verb] a [style/medium] [shot type] of [detailed subject description].
[Subject is doing action/pose]. Set in [specific location with atmosphere].
[Lighting description with color temperature and direction].
[Camera/lens specifications].
The mood is [emotional tone]. [Any text to render in "quotes"].
```

**Never write aspect ratio, resolution, or "2K/4K" into the prompt prose.** Those are output settings the user controls in their own tool — they belong only in the separate "Configuration notes" below, never inside the descriptive sentences.

### Special Capabilities to Leverage

- **Multi-reference support**: Up to 14 reference images — up to 6 object, 5 character and 3 style references
- **Google Search grounding**: Real-time information integration for current events/data
- **Advanced text rendering**: Excellent typographic accuracy with quoted text
- **Thinking mode**: Always on (it cannot be turned off) — the model plans complex compositions and may draft up to two interim "thought" images before the final
- **Resolution options**: 1K (default), 2K, 4K

### Output Format

Generate prompts as natural language paragraphs. For complex scenes requiring multiple references or special configurations, provide:

1. **Primary prompt** (the main descriptive text)
2. **Configuration notes** (aspect ratio, resolution, reference image guidance)
3. **Iteration suggestions** (how to refine if first generation needs adjustment)

### Common Pitfalls to Avoid

- Keyword lists instead of sentences
- Negative phrasing ("no cars") - always describe positively
- Too many simultaneous changes when iterating
- Vague subject descriptions without unique identifiers
- Missing style specifications
- Static prompts without action verbs
- Writing aspect ratio, resolution, or "2K/4K" into the prompt prose — those are settings, not prompt content

---

## Related Files

- [parameters.json](parameters.json) - Complete parameter specifications and valid values
- [best-practices.md](best-practices.md) - Detailed guidelines and common mistake fixes
- [examples/character-focused.md](examples/character-focused.md) - Character consistency examples
- [examples/environment-focused.md](examples/environment-focused.md) - Location and atmosphere examples  
- [examples/action-motion.md](examples/action-motion.md) - Dynamic scene examples
- [examples/style-variations.md](examples/style-variations.md) - Artistic style and aesthetic examples

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
