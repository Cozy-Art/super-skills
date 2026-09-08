# seedance-v2-5 — build notes

Human-facing build notes.

**Built:** 2026-08-11 · **Skill version:** 1.1 · **Model:** Seedance 2.5 (ByteDance), launched 31 July 2026

**v1.1 supersedes v1.0**, which was built before ByteDance's ModelArk documentation could be
retrieved. Several v1.0 claims were wrong — see "Corrections to v1.0" below. That section is kept
deliberately, because two of the errors were mine rather than the research file's.

---

## Model ID

**`dreamina-seedance-2-5-260628`** — confirmed in ByteDance's published API examples.

The 2.0 family, for routing and for the `seedance-v2` update:

| Model | ID | Duration | Resolution | Refs |
|---|---|---|---|---|
| Seedance 2.5 | `dreamina-seedance-2-5-260628` | 4–30 s | 480p, 720p | 50 |
| Seedance 2.0 | `dreamina-seedance-2-0-260128` | 4–15 s | 480p, 720p, **1080p, 4K** | 15 |
| Seedance 2.0 fast | `dreamina-seedance-2-0-fast-260128` | 4–15 s | 480p, 720p | 15 |
| Seedance 2.0 mini | `dreamina-seedance-2-0-mini-260615` | 4–15 s | 480p, 720p | 15 |

The numeric suffix is a **build tag, not a release date** — see below.

---

## Corrections to v1.0

### 🔴 Mine: I wrongly rejected the real model ID

v1.0 said: *"One SEO site offers `dreamina-seedance-2-5-260628`, whose date suffix predates the launch —
internally inconsistent and not reported."*

**That is the correct model ID**, and it appears verbatim in ByteDance's own curl examples. I read
`260628` as "28 June 2026," noted it preceded the 31 July launch, and treated a correct answer as
evidence of fabrication. The suffix is a build/version tag — the same convention runs across the family
(`260128` for 2.0, `260615` for mini).

**The lesson worth keeping:** skepticism has a false-positive rate. A heuristic that rejects plausible
data on a self-derived inconsistency needs the inconsistency verified before it fires, not assumed.

### 🔴 Mine: resolution was wrong, and inverted

v1.0 said Seedance 2.5 offers **4K**, citing Dreamina's product page, and dismissed the 480p/720p
figure as *"a fal.ai endpoint fact presented as the model's ceiling."*

**Backwards. Seedance 2.5 outputs 480p and 720p only. Seedance 2.0 offers 1080p and 4K.**

The 4K claim on ByteDance's consumer surface does not describe the API model's output specification.
The aggregator was right and I overrode it with marketing copy. This is now flagged prominently in
`parameters.md`, `continuity-and-references.md` and `examples.md`, because it is counter-intuitive and
is the most likely reason to route away from this model.

### The token-form claim was overconfident

v1.0 asserted *"the space before the numeral is part of the syntax"* on the strength of the Seed blog's
`@Image 1`. ByteDance's full documentation uses **at least five delimiter forms interchangeably**:

| Form | Where |
|---|---|
| `@Image1` | Published API curl examples |
| `@Image 1` | Keyframe reference example |
| `@video1` / `@image1` | Task-instruction examples |
| `[Video 1]` / `[Image 1]` | 3D clay-model examples |
| `<video1>` / `<2pic>` | Coarse-grained clay example |
| `Image 1:` (bare) | Multi-panel storyboard example |

The **normative rule** is positional: *"The numbering should correspond to the upload order of the
assets, such as Image 1 / Video 1 / Audio 1, and each asset should be explicitly bound in the text
prompt."* The delimiter is not load-bearing. numbered reference tokens remains correct; the reasoning
behind it is now right too.

### Working prompt length was far too narrow

v1.0 carried a "60–300 words" community range. ByteDance's own published examples run **400–700 words**
with full shot lists, per-shot dialogue, timestamps and style blocks. Long structured prompts are the
documented house style. What degrades output is unstructured length, not length.

### `@Audio` is confirmed

v1.0 flagged it unverified. ByteDance documents audio reference explicitly, and **standalone audio
reference is 2.5-exclusive** — 2.0, fast and mini all require an accompanying image or video.

### `output_format` was miscategorised

v1.0 listed it under "reported only by third parties." It is first-party, `mp4` or `mov`, with `mov`
recommended for editing and extension. **2.5 is the only Seedance offering `mov`.**

---

## What v1.0 got right

- The **fabricated bracket-syntax table** — music `( )`, SFX `< >`, dialogue `{ }`, subtitles `【 】` —
  appears in no ByteDance source. Confirmed dead. Dialogue is double quotes behind a speaker label
- The **"~3 minutes" ceiling** was overstated. Documented output is 4–30 s per generation
- **Reference budgets**: 30 images / 10 videos / 10 audio, 50 total
- The **clay-model capability** being genuinely distinctive, and absent from the research file's token
  list despite being discussed in its prose

---

## What the ModelArk docs added that nothing had

Substantial material absent from both the research file and v1.0:

1. **The locked/unlocked task taxonomy.** Editing, first/last frame and extension lock the output's
   aspect ratio to the input asset; editing also locks duration to `-1`. Reference, storyboard and
   keyframe tasks are unlocked. **This distinction does not exist in Seedance 2.0.** Getting it wrong
   fails the request.
2. **Trigger words are required in the prompt text.** Editing needs one of `edit video / add / insert /
   remove / delete / modify / replace / change to`; extension needs `extend forward / extend backward /
   continue / continue from / extend the story`. Without one the model does not know the task type.
   Where several videos are supplied, it picks the target from the prompt.
3. **Integer-second timestamps**, with three documented forms and explicit rules — no gaps, balance the
   load, not for high-frequency action. **Seedance 2.0 does not respond to timestamps at all.**
4. **Storyboard vs keyframe.** Storyboards are a *high-level plot reference* and will not be followed
   frame-for-frame; keyframes align strictly. Opening line for keyframes: `Use Images 1 to 7 in order
   as keyframes.`
5. **Per-capability stability recommendations** — 1–8 subjects by image reference, 1–5 by audio/video,
   5–10 s reference clips, ≤15 storyboard panels, ≤20 s videos for editing, single-view above five
   subjects.
6. **Negative control is documented but narrowly scoped** — subtitles and audio only. Broader
   exclusions appear in ByteDance's own examples and work, but sit outside the guarantee.
7. **Two task types nothing had recorded**: one-click video creation, and seamless video transition
   (generating the missing in-between segment joining two clips).
8. **Backward extension** — 2.5 extends in either direction.
9. **Editing duration tolerance** — up to ~0.3 s difference, compressing transition frames only, and
   **zero difference when the source was itself Seedance 2.5 output**.
10. **ByteDance ships a first-party prompt-engineering skill**, `sd25-pe`, installable via npx. Their
    own tooling for the same job this skill does.

---

## Capability findings

**No structured JSON prompt format.** ByteDance's long-form examples use bracketed section headers
(`[Subject settings]`, `[Shot list]`, `[Strictly exclude]`) which superficially resemble structure —
but they are an in-prose organising convention, not a documented structured output format. The API
takes one `text` item.

**No published prompt-length cap** — no vendor figure exists. Rather than invent a figure, stated in `parameters.md`
instead.

**Scripted dialogue is supported.** Native lip-synced audio in 10+ languages, with double-quoted lines behind
speaker labels throughout ByteDance's own examples.

**No negative-prompt parameter** — no `negative_prompt` field exists. But note the body's
framing changed between versions: v1.0 called in-prompt negation "a working technique, not documented
behaviour"; it is now **documented, for subtitles and audio specifically**, with broader use noted as
outside the guarantee. Three models, three defensible positions on negation — FLUX 3 endorsed,
Seedance scoped, MiniMax H3 undocumented.

**No storefronts named.** BytePlus, ModelArk, Dreamina and Jimeng appear in
`parameters.md` and this README only as **sourcing labels**, never as destinations.

---

## Routing position

**Reach for Seedance 2.5 when the scene is long, crowded, previz'd, or needs editing and extension with
clean joins.**

- **Long** — 30 s single-pass, double the 2.0 family
- **Crowded** — 50 reference assets against `minimax-h3`'s 12 and `veo-v3`'s 3
- **Previz'd** — 3D clay-model reference, with no equivalent elsewhere here
- **Editable** — timestamp-scoped editing of picture *and* audio independently, with `mov` joins

**Route away when:**

- **1080p or 4K is needed.** 720p ceiling. This is the big one, and it is counter-intuitive enough that
  it is flagged in three files
- **Per-attribute reference control** — `minimax-h3` splits appearance and motion within one subject
  definition, with retention markers
- **Cheap preview iteration** — no draft mode on any Seedance. `flux-v3-video` has draft/enhance
- **A lead's voice across a production** — dedicated voice model, audio laid against the picture

**Against `seedance-v2`:** not superseded, and now for a concrete reason beyond cost — **2.0 is the
higher-resolution model.** Where 15 s and 15 references suffice and 1080p or 4K is required, 2.0 is
strictly the better choice.

---

## Integration implications

Sizing and endpoint parameters never belong in prompt prose — so the API surface below is
not a prompting concern. **It is an integration concern**, and a sharp one, because three of these
constraints are enforced server-side and will fail a request rather than degrade gracefully:

1. **Locked tasks constrain parameters the integration layer would otherwise set freely.** Editing requires
   `ratio: adaptive` *and* `duration: -1`; first/last-frame and extension require `ratio: adaptive`.
   Any code path that always writes an explicit ratio will break on all three task types.
2. **Trigger words live in the prompt text, not in a parameter.** The integration layer cannot select "edit" or
   "extend" through the request body alone — the prompt must contain one of the documented trigger
   words. A task-type enum in the integration layer's own model would need to *emit* the trigger word, not just
   set a flag.
3. **Reference numbering is bound to upload order.** If the integration layer ever reorders, de-duplicates or
   lazily uploads assets, the numbers in the prompt silently stop matching the assets. That fails
   quietly — wrong character, not an error.

Two softer ones: the 720p ceiling means the integration layer should not offer a 1080p/4K option for this model
(it should for Seedance 2.0), and `mov` should be the default output format for edit and extend paths
rather than `mp4`.

Worth raising as an integration issue independently of this skill.

---

## Open questions

1. **Does `seedance-v2` need updating?** Its skill predates this documentation. At minimum it should
   carry the real model IDs (`dreamina-seedance-2-0-260128`, plus fast and mini variants), the 1080p/4K
   capability, and the fact that it does **not** respond to timestamps.
2. **The `sd25-pe` first-party skill** was not mined for this build. Worth a pass before v1.2 — it is
   the vendor's own prompt tooling and may resolve remaining ambiguity.
3. **One-click video creation and seamless transition** are documented but only lightly covered here.
   Both warrant fuller treatment once there is production experience with them.
4. **Why 2.5 regressed on resolution** is unexplained. If a 1080p/4K tier ships later, `parameters.md`,
   `continuity-and-references.md` and `examples.md` all need updating together.
5. **Slug.** `seedance-v2-5` per the agreed point-release convention. Sits alongside `seedance-v2`;
   both ship, and they are now genuinely complementary rather than one superseding the other.
