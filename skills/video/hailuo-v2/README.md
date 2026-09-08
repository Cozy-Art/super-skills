# hailuo-v2 — build notes

Human-facing build notes.

---

## Skill Metadata

**Trigger Contexts:**
- When user requests short-form video (6-10 seconds)
- When motion realism and physics accuracy are priority
- When character consistency with single reference image is needed
- When emotion rendering is critical

**Primary Use Cases:**
- Social media content (TikTok, Reels, Shorts)
- Commercial B-roll footage
- Character-driven emotional scenes
- Realistic motion capture
- Product demonstrations with natural physics

**Optimal Workflow:**
1. Generate hero character shot with Subject Reference
2. Use same reference for all subsequent shots
3. Keep clips 4-6 seconds for stability
4. Chain clips together in post-production

---

## Integration Notes

### When driven from structured scene data

When generating prompts from structured scene records:
- Extract character descriptions for Subject Reference upload
- Map shot duration to 6s (1080P) or 10s (768P) increments
- Translate camera movements to bracket notation
- Keep sequences focused: 1-2 actions per 6s clip
- Use character reference images as Subject Reference

### Subject Reference Workflow

**Character Consistency:**
1. Upload high-quality portrait (front-facing works best)
2. AI automatically detects facial features
3. Generate initial scene with character
4. Use same reference for all related shots
5. Maintains facial consistency across entire sequence

**Best Practices:**
- Front-facing portrait images produce best results
- Realistic human images work better than stylized/anime
- High-quality source images prevent artifacts
- Add emotion keywords for better expression rendering

**Limitations:**
- Single entity only (multi-character in development)
- Hands can have issues when holding objects
- Occasional lighting artifacts
- Works best with realistic styles

### Image-to-Video Strategy

When using reference image as first frame:
- AI already knows subject and scene
- Focus prompt on: camera movement, action, mood changes
- Match actions to what's feasible from starting pose
- Avoid sudden dramatic movements from static images

### Multi-Shot Scene Building

For scenes with multiple shots:
1. **Keep each shot 4-6 seconds** for stability
2. **Use Subject Reference** consistently across all shots
3. **Plan camera coverage**: Wide → Medium → Close-up
4. **Chain in post-production**: Edit clips together for longer sequences
5. **Match lighting/mood**: Keep environmental descriptions consistent

---

## Version Information

- **Skill Version:** 1.0
- **Model Version:** MiniMax Hailuo 2.3 (Standard/Pro/Fast)
- **Aliases:** hailuo2
- **Last Updated:** 2026-02-11
- **Maintained By:** Visual Horizon Studio

---
