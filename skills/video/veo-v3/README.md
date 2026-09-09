# veo-v3 — build notes

Human-facing build notes.

**Model:** Veo 3.1 (Google DeepMind) · **Skill version:** 1.2 · **Last content pass:** 2026-08-11

---

## The literal token form

**There isn't one.** Recorded here as prominently as the models that *do* have one, because the absence
is the fact most likely to be got wrong.

Google documents no in-prompt reference token of any kind — not `@Image1`, not `<IMAGE_1>`, not a bare
ordinal. References bind through the `referenceImages[]` API array with a `referenceType` of
`character` or `asset`, and every first-party example **re-describes** the subject in prose.

Compare across the catalogue, where `numbered` alone covers five incompatible literal forms:
`@Image1` (seedance-v2), `@Image 1` *spaced* (seedance-v2-5), `<IMAGE_1>` (grok-imagine-video-v1-5),
`<IMAGE_REF_0>` *zero-indexed* (gemini-omni-flash), `<Subject N>` / `<Picture N>` *typed* (minimax-h3),
`[Image 1]` (happyhorse-v1, Qwen-Image). Veo is in none of them.

---

## Research corrections

**The reference-token convention was wrong, and it was live.** This skill previously declared numbered
tokens with the comment "Veo binds up to 3 reference images, addressed positionally (@Image1,
@Image2…)". Google documents nothing of the kind.

The correction was first filed as low-priority on the assumption that the declaration was inert. That
was also wrong — it was being read, and Veo prompts had been carrying a reference-token instruction the
model has no way to honour. Now corrected, and pinned by a test.

A prose convention was considered and rejected. That applies to models documenting a role-assignment
*convention* — Luma's `IMAGE1 (CHARACTER)`, OpenAI's `"Image 1: product photo…"`, BFL's "subject from
image 1". Google documents none, so what remains is ordinary scene description with the real role
assignment living in the `referenceType` API field.

**No structured JSON prompt format.** Google documents a prose formula and timestamp prompting, both plain text.
The "Veo 3 JSON prompting" templates circulating online are community inventions; the request body
being JSON is transport, not a prompt format.

**No length ceiling asserted.** The token limit is 1,024 (~7,500 characters) but the useful
number is Google's 100–180 word sweet spot, which is prose guidance rather than a cap. Following the
convention that the cap is a ceiling and not a target, the ceiling is documented in `parameters.md` and
the target is taught in the body.

---

## Capability findings

**Content pass 2026-08-11.** `parameters.json` → `parameters.md` (a bare JSON file cannot carry the
resolution/duration coupling, the storage-window trap, or a "what Google does not publish" section);
`examples/comprehensive-examples.md` → `examples.md`; `continuity-and-references.md` written from
scratch, since the reference mechanism is this model's biggest trap and had no dedicated file.

`### Parameter Strategy` was removed from the prompt body — resolution and duration tables are
`parameters.md` material — and replaced with a `## Suggested Settings` section plus the standing rule
that settings never appear in prompt text.

---

## Open questions

1. **Two-day storage on extension chains** is documented but the reset-on-reference behaviour is worth
   testing before relying on it for a long sequence built over several days.
2. **4K is listed as Veo 3.1 Preview only** in the source research. Whether that gating still applies
   was not re-verified in this pass.
3. **Pricing is not in the model docs** and moves independently on the Vertex AI pricing page, so it is
   deliberately absent rather than captured as a stale number.

---

## Skill Metadata

**Trigger Contexts:**
- When user requests video generation with audio
- When cinematic camera work is priority
- When character consistency across video shots is needed
- When professional cinematography aesthetic is required

**Primary Use Cases:**
- Narrative short films and scenes
- Commercial video content
- Character-driven storytelling
- Cinematic establishing shots
- Dialogue scenes with lip-sync
- Extended video sequences (up to ~148s)

**Optimal Workflow:**
1. Generate initial 8s clip with reference images
2. Review and identify best take
3. Extend video by 7s increments if longer sequence needed
4. Use consistent references and seed for related shots

---

## Integration Notes

### When driven from structured scene data

When generating prompts from structured scene records:
- Extract character descriptions from character records
- Pull environment details from location records
- Translate shot parameters to Veo cinematography terms
- Apply theme-specific lighting and style to ambiance element
- Use character reference images for subject consistency
- Leverage scene dialogue for audio specifications

### Reference Image Workflow

**Character Consistency:**
1. Upload 1-3 high-quality character reference images
2. Set `referenceType: "character"`
3. Maintain same references across all shots in sequence
4. Keep character descriptions consistent in text prompts

**Style/Environment Consistency:**
1. Upload location concept images
2. Set `referenceType: "asset"`
3. Use for establishing shots and environment continuity

### Video Extension Strategy

For longer sequences (multi-shot scenes):
1. Generate initial 8s anchor shot at 720p
2. Extend by 7s describing next action: "The detective stands, walks toward window..."
3. Continue extending up to 20 times (~148s total)
4. Videos stored 2 days (timer resets when referenced)

### Multi-Shot Scene Building

For scenes with multiple shots:
1. **Establish with hero shot** - Primary character/environment with references
2. **Use same references** - Maintain across all shots in scene
3. **Consistent style language** - Keep lighting/mood descriptors identical
4. **Sequential extension** - Build longer sequences through extension vs separate clips
5. **Seed consistency** - Use same seed for deterministic results

---

## Version Information

- **Skill Version:** 1.0
- **Model Version:** Veo 3.1 (Released October 2025)
- **Aliases:** veo3
- **Last Updated:** 2026-02-11

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
