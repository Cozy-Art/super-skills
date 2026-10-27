# gemini-v3-pro — build notes

Human-facing build notes.

---

## Update — 2026-10-19

Fact refresh against current first-party docs (skill v1.1 → v1.2). Craft, structure and examples unchanged apart from the wording fixes listed.

| Claim was | Now | Source |
|---|---|---|
| Model ID `gemini-3-pro-image-preview` | `gemini-3-pro-image`, GA 2026-05-28; preview ID deprecated and shut down 2026-06-25 | https://ai.google.dev/gemini-api/docs/changelog · https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image |
| References "5 humans, 6 objects" (+ general slots) | Up to 6 object, 5 character, 3 style (14 total) | https://ai.google.dev/gemini-api/docs/image-generation |
| Thinking mode "automatic" | Always on, cannot be disabled; up to two interim thought images; thinking tokens billed | image-generation guide |
| Resolutions 1K/2K/4K | Unchanged; 1K is the default, uppercase K required, no 512px on Pro | image-generation guide |
| Google Search grounding "Gemini 3 Pro exclusive", `tools=[{"google_search": {}}]` | Supported on Pro and also on Nano Banana 2.1; Interactions syntax `tools=[{"type": "google_search"}]`; Image Search grounding documented only for 2.1 / 3.1 Flash | model page + image-generation guide |
| Context "32K free / 1M pro" tokens, 1,290 output tokens per image | 65,536 input / 32,768 output tokens; image output 1,120 tokens (1K/2K), 2,000 (4K); image input 560 tokens | model page + https://ai.google.dev/gemini-api/docs/pricing |
| "1M token context" in the multi-turn method (best-practices, character example) | Reworded to "one conversation thread" | as above |
| Free tier 15 RPM / 1,500 RPD | No free tier for this model | pricing page |
| No pricing | $2.00/1M in, $12.00/1M text+thinking out, $120/1M image out ≈ $0.134 per 1K or 2K image, $0.24 per 4K; Batch/Flex half; Priority $3.60 / $21.60 / $216 | pricing page |
| `comparison_to_flash` (vs Gemini 2.5 Flash) in parameters.json | Replaced with current Nano Banana lineup (Pro · 2.1 · 2 Lite · deprecated 2) | changelog + image-generation guide |
| API config `image_config` | Interactions API `response_format.aspect_ratio` / `image_size` (current first-party examples) | image-generation guide |
| — | Added a short "Which Nano Banana?" table to SKILL.md so users route to Pro vs the 2.1 skill | changelog + image-generation guide |
| Aliases `nano-banana` | Added `gemini-3-pro-image`, `nano-banana-pro` (none removed) | — |

Still unverified (marked in parameters.json):
- Full aspect-ratio list for Pro — the guide prints no Pro table; only 1:1, 5:4, 16:9 appear in Pro examples. The standard 10-ratio set is kept as expected. Panoramic 1:4/4:1/1:8/8:1 are documented for 2.1 only.
- Thinking levels for Pro (the guide's thinking-level table does not list Pro).
- Whether the older generateContent `image_config` / `{"google_search": {}}` shapes still work; output MIME type; Gemini-app plan limits.
- Vertex / Gemini Enterprise Agent Platform model page is client-rendered and could not be read.
- Not changed (craft, flagged for a later pass): examples bind references as "Image 1 / Image 2"; Google's own examples bind by content + role ("the attached napkin sketch as the structure…").

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

- **Skill Version:** 1.2
- **Model Version:** Gemini 3 Pro Image, `gemini-3-pro-image` (GA 2026-05-28)
- **Aliases:** nano-banana, gemini-3-pro-image, nano-banana-pro
- **Last Updated:** 2026-10-19 - Fact refresh (model ID, reference split, thinking, pricing, lineup); see Update section above.
- **Last Updated:** 2026-07-23 - Removed the mandated aspect-ratio/orientation sentence slot from the prompt formula; ratio/resolution now live only in Configuration notes, never in the prompt prose.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
