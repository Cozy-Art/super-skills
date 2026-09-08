# qwen-image-v3 — build notes

Human-facing build notes.

**Built:** 2026-08-11 · **Skill version:** 1.0 · **Model:** Qwen-Image-3.0 (Alibaba), released 21 July 2026

> ⚠️ **PROVISIONAL — flagged for re-research.** A follow-up research pass is scheduled on this
> model. This build is corrected against Alibaba's real API surface, but several widely-quoted
> capability figures could not be confirmed and are deliberately absent. The "Unverified" section below
> is the concrete diff for that follow-up to work against.

---

## The literal token form

**Bare numbers or square brackets, matching array position.** Alibaba documents both, verbatim:

> *"Image numbers in prompts correspond to array position: the first image is 'image 1', the second is
> 'image 2'. **You can also use markers like '[image 1]' and '[image 2]'**."*

Casing is not load-bearing — the same page uses `Image 1` in its own examples. Role assignment across
references is the intended use: *"The girl in Image 1 wears the black dress from Image 2 and sits in the
pose from Image 3."*

Across other models: `@Image1` (Veo 3.1 — **now corrected to no token at all** — and Seedance 2.0),
`@Image 1` spaced (Seedance 2.5), `<IMAGE_1>` (Grok Imagine Video 1.5), `<IMAGE_REF_0>` zero-indexed
(Gemini Omni Flash), `<Subject N>` typed (MiniMax H3), `[Image 1]` (here, HappyHorse 1.0, Qwen-Image
2.0). All positional. None interchangeable.

### 🔴 v1.0 shipped this wrong — corrected same day

**v1.0 declared that no reference-token convention existed**, on the basis that Alibaba's API
reference documents only positional array binding: *"When multiple images are provided, the order is
defined by the array sequence."*

That was an **incomplete read**. The marker documentation lives in Alibaba's **editing guide**
(`help.aliyun.com/en/model-studio/qwen-image-edit-guide`, "Image input order"), not the API reference.
Every code sample on that guide page uses `qwen-image-3.0-pro`, its model-recommendations section lists
only the 3.0 models, and Alibaba's own model-selection page routes 3.0 editing users to it.

The error surfaced from an unrelated direction: verifying Qwen-Image 2.0 found Alibaba documenting
`[Image 1]` markers for **2.0**, which made a bare `null` for 3.0 look more like a documentation gap
than a design difference. It was.

**What changed in the fix:** that call, plus the reference sections in `SKILL.md`,
`continuity-and-references.md` and `best-practices.md` — all of which previously told users *not* to do
role assignment, which Alibaba's own examples do. Examples 4 and 5 were rewritten to use markers.

**The lesson worth keeping:** on this vendor, the API reference is not the complete surface. Two
first-party pages differed in completeness, and checking only the more authoritative-sounding one
produced a wrong answer that read as well-sourced.

---

## Research corrections

The upstream research draft for this skill was **the weakest of the set**, and the failure is
systematic rather than incidental: **its entire parameter table describes Runware's API, not
Alibaba's.**

### 🔴 Every field name is wrong

| Widely published (Runware) | Actual (Alibaba) |
|---|---|
| `positivePrompt` | `{"text": "…"}` inside `input.messages[0].content` — **there is no field named `prompt`** |
| `negativePrompt` | `parameters.negative_prompt` |
| `promptExtend` | `parameters.prompt_extend` |
| `inputs.referenceImages` | `{"image": "…"}` objects in the same content array |
| `width` + `height` integers | `parameters.size` as a **`"width*height"` string** |
| — *(omitted)* | `parameters.watermark`, boolean, default `false` |

### 🔴 CFG and inference steps do not exist

The draft's parameter table lists *"Guidance scale / CFG … 0–20, ~5"* and *"Inference steps … 1–50,
~28"*, with a *"recommended combination for most production work: guidance scale 4.0–5.0, 40–50
steps."*

**Neither parameter is in the API.** The complete `parameters` object is six fields: `prompt_extend`,
`n`, `size`, `negative_prompt`, `seed`, `watermark`.

Those values were carried over from **open-weight Qwen-Image v1 / 2512** guides — different, earlier
models — cited to Segmind, fal and CivitAI. The "recommended combination" is unusable.

### Other corrections

| Widely published claim | Actual |
|---|---|
| Two variants, `qwen-image-3.0` and `-3.0-pro` | *"The currently available model is `qwen-image-3.0-pro`."* **One.** The base/pro split is cited to `docs.qwencloud.com`, **not an Alibaba domain** |
| Pixel budget to 6,553,600; drops to 2,250,000 with references; "Invalid image pixels" error | **512×512 to 2048×2048 for BOTH T2I and I2I — no drop.** Those figures and that error string are **Runware platform limits** |
| Default size 1024×1024 | **No default.** *"If not specified, the model automatically recommends a resolution based on the prompt"* |
| Seed: "any integer" | **0 – 2,147,483,647** |
| File formats "not explicitly documented for 3.0" | **Documented: PNG output**, URL valid 24 h. Input: JPG, JPEG, PNG, BMP, TIFF, WEBP, GIF; 384–2048 px per side, ≤10 MB |
| `prompt_extend` "true/false, varies by platform" | **Defaults to `true`**, and Alibaba recommends it. Load-bearing — the file's whole reproducibility section depends on knowing this |

### 🔴 The hard constraint the file missed entirely

> *"Only one text object is allowed. Omitting it or providing multiple text objects will result in an
> error."*

**Exactly one prose field per call, named `text`.** The `LAYOUT:/HEADER:/COLUMN:` brief in the research
draft's example #7 is a writing convention *inside* that one string — the draft presents it as though
it were structure. It is not, and an integration that tried to emit separate text objects per section
would error.

This is also why no structured output format is defined: one prose field, hard-enforced.

### Dropped as unsourced

- *"this alone reportedly raises spelling accuracy from ~65% to ~85%."* Cited to a CivitAI article about
  **Qwen-Image-2512 — a different model** — and unsourced within that article
- *"Community day-one testing still flags photorealistic human portraits as comparatively weak."*
  Third-party

---

## Unverified — the diff for re-research

**The headline number could not be confirmed.** The **~4,500 token** prompt limit (and the "~1,000 for
2.0" comparison) appears **nowhere in Alibaba Cloud Model Studio's API reference** — the only
first-party document retrievable. Every instance traces to Qwen's launch post *as relayed by third
parties*; the draft's own citation is `qwe.edu.pl`, a tutorial site.

`qwen.ai/blog?id=qwen-image-3` returns a JavaScript shell with no article text, and
`qwenlm.github.io/blog/qwen-image-3/` returns empty. **Opening the Qwen blog post in a real browser is
the single highest-value action for the re-research pass** — it likely resolves the token limit and the
capability figures below in one go.

**Also unconfirmed, all launch-marketing-relayed:**

- 12-language text rendering
- 20+ fonts
- 100+ styles
- ~10 px minimum legible text size

**The status caveat still holds as of August 2026:** no open weights, no technical report, no model
card, no independent benchmarks. A search of the Qwen Hugging Face org returns no 3.0 repository — only
`Qwen/Qwen-Image` and `Qwen-Image-Edit-2511` plus community forks. The model is in **limited preview**
requiring Model Gallery application.

**The double-quote text convention** is **not documented first-party for 3.0.** Alibaba's API reference
says nothing about quoting. It *is* documented on Runware (secondary) and it works — the skill teaches
it while labelling the sourcing. Contrast Krea 2, where the same convention is genuinely
vendor-documented.

---

## Capability findings

**A real negative-prompt parameter.** `negative_prompt` is documented first-party by Alibaba. Worth
flagging because it inverts the usual advice: the habit of phrasing everything positively, correct on
every model that lacks the field, is unnecessary here, and `best-practices.md` says so explicitly.

**Numbered reference tokens** — corrected from v1.0, which declared none. See above.

**No structured JSON prompt format.** Hard-enforced single prose field. The API request body is JSON,
which is transport only.

**No published prompt-length cap.** The 4,500-token figure is unconfirmable first-party, so it is
stated in `parameters.md` rather than asserted as spec — the same position taken on FLUX 3 Video,
Seedance 2.5, Grok Imagine Video 1.5 and Krea 2.

**No scripted dialogue** — image model.

**No storefronts named.** Runware appears in `parameters.md` and this README **only as a
sourcing label**, to explain where the wrong field names came from.

---

## The finding worth carrying to other skills

**A default-on prompt-expansion stage silently defeats seed reproducibility.**

`prompt_extend` defaults to `true`. A seed only reproduces a result if the prompt reaching the model is
identical each run — and expansion regenerates it. So a pipeline that fixes a seed *appears*
reproducible and is not.

This is structurally the same as Grok Imagine Video's upsampler, but with a sharper consequence: Grok
has **no seed at all**, so nothing is silently broken. Here there is a seed, and it appears to work.

**More than one model here has a documented prompt-rewriting stage.** Worth checking whether
others do — it changes prompting advice (specificity becomes a constraint on the rewrite) and, where a
seed exists, it changes what reproducibility means.

---

## Routing position

**Reach for Qwen-Image-3.0 for text-heavy and layout-heavy work** — posters, signage, multi-element
design — and when a working negative prompt is worth having. The Qwen Image family's text rendering is
its reason to exist, and the negative-prompt support is a reason on its own.

**Route away when:**

- **A named character recurs across many images.** No identity mechanism; no LoRA path (no open
  weights); three-reference ceiling. GPT Image 2 (16 refs), Gemini 3 Pro Image (14 refs) or Phota
  (trained profiles)
- **More than three references** are needed
- **Above 2048×2048**
- **Production-critical work.** Limited preview, no published documentation beyond the API reference,
  behaviour may change without notice
- **Project-wide aesthetic consistency across many images.** Krea 2 moodboards do this better

**Against Qwen-Image 2.0:** the predecessor covers Qwen-Image v1, 2512 and 2.0/2.0-Pro, has
**open weights** and a LoRA/ControlNet ecosystem, and is not a limited preview. For anything needing
fine-tuning, structural control or dependability, 2.0 remains the better choice. This skill is for 3.0's
improved text and layout work specifically.

---

## Integration implications

1. **There is no `prompt` field.** A generic image-request builder writing `prompt` will fail. The text
   goes in `input.messages[0].content` as a `{"text": …}` object.
2. **Exactly one text object, enforced.** Emitting one per logical section errors.
3. **`size` is a `"width*height"` string**, not integer `width`/`height`.
4. **`prompt_extend` defaults true, and silently defeats seeds.** If an integration exposes a seed control
   for this model, it should force `prompt_extend: false` when a seed is set, or warn. Otherwise it
   promises reproducibility it does not deliver.
5. **No default `size`.** For deliverables an integration should always set it rather than letting the model
   choose, or output dimensions will vary within a set.
6. **CFG and steps do not exist.** Any shared image-request shape carrying them will need them stripped.

---

## Open questions

1. **The Qwen blog post** — JS-rendered and unretrievable here. Highest-value action for the
   re-research pass; likely resolves the token limit and every capability figure at once.
2. **Does the 4,500-token limit exist at all?** Unconfirmed in either direction.
3. **Has anything shipped since?** Open weights, a technical report, or a model card would change this
   skill's provisional status materially. Worth checking the Qwen HF org at re-research time.
4. **Is the double-quote convention actually vendor-documented anywhere** for 3.0? Only found on a
   third-party platform.
5. **Does `seed` reproduce reliably with `prompt_extend: false`?** Assumed, not tested. The whole
   reproducibility guidance rests on it.
