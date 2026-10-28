# nano-banana-v2-1 — build notes

Human-facing build notes. Not loaded as part of the skill.

**Built:** 2026-10-19 · **Skill version:** 1.0 · **Model:** Nano Banana 2.1 (Google)

---

## Research verification

The research guide was an *update* guide (grammar carries over from Nano Banana 2); most of its footnotes point at third-party pages (Runware, fal, piax.org, ud.com.hk). Load-bearing facts were re-checked first-party.

Confirmed:
- Model ID `gemini-nano-banana-2.1`, GA 2026-10-06; `gemini-3.1-flash-image` deprecated, no shutdown date — https://ai.google.dev/gemini-api/docs/changelog
- Inputs text/image/video/PDF, outputs image/text; 131,072 in / 32,768 out tokens; 1K (default)/2K/4K; thinking minimal / medium (default) / high; up to 14 references (4 character, 10 object); search grounding (Web + Image); Batch supported — https://ai.google.dev/gemini-api/docs/models/gemini-nano-banana-2.1
- `response_format` carries `aspect_ratio` / `image_size` / `mime_type`; uppercase K required; `previous_interaction_id` for multi-turn; `/v1beta/interactions`; no 512px on 2.1 — https://ai.google.dev/gemini-api/docs/image-generation

Corrections:
- Reference binding taught as "image 1 / image 2" positional convention (sourced to Runware/fal) → Google's own 2.1 example binds by content ("An office group photo of these people…") and Google's prompting guide uses "[Reference images] + [Relationship instruction] + [New scenario]" ("Using the attached napkin sketch as the structure and the attached fabric sample as the texture…"). Skill teaches content + role; ordinals as a tiebreaker only — https://ai.google.dev/gemini-api/docs/image-generation · https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana
- Panoramic change described only as "tiling fixed at 2K/4K" → changelog frames it as improved "wide and panoramic aspect ratio generation (1:4, 4:1, 1:8, 8:1) across 1K, 2K, and 4K"; the model card adds the 2K/4K tiling fix — changelog + model card above
- Research gave no pricing → added: $1.50/1M input, $7.50/1M text+thinking, image ≈ $0.0336 (1K) / $0.0504 (2K) / $0.113 (4K); Batch half; no free tier; thought images not charged — https://ai.google.dev/gemini-api/docs/pricing
- Sibling lineup added from first-party: Nano Banana Pro is `gemini-3-pro-image` (GA 2026-05-28; refs 6 object / 5 character / 3 style); Nano Banana 2 Lite is `gemini-3.1-flash-lite-image` (1K only, 14 object refs, minimal/high thinking) — image-generation guide + changelog
- Thinking cannot be disabled on Gemini 3 image models (added) — image-generation guide

Unverified (marked in the skill):
- Full aspect-ratio list for 2.1 — only 1:4 / 4:1 / 1:8 / 8:1 (changelog) and 1:1 / 5:4 / 16:9 / 3:2 (examples) confirmed; the standard 10-ratio set is listed as expected. Pixel-dimension table not retrievable.
- `image/png` output (only `image/jpeg` seen in 2.1 examples); default ratio fallback (1:1) and edit-follows-source behaviour.
- `system_instruction` for image models; image-search grounding sub-option field.
- seed/temperature/topP/topK rejected with an error (secondary source citing Google Cloud docs; Cloud page is client-rendered).
- fal prompt range 3–50,000 characters (wrapper).

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
