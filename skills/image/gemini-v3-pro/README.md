# gemini-v3-pro — build notes

Human-facing build notes.

---

## Skill Metadata

**Trigger Contexts:**
- When user requests image generation for professional assets
- When character/object consistency across multiple images is critical
- When text rendering quality matters (logos, signage, typography)
- When real-time information needs to be visualized (requires Google Search grounding)

**Primary Use Cases:**
- Character concept art with multi-angle references
- Brand assets with precise text rendering
- Photo-realistic product visualization
- Editorial illustrations with specific style requirements
- Sticker/icon generation with consistent design language

**Optimal Generation Settings:**
- Resolution: 2K for balanced quality/speed, 4K for final assets
- Aspect Ratio: Match intended use case (see parameters.json)
- Multi-turn conversation: Recommended for character consistency

---

## Integration Notes

### When driven from structured scene data

When generating prompts from structured scene records:
- Extract character descriptions from character records
- Pull location atmosphere from location records
- Apply theme-specific lighting/mood from project settings
- Translate camera specifications from shot records

### Reference Image Workflow

When the pipeline provides reference images:
1. Identify reference types (human vs object vs style)
2. Structure prompt to describe relationships between references
3. Use "Image 1", "Image 2" naming convention
4. Recommend multi-turn conversation for character consistency

### Continuity Management

For maintaining consistency across shots:
- Use multi-turn chat mode (leverages 1M token context window)
- Include preservation commands: "Keep exact same composition", "Maintain identical facial features"
- Reference previous generations explicitly
- Save successful prompts as templates in project library

---

## Version Information

- **Skill Version:** 1.1
- **Model Version:** Gemini 3 Pro Image Preview (2024-2026)
- **Aliases:** nano-banana
- **Last Updated:** 2026-07-23 - Removed the mandated aspect-ratio/orientation sentence slot from the prompt formula; ratio/resolution now live only in Configuration notes, never in the prompt prose.
- **Maintained By:** Visual Horizon Studio

---
