# mystic-v2 — build notes

Human-facing build notes.

---

## Skill Metadata

**Trigger Contexts:**
- When user requests photorealistic images
- When character consistency with LoRA is needed (Standard only)
- When vivid, illustrative styles are required (Flexible)
- When cinematic consistency matters (Fluid)
- When editorial portrait quality is needed (API: editorial_portraits)

**Primary Use Cases:**
- Product photography (Standard/Super Real)
- Fantasy illustrations (Flexible)
- Cinematic storyboards (Fluid)
- Editorial portraits (API: editorial_portraits)
- Brand assets with consistent characters (Standard + LoRA)
- High-volume campaign work (Fluid)

---

## Integration Notes

### When driven from structured scene data

When generating prompts from structured scene records:
- **Standard variant**: Use for realistic scenes, characters with LoRA
- **Flexible variant**: Use for fantasy, stylized, illustrative scenes
- **Fluid variant**: Use for cinematic consistency, shot sequences
- Extract character descriptions for Custom Character LoRA training
- Map shot visual style to engine selection (Illusio/Sharpy/Sparkle)
- Use negative prompts for refinement rather than prompt bloat

### Custom Characters (LoRA) Workflow

**ONLY works with Standard (realism) model:**
1. Train Custom Character LoRA from 5-15 reference images
2. Reference in prompt: `@character_name::80`
3. Adjust strength: Higher = more adherence (100-200 range)
4. Generate across multiple scenes with consistency
5. Fix faces/hands using Retouch tool if needed

**Note:** Switching to Flexible/Fluid silently disables LoRAs.

### Variant Selection Strategy

**Choose Standard (realism) when:**
- Need photorealism with natural colors
- Using Custom Characters or Custom Styles (LoRA)
- Want "less AI look"
- General-purpose photography or illustrations

**Choose Flexible when:**
- Need best prompt adherence
- Want vivid, saturated colors
- Creating fantasy or branding assets
- Specific visual styles required

**Choose Fluid when:**
- Need fast generation for volume work
- Creating cinematic frame sequences
- Consistency across multiple related images
- Visual campaigns or storyboards

**Choose API sub-models when:**
- Zen: Minimalist, soft aesthetics
- Super Real: Hyper-realistic medium shots
- Editorial Portraits: Professional close-up portraits (use long prompts)

---

## Version Information

- **Skill Version:** 1.0
- **Model Version:** Mystic 2.5 (Standard/Flexible/Fluid) + API sub-models
- **Last Updated:** 2026-02-11

---

## Output Format

Generate prompts as concise, direct descriptions optimized for the chosen variant. For complex requirements, provide:

1. **Primary prompt** (focused, 1-3 sentences)
2. **Negative prompt** (refinements)
3. **Variant recommendation** (Standard/Flexible/Fluid)
4. **Technical parameters** (resolution, engine, creative detailing)
5. **Character reference guidance** (if using LoRA)

### Example Output Structure:

```
Prompt: A weathered detective in noir attire examines evidence under harsh 
streetlight, rain-soaked city alley, shot with ARRI Alexa LF, cinematic depth.

Negative: cartoon, bright colors, smooth skin, perfect lighting, blurry

Variant: Mystic 2.5 (Standard - realism)
Resolution: 2K
Engine: Sharpy
Creative Detailing: 40
Character: @detective::80 (if LoRA trained)
```

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
