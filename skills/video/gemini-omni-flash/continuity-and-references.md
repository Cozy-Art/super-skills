# Gemini Omni Flash — Continuity and References

Omni Flash has real in-prompt reference tags, and a genuinely different continuity model from the rest
of the catalogue: **continuity comes from staying in the conversation**, not from re-binding assets.

---

## Image role tags

Two documented tags, written inline where the reference applies.

| Tag | Role |
|---|---|
| `<FIRST_FRAME>` | This image is the video's opening frame |
| `<IMAGE_REF_N>` | This image is a reference — **N starts at 0** |

Google's own examples:

```
<FIRST_FRAME> a woman is walking

in the style of <IMAGE_REF_0> a woman <IMAGE_REF_1> is walking
```

The tag sits at the point in the sentence where its influence applies — `in the style of
<IMAGE_REF_0>` binds that image to style, `a woman <IMAGE_REF_1>` binds the other to the subject.
Placement carries meaning; don't collect the tags at the front.

---

## ⚠️ The zero-indexing trap

**`<IMAGE_REF_0>` is the first reference image.**

Every other numbered-reference model in the catalogue starts at 1 — `@Image1` on Veo and Seedance,
`<IMAGE_1>` on Grok video, `<Subject 1>` on MiniMax H3. Omni Flash starts at 0.

Worse, Google's **declaration-block** form mixes the two bases in one line:

```
[# Sources <FIRST_FRAME>@Image1] [# References <IMAGE_REF_0>@Image2]
```

`@Image1` is the **first uploaded image** (1-based). `<IMAGE_REF_0>` is the **first reference**
(0-based). Both appear in the same block, referring to different things. That is Google's convention,
not an error in the docs.

**Practical rule:** `@ImageN` counts uploads from 1. `<IMAGE_REF_N>` counts references from 0.

---

## Declaration blocks

For clarity with several assets, roles can be declared up front rather than inferred from inline
placement:

```
[# Sources <FIRST_FRAME>@Image1] [# References <IMAGE_REF_0>@Image2]
```

Useful when a prompt carries both a first frame and multiple style references, or when the inline tags
would clutter the prose. The inline form remains the primary one for short prompts.

**Reference count:** Google publishes no cap. Their own worked example uses six. Third-party sources
quote figures between five and ten; none is a documented spec. Treat six as demonstrated and anything
higher as untested.

---

## What does not work, despite appearances

Three reference paths look available and are not. All three are documented by Google.

**Video references** are *accepted by the API schema* but **"not correctly processed by the model at
this time."** A schema accepting a field is not evidence the model honours it — this is the kind of
thing that produces a plausible-looking result that simply ignored the reference.

**Multi-video referencing** — *"Referencing or reasoning across multiple videos is not supported."*

**Audio reference uploads** — *"unsupported in the current version of the API."*

**Consequence:** the only reference channel that actually works is **images**. Any workflow built on
combining a source video, a reference image and reference audio in one prompt is a dead end on this
model, regardless of what circulates in third-party guides.

---

## Continuity through conversation

This is the model's distinctive answer to continuity, and it is worth thinking about differently.

On most models, holding a character across shots means re-binding the same reference asset every time.
On Omni Flash, it means **staying in the same conversation**. Each edit turn builds on the previous
result, so the subject, look and setting persist because they are the same clip — not because they were
re-described.

**What that gives you:**

- Strong continuity across a refinement chain, effectively for free
- No drift from re-description, because there is no re-description
- The ability to converge on a shot rather than re-roll toward it

**What it does not give you:**

- Continuity across *separate* generations. A new conversation is a new subject
- A way back if the chain is broken — see below

### Retention gates all of it

If a clip is generated without being stored, **it cannot be edited in a later turn.** The conversational
chain simply is not available.

The trap is that the fastest configuration is the one that breaks it: `store=false` gives a quicker
synchronous response and silently forfeits editing. If there is any chance a result will be refined, it
must be retained.

---

## Holding a look across separate generations

When shots genuinely must be separate conversations, there is no persistent mechanism — the same
discipline as any model without one applies.

1. **Write a look block once and reuse it verbatim.** Three or four elements, not a list:

```
Overcast north light, desaturated except for the lamp warmth, fine grain,
shallow focus with the background dissolved.
```

2. **Reuse the same reference images** in the same `<IMAGE_REF_N>` slots. A different photo of the same
   subject is a different reference.

3. **Keep the character description identical** — not paraphrased. Any rewording is a new person.

4. **Prefer one conversation over several generations** wherever the shots must match. This is the
   model's actual strength; designing around it beats fighting it.

**Consistency is a stated limitation** on Google's own model card. Expect drift across separate
generations and plan for it rather than being surprised.

---

## What this model cannot do for continuity

No extension, no interpolation. A clip cannot be continued past its generated length, and there is no
first-and-last-frame in-betweening. Combined with the 10-second ceiling, that means **Omni Flash cannot
produce a sequence longer than 10 seconds by itself.** Longer material has to be assembled from
separate clips in an edit, with all the continuity risk that implies.

---

## When to route elsewhere

- **Anything longer than 10 seconds in one piece** — `seedance-v2-5` generates 30 s and extends;
  `minimax-h3` does 15 s
- **Scripted dialogue** — no documented way to specify spoken lines here. `flux-v3-video` (quoted
  lines), `minimax-h3` (`<d>` tags) and `seedance-v2-5` all support it
- **1080p or higher** — 720p is the only option. Note `seedance-v2-5` is also capped at 720p; Seedance
  2.0 and others go higher
- **Persistent character identity across many separate shots** — `minimax-h3`'s `<Subject N>` with
  retention markers, or `seedance-v2-5`'s 30-image budget
- **Legible on-screen text** — a stated model limitation

**Reach for Omni Flash when** the piece is short, the look needs to be found rather than specified, and
iteration is the workflow. Conversational refinement of a 3–10 second clip is something no other model
in the catalogue offers, and for that job it is the right choice.
