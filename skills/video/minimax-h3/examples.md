# MiniMax H3 — Example Prompts

Eight annotated examples across all five modes, including a full six-section structured output. Drawn
from the recurring example projects.

---

## Example 1 — Simple text-to-video

**Project:** *Shadows of Ashford* · **Mode:** text-to-video

**Prompt:**
```
A stooped archivist in his sixties, close-cropped grey beard, round wire
spectacles, a moth-eaten charcoal cardigan buttoned wrong at the collar,
lifts a ledger down from a high shelf and carries it to the window [pan].
He sets it on the sill and opens it, turning it toward the light [static].
Overcast north light through tall dusty glass, deep falloff into the stacks
behind him.
```

**Soundscape:** `Paper dragging against paper, a floorboard settling, low room tone underneath.`
**Music:** *(empty — unscored)*

**Settings:** `768P` · 16:9 · 8s

**Technique notes:**
- Camera cues sit **inline, directly after the description they apply to** — not collected at the end
- Two beats, each with its own cue: `[pan]` for the carry, `[static]` for the settle
- `ratio` must be explicit and non-`adaptive` for text-to-video
- `non_diegetic_music` left genuinely empty. A vague entry here is a suggestion the model will act on

---

## Example 2 — Multi-speaker dialogue

**Project:** *Iron Crown* · **Mode:** text-to-video

**Prompt:**
```
A young queen in a dark riding coat stands at a map table in a stone council
chamber. An older general stands opposite, arms folded.

<Subject 1> (S1) plants both hands on the parchment and looks up.
<d>[English] Then we hold the bridge until spring.</d>

<Subject 2> (S2) does not move. <d>[English] Spring is four months away,
your grace.</d>

Medium two-shot at eye level [static]. Torchlight from camera-left, the far
wall lost in shadow.
```

**Soundscape:** `Fire crackle, a cloak shifting, the hollow quiet of a large cold room.`

**Settings:** `768P` · 16:9 · 10s

**Technique notes:**
- **Stable speaker IDs.** `(S1)` and `(S2)` are assigned once and never reused for another character
- Language named in **every** `<d>` tag, even though it doesn't change
- Two short exchanges fit comfortably in 10 seconds; four would not
- Locked-off two-shot is deliberate — both mouths stay in frame, which is what makes lip-sync worth
  having
- Dialogue appears **only** inside `<d>`, never repeated in the soundscape

---

## Example 3 — Reference-to-video, full six-section structure

**Project:** *Stellar Drift* · **Mode:** reference-to-video
**References:** `<Picture 1>` hero portrait of the flight engineer, `<Video 1>` handheld corridor move

This is the complete structured form. All six sections, in fixed order.

**1. `subject_definitions`**
```
<Subject 1> is the flight engineer in <Picture 1> — mid-thirties, shaved
head, a healed burn scar across the left jaw, scuffed orange pressure suit
with a hand-stencilled callsign on the chest plate.
```

**2. `summary`**
```
The engineer pulls herself along a dim service corridor and stops at a
junction as a warning light begins to cycle.
```

**3. `retention_analysis`**
```
<Subject 1>'s face, scar and suit markings are fully_preserved from
<Picture 1>. Lighting on her may change. Camera behaviour follows <Video 1>
as a weak_reference only — do not carry its subject, setting or colour.
```

**4. `detailed_description`**
```
<Subject 1> pulls herself hand-over-hand along a narrow service corridor,
moving away from camera, boots never touching the deck [pan]. She reaches a
junction, catches a strut and stops herself, turning back toward the way she
came [static]. An amber warning light begins to cycle above her, throwing
her shadow long down the corridor and pulling it back again. Tight corridor
framing, practical lighting from recessed strips at knee height, everything
beyond ten metres falling into dark.
```

**5. `overall_soundscape`**
```
Suit fans running continuously, gloves catching on metal, a distant
structural knock through the hull, low system hum underneath.
```

**6. `non_diegetic_music`**
```
A single sustained low string tone, entering as the warning light starts.
```

**Settings:** `768P` · 21:9 · 12s

**Technique notes:**
- `retention_analysis` explicitly **fences the video reference** — without "do not carry its subject,
  setting or colour," a `<Video N>` tends to bring its whole scene along
- `weak_reference` is the correct marker for camera-only guidance. `attribute_transfer` would be wrong;
  it means moving characteristics onto a *different* subject
- The subject definition names three fixed, reproducible details — scar, callsign, shaved head
- Music section is used here and left empty in Example 1; both are deliberate

---

## Example 4 — Split-source subject

**Project:** *Neon Pulse* · **Mode:** reference-to-video
**References:** `<Picture 1>` dancer portrait, `<Video 1>` reference choreography, `<Audio 1>` voice clip

**`subject_definitions`:**
```
<Subject 1> is the dancer whose appearance comes from <Picture 1> and whose
movement comes from <Video 1>. Her speaking voice comes from <Audio 1>.
```

**`retention_analysis`:**
```
Appearance fully_preserved from <Picture 1>. Movement partially_preserved
from <Video 1> — follow the phrasing and weight, not the exact steps. Voice
timbre from <Audio 1> as fully_copy.
```

**`detailed_description`:**
```
<Subject 1> turns under a dead neon sign on wet asphalt, catching herself
mid-phrase as the light above her cuts out [static]. She looks up at it.
<Subject 1> (S1) says, half to herself, <d>[English] Every night this
week.</d> Handheld low angle, the only remaining light spilling from an
open doorway camera-right.
```

**Settings:** `768P` · 9:16 · 10s

**Technique notes:**
- **The model's most distinctive capability**: identity, motion and voice drawn from three different
  assets in one subject definition
- All three layers active simultaneously — `<Subject 1>` for identity, `(S1)` for attribution,
  `<Audio 1>` for timbre. They compose without substituting
- `partially_preserved` on movement is deliberate: follow the phrasing, not the literal steps
- Vertical delivery is chosen in settings, never written into the prompt

---

## Example 5 — Image-to-video, product

**Project:** *Aurelia* · **Mode:** image-to-video
**Input:** hero bottle still as `first_frame`

**Prompt:**
```
A single specular highlight travels slowly down the glass edge and the amber
liquid catches it [static]. Almost imperceptible drift toward the label.
```

**Soundscape:** `A crystalline chime, then a soft low room tone settling behind it.`

**Settings:** `768P` → regenerate approved take at `2K` · `adaptive` · 5s

**Technique notes:**
- The first frame carries the product exactly, so the prompt **never redescribes the bottle** — brand
  assets are where redescription does the most damage
- `ratio` is **forced to `adaptive`** in image-to-video; specifying otherwise is ignored
- Iterate at 768P, regenerate at 2K. Generating directly at 2K costs $0.13/s against $0.08 + $0.05
- Minimal, specific motion. Luxury product work is one of the few places "almost imperceptible" is the
  right instruction

---

## Example 6 — Last-frame conditioning

**Project:** *Forgotten Waters* · **Mode:** last-frame
**Input:** empty horizon still as `last_frame`

**Prompt:**
```
The camera begins tight on knuckles white against wet rope and lifts away
across the deck [zoom], the rail dropping out of frame, until nothing
remains but open water.
```

**Soundscape:** `Hull working against the sea, rigging ticking, gulls somewhere off frame and thinning out.`

**Settings:** `768P` · 21:9 · 9s

**Technique notes:**
- **Last-frame-only is easy to overlook and genuinely useful** — it fixes where the shot lands and
  lets the model find the approach
- The prompt describes the *journey to* the fixed frame, not the frame itself
- Ambience thins deliberately across the clip, doing narrative work through sound

---

## Example 7 — Multi-shot in one generation

**Project:** *Shadows of Ashford* · **Mode:** text-to-video

**Prompt:**
```
[Shot 1] A wide of an empty station platform at dusk, rain blowing across
it in sheets [static].

[Shot 2] Tight on the departure board as the letters roll over and settle
[zoom].

At 00:06.000, the board stops on a single destination and the platform
lights come up.
```

**Soundscape:** `Rain on a tin canopy, the mechanical clatter of split-flap letters, a distant announcement too muffled to parse.`

**Settings:** `768P` · 16:9 · 10s

**Technique notes:**
- Shot markers keep two beats matching inside one generation — cheaper and more reliable than two
  separate generations
- **A timestamp places the reveal at 6 seconds** rather than letting the model choose. Use these
  sparingly; timestamping everything reads as a spec, not a scene
- Two or three shots is the realistic ceiling inside the 15-second duration cap

---

## Example 8 — Routing away

**Project:** *Iron Crown* · **Scenario:** the queen appears in 40 shots across the production

**Notes field:**
```
H3 is a good fit for identity here — <Subject 1> bound to <Picture 1> with
fully_preserved holds well across shots, and up to 9 reference images allow
adding angles as approved frames accumulate.

Two caveats routed elsewhere:

- The queen's VOICE across 40 shots should not come from H3's native audio.
  Bind a dedicated voice model with a real identity lock and lay the audio
  against H3's picture. H3's native speech is excellent for incidental and
  background lines, not for a lead's consistent voice across a production.

- Any shot needing more than 15 seconds in a single take should go to
  seedance-v2-5 (30s single-pass, extends twice). There is no Extend
  endpoint on H3 despite widespread claims otherwise.
```

**Technique notes:**
- Following the D5 precedent — `notes` is where honesty lives, including recommending a different
  model when this one is the wrong choice
- A skill that only advocates for its own model makes the routing layer's job harder

---

## Quick reference — which mode

| Situation | Mode |
|---|---|
| Imagined scene, nothing exists yet | Text-to-video |
| Opening frame is fixed | Image-to-video (`first_frame`) |
| Ending is fixed, approach open | Last-frame |
| Both ends fixed | First-and-last-frame |
| Character carried from a photo | Reference-to-video |
| Identity and motion from different assets | Reference-to-video, split-source subject |
| Two beats that must match | One generation with `[Shot 1]` / `[Shot 2]` |
| Fixed opening **and** a referenced character | **Not possible in one call** — see `continuity-and-references.md` |
| Longer than 15 seconds | **Route to `seedance-v2-5`** |
