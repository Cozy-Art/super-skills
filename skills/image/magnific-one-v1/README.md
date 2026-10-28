# magnific-one-v1 — build notes

Human-facing build notes. Not loaded as part of the skill.

**Built:** 2026-10-18 · **Skill version:** 1.0 · **Model:** Magnific One (Magnific)

---

## Research verification

- **Model:** Magnific One (Magnific, launched Oct 8 2026; no prior versions). Endpoint `POST https://api.magnific.com/v1/ai/magnific-one`.

## Verified (matches research)
- All 8 API fields, enums, defaults, 1–2000 char prompt, additionalProperties false, `x-magnific-api-key` header, 1–10 public reference URLs, Draft billed once at medium/2k, tiles 8 (2x4, exact only 1:1/2:3/3:2/3:4) vs 16 (4x4, all exact) — https://docs.magnific.com/api-reference/text-to-image/magnific-one/generate , /overview , https://docs.magnific.com/changelog/2026
- UI Draft 4/8/16, Final default 2K High up to 4K/Max, Style tab 1–5 refs, the eight corrective lines, control-dial example — https://www.magnific.com/prompts/magnific-one
- Credit costs 180/250/600/1000 (High/Max x 2K/4K) — VentureBeat launch article

## Corrections / additions to the research
- Research said exact pixel dims unpublished → prompting guide shows 2K High @ 3:4 = 1536×2048 (added as the one known data point) — magnific.com/prompts/magnific-one
- Research gave no response schema → added `data.task_id/status/generated`, status enum CREATED/IN_PROGRESS/COMPLETED/FAILED, `GET /v1/ai/magnific-one/{task-id}` polling, list endpoint, 503 backoff — docs generate/overview pages
- Brand Kit: research didn't note limits → Brand Kit doc says Final-only with Magnific One, up to 5 reference images alongside the kit (2 usually best), sources include ZIP, does NOT guarantee exact typography/colour values/placement; used in Image Generator, Spaces, Designer, agent; no API field documented — https://www.magnific.com/ai/docs/brand-kit
- Draft tile counts in app are inconsistent across official pages: product page says 8 or 16, prompting guide says 4/8/16 → skill states 4 is app-only; API is 8/16 — magnific.com/one vs /prompts/magnific-one
- Research presented "light-only edit"/"composition lock" lines as edits → clarified that the API has no source-image field (reference_images = style only), so those lines are true edits only in the app
- Pricing figures come from VentureBeat, not the official pricing page (Magnific credits doc says the interface always shows exact cost) → labelled as launch figures, confirm in UI

## Unverified / left soft
- Full verbatim wording of the "light-only" and "composition lock" corrective lines (official page only partially quoted on fetch; research wording kept)
- API dollar pricing per quality/resolution (not published on fetched pages)
- Result URL lifetime, output file format, alpha, colour profile
- Video Generator first/last-frame specifics (kept generic: "depends on the chosen video model")
- Whether Brand Kit is usable via MCP/API

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
