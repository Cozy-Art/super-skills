# midjourney-v7 — build notes

Human-facing build notes.

---

## Skill Metadata

**Trigger Contexts:**
- When user requests artistic or stylized image generation
- When rapid iteration/exploration is priority (Draft Mode)
- When character consistency across multiple images is needed (Omni Reference)
- When specific artistic style control is required (Style References)

**Primary Use Cases:**
- Concept art and character design
- Artistic photography styles
- Fantasy and sci-fi illustrations
- Brand visual exploration
- Rapid ideation and iteration

**Optimal Workflow (settings the director applies in Midjourney — never in the generated prompt):**
1. Explore concepts quickly, then refine the winning directions
2. Use Omni Reference for character consistency across shots
3. Raise quality for final polish

The generated prompt stays pure description regardless of which of these the director chooses.

---

## Integration Notes

### When driven from structured scene data

When generating prompts from structured scene records:
- Extract subject descriptions from character records
- Pull environment details from location records
- Translate mood/theme into descriptive lighting and stylistic language (not parameters)
- Note when character consistency matters so the director can apply Omni Reference in Midjourney

### Reference Image Workflow

**Omni Reference (`--oref`)**: For character/object consistency
- Keep `--ow` (weight) below 400 for best results
- Use with character or specific object consistency needs
- Replaces Character Reference from V6

**Style Reference (`--sref`)**: For artistic style consistency
- Use `--sv 6` for V7 native behavior (default)
- Use `--sv 4` for legacy V4/V6 sref codes
- Adjust `--sw` (0-1000, default 100) for style strength

**Image Prompt Weight (`--iw`)**: For image-to-image influence
- Range: 0-3 (default 1)
- Higher values = stronger image reference influence

### Draft Mode Strategy

Use `--draft` for:
- Initial concept exploration (10x faster)
- Testing multiple variations quickly
- Thumbnail/composition previews
- Budget-conscious iteration

Skip Draft Mode for:
- Final deliverables
- When resolution matters
- Text rendering requirements
- Fine detail work

---

## Version Information

- **Skill Version:** 1.1
- **Model Version:** Midjourney v7 (Released April 2025, Default June 2025)
- **Aliases:** midjourney7
- **Last Updated:** 2026-07-23 - Removed all trailing `--` parameter generation (aspect ratio, stylize, quality, chaos, references); output is now pure descriptive prose. The director owns all Midjourney settings.
- **Maintained By:** Visual Horizon Studio

---
