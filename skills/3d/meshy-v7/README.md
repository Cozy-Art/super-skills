# meshy-v7 — build notes

Human-facing build notes. Not loaded as part of the skill.

**Built:** 2026-10-18 · **Skill version:** 1.0 · **Model:** Meshy 7.1 (Meshy)

---

## Research verification

- **Model:** Meshy 7.1 (`ai_model: meshy-7.1`; `latest` resolves to it; `meshy-7` deprecated). Covers Text to 3D (preview/refine), Image to 3D, Multi-Image to 3D, Retexture, Remesh, Smart Topology, Rigging, Animation, Text to Motion.

## Corrections to the research

- Smart Topology default model: research said `meshy-t2` (100–15,000, def 4,000) → `meshy-t2.5` added 15 Oct 2026 and is now the default (100–30,000, def 15,000); lowpoly migration target updated. https://docs.meshy.ai/en/api/changelog , https://docs.meshy.ai/en/api/image-to-3d
- Image inputs: research said JPG/JPEG/PNG → also `.webp`, max 20 MB per image. https://docs.meshy.ai/en/api/image-to-3d
- `multi_view_thumbnails`: research presented it as a general option (and used it in the multi-image example) → docs say it applies only when `auto_size: true`. https://docs.meshy.ai/en/api/multi-image-to-3d
- `remove_lighting`: research said 7.1 ignores it only on Text to 3D Refine → also ignored by 7.1 on single Image to 3D and Retexture (only meshy-6 acts on it); Multi-Image docs list it as supported for 7.1 (doc inconsistency noted in skill). https://docs.meshy.ai/en/api/image-to-3d
- Retexture: research implied 7.1 ecosystem → Retexture `ai_model` is `meshy-6-lite`/`meshy-6`/`meshy-7`/`latest` (= Meshy 7); `multiview_image_urls` requires `meshy-7`; style fields are `text_style_prompt`/`image_style_url`; added `enable_original_uv`. https://docs.meshy.ai/en/api/retexture
- Release date: research mixed Sep 10 → web app launch 10 Sep 2026 (blog); API `meshy-7.1` + `geometry_resolution` added 18 Sep 2026 (changelog). https://www.meshy.ai/blog/meshy-7-1-launch
- Asset retention (missing in research): API assets kept max 3 days for non-Enterprise; signed URLs expire; re-sending expired URL = 400. https://docs.meshy.ai/en/api/asset-retention
- Rigging limits (missing in research): textured humanoid only, ≤300k faces via task ID, `model_url` GLB only, face +Z, `height_meters` default 1.7, 5 credits, 422 on pose failure. https://docs.meshy.ai/en/api/rigging
- Remesh: `target_formats` default `["glb"]` and includes `blend`; resize/convert fields deprecated. https://docs.meshy.ai/en/api/remesh
- Multi-Image has no `model_type` (no Smart Topology). https://docs.meshy.ai/en/api/multi-image-to-3d
- Additional deprecated no-op field `surface_mode` (Image to 3D). Added.
- Pricing confirmed and expanded (Image/Multi 7.1: 20 / 30 / 35; Remesh/Rig/UV 5; animation 3 per action). https://docs.meshy.ai/en/api/pricing
- Official webapp prompting guide gives no word-count target; 20–60 words kept as a practical heuristic (from help-center article cited by research). It endorses short "no floating parts"-style exclusions. https://docs.meshy.ai/en/webapp/guides/prompting

## Unverified / caveats

- "Up to ~80M triangles raw at 4K" is Meshy's own blog claim (kept, attributed).
- Reference-image prep figures (≥1024², 70–90% fill, 512 minimum) come from help-center articles not re-fetched.
- Single `action_id` animation cost (3 credits) inferred from per-action rate.
- Multi-Image `remove_lighting` behavior on 7.1 is inconsistent across doc pages.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
