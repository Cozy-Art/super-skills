# gemini-omni-flash — build notes

Human-facing build notes.

**Built:** 2026-08-11 · **Skill version:** 1.0 · **Model:** Gemini Omni Flash (Google), preview

---

## The literal token form

Recorded prominently because numbered reference tokens covers five different literal syntaxes across
the catalogue, and this one has the sharpest trap.

**Omni Flash's form: `<IMAGE_REF_N>` and `<FIRST_FRAME>`, written inline. References are ZERO-INDEXED.**

```
<FIRST_FRAME> a woman is walking
in the style of <IMAGE_REF_0> a woman <IMAGE_REF_1> is walking
```

⚠️ **`<IMAGE_REF_0>` is the first reference image.** Every other numbered-reference model in the
catalogue starts at 1: `@Image1` (veo-v3, seedance-v2), `@Image 1` (seedance-v2-5), `<IMAGE_1>`
(grok-imagine-video-v1-5), `<Subject 1>` (minimax-h3). Only this one starts at 0.

**And the declaration block mixes bases in a single line** — Google's own convention, not a doc error:

```
[# Sources <FIRST_FRAME>@Image1] [# References <IMAGE_REF_0>@Image2]
```

`@ImageN` counts **uploads from 1**. `<IMAGE_REF_N>` counts **references from 0**.

**Tag placement carries meaning.** `in the style of <IMAGE_REF_0>` binds that image to style;
`a woman <IMAGE_REF_1>` binds the other to the subject. Collecting tags at the front loses the binding.

---

## Research corrections

The upstream research draft was **materially the most accurate of this set** —
the specs most prone to fabrication (context window, output envelope, parameter enums) are genuinely
first-party here, and the file correctly declines to invent a prompt-length cap.

| Research file claimed | Actual |
|---|---|
| Watermarking: "invisible SynthID **+ C2PA** provenance metadata" | **C2PA is not documented.** Neither cited source mentions it; the API docs and model card reference SynthID only |
| Input modalities: "Text, image, **audio (limited)**, video" | Model page lists **Text, Image, Video**. API docs: *"Uploading audio references is unsupported in the current version of the API."* The model card discusses audio at the architecture level, which is not API-available |
| A "reference stacking" workflow combining source video + reference image + reference audio | **Contradicted on all three counts.** Audio refs unsupported; video refs *"accepted by the API schema but not correctly processed by the model at this time"*; *"Referencing or reasoning across multiple videos is not supported."* Cut entirely — it would send users down a dead end |
| "If unspecified, the model defaults to a static medium shot" | Google says the default is a **multi-shot narrative**. The medium-shot specific is from a third-party blog |
| Access: Gemini Enterprise Agent Platform, YouTube Shorts/Create | **Not confirmed** by model page or model card. Confirmed surfaces: Gemini API, AI Studio, Gemini App, YouTube, Google Flow, Google Flow Music |
| Google Flow 4/6/8/10s and 720p/1080p/4K tiers | Third-party. Google's model page states 3–10 s at 720p/24 fps, no tiering |
| Veo 3.1 comparison table | Entirely third-party sourcing. Dropped |

**Missing from the file entirely, and load-bearing:** the **regional restrictions**. Editing *uploaded*
videos is unavailable in the EEA, Switzerland and the UK (editing model-generated video is fine);
uploading or editing images containing minors is blocked in the same regions; only English has been
evaluated.

**Confirmed verbatim and carried through:** context window 1,048,576 tokens; output 3–10 s at 720p /
24 fps; the `task` enum; `aspect_ratio` enum and default; `delivery: "uri"` above 4 MB;
`previous_interaction_id`; the `store=false` retention behaviour; timecode syntax; the multi-shot
default; the "keep everything else the same" preserve instruction; the full unsupported-features list;
pricing and paid-tier-only status; SynthID.

---

## Capability findings

**No scripted dialogue — the most considered call on this skill, and not the obvious one.**

Omni Flash *does* generate native synchronized audio and has a full audio-prompting section. The
temptation is to treat it as scriptable. But three documented facts point the other way:

1. There is **no documented mechanism for scripting specific spoken lines**
2. `No dialogue` appears only as a **suppression** instruction — there is no positive counterpart
3. Voice editing is unsupported, and the model card states: *"Gemini Omni Flash is capable of changing
   people's speech. For now, we are restricting this capability."*

A model counts as supporting dialogue only when it generates *spoken words from a script*. This one
generates speech but takes no script. Treating it as scriptable would push assigned dialogue lines into a
prompt with no way to deliver them — worse than not injecting them, because the failure is silent.

Same reasoning applied to `grok-imagine-video-v1-5`. Both differ from `flux-v3-video`,
`minimax-h3` and `seedance-v2-5`, where the trigger is documented.

**Context window: 1,048,576 tokens**, stated on the model page. Google publishes no separate
prompt-length recommendation, so the context window is the only published figure.

Obviously a ceiling and not a target — `parameters.md` says so explicitly, since a million-token video
prompt is not a prompt. Working range is a few hundred words.

**No structured JSON prompt format.** The Interactions API request body is JSON, as it is
for nearly every model — that is **not** the same as a structured prompt format. Google documents no JSON scene
schema; the prompt is a string and all structure (timecodes, role tags, declaration blocks) is inline
text. This distinction was worth checking carefully because the model's request shape is more
structured than most.

**No negative-prompt parameter** — and here it is unusually clean: Google lists negative-prompt
fields among the **explicitly unsupported** inference controls, alongside system instructions,
temperature, top-p and stop sequences. Not merely absent — documented as unsupported. Exclusions go in
prompt text, which Google's own guidance directs.

**Numbered reference tokens** — see the token-form section above.

**Slug: `gemini-omni-flash`.** The only skill here that cannot take a `-vN` suffix, because the
model carries no version number (`gemini-omni-flash-preview`; `-preview` is transient state, not a
version). Note that Gemini 3 Pro Image is a separate model line, not a version of this one.

**No storefronts named.**

---

## Routing position

**Reach for Omni Flash when the piece is short and the look needs to be found rather than specified.**
Conversational refinement of a 3–10 second clip — generate roughly, then converge across short
single-change edit turns — is something no other model in the catalogue offers. For that job it is
clearly the right choice.

Its continuity model is also genuinely different and worth understanding: continuity comes from
**staying in the conversation**, not from re-binding assets. Within a chain it is free and drift-proof,
because it is the same clip rather than a re-description.

**Route away when:**

- **Longer than 10 seconds.** The hardest constraint. No extension, no interpolation — there is no way
  to chain past it within the model. `seedance-v2-5` (30 s, extends twice) or `minimax-h3` (15 s)
- **Scripted dialogue is needed.** `flux-v3-video` (quoted lines), `minimax-h3` (`<d>` tags),
  `seedance-v2-5` all support it
- **Above 720p.** Note `seedance-v2-5` shares this ceiling; Seedance 2.0 and others go higher
- **Persistent identity across many separate shots.** `minimax-h3`'s `<Subject N>` with retention
  markers, or `seedance-v2-5`'s 30-image budget
- **Legible on-screen text** — a stated model-card limitation
- **Any workflow needing video or audio as a reference** — images are the only channel that works

---

## Integration implications

Three items that will bite an API integration:

1. **`store=false` silently disables editing.** The fastest synchronous configuration
   (`background=false, store=false, stream=false`) forfeits the model's best feature, and the failure
   surfaces only later when an edit is attempted. The integration layer should retain by default for this model
   and treat non-retention as an explicit opt-out.
2. **`delivery: "uri"` is required above 4 MB.** At 720p/24fps a 10-second clip will exceed this
   routinely. A code path that only handles inline delivery will fail on most real outputs.
3. **Video references pass schema validation and do nothing.** The integration layer cannot detect this by
   validating the request — the field is accepted. If it exposes video reference as an option for this
   model, users will get silently-ignored references rather than an error.

Softer: `task` is inferred if omitted, so the integration layer need not set it — but setting it wrongly is worse
than omitting it. And the regional restrictions on uploaded-video editing are a real compliance surface,
not just a capability note.

---

## Open questions

1. **The reference-image cap is unpublished.** Google's own example uses six; third-party sources quote
   five to ten with no basis. Worth an empirical test before relying on more than six.
2. **Is the multi-shot default suppressible other than by explicit instruction?** The documented
   approach is a prompt-level request. Whether a parameter exists is not stated.
3. **Video-reference support is described as broken "at this time."** If it starts working,
   `continuity-and-references.md` and the routing notes both change.
4. **Dialogue restriction is described as temporary** — *"For now, we are restricting this
   capability."* If scripted speech becomes available, this becomes scripted dialogue and the audio section
   needs a real trigger documented. Worth watching; this is the single change that would most alter the
   skill.
5. **Launch date** (30 June 2026) is circumstantial — consistent with the model page's "last updated"
   and "Latest update: June 2026," but not stated. Not load-bearing.
