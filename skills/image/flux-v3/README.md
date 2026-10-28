# flux-v3 — build notes

Human-facing build notes. Not loaded as part of the skill.

**Built:** 2026-10-18 · **Skill version:** 1.0 · **Model:** FLUX 3 Image (Black Forest Labs)

---

## Research verification

Corrections:
- safety_tolerance range 0–4 → 0–7 (route/org sets max; 422 lists allowed) — docs.bfl.ai/api-reference/utility/generate-an-image-with-flux-3
- aspect_ratio auto: a ratio requested in the prompt takes precedence over image 1 — same source
- Edit rows: added `kind` field (new / anchor / move) present in current BFL bbox examples — docs.bfl.ml/flux_3/flux3_image_bounding_boxes
Unverified: per-reference 256px/16MP limits (from BFL guide, not in API schema); removal row shape; `hidden` field behaviour.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
