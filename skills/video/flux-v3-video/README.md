# flux-v3-video — build notes

Human-facing build notes.

**Built:** 2026-08-11 · **Skill version:** 1.0 · **Model:** FLUX 3 Video (Black Forest Labs)

---

## Research corrections

The upstream research draft for this skill was built on a **false premise** and required heavy
correction. It states BFL's API spec is "still finalizing" and marks most parameters "Provisional."
BFL had in fact shipped full first-party docs and an OpenAPI schema; the release note is dated
**4 August 2026**. Because the author assumed no spec existed, the parameter table was reconstructed
from early third-party schemas and is wrong in nearly every row.

| Research file claimed | Actual (BFL OpenAPI) |
|---|---|
| `images_list` parameter for image-to-video | **No such parameter.** The field is `keyframes` |
| `aspect_ratio` default `1:1`; enum includes `2:3`, `3:2` | Default `auto`. `2:3`/`3:2` don't exist; `2:1` was missing from the file |
| `resolution` `480p`/`720p`/`1080p`, default `720p` | `hd` \| `fhd`, default `hd`. The 480/720/1080 enum is invented |
| `resolution` (image) `1k`/`2k`/`4k`, default `2k` | **No FLUX 3 image endpoint exists.** Only `/v1/flux-3-video` |
| `duration` ~4–10s, default 5s | Integer 5–20 or `"auto"` (default). Minimum is 5; no 5s default |
| "Up to 10 reference images for character consistency — **Confirmed**" | FLUX.2 image-editing behaviour misapplied. `keyframes` are timeline frames, not identity references |
| "No official deprecations announced by BFL" | False — deprecations documented effective 31 Oct 2025 |

**Omitted from the research entirely:** `safety_tolerance`, `draft`, `draft_cache`, `version`, and the
whole **draft → draft_enhance** workflow, which is a first-class feature.

**Marked "Confirmed" without support:** "open-weight FLUX 3 Dev planned later in 2026." Not confirmed
anywhere; BFL's Hugging Face path offers FLUX.2 `[klein]`/`[dev]` only.

**Unsourced throughout:** the "Self-Flow unified multimodal" architecture name, "FLUX 3 Action
(robotics)" as a product, and the entire §7 version-delta table. All dropped.

**What the research got right:** its prompting advice. Audio as its own layer, shot terms over thematic
terms, describing only the delta for image-continuation, and preservation clauses all match BFL's audio
guide well and were carried through largely intact.

---

## Capability findings

**No reference-token mechanism — the judgement call on this skill.** `keyframes` accepts up to 10 images and
looks exactly like a reference-image array. It is not one. BFL is explicit that the images become
*frames of the video*, and equally explicit that Omni Reference "will be available soon" — i.e. does not
exist. Declaring a numbered convention here would make an integration emit a token instruction the model
cannot honour. This is the same class of error as the kling-v3 `@Character` trap, arriving from a
different direction: there, a token that looked like identity was really lip-sync; here, an array that
looks like references is really a timeline.

**Revisit when Omni Reference ships.** At that point this decision, `continuity-and-references.md`, and the
"no cross-generation identity mechanism" section in SKILL.md all need updating together.

**Scripted dialogue is supported.** BFL documents the trigger verbatim: *"Quote the line in your prompt and the
character says it."* Unambiguous, unlike Grok video and Gemini Omni Flash where audio is generated but
scripting specific lines is undocumented; neither of those is scriptable.

**No structured JSON prompt format.** BFL documents JSON structured prompting only for
FLUX.2 *image*. FLUX 3 Video takes a single free-text `prompt` string.

**No published prompt-length cap.** BFL publishes no cap. Rather than invent a figure — *"If the vendor publishes no figure,
say so in the README rather than passing an invented number off as spec"* — it is stated here instead.
The 512-token figure circulating in third-party write-ups is a FLUX.1 Kontext fact carried over by
analogy and was not used.

**No negative-prompt parameter.** But note the body still *teaches* in-prompt
negation, because BFL endorses it for video specifically and uses it in their own examples. The
frontmatter flag describes the API surface; the prose describes the technique. These are not in
conflict.

**No storefronts named.** BFL is the vendor; aggregators carrying FLUX 3 are deployment
detail and are not mentioned.

---

## Routing position

**Reach for FLUX 3 when** the shot needs synchronised speech and the beats are known in advance —
keyframe timing is its distinctive lever, and multi-shot-in-one-generation is the strongest continuity
tool it has.

**Route away when** a character must persist across separate generations. FLUX 3 has no mechanism for
this today. Prefer `minimax-h3` (`<Subject N>` typed reference tokens), `seedance-v2-5` (`@Image 1`),
or `veo-v3` (numbered reference images) when cross-shot identity is the requirement.

**Against `ltx-v2`**, the other single-pass audio-video model in the catalogue: LTX requires a single
flowing paragraph and has no reference mechanism either, but no keyframe timing. FLUX 3 wins where
timing matters; LTX wins where duration >20s is needed.

---

## Open questions

1. **Prompt-length ceiling is genuinely unknown.** Worth an empirical test — find where quality starts
   degrading and record it in `parameters.md` as an observed working range clearly labelled as such,
   not as a spec.
2. **Omni Reference timing.** BFL says "soon" without a date. Whoever notices it ship should reopen
   this skill; the capability key, the continuity file and one SKILL.md section all change together.
3. **`draft_cache` shape is undocumented in detail.** Described as an encrypted bundle pinning mode,
   prompt, seed and conditioning media, but its structure and lifetime aren't published. The skill
   teaches the workflow without asserting bundle internals.
4. **Slug.** `flux-v3-video` rather than the endpoint name (`flux-3-video`). If BFL ships a FLUX 3
   *image* model it would need its own skill, and the `-video` suffix keeps the two unambiguous.
