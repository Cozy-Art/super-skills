# recraft-v4 — build notes

Human-facing build notes. Not loaded as part of the skill.

**Built:** 2026-10-18 · **Skill version:** 1.0 · **Model:** Recraft V4 / V4.1 (Recraft)

---

## Research verification


Corrections:
- Image-to-image: research implied style_id/style refs usable alongside → style, style_id, style_match, negative_prompt, text_layout are V3-only on /images/imageToImage; strength is required with no default; model default recraftv4_1; accepts V3/V4/V4.1 raster or vector; Flash unsupported; upload limits PNG/JPG/WEBP/SVG <20 MB, ≤16 MP, sides 256–4096 px — https://www.recraft.ai/docs/api-reference/tools/image-to-image.md
- Model list incomplete → added recraftv4_styles (+_pro), recraftv4_1_pro, recraftv4_1_utility (+_pro), `_raster` alias; default is recraftv4_styles when style refs are attached and no model given — https://www.recraft.ai/docs/api-reference/models/overview , /appendix
- Pricing gaps → V4.1 $0.035 / Pro $0.21; V4 Styles $0.035 / vector $0.05 / Pro $0.10 / Pro vector $0.12; style references +$0.005/request; pricing page lists image-to-image only under V3 — https://www.recraft.ai/docs/api-reference/pricing
- Temporary URL lifetime unspecified → ~24 hours — https://www.recraft.ai/docs/llms-full.txt
- `style` on V4 → only base style `any` (docs inconsistent; advise omitting); style created with recraftv4_styles is bound to that model — llms-full.txt
- style references limits → 1–10 images, ≤64 MB total; JSON field `style_reference_urls`, multipart `style_references`; combining with style_id rejected; POST /v1/styles creates reusable style ($0.005) — llms-full.txt
- Added: vector-enforcing endpoint /images/generations/vector; vector models accept ratio-form size only; POST /v1/prompts/enhance (≤2,000 chars, $0.01); base URL + Bearer auth — llms-full.txt, appendix
- Confirmed (no change): 10,000-char prompt limit, 14-ratio size table, n 1–6, controls.colors ≤10 with weights ≤1.0 sum, V3-only negative_prompt/text_layout/artistic_level/no_text, V4 $0.04/$0.08/$0.25/$0.30, Flash $0.007 ~1.3 s, Flash released Sept 23 2026, V4 Styles Aug 27 2026 — changelog https://feedback.recraft.ai/changelog

Unverified (marked in skill):
- V4 ~10 s and V4 Pro ~30 s latency
- recraftv4_styles_vector exact id
- Image-to-image price for V4 tiers
- Using /imageToImage with recraftv4_pro at low strength as a 1K→2K composition-preserving handoff
- V4.1 release month (May 2026, from research) — not stated in skill

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
