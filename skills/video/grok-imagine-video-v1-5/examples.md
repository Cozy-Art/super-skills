# Grok Imagine Video 1.5 — Example Prompts

Annotated examples across all five modes, drawn from the recurring example projects.

Note the prompt lengths. These are deliberately not short — see `best-practices.md` on writing for the
upsampler.

---

## Example 1 — Text-to-video, 1080p

**Project:** *Shadows of Ashford* · **Mode:** text-to-video

**Prompt:**
```
An elderly archivist in round wire spectacles and a moth-eaten charcoal
cardigan lifts a heavy ledger down from a high shelf and turns it toward the
window light. Low-angle medium shot at chest height, slow push in, slight
handheld drift. A long archive hall with tall dusty windows down one side and
floor-to-ceiling shelving on the other. Overcast north light through the
glass, deep falloff into the stacks behind him, dust visible in the beam.
Paper dragging against paper, a floorboard settling, low room tone
underneath.
```

**Settings:** 8s · 1080p · 16:9

**Technique notes:**
- **Around 80 words — deliberately.** The "10–20 words" advice circulating for this model has no
  first-party basis, and xAI's own showcase prompt runs about 90. Every element left unspecified is one
  the upsampler decides
- Camera, light and setting all stated concretely — these are exactly the elements the upsampler fills
  in generically when omitted
- **1080p is available here** because this is text-to-video. Reference mode would cap at 720p
- One primary action, with a settle. Eight seconds holds one beat

---

## Example 2 — Reference-bound character with assigned voice

**Project:** *Neon Pulse* · **Mode:** reference-to-video
**References:** `<IMAGE_1>` dancer portrait, `<IMAGE_2>` jacket detail · `<AUDIO_0>` preset voice

**Prompt:**
```
The dancer from <IMAGE_1> stands under a dead neon sign on wet asphalt,
wearing the jacket from <IMAGE_2> over black trousers. She looks up at the
sign as it cuts out, then speaks to camera with the voice from <AUDIO_0>,
half to herself. Handheld low angle, slow drift left, the only remaining
light spilling from an open doorway camera-right. Rain on asphalt, a
transformer buzz cutting to silence, a distant bassline continuing under it.
```

**Settings:** 8s · **720p** · 9:16

**Technique notes:**
- **Angle brackets, not `@`.** The `@Image1` form circulates widely and appears nowhere in xAI's
  documentation
- **Each token sits beside what it governs** — `<IMAGE_1>` on the person, `<IMAGE_2>` on the jacket.
  Collecting them at the front would lose the scoping
- **`<AUDIO_0>` selects a voice, not a script.** The prompt describes *manner* — "half to herself" —
  because there is no way to specify words. Writing a quoted line here would do nothing
- **720p is forced.** Reference mode caps there; this shot trades resolution for identity binding
- If the references don't bind, try `<IMAGE_0>` — xAI's docs are inconsistent about the base

---

## Example 3 — Image-to-video

**Project:** *Aurelia* · **Mode:** image-to-video
**Input:** hero bottle still

**Prompt:**
```
A single specular highlight travels slowly down the glass edge and the amber
liquid catches it as the camera drifts almost imperceptibly toward the label.
Locked-off framing otherwise, no reframing. A crystalline chime, then a soft
low room tone settling behind it.
```

**Settings:** 5s · 1080p · **aspect ratio inherited from the source image**

**Technique notes:**
- The source image carries the product exactly, so the prompt **never redescribes the bottle**
- **Do not override the aspect ratio.** Image-to-video inherits the source image's ratio, and
  overriding it *stretches* rather than crops
- **1080p available** — image-to-video keeps the top tier, unlike reference mode
- Minimal specific motion; five seconds holds one highlight travel

---

## Example 4 — Extension

**Project:** *Stellar Drift* · **Mode:** extend
**Source:** approved 10-second corridor clip

**Prompt:**
```
She reaches the junction panel and gets it open, the light from inside
catching her face. The camera holds where it is. The system hum drops a
semitone and steadies.
```

**Settings:** `duration: 6` → **returns a 16-second video**

**Technique notes:**
- ⚠️ **`duration` is the portion ADDED, not the total.** 10-second source + `duration: 6` = 16 seconds
  out. xAI's own wording: *"if your input video is 10 seconds and you set duration to 5, the returned
  video will be 15 seconds"*
- **The extension range is 2–10, default 6** — narrower than the 1–15 generation range. Asking for 12
  here fails
- Short and continuation-focused; the source supplies everything else
- "The camera holds where it is" prevents a new move at the join
- Continues from the **last frame**. There is no frame-selection option

---

## Example 5 — Edit

**Project:** *Aurelia* · **Mode:** edit
**Source:** approved 4-second 1080p product clip

**Prompt:**
```
Replace the black marble surface with brushed brass. Keep the bottle, the
label, the highlight travel and the camera movement unchanged.
```

**Settings:** duration and resolution both **inherited from the source**

**Technique notes:**
- **Inherit-then-cap, not fixed output.** A 4-second input yields 4 seconds out — not 8.7. The 8.7s
  figure is a *ceiling*, not a fixed length
- ⚠️ **The 1080p source will come back at 720p.** Edit caps resolution at 720p, so an edit cannot serve
  as a finishing pass on a 1080p generation
- **Edit runs on the non-1.5 `grok-imagine-video` model** — 1.5's improvements do not apply
- Naming the invariants is what keeps an edit from becoming a re-generation

---

## Example 6 — Resolution trade-off decision

**Project:** *Iron Crown* · **Scenario:** hero shot of the queen, delivery at 1080p

**Notes field:**
```
Two viable approaches, and the trade-off is unusual on this model:

A) Reference-to-video with <IMAGE_1> bound to the approved queen portrait.
   Identity matches other shots exactly. CAPS AT 720p.

B) Text-to-video at 1080p, with the queen described in prose reusing the
   locked character block. Full resolution, but identity is descriptive
   rather than bound — expect variation from the reference.

For a hero shot cut against reference-bound coverage, A is correct despite
the resolution cost — a queen who doesn't match her own coverage is worse
than a softer queen.

For an isolated establishing or insert shot where she is small in frame,
B is the better trade.

No cost dimension either way: $0.08/second at every resolution.
```

**Technique notes:**
- This trade-off is specific to Grok — most models don't penalise reference binding with resolution
- Following the D5 precedent: `notes` carries the real decision, including its cost

---

## Example 7 — Routing away

**Project:** *Iron Crown* · **Scenario:** the council scene, two characters exchanging lines

**Notes field:**
```
Grok Imagine Video cannot deliver this scene as written.

<AUDIO_0> and <AUDIO_1> can assign two distinct preset voices, and <IMAGE_1>
and <IMAGE_2> can bind both characters' appearances. But xAI documents NO
mechanism for specifying what a voice says. Assigning a voice does not
assign words, and there is no quoted-line convention on this model.

Options:

1. Route the scene to minimax-h3 (<d>[Language] … </d> with (S1)/(S2)
   speaker IDs), flux-v3-video (quoted lines), or seedance-v2-5. All three
   document a dialogue trigger.

2. Keep Grok for the picture and generate the dialogue with a dedicated
   voice model, laying the audio against it in the edit. Viable, but it
   forfeits native lip-sync.

Recommend option 1.

Grok remains the right tool for the reaction shots and coverage in this
scene, where presence matters and specific words do not.
```

**Technique notes:**
- The dialogue gap is the most likely reason to route away from this model, and the easiest to
  discover too late — native audio *and* voice assignment both exist, which makes it look like
  scripted speech should work
- Note the last line: routing away from part of a scene is not routing away from the model

---

## Quick reference

| Situation | Mode | Notes |
|---|---|---|
| Imagined scene, top resolution | Text-to-video | 1080p available |
| Fixed opening image | Image-to-video | 1080p; inherits source ratio |
| Character bound from a reference | Reference-to-video | **Caps at 720p** |
| Character *and* a distinct voice | Reference-to-video with `<AUDIO_N>` | Voice ≠ script |
| Continuing an approved clip | Extend | `duration` is the **addition**; range 2–10 |
| Changing an approved clip | Edit | Inherits then caps at 8.7s / 720p |
| Specific spoken lines | **Route elsewhere** | No scripting mechanism |
| Reproducible from a seed | **Route elsewhere** | No `seed` parameter |
| More than three identities | **Route elsewhere** | Three is what xAI demonstrates |
