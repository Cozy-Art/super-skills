# MiniMax H3 — Best Practices

Depth on prompt construction. The hard rules live in `SKILL.md`; this file covers the craft.

---

## Keep the three layers straight

Worth repeating because it is the error this model invites. H3 has three token systems that all look
like pointing at something, and conflating them is the most common way to get a prompt subtly wrong.

```
<Subject 1>  →  who appears and what they look like
(S1)         →  who is speaking
<Audio 1>    →  what a voice sounds like
```

A character delivering a line while carrying an identity from a reference photo and a voice from a
reference clip uses **all three at once**, and they are not interchangeable:

```
<Subject 1> (S1) steps into the doorway and says, <d>[English] You're late.</d>
```

If dialogue is landing on the wrong character, the cause is almost always a `(Sx)` problem, not a
`<Subject N>` problem.

---

## Writing the six sections

### 1. `subject_definitions`

Define once, at the top, and never redefine mid-prompt.

```
<Subject 1> is the young woman in <Picture 1>, with long dark hair, a blue
cardigan, and a thin silver necklace.
```

- **Three to five fixed, specific details.** Enough to disambiguate, not a catalogue.
- **Bind to sources explicitly.** `<Subject 1>` on its own is undefined; it needs a `<Picture N>` or
  `<Video N>` to mean anything.
- **Split-source subjects are the model's distinctive move** — appearance from one asset, motion from
  another:

```
<Subject 1> is the woman whose appearance comes from <Picture 1> and whose
walking motion comes from <Video 1>.
```

### 2. `summary`

One or two sentences. What the shot *is*, not how it looks. This section orients the model before the
detail arrives; a long summary defeats its purpose.

### 3. `retention_analysis`

What must survive from each reference and what may change. This is where you resolve tension between
references before the model has to guess.

```
<Subject 1>'s face and necklace are fully_preserved from <Picture 1>. The
cardigan may change colour. Camera behaviour follows <Video 1> as a
weak_reference only — do not carry its subject or setting.
```

**Choose retention markers precisely** — they are a fixed vocabulary, not adjectives:

| Marker | Means |
|---|---|
| `fully_preserved` | Reproduce exactly |
| `partially_preserved` | Keep the identifying features, allow variation elsewhere |
| `attribute_transfer` | Move characteristics **to a different identifiable target subject** |
| `weak_reference` | Loose guidance only |

The common misuse is `attribute_transfer` for "loosely inspired by." It specifically means moving
attributes onto a *different* subject. For a video reference guiding only camera behaviour,
`weak_reference` is correct.

### 4. `detailed_description` / `integrated_multimodal_description`

The main block, and where nearly everything happens. **350–500 English words** is MiniMax's own
recommended range for generation tasks.

Carries: action, camera, setting, light, and dialogue. Camera cues and timestamps go **inline**, not
collected at the end.

**One primary action per beat.** If there are three beats, use shot markers rather than stacking them
into one sentence.

### 5. `overall_soundscape`

Diegetic sound only — effects and ambience. Foreground to background.

```
Rain on a tin roof, a chair scraping, low room tone underneath.
```

**Never repeat dialogue here.** Lines live inside `<d>` in the main description. Duplicating them
produces doubled audio, and it is a mistake that is hard to hear as a *duplication* rather than as a
generation artefact.

### 6. `non_diegetic_music`

Score only. **Leave it empty for unscored shots** rather than inventing a bed — an empty section is an
instruction, a vague one is a suggestion the model will act on.

---

## Camera and timing cues

H3 reads cues **directly after the description they apply to**. This is different from models that take
a camera instruction as a separate clause.

```
✅ She crosses to the window [pan] and stops, looking down at the street [static].

❌ She crosses to the window and stops, looking down at the street.
   Camera: pan, then static.
```

Available cues: `[pan]` · `[zoom]` · `[static]`

Shot markers and timestamps, also inline:

```
[Shot 1] A wide of the empty platform, rain blowing across it [static].
[Shot 2] Tight on the departure board as the letters roll over [zoom].

At 00:04.000, the board settles on a single destination.
```

Timestamps are useful when a beat must land at a specific moment — a sound cue, a light change, a
reveal. Use them sparingly; a prompt that timestamps everything reads as a spec rather than a scene.

---

## Multi-speaker dialogue

Assign a speaker ID per character and keep it stable for the whole prompt.

```
<Subject 1> (S1) leans against the door frame and says, <d>[English] You
told them already.</d> <Subject 2> (S2) does not look up. <d>[English] I
told them what they'd find out anyway.</d>
```

Rules that make this work:

- **Stable IDs.** `(S1)` is the same person from first line to last. Reassigning mid-prompt scrambles
  attribution.
- **Name the language in every `<d>` tag**, even when it doesn't change.
- **Budget the lines against the duration.** 4–15 seconds is the range; two short exchanges fit
  comfortably in 10 s, four do not.
- **Frame the speakers.** Lip-sync is only worth having if the mouth is visible — pair dialogue with
  framing that shows it.
- **Use `<scenetrans>`** when a line carries across a cut, and **`<cutoff>`** when speech is deliberately
  truncated by the end of the clip. Both are real tags, and using them is better than letting the model
  decide where the line breaks.

---

## Negation — treat as untested

H3 has no `negative_prompt` parameter, and **in-prompt negation is not documented first-party**. This
is the opposite of FLUX 3, where BFL endorses it explicitly.

Prefer positive replacement:

| ❌ Negation | ✅ Positive |
|---|---|
| "no smiling" | "expression flat, mouth closed" |
| "no camera movement" | `[static]` |
| "not a cluttered room" | "a bare room, one chair, nothing on the walls" |

If a negation is genuinely needed, use it — but flag it in `notes` as untested rather than presenting
it as technique.

---

## Mistakes and fixes

| Symptom | Cause | Fix |
|---|---|---|
| Dialogue on the wrong character | `(Sx)` reused or reassigned | One stable speaker ID per character |
| Doubled or echoing speech | Lines repeated in `overall_soundscape` | Dialogue lives only inside `<d>` |
| Reference ignored | `<Subject N>` used without being defined | Bind it to a `<Picture N>` or `<Video N>` first |
| Wrong attributes carried from a reference | Retention marker too strong | `weak_reference` for camera-only guidance |
| Camera cue ignored | Cues collected at the end | Place them inline, after the description they apply to |
| Request fails with 400 | `first_frame` mixed with `reference_*` | The two conditioning modes are mutually exclusive |
| Request fails, no obvious cause | `resolution` or `duration` omitted | Both are required with no defaults |
| Output softer than expected at 2K | Generated directly at 2K | Generate at 768P, regenerate the approved take |
| Score appears on an unscored shot | `non_diegetic_music` left vague | Leave it empty |
| Quality degrades on a long prompt | Writing to the 7,000-char cap | 350–500 words for the main block |

---

## Iterating

**Change one section at a time.** The six-section structure makes this easy and it is the main practical
benefit of the format — if the sound is wrong, revise `overall_soundscape` alone and leave the
description untouched.

**Iterate at 768P.** It is the base model's native output and $0.08/second against 2K's $0.13. Find the
take, then regenerate at 2K for $0.05/second. Generating directly at 2K throughout is the expensive way
to get the same result.

**Watch the input billing.** Images past the first five cost $0.04 each and video input is billed by
duration at output resolution. A reference-heavy iteration loop costs more than the per-second output
figure suggests.
