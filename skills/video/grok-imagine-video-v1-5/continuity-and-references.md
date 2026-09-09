# Grok Imagine Video 1.5 — Continuity and References

Grok Imagine Video draws one distinction unusually cleanly: **who appears** and **what they sound
like** are separate token systems, and neither substitutes for the other.

---

## Two token systems

| Token | Binds | Supplied via | Max |
|---|---|---|---|
| `<IMAGE_N>` | **Visual identity** — person, wardrobe, object | Reference images | No published cap; examples use 3 |
| `<AUDIO_N>` | **Voice timbre** — how a speaker sounds | A preset `voice_id` from xAI's roster | **3** |

xAI's own example uses both in one sentence:

```
The person from <IMAGE_1> speaks to camera with the voice from <AUDIO_0>.
```

**`<AUDIO_N>` is not a reference token.** It carries no likeness and no visual information — it selects
a timbre from a fixed roster. Only `<IMAGE_N>` holds identity.

This is the same trap that `kling-v3` documents at length, resolved correctly by the vendor here rather
than needing to be untangled. Grok and `minimax-h3` both keep the two layers genuinely separate.

---

## Writing reference tokens

**Angle brackets, inline, beside what they govern.** xAI's showcase prompt:

```
the model from <IMAGE_1> walks in from the back of the shot … they wear the
shirt from <IMAGE_2> and black flared jeans
```

`<IMAGE_1>` scopes to the person; `<IMAGE_2>` scopes to the shirt. Placement is the scoping mechanism —
there is no separate role-declaration syntax.

> **The `@Image1` form does not exist on this model**, despite circulating widely. It appears nowhere in
> xAI's documentation.

### The index-base ambiguity

xAI's documentation contradicts itself, and this accounts for most "the reference did nothing" reports.

- The **main worked examples** are 1-indexed: `<IMAGE_1>`, `<IMAGE_2>`
- The **reference-audio subsection** says to tag images `<IMAGE_0>` when audio is also passed
- That same subsection's **combined example** then uses `<IMAGE_1>` alongside `<AUDIO_0>`

**Stance:** default to `<IMAGE_1>`. If references are not binding, try zero-based before assuming the
prompt is at fault. Do not assert a base confidently in generated output — note the ambiguity if it
matters.

Note `<AUDIO_N>` is consistently zero-based in every example: `<AUDIO_0>`, `<AUDIO_1>`, `<AUDIO_2>`.

### How many

**No numeric cap is published.** xAI's own examples use three. A figure of seven circulates in
third-party guides with no basis in the REST schema — do not rely on it. Three is demonstrated;
anything higher is untested.

---

## The resolution trade-off

Unusual, and worth deciding deliberately.

| Mode | Max resolution |
|---|---|
| Text-to-video | **1080p** |
| Image-to-video | **1080p** |
| **Reference-to-video** | **720p** |

**Binding a character from reference images costs you the top resolution tier.**

When identity is already well-described in prose and does not need to match a specific asset, a
text-to-video generation at 1080p may be the better shot than reference-to-video at 720p. When identity
must match across shots, reference mode wins regardless of resolution.

There is no cost dimension to the decision — pricing is $0.08/second at every resolution.

---

## Continuity without a seed

**There is no `seed` parameter on this model.** Seed-locked reproducibility, a standard technique
elsewhere, is unavailable.

That leaves reference images as the only continuity mechanism, and the usual discipline applies:

1. **Fix the asset.** One approved image per identity, reused as the same `<IMAGE_N>` slot every time.
   A different photo of the same person is a different reference
2. **Keep the binding phrasing identical.** If `<IMAGE_1>` is "the model" in shot one, it is "the model"
   in shot four — not "the woman"
3. **Keep slot numbers stable** across a sequence. Costs nothing, makes prompts diffable
4. **Write the character description once and reuse it verbatim** alongside the token. The reference
   does the heavy lifting, but the prose should not contradict it

**Do not promise repeatable output from a fixed seed.** It does not exist here.

### What the folklore claims, and why it is not in this skill

Third-party guides state that a single reference "holds up for 5–10 clips before drift," and that clean
backgrounds produce "roughly 60% more consistent subject appearance." Neither figure has a stated
methodology or a first-party source. The 60% number in particular should not survive into production
guidance.

The underlying advice — that uncluttered reference images bind more reliably — is plausible and matches
general experience. Treat it as a working heuristic, not a measured effect.

---

## Voice continuity

`<AUDIO_N>` selects from a **fixed roster of preset voices** via `voice_id`. Because the roster is
fixed, voice continuity across shots is straightforward: use the same `voice_id` every time.

**Constraints:**

- Maximum **3** voices per generation
- **Custom voice cloning is trusted-partner only** — you cannot upload a specific person's voice
- **There is no way to script what a voice says**

That last point is the binding constraint. A recurring character can sound consistent across a
production, but the words are not yours to choose.

**Routing consequence:** for any character whose lines matter, generate speech with a dedicated voice
model and lay it against Grok's picture. Grok's native audio is good for presence and atmosphere — a
figure speaking at a distance, someone mid-sentence as a shot opens — not for delivering a script.

---

## Extension

Continues **from the last frame** of the source. There is no frame-selection option; claims that 1.5
added one are unsupported.

**`duration` is the portion added, not the total.** A 10-second source with `duration: 5` returns 15
seconds.

**The extension range is 2–10 seconds, default 6** — narrower than the 1–15 range for generation.

Extension is the strongest continuity link available here, because it is pixel-continuous at the join.
Its limit is the usual one: it constrains the *start* of the new segment, and drift resumes after that.

---

## Editing

**Runs on the non-1.5 `grok-imagine-video` model**, so 1.5's improvements do not apply to edits.

**Inherit-then-cap:**

- Duration retains the source's, **capped at 8.7 seconds**. A 4-second input yields 4 seconds out
- Resolution matches the source's, **capped at 720p**. A 1080p input is downsized

This means an edit cannot be used as a finishing pass on a 1080p generation — the edit itself reduces
resolution.

---

## When to route elsewhere

- **Scripted dialogue.** No mechanism exists. `flux-v3-video` (quoted lines), `minimax-h3` (`<d>` tags)
  and `seedance-v2-5` all support it
- **Reproducible output from a seed.** No seed parameter here
- **Per-attribute reference control.** `minimax-h3` splits appearance and motion within one subject
  definition, with explicit retention markers. Grok scopes by token placement, which is looser
- **Many simultaneous identities.** Three is what xAI demonstrates. `seedance-v2-5` takes 30 images
- **1080p with reference binding.** Not available in combination — pick one
- **Anything past 15 seconds in one generation**, or past 25 with an extension

**Reach for Grok Imagine Video when** a shot needs a character bound from a reference *and* a distinct
voice presence, and 720p is acceptable. The clean identity/voice separation is genuinely useful, and
few models offer preset voice assignment at all.
