# kling-v3 — build notes

Human-facing build notes.

---

## Skill Metadata

**Trigger Contexts:**
- When user requests multi-shot video sequences
- When character consistency across shots is critical
- When native dialogue with lip-sync is needed
- When 10-15 second scenes are required

**Primary Use Cases:**
- Narrative storytelling with dialogue
- Multi-shot scene construction
- Character-driven content
- Cinematic sequences with camera movement
- Extended video (up to 3 minutes)

**Optimal Workflow:**
1. Generate hero character shot with Elements references
2. Extract best frames for new reference angles
3. Build multi-shot sequences using storyboard format
4. Extend via continuation if >15s needed

---

## Integration Notes

### When driven from structured scene data

When generating prompts from structured scene records:
- Map scene structure to multi-shot storyboard format
- Extract character descriptions from character records for Elements
- Pull location details for Scene/Context layer
- Translate shot parameters to Kling camera terminology
- Convert dialogue to character-attributed format (@syntax)
- Use character reference images as Elements references

### Elements Reference Workflow

**Character Consistency:**
1. Generate initial character shot with detailed description
2. Extract frames showing different angles/expressions
3. Upload 1-4 best frames as Elements references
4. Set face adherence: 70-100 for strict consistency
5. Use same references across all shots in sequence

**Reference Types:**
- **Face only**: Maintains facial identity, allows clothing variation
- **Subject**: Includes body, pose, clothing consistency
- **Entire image**: Preserves full composition and style

### Multi-Shot Scene Building

For scenes with multiple shots:
1. **Plan shot progression**: Wide establishing → Medium → Close-up
2. **Use storyboard format**: Define each shot with duration
3. **Maintain continuity**: Same Elements, lighting, color grading
4. **Attribute dialogue**: Use @Character syntax for each speaker
5. **Specify camera coverage**: Ensure logical scene flow

### Video Extension Strategy

**For sequences >15 seconds:**
1. Generate initial 15s at 1080p
2. Use continuation feature to extend by increments
3. Describe next action/movement in continuation prompt
4. Can extend up to 3 minutes total
5. Maintains seamless transitions

---

## Version Information

- **Skill Version:** 1.0
- **Model Version:** Kling 3.0 / 3.0 Omni (Released Feb 4, 2026)
- **Aliases:** kling3
- **Last Updated:** 2026-02-11

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
