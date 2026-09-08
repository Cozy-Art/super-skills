# FLUX 3 Video — Example Prompts

Eight annotated examples across all four modes. Each shows the prompt, the settings line that would
accompany it, and technique notes. Drawn from the recurring example projects.

---

## Example 1 — Simple T2V, character shot

**Project:** *Shadows of Ashford* · **Mode:** `t2v`
**Best for:** single-shot character introductions, coverage, quick ideation

**Prompt:**
```
A stooped archivist in his sixties, close-cropped grey beard, round wire
spectacles, a moth-eaten charcoal cardigan buttoned wrong at the collar,
lifts a ledger from a shelf and turns it toward the window light. Slow
push in at chest height, overcast north light through tall dusty glass,
deep falloff into the stacks behind him. Paper dragging against paper,
a floorboard settling, low room tone under everything.
```

**Settings:** `t2v` · `hd` · 16:9 · `auto` duration · audio on

**Technique notes:**
- Character block is front-loaded and specific enough to reuse verbatim in later prompts — "buttoned
  wrong at the collar" is the kind of detail that reproduces
- One primary action: lifts and turns. Not "walks in, lifts, opens, reads"
- Camera stated explicitly and concretely — "slow push in at chest height," not "cinematic"
- Three audio layers ordered foreground to background: effects, then a settling detail, then bed
- No format words anywhere in the text

---

## Example 2 — Dialogue with lip-sync

**Project:** *Iron Crown* · **Mode:** `t2v`
**Best for:** any beat where the line matters as much as the image

**Prompt:**
```
A young queen in a dark riding coat stands at a map table in a stone
council chamber, both hands flat on the parchment. She looks up and
speaks, low and even: "Then we hold the bridge until spring." Locked-off
medium shot at eye level, torchlight from camera-left, the far wall lost
in shadow. Fire crackle, a cloak shifting, the hollow quiet of a large
cold room.
```

**Settings:** `t2v` · `hd` · 16:9 · 6s · audio on

**Technique notes:**
- **Double quotes are the trigger** — BFL: *"Quote the line in your prompt and the character says it"*
- Speaker described immediately before the line, so attribution is unambiguous
- Delivery note ("low and even") shapes the performance, not just the transcript
- One sentence for a 6-second clip — comfortable. Two would rush
- Locked-off camera is deliberate: a moving camera competes with lip-sync legibility
- Framing shows the face, which is what makes the lip-sync worth having

---

## Example 3 — Keyframe-timed sequence

**Project:** *Forgotten Waters* · **Mode:** `i2v`
**Best for:** hitting known beats at known moments

**Keyframes:** `[[0, deck_wide_dawn.png], [4, rail_closeup.png], [9, horizon_empty.png]]`

**Prompt:**
```
The deck rolls slowly with the swell as the light comes up. The camera
drifts to the rail, holds on knuckles white against wet rope, then lifts
away to open water with nothing on it. Long slow moves throughout, no cuts.
Hull working against the sea, rigging ticking, gulls somewhere off frame
and getting further away.
```

**Settings:** `i2v` · `hd` · 21:9 · 12s · audio on

**Technique notes:**
- **Describes only the delta.** The three keyframes already supply their own content; redescribing the
  deck, the rail and the horizon would fight the conditioning
- Explicit timing places the rail beat at 4s rather than accepting even spacing — the directorial
  choice keyframes exist for
- "No cuts" is a constraint, not negation of an artifact — it stops the model inventing a cut between
  the supplied frames
- Ambience thins deliberately across the clip ("getting further away"), which is a sound cue doing
  narrative work

---

## Example 4 — Multi-shot in one generation

**Project:** *Stellar Drift* · **Mode:** `t2v`
**Best for:** two shots that must match — the only real continuity guarantee FLUX 3 offers

**Prompt:**
```
SHOT ONE — A flight engineer in a scuffed orange pressure suit floats
into a dim instrument bay and steadies herself against a strut, breathing
hard. Handheld medium shot, drifting slightly. HARD CUT. SHOT TWO — Tight
on her face through the visor as the readout light shifts from amber to
red across the glass. Locked off, shallow focus. Suit fans, a metallic
knock through the hull, low continuous system hum under both shots.
```

**Settings:** `t2v` · `hd` · 16:9 · 14s · audio on

**Technique notes:**
- **Two separate generations would drift.** Inside one generation the character, look and audio bed
  carry across the cut — this is the model's actual continuity feature, not a workaround
- One beat per shot. The two-shot structure is not licence to stack more action
- Ambience is stated once and explicitly spans both shots ("under both shots"), which is what makes
  the cut read as a cut rather than two clips
- Camera changes between shots — handheld to locked-off — because that contrast is the edit

---

## Example 5 — Product / brand, image-continuation

**Project:** *Aurelia* · **Mode:** `i2v`
**Best for:** preserving an exact product look while adding motion

**Keyframes:** `[[0, aurelia_bottle_hero.png]]`

**Prompt:**
```
The bottle holds still as a single specular highlight travels slowly down
the glass edge and the amber liquid catches it. Almost imperceptible
drift toward the label. A crystalline chime, then a soft low room tone
settling behind it. No on-screen text, no subtitles.
```

**Settings:** `i2v` · `fhd` · 1:1 · 5s · audio on

**Technique notes:**
- The keyframe carries the product exactly, so the prompt never redescribes the bottle — a brand asset
  is precisely where redescription does the most damage
- Motion is minimal and specific. Luxury product work is one of the few places "almost imperceptible"
  is the right instruction
- **In-prompt negation, vendor-endorsed** — spurious on-screen text is a documented FLUX 3 tendency and
  `No on-screen text, no subtitles.` is BFL's own fix
- `fhd` chosen because this is a finishing shot, not exploration

---

## Example 6 — Environment / b-roll

**Project:** *Shadows of Ashford* · **Mode:** `t2v`
**Best for:** coverage, transitions, establishing atmosphere without a subject

**Prompt:**
```
Mist moves through a stand of bare beeches on a hillside, thinning enough
to show a stone wall running downhill and thickening again. Slow lateral
tracking move, low sun raking from the left, long shadows toward camera.
Low wind across open moorland, distant rooks, no music.
```

**Settings:** `t2v` · `hd` · 21:9 · 8s · audio on

**Technique notes:**
- No subject at all — the weather is the action, and giving it a verb ("thinning… thickening") stops
  the clip reading as a still
- Camera and light both concrete: "slow lateral tracking," "raking from the left"
- `no music` prevents the model scoring an atmospheric shot, which it will otherwise tend to do
- Ambience here is the same locked phrasing used across the project, which is what makes separate
  Ashford clips feel like one place

---

## Example 7 — Draft to enhance

**Project:** *Neon Pulse* · **Mode:** `t2v` with `draft: true`, then `draft_enhance`

**Prompt (unchanged between passes):**
```
A dancer in a wet reflective street stops mid-turn as the sign above her
cuts out, leaving only the spill from a doorway. Handheld, low, following
the turn and settling as the light drops. Rain on asphalt, a transformer
buzz cutting to silence, a distant bassline continuing through it.
```

**Settings, pass 1:** `t2v` · `draft: true` · `hd` · 9:16 · 8s · audio on
**Settings, pass 2:** `draft_enhance` with the approved draft's cache bundle

**Technique notes:**
- **The prompt does not change between passes.** `draft_enhance` re-renders *that same take* from a
  cache bundle pinning mode, prompt, seed and conditioning — it is not a re-roll
- Explore in draft, enhance once. Substantially better economics than iterating at full quality
- The audio beat carries the shot: the buzz cutting to silence is the edit, and it is written as sound
  rather than described as a mood
- 9:16 because this is social delivery — chosen in settings, never in the prompt text

---

## Example 8 — Video continuation

**Project:** *Stellar Drift* · **Mode:** `v2v`
**Best for:** extending an approved clip with continuous action

**Start video:** approved 12s clip ending on the engineer reaching for a panel

**Prompt:**
```
She gets the panel open and the light from inside catches her face. Camera
holds where it is. The system hum drops a semitone and steadies.
```

**Technique notes:**
- **Short by design.** Continuation prompts describe only what happens next; the source clip supplies
  everything else
- "Camera holds where it is" explicitly prevents a new move being invented at the join
- Carrying the audio forward — and changing it deliberately — is what makes the continuation read as
  one shot rather than two
- Note this constrains the *opening* of the new segment; drift resumes after the join. For shots
  separated in time rather than continuous, use one multi-shot generation instead

---

## Quick reference — which mode

| Situation | Mode |
|---|---|
| Imagined scene, nothing exists yet | `t2v` |
| Two shots that must match | `t2v`, multi-shot in one generation |
| Known beats at known times | `i2v` with timed keyframes |
| Exact product or brand asset must be preserved | `i2v` with one keyframe at 0 |
| Continuing an approved clip | `v2v` |
| Exploring cheaply | `t2v` or `i2v` with `draft: true` |
| Finishing an approved draft | `draft_enhance` |
| A character across many separate shots | **Route elsewhere** — see `continuity-and-references.md` |
