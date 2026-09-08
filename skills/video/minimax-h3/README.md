# minimax-h3 — build notes

Human-facing build notes.

**Built:** 2026-08-11 · **Skill version:** 1.0 · **Model:** MiniMax H3 (Hailuo 3.0)

---

## The literal token form

Recorded prominently because numbered reference tokens covers four different literal syntaxes across
the catalogue, and the classification alone nearly shipped the Grok video skill with the wrong
delimiter.

**H3's form: angle brackets, capitalised type word, space, arabic numeral.**

```
<Subject 1>   <Picture 1>   <Video 1>   <Audio 1>
```

Numbering is **independent per category** — `<Picture 1>` and `<Video 1>` are unrelated assets.

Compare across the catalogue: `@Image1` (veo-v3, seedance-v2), `@Image 1` *with a space*
(seedance-v2-5), `<IMAGE_1>` (grok-imagine-video-v1-5), `<IMAGE_REF_0>` *zero-indexed*
(gemini-omni-flash). All classify as `numbered`. None are interchangeable.

---

## Research corrections

Research file: `MiniMax H3-prompt guide-aug11.md`. **A strong file** — its
load-bearing claims survive contact with MiniMax's API reference, OpenAPI schema, Hugging Face model
card and two official prompt-writing guides.

Its weakness is sourcing hygiene rather than accuracy: it credits `hailuo3.me`, `jxp.com` and an X post
for the reference-label and dialogue-tag syntax, which MiniMax publishes itself. The conclusions were
right; the citations made them look riskier than they were and were replaced with primary sources.

**Corrections applied:**

| Research file claimed | Actual |
|---|---|
| `resolution` default `2K`; 768P "in closed beta on the direct API" | **Inverted.** `resolution` is required with **no default**, no beta gating. 768P is the base model's native output (*"the shorter side is set to 768 pixels by default"*); 2K comes from a separate H3-Regenerate-2K module |
| `duration` default 5 | **Required, no default.** 5 is merely what MiniMax's examples pass |
| Four generation modes | **Five.** The file omits **last-frame-only** (`text` + 1 image, `role=last_frame`) |
| — *(not mentioned)* | **i2v and r2v are mutually exclusive.** `first_frame`/`last_frame` cannot mix with any `reference_*` role. Will cause 400s if taught otherwise |
| "released with open weights as a 33B model on Hugging Face" | True but materially incomplete — see below |
| "2K (1440px short edge)" | Not stated first-party. Only the 768px default short side is published |
| Per-second pricing only | **Input material is billed separately** — images past the first five at $0.04 each, video by input duration, Context-IR as tokens |

**Open weights are narrower than the file implies.** Released under the MiniMax H3 Community License
(`license: other`, not Apache/MIT), with a **separate application required for USA / EU / UK / South
Korea**. Only **H3-Base** is open — H3-Context-IR and H3-Regenerate-2K are not. Since Context-IR
produces the structured prompt and Regenerate-2K produces 2K output, self-hosting the base model gives
you the generator without either end of the pipeline.

**Unverifiable and load-bearing — dropped:** *"extendable to ~30s via a separate Extend tool."* Appears
twice in the file including the spec table. **No Extend endpoint exists** in the API surface (create /
context-IR / regeneration / query / list / delete) and it is absent from the model card. Possibly a
Hailuo app feature. A skill promising 30s output would be wrong, so the 15s ceiling is stated plainly
and longer sequences route to `seedance-v2-5`.

**Also flagged:** the file's `<Video 1> attribute_transfer for camera movement only` example teaches the
marker slightly wrong. `attribute_transfer` is real, but MiniMax defines it as characteristics
transferred *to a different identifiable target subject*. Camera-only guidance is `weak_reference`.
Corrected in `best-practices.md` and `continuity-and-references.md`.

**Version-comparison table against Hailuo 2.3** is entirely third-party (imagine.art, orcarouter.ai, an
HF community blog) and was not carried across. `hailuo-v2` remains in place for users who want the
cheaper tier.

---

## Capability findings

**A documented structured prompt format.** MiniMax documents six named prose sections in fixed
order (`subject_definitions`,
`summary`, `retention_analysis`, `detailed_description`, `overall_soundscape`, `non_diegetic_music`).
The body defines that shape and a `schema.json` ships alongside it.

**Important caveat recorded in the schema itself:** these sections are **labelled prose blocks inside a
single newline-delimited text string**, not JSON keys on the API. They arrive as `content.prompt` from
H3-Context-IR and are passed back as the one `text` item the API accepts. The schema describes the
composition surface, not the wire format.

**Six prose fields, and the main one changes name by mode.** H3 takes **six** prose fields in a
single call, and the primary description field is `integrated_multimodal_description` in
T2VA/I2VA/FL2VA but `detailed_description` in full-reference mode. Any integration that auto-populates
"the prompt field" has to resolve the mode first, or it will write the full prose into a field that
must not contain it.

The body states which fields are authoritative and that nothing auto-syncs between them.

**Prompt-length cap: 7,000** — confirmed first-party **twice**, in the video generation guide and the API
schema — a genuine vendor-published cap, which is not a given. The body teaches the
sweet spot separately (350–500 English words for the main block, MiniMax's own recommendation), per the
C1 convention that the cap is a ceiling, not a target.

**Scripted dialogue is supported.** `<d>[Language] … </d>` is a real tokenizer token, documented in the model repo
(*"We add several special tokens, such as `<d>`, to the tokenizer configuration"*), paired with
`(S1)`/`(S2)` speaker IDs. Unambiguous.

**Numbered reference tokens, and the trap handled explicitly.** H3 is the clearest example in this set
of three genuinely separate mechanisms that look alike:

- `<Subject N>` / `<Picture N>` → visual identity
- `(S1)` / `(S2)` + `<d>…</d>` → speech attribution
- `<Audio N>` → voice timbre

MiniMax states the distinction directly: *"`<Subject N>` identifies the referenced subject, while
`(Sx)` identifies the actual speaker."* Only the first layer feeds the reference-token convention. This is the
kling-v3 trap resolved *correctly by the vendor* rather than needing untangling — worth noting as the
positive example when documenting the pattern elsewhere.

Two further tags the research file missed and that are documented in the skill: `<scenetrans>`
(dialogue crossing a cut) and `<cutoff>` (speech truncated by video end).

**No negative-prompt parameter.** None exists, and unlike FLUX 3, in-prompt negation is
**not** documented first-party here. `best-practices.md` teaches positive replacement and marks any
negation as untested — deliberately different guidance from the FLUX 3 skill, where BFL endorses it.

**No storefronts named.**

---

## Routing position

**Reach for H3 when** identity must be carried across shots with per-attribute control. Its
split-source subject definition — appearance from one asset, motion from another, voice from a third —
is the reason to choose it.

**Route away when:**

- **A lead character's voice must be identical across a production.** Use a dedicated voice model with
  a real identity lock and lay the audio against H3's picture. H3's native speech is strong for
  incidental and background lines, not for a lead.
- **A single take needs more than 15 seconds.** `seedance-v2-5` generates 30s single-pass and extends
  twice. There is no Extend endpoint on H3.
- **More than 12 reference files are needed.** `seedance-v2-5` takes up to 30 images, 10 videos and 10
  audio clips.
- **A fixed opening frame AND a referenced character are both required.** Not possible in one call —
  the two conditioning modes are mutually exclusive.

**Against `hailuo-v2`** (Hailuo 2.3), deliberately left in place: 2.3 is the cheaper tier and remains
the right choice for volume coverage where H3's reference system isn't needed.

---

## Open questions

1. **Does `<Audio N>` voice timbre survive across generations** the way `<Picture N>` identity does?
   Not documented. Worth testing before relying on it for a recurring character.
2. **Context-IR is not open-sourced**, so self-hosted H3-Base users have no documented path to the
   structured six-section prompt. Whether hand-authoring the IR works as well as generating it is
   untested — this skill assumes it does, since it emits the token form directly.
3. **In-prompt negation is undocumented**, not documented-as-unsupported. Empirical testing would
   settle whether the FLUX 3 pattern transfers. Currently marked untested rather than discouraged.
4. **MiniMax ships official prompting skills** at `github.com/MiniMax-AI/MiniMax-H3/tree/main/skills`.
   Not mined for this build beyond the two prompt-writing guides. Worth a pass before v1.1 — it is the
   most authoritative available source and may resolve items 1 and 3.
5. **Slug.** `minimax-h3` uses the real product ID — `MiniMax-H3` is the literal API model ID. Note
   this breaks family naming with `hailuo-v2`, which is named for the product line rather than the
   model. Deliberate.
