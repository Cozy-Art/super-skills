# Grok Imagine Video 1.5 — Example Prompts

Annotated examples across the modes, drawn from the recurring example projects.

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
**References:** `<IMAGE_0>` dancer portrait, `<IMAGE_1>` jacket detail · `<AUDIO_0>` preset voice

**Prompt:**
```
The dancer from <IMAGE_0> stands under a dead neon sign on wet asphalt,
wearing the jacket from <IMAGE_1> over black trousers. She looks up at the
sign as it cuts out, then speaks to camera with the voice from <AUDIO_0>,
half to herself: "Every light on this street owes me money." Handheld low
angle, slow drift left, the only remaining light spilling from an open
doorway camera-right. Rain on asphalt, a transformer buzz cutting to
silence, a distant bassline continuing under it.
```

**Settings:** 8s · **720p** · 9:16

**Technique notes:**
- **Angle brackets, not `@`.** The `@Image1` form circulates widely and appears nowhere in xAI's
  documentation
- **Each token sits beside what it governs** — `<IMAGE_0>` on the person, `<IMAGE_1>` on the jacket.
  Collecting them at the front would lose the scoping
- **Zero-based.** The first attached reference is `<IMAGE_0>` — xAI's stated convention
- **`<AUDIO_0>` selects the voice; the quoted line is the script.** Delivery — "half to herself" — sits
  outside the quotes as prose. One short line suits an 8-second clip
- **720p is forced.** Reference mode caps there; this shot trades resolution for identity binding

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

**Settings:** 5s · 1080p · aspect ratio set by the source image

**Technique notes:**
- The source image carries the product exactly, so the prompt **never redescribes the bottle**
- **Crop the source to the delivery ratio first.** Image-to-video ignores `aspect_ratio` — the
  output always matches the source image
- **Native 1080p available** — image-to-video keeps the top tier, unlike reference mode
- Minimal specific motion; five seconds holds one highlight travel

---

## Example 4 — Extension

**Project:** *Stellar Drift* · **Mode:** extend (classic `grok-imagine-video`)
**Source:** approved 10-second corridor clip generated on 1.5

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
- Extension runs on classic `grok-imagine-video` — 1.5 does not extend

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

A) Reference-to-video with <IMAGE_0> bound to the approved queen portrait.
   Identity matches other shots exactly. CAPS AT 720p.

B) Text-to-video at 1080p, with the queen described in prose reusing the
   locked character block. Full resolution, but identity is descriptive
   rather than bound — expect variation from the reference.

For a hero shot cut against reference-bound coverage, A is correct despite
the resolution cost — a queen who doesn't match her own coverage is worse
than a softer queen.

For an isolated establishing or insert shot where she is small in frame,
B is the better trade.

Cost: A runs at $0.14/second (720p), B at $0.25/second (1080p).
```

**Technique notes:**
- This trade-off is specific to Grok — most models don't penalise reference binding with resolution
- Following the D5 precedent: `notes` carries the real decision, including its cost

---

## Example 7 — Two-character dialogue with assigned voices

**Project:** *Iron Crown* · **Mode:** reference-to-video
**References:** `<IMAGE_0>` queen portrait, `<IMAGE_1>` chancellor portrait, `<IMAGE_2>` council
chamber · `<AUDIO_0>`, `<AUDIO_1>` preset voices

**Prompt:**
```
In the council chamber from <IMAGE_2>, the queen from <IMAGE_0> sits at the
head of the long table, the chancellor from <IMAGE_1> standing at her right.
Wide shot, then a cut over his shoulder onto her face. The chancellor, with
the voice from <AUDIO_1>, says stiffly: "The northern lords will not wait
for spring." The queen, with the voice from <AUDIO_0>, answers without
looking up: "Then they will wait for me." Candlelight from the table,
cold daylight from the high windows behind her. Fire crackling, a chair
creaking, otherwise silence.
```

**Settings:** 10s · **720p** · 16:9

**Technique notes:**
- **Each line attributed and placed** — speaker named, token-bound, and given a delivery note before
  the quotes, so the lip-sync lands on the right face
- **Voice paired to speaker explicitly.** `<AUDIO_0>`/`<AUDIO_1>` are numbered independently of the
  images; the prompt says which voice belongs to whom
- **Two short lines for 10 seconds.** xAI's own four-line exchange runs 15 seconds
- The shot direction ("wide shot, then a cut over his shoulder") follows xAI's own dialogue example

---

## Example 8 — Keyframed seasons

**Project:** *Shadows of Ashford* · **Mode:** reference-to-video (pinned frames)
**Inputs:** `image` spring oak · `keyframes` summer, autumn, winter oak at 3 s, 6 s, 9 s

**Prompt:**
```
The oak on the hill moves through the year: blossom falls away into dense
summer green, the canopy burns amber and sheds, and the first snow settles
on bare branches. Locked-off wide, clouds racing overhead, the light cooling
with each season. Birdsong thinning to wind, then a muffled winter hush.
```

**Settings:** 12s · 720p · 16:9 · keyframes at 3 / 6 / 9 s

**Technique notes:**
- **The pins carry the pictures; the prompt carries the journey.** No pinned frame is re-described —
  only the transitions, camera and sound
- **Locked off** keeps every pinned composition reachable
- Keyframe timestamps sit strictly inside the clip and at least 1/3 s apart; they are inputs, not prompt
  text
- Any pinned frame caps the request at 720p

---

## Quick reference

| Situation | Mode | Notes |
|---|---|---|
| Imagined scene, top resolution | Text-to-video | 1080p available |
| Fixed opening image | Image-to-video | 1080p; inherits source ratio |
| Character bound from a reference | Reference-to-video | **Caps at 720p**; tokens from `<IMAGE_0>` |
| Character *and* a distinct voice | Reference-to-video with `<AUDIO_N>` | Voice picks timbre; quoted line is the script |
| Specific spoken lines | Any mode — quoted, attributed lines | Lip-synced; keep lines short |
| Exact start/end/mid frames | `image` / `last_frame` / `keyframes` | Up to 4 keyframes; caps at 720p |
| Continuing an approved clip | Extend (classic model) | `duration` is the **addition**; range 2–10 |
| Changing an approved clip | Edit (classic model) | Inherits then caps at 8.7s / 720p |
| Reproducible from a seed | **Route elsewhere** | No `seed` parameter |
| More than 14 references or 3 voices | **Route elsewhere** | 1.5's ceilings |
