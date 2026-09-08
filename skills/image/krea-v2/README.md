# krea-v2 — build notes

Human-facing build notes.

**Built:** 2026-08-11 · **Skill version:** 1.0 · **Model:** Krea 2 (Krea AI), released 12 May 2026

**No reference-token syntax of any kind.**

---

## No literal token form — because there is none

This is where a skill records its reference-token syntax. Krea 2 has none.

**No `@Image1`, no `<IMAGE_1>`, no brackets, no prose role-assignment convention.** Confirmed by absence
across every first-party source: `prompting.md`, the user guide, the developer guide, and the OpenAPI
schemas on all three endpoints. Nothing addresses a reference from prompt text.

Every reference is a **separate attachment** — `image_style_references` (URL), `moodboards` (UUID),
`styles` (UUID, trained LoRA) — each with a numeric strength, bound outside the prompt.

This is absence in its purest form: not "undocumented," but structurally absent. The upstream research
draft was essentially right about this but never stated it plainly enough to act on, so `SKILL.md` and
`continuity-and-references.md` both lead with it.

---

## Research corrections

The upstream research draft for this skill was **the most accurate of the image drafts**, but it
missed a whole mode and two first-party conflicts.

### 🔴 Missing mode — image-to-image

The file states Krea 2 is text-to-image only and lists no editing mode.

**`krea-2/medium` and `krea-2/large` both accept `image_url`** — *"Optional source image for
image-to-image generation. When provided, generation starts from this image instead of pure noise"* —
plus **`strength`** (0–1, default **0.99**, *"0 keeps the input image, 1 fully replaces it"*).

`krea-2/medium-turbo` does **not** have these fields.

A whole capability absent from the research. The 0.99 default is also a trap worth flagging: it is very
nearly a full replacement, which is why image-to-image on this model often feels like the source was
ignored.

### Other corrections

| Widely published claim | Actual |
|---|---|
| *"The only required field is the text `prompt`; everything else is optional and defaults to preset values"* | **`required: [prompt, aspect_ratio, resolution]`** on all three schemas. Omitting either returns 400. **No server-side defaults** |
| `image_style_references` "up to 4 images"; "some third-party tools report up to 5" | API allows **`maxItems: 10`**. The 4 is the **UI** limit. The "up to 5" claim is unsupported by anything |
| Turbo "roughly 2 seconds" / "Fastest (~2 seconds)" | **~4 seconds per generation**, first-party. "Medium/Large: 15 seconds or less" appears nowhere first-party |
| "Batch size — up to 4 images per generation" listed as an API parameter | **No `n`/batch parameter exists.** 4 is a UI figure |
| — *(not mentioned)* | **Deprecated aliases already expired**: `presetStyles` → `styles` and `imageStyleRefs` → `image_style_references`, accepted only until **2026-06-19**. Legacy camelCase tooling now 400s |
| — *(not mentioned)* | **Medium Turbo pricing**: $0.015 / $0.0175 / $0.02 |

### Two genuine first-party conflicts — recorded, not silently resolved

Krea's own pages disagree with Krea's own schema in two places. Both are documented in
`parameters.md` rather than picking a winner quietly.

**1. `creativity` default.** User guide and developer overview both say `medium (default)`. **The
OpenAPI schema on all three endpoints says `default: low`.** The skill's guidance is to set it
explicitly, which sidesteps the question — and is better practice anyway.

**2. `image_style_references.strength` range.** Schema: `minimum: 0, maximum: 1, default: 0.5`. The
style-transfer prose page says *"between -2 and 2 per reference."* That −2…2 range is what the schema
actually assigns to **`styles`** (LoRAs) — the prose page appears to have copied the wrong range. Trust
the schema.

Same shape for moodboards: schema `0–1, default 0.23`; prose page *"between -0.5 and 1.5 … start around
0.35."* Use the schema.

Interestingly the research draft's "0.0–1.0 (shown as 20%–80% in UI)" was **closer to right than Krea's
own prose page** on this one.

### Sourcing problem

The research draft's **entire parameter table** is cited to `developers.cloudflare.com/ai/models/krea/` —
**Cloudflare Workers AI, an aggregator**, not Krea. The values are mostly right, but first-party
equivalents exist and now replace it.

Similarly, its core "flowing prose, avoid 'In this image…'" guidance leans on a **Hugging Face user
discussion thread** (`/discussions/4`), not Krea's model card. The guidance itself checks out against
`prompting.md`, so it survives — with better sourcing.

### Unverifiable — dropped or flagged

- **"12-billion-parameter."** Third-party sourced (an NYU page); not stated in the technical report
  sections reviewed. Not load-bearing — dropped from the skill, noted in `parameters.md`
- **Moodboard "taste profile" / "keywords" / "avoids" list.** From Krea's blog; the moodboards
  *developer* doc exposes only `id` + `strength`. If the skill told users to write an "avoids list,"
  that would need re-verifying — it doesn't
- **Diffusers step/CFG values** (28 steps @ 4.5, 8 steps @ 0.0) — HF diffusers docs for the
  open-source checkpoints. **Irrelevant to the hosted API**, which exposes neither parameter
- **"3–6 short comma-separated phrases for Turbo"** and **"the Chinese Text Trap"** — YouTube and blog
  sourced. Not carried
- **Turbo "ignores negative instructions because CFG 0"** — community-sourced, and moot: the hosted API
  has no negative field at all

### Confirmed and carried through

Three hosted variants and their endpoint names; two open-source checkpoints (RAW undistilled, Turbo
8-step) genuinely shipped on HF and GitHub; the 8 aspect ratios with pixel dimensions including
`2.35:1` → 1568×672; `creativity` enum; the three sliders at −100…100 default 0; `resolution` hosted =
`1K` only with open-source Turbo to 2K; one moodboard per request; no negative field; tier pricing and
the non-stacking rule; the architecture (Qwen 3 VL text encoder, Qwen Image VAE, FLUX 2 AE).

**And the headline one:** *"For text rendering, we recommend putting quotes around the words to be
rendered."* **Genuinely first-party** — Krea states the convention themselves, rather than it being
inferred from community write-ups.

---

## Capability findings

**No scripted dialogue** — image model, no speech. Trivial here, unlike the video models where it took
real judgement.

**No structured JSON prompt format.** Krea documents flowing natural-language prose only;
exactly one prose field, `prompt`.

**No reference-token mechanism** — see above. Structurally absent, not merely undocumented.

**No published prompt-length cap.** Krea publishes no cap, and the `prompt` field is an unconstrained
string in the schema. Rather than invent a figure, that is stated in `parameters.md` instead — the
same position taken on FLUX 3 Video, Seedance 2.5, Grok Imagine Video 1.5 and Qwen-Image 3.0.

**No negative-prompt parameter.** No field, and `additionalProperties: false` means adding one is
*rejected* rather than ignored.

**No storefronts named.** Cloudflare Workers AI and Hugging Face appear in this README
only as sourcing labels.

---

## Routing position

**Reach for Krea 2 when the look matters more than the likeness.** Its taste controls — moodboards,
style references, and three aesthetic sliders — make it unusually good at holding a consistent
aesthetic across many images without spending prompt on it. For environments, props, establishing
images and anything where a project needs a coherent visual identity, it is a strong choice.

**Route away when:**

- **A named character must recur across many images.** No identity mechanism exists. Style references
  transfer look, not likeness. GPT Image 2 (16 refs), Gemini 3 Pro Image (14 refs, prose role
  assignment) or Phota (trained identity profiles) all bind likeness properly. A trained
  LoRA via `styles` is the only in-model option and requires training
- **Output above 1K.** The hosted API offers 1K only. The open Turbo checkpoint reaches 2K — that is
  self-hosting
- **Precise per-subject placement.** Seedream 5.0 supports structured positioning
- **Negative prompting.** No field, and unknown properties are rejected

---

## Integration implications

1. **Three required fields with no defaults.** `prompt`, `aspect_ratio`, `resolution` — omitting either
   of the latter two returns 400. Most image APIs default both, so a generic image-request builder will
   fail here.
2. **`additionalProperties: false`.** Unknown fields are *rejected*, not ignored. Any shared request
   shape carrying extra keys across models will fail on Krea specifically.
3. **The camelCase aliases expired 2026-06-19.** If an integration was written against older Krea docs,
   `presetStyles` and `imageStyleRefs` now 400. Worth grepping for.
4. **Image-to-image is tier-dependent.** Offering it on Medium Turbo will fail — Medium and Large only.
5. **The `creativity` default is genuinely ambiguous** between Krea's guide and its schema. An integration
   should set it explicitly rather than relying on the server default.
6. **API and UI ceilings differ** for style references (10 vs 4). If an integration mirrors the UI
   limit it is leaving capability unused.

---

## Open questions

1. **`creativity` default** — schema says `low`, docs say `medium`. A single empirical test with the
   field unset would settle it, and would be worth reporting to Krea.
2. **`image_style_references.strength` range** — the −2…2 figure on Krea's prose page looks like a
   copy error from the `styles` field, but that is inference. Testing a negative value would confirm.
3. **`seed`** was not present in the reviewed schema. Whether reproducibility is available at all is
   unconfirmed; if it is, `continuity-and-references.md` gains an option.
4. **Moodboard internals** — the blog describes keywords and an "avoids" list; the developer doc exposes
   only `id` and `strength`. Whether those are authorable and whether they affect generation is worth
   checking before advising anyone to build one a particular way.
