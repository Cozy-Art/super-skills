# grok-imagine-video-v1-5 — build notes

Human-facing build notes.

**Built:** 2026-08-11 · **Skill version:** 1.0 · **Model:** Grok Imagine Video 1.5 (xAI), released 30 May 2026

---

## The literal token form

**`<IMAGE_1>`, `<IMAGE_2>` — angle brackets, written inline beside what they govern.**

```
the model from <IMAGE_1> walks in from the back of the shot … they wear the
shirt from <IMAGE_2> and black flared jeans
```

⚠️ **The `@Image1` form does not exist on this model.** See the research corrections below — this was
the single biggest error in the source material and would have shipped a non-functional skill.

**Index base is genuinely ambiguous in xAI's own docs.** Main examples are 1-indexed; the
reference-audio subsection instructs `<IMAGE_0>` when audio is also passed, then uses `<IMAGE_1>` in its
own combined example. The skill defaults to `<IMAGE_1>` and tells the reader to try zero-based if
binding fails. `<AUDIO_N>` is consistently zero-based.

Across the catalogue: `@Image1` (veo-v3, seedance-v2), `@Image 1` spaced (seedance-v2-5), `<IMAGE_1>`
(here), `<IMAGE_REF_0>` zero-indexed (gemini-omni-flash), `<Subject N>` typed (minimax-h3). All
`numbered`. None interchangeable.

---

## Research corrections

The upstream research draft was **the weakest of this set.** Its prompt-craft guidance
is largely sourced to YouTube videos and a third-party fan site (`grokimagineai.net`), and its single
most important technical claim is fabricated.

### 🔴 The `@` reference syntax does not exist

The file states references are tagged *"inline using the `@` symbol."* xAI uses **angle-bracket
tokens** — `<IMAGE_1>`, `<IMAGE_2>` — in its own showcase prompt. There is **no `@` anywhere in xAI's
video documentation.** The claim traces to two YouTube citations in the file's own reference list.

A skill built on the `@` form would have produced prompts where every reference was silently read as
ordinary text.

### Other corrections

| Research file claimed | Actual |
|---|---|
| Default resolution 720p ("typical for final output") | **`480p`** — *"Standard definition, faster processing (default)"* |
| Default duration "5–6 seconds depending on interface" | **8 seconds** |
| Extension uses the 1–15 generation range | **Its own range: 2–10, default 6.** Absent from the file entirely |
| "Up to 7 tagged references" | **No numeric cap in the REST schema.** Vendor examples show 3. The 7 comes from YouTube |
| "Video 1.5 added explicit frame selection for extensions" | **Unsupported.** Extension continues from the last frame; no such field exists |
| Video Edit "hard-caps output at 8.7s and 720p regardless of the source clip" | **Inherit-then-cap.** Edit *retains* the source's duration (capped at 8.7s) and *matches* its resolution (capped at 720p). A 4s input yields 4s |
| Reference-to-video is "a separate capability on the broader `grok-imagine-video` API suite" | A **mode of the same endpoint**, selected by which inputs are present |

### Stripped as unverified

- **"10–20 words for simple motion prompts."** Load-bearing — it would shape every prompt the skill
  writes. Sourced to a fan site, and contradicted twice over: xAI's own showcase reference-to-video
  prompt runs **~90 words**, and the API documents a **prompt-rewriting (upsampler) LLM** that expands
  prompts before generation, which makes a short-prompt optimum implausible. The skill teaches the
  opposite, and explains why
- **"Negative prompts are explicitly ignored."** Downgraded to what is actually verifiable: no
  `negative_prompt` parameter exists; in-prompt negation behaviour is **undocumented in either
  direction**
- **`camera switch`, `fixed lens` / `unfixed lens`.** Zero first-party support. The lens toggle implies
  a control existing in neither the API schema nor any documented UI
- **Benchmark and version claims** — "+52 Elo," "57% blind-test win rate," "1.0 max was 10s." All
  third-party blogs
- **"Running on the Aurora engine."** No xAI statement ties Aurora to this model. Aurora is historical
  xAI *image* branding, and applies to their image model, not this one
- **Consistency folklore** — "a reference holds for 5–10 clips before drift," "clean backgrounds gave
  ~60% more consistent subject appearance." No methodology, third-party blog. The underlying advice is
  plausible and is kept as a heuristic; the 60% figure is not

### The trap, and this model handles it well

`<AUDIO_0>` / `<AUDIO_1>` / `<AUDIO_2>` bind **preset voices** supplied via
`reference_audios: [{"voice_id": "eve"}]` — max 3, from xAI's TTS roster, with custom cloning restricted
to trusted partners.

> *"The person from `<IMAGE_1>` speaks to camera with the voice from `<AUDIO_0>`."*

This is **voice attribution, not visual identity.** Only `<IMAGE_N>` feeds the reference-token convention. Grok and
`minimax-h3` are the two clearest catalogue examples of a vendor keeping the layers genuinely separate —
unlike `kling-v3`, where the same distinction had to be untangled after the fact.

---

## Capability findings

**Template:** `video/seedance-v2`.

**No scripted dialogue** — the same considered call as `gemini-omni-flash`, and equally counter-intuitive.
Grok generates an audio track by default **and** lets you assign a specific voice, which makes it look
like scripted speech should work. It does not: xAI documents **no mechanism for specifying what a voice
says.** No quoted-line convention, no scripting syntax.

A model counts as supporting dialogue only when it generates *spoken words from a script*. Assigning a
timbre is not a script. Treating it as scriptable would push dialogue lines into a prompt with no way
to deliver them, and the failure would be silent.

Two models in this set are ✗ for related-but-distinct reasons — worth keeping straight:

| Model | Audio? | Voice control? | Script? | Scripted dialogue? |
|---|---|---|---|---|
| `flux-v3-video` | ✓ | — | ✓ quoted lines | ✓ |
| `minimax-h3` | ✓ | ✓ `<Audio N>` | ✓ `<d>` tags | ✓ |
| `seedance-v2-5` | ✓ | ✓ audio ref | ✓ quoted lines | ✓ |
| **`grok-imagine-video-v1-5`** | ✓ | **✓ `<AUDIO_N>`** | **✗** | **✗** |
| `gemini-omni-flash` | ✓ | ✗ | ✗ | ✗ |

Grok is the interesting row: voice control without script control. That combination is what makes the
✗ non-obvious.

**No published prompt-length cap.** A ceiling exists — xAI's error table covers *"a prompt that is too
long"* — but **no figure is published.** Rather than invent one, that is stated in `parameters.md`.

**No structured JSON prompt format.** xAI documents `prompt` as a plain string; no JSON
scene schema exists.

**No negative-prompt parameter.** But note the body's framing is *"genuinely
unknown"* rather than "doesn't work," because xAI says nothing either way. That is deliberately weaker
than the FLUX 3 skill (BFL endorses negation) and matches `minimax-h3` (equally undocumented). Three
positions across five video models, each grounded in what the vendor actually says.

**No storefronts named.**

---

## Two things worth carrying to other skills

**1. The upsampler changes prompting advice.** xAI documents a prompt-rewriting LLM that expands
prompts before generation (`input_tokens_details.text_tokens`: *"Prompt text tokens consumed by the
prompt-rewriting (upsampler) LLM"*). This reframes specificity as *constraint on the rewrite* rather
than as verbosity — every unstated element is one the upsampler decides. It also single-handedly
refutes the short-prompt advice. Worth checking whether other models have a similar stage.

**2. Reference binding costs resolution here.** Text-to-video and image-to-video reach 1080p;
reference-to-video caps at 720p. Most models don't penalise reference use this way, and it turns
identity binding into a genuine trade-off rather than a free win. Example 6 works the decision through.

---

## Routing position

**Reach for Grok Imagine Video when** a shot needs a character bound from a reference *and* a distinct
voice presence, and 720p is acceptable. Preset voice assignment alongside visual reference is rare in
the catalogue.

**Route away when:**

- **Scripted dialogue is needed.** The most likely reason, and the easiest to discover too late —
  native audio *and* voice assignment both exist, which makes scripted speech look available
- **Reproducibility from a seed matters.** No `seed` parameter
- **1080p is needed with reference binding.** Not available in combination
- **More than three identities.** Three is what xAI demonstrates; `seedance-v2-5` takes 30 images
- **Per-attribute reference control.** `minimax-h3` splits appearance and motion inside one subject
  definition with retention markers; Grok scopes by token placement, which is looser
- **Past 15 seconds in one generation**, or past 25 with an extension

---

## Integration implications

1. **Mode exclusivity is enforced.** `image` and `reference_images` together return 400. Any code path
   offering both simultaneously will fail.
2. **Extension `duration` is the addition, not the total** — and has its own 2–10 range. A UI slider
   reusing the 1–15 generation range will produce rejected requests at 11+ and confusing results
   throughout.
3. **Reference mode silently caps at 720p.** If the integration layer offers 1080p alongside reference images, the
   result comes back at 720p rather than erroring.
4. **Edit downsizes 1080p sources to 720p.** An edit-as-finishing-pass workflow loses resolution.
5. **No `seed`** — do not expose a reproducibility control for this model.

---

## Open questions

1. **Index base.** The highest-value empirical test on this skill — a single generation with a
   reference tagged `<IMAGE_0>` versus `<IMAGE_1>` would settle it. xAI's docs contradict themselves.
2. **Reference count ceiling** is unpublished. Three is demonstrated; anything higher is untested.
3. **Does in-prompt negation work?** Genuinely undocumented in either direction. Worth testing.
4. **Is the upsampler bypassable?** Not documented. If it is, that materially changes prompting advice.
5. **The preset voice roster** is referenced but not enumerated in the sources reviewed. Worth
   capturing the available `voice_id` values into `parameters.md` before v1.1.
6. **Aurora branding.** Aurora names an xAI *image* model, and nothing xAI publishes ties it to this
   video model. Treat any "runs on Aurora" claim about Grok Imagine Video as unsourced.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
