# Seedance 2.0 — Example Prompts

Seven annotated examples covering the full range of Seedance 2.0 modes and techniques. Each shows the prompt, the formula breakdown, and the settings line that would accompany it when handed to a director.

---

## Example 1 — Simple T2V (Character Focus)

**Formula:** Subject + Action + Camera / Setting + Lighting + Style / Audio
**Mode:** Text-to-Video
**Best for:** Single-shot character introductions, coverage, quick ideation

**Prompt:**
```
A weathered private investigator in his fifties, rain-soaked trench
coat and a battered fedora, walks slowly beneath a flickering
streetlamp and looks back over his shoulder. Slow tracking shot at
eye level, wet pavement reflecting neon signage in a rain-drenched
alley at night. High-contrast noir style with deep shadow. Rain
hitting pavement, a distant foghorn, his footsteps echoing off brick.
```

**Settings:** 720p · 16:9 · 6s · audio on

**Technique notes:**
- Subject description (age, wardrobe, key props) is specific enough to reuse verbatim in later prompts for the same character
- One action — "walks and looks back" — not a chain of unrelated beats
- Camera and style both stated explicitly; style label ("high-contrast noir") is singular, not stacked
- No format words anywhere in the text — 16:9, 6 seconds, and audio-on all live in the settings line instead

---

## Example 2 — Dialogue / Lip-Sync

**Formula:** Setting + Subject / Action + Dialogue / Camera + Audio
**Mode:** Text-to-Video
**Best for:** Character scenes, exposition delivery, any beat where the line matters as much as the visual

**Prompt:**
```
A hooded sorceress stands before a cracked stone altar deep inside a
candlelit crypt. She raises her hand toward the flame and speaks,
low and commanding: "The seal will not hold past moonrise." Locked-off
medium shot, eye level. Flickering candlelight, distant dripping
water, a low ambient drone under her voice.
```

**Settings:** 720p · 16:9 · 5s · audio on

**Technique notes:**
- Dialogue is in double quotes with a delivery note ("low and commanding") — this shapes the voice performance, not just the transcript
- Locked-off camera is a deliberate choice for dialogue: a moving camera competes with lip-sync legibility
- Audio names three layers even without labeling them explicitly: the line itself (foreground), the drone (background bed), the dripping water (a placed detail) — Seedance blends these from plain description, no special syntax required

---

## Example 3 — Environment / B-Roll

**Formula:** Setting + Subject / Camera + Lighting / Audio
**Mode:** Text-to-Video (Fast tier — good fit for coverage/b-roll)
**Best for:** Landscape and location coverage, transitional footage, documentary establishing shots

**Prompt:**
```
A weathered fishing trawler drifts on still water at first light, mist
clinging to the surface of a northern harbor. Slow drone push-in from
a low angle, gaining height as it clears the boat's mast. Cool blue
dawn light, soft fog diffusing the horizon. Distant gulls, water
lapping against the hull, low wind.
```

**Settings:** 720p · 21:9 · 8s · audio on

**Technique notes:**
- No named character — the environment itself is the subject, and gets the same specificity a character would ("weathered," "northern harbor," "still water at first light")
- 21:9 chosen for a widescreen documentary b-roll feel — worth calling out in the settings line since it's a less common default than 16:9
- Fast tier suggested here deliberately: b-roll and coverage are exactly the use case where the cost/latency savings matter more than squeezing out the last bit of quality

---

## Example 4 — Product Image-to-Video

**Formula:** Motion + Camera / Audio (image already fixes subject and setting)
**Mode:** Image-to-Video
**Best for:** Bringing an approved product still to life without re-describing it

**Prompt:**
```
The bottle catches the light as the camera completes a slow 180-degree
orbit around it, liquid inside catching a faint amber glow. Subtle
depth-of-field shift as the camera settles on the label. Soft ambient
room tone, a single delicate chime as the motion resolves.
```

**Settings:** 720p · adaptive/matches source image · 6s · audio on · image reference: approved product still, first frame

**Technique notes:**
- The prompt never re-describes the bottle, the surface it sits on, or the lighting setup — all of that is already fixed by the source image
- Only what changes gets written: the camera move, the light catching the liquid, the audio
- Aspect ratio set to adapt to the source image rather than forced to a fixed ratio, since the image is the anchor

---

## Example 5 — Vertical Social / Native Multi-Shot

**Formula:** Shot 1 (Subject + Action + Camera) / Cut scene to Shot 2 / Style + Audio
**Mode:** Text-to-Video
**Best for:** Short-form vertical content, music-video cutaways, anywhere a hard cut reads better than a single continuous take

**Prompt:**
```
A singer in a mirrored bomber jacket bursts through a curtain of neon
light, mid-performance, punch-in to a tight vertical close-up on her
face under strobing pink and blue light. Cut scene to the full band
hitting the chorus together on a smoke-filled stage, wide shot from
low angle. Energetic concert-film style, driving bassline with crowd
noise swelling under the cut.
```

**Settings:** 720p · 9:16 · 10s · audio on

**Technique notes:**
- The scene cut is written directly into the prose ("Cut scene to...") — there's no separate multi-shot parameter to set
- Two shots, each with one clear beat — pushing to three or more inside a single generation starts compressing each beat until none of them land
- Vertical framing (9:16) stated only in the settings line, never in the text itself

---

## Example 6 — Reference-to-Video Continuity

**Formula:** Reference roles + Subject/Action continuation / Camera continuity / Audio
**Mode:** Reference-to-Video
**Best for:** Continuing a sequence so the new shot reads as part of the same scene as the one before it

**Prompt:**
```
Keep the camera movement and lighting from @Video1. The same pilot,
now outside the wreckage, steadies herself against the hull and looks
up at the twin suns breaking through the dust storm. Same handheld
tracking style as the previous shot, continuing the low, gritty
practical lighting. Wind howling, distant metal groaning, her
breathing audible over the storm.
```

**References:** `@Video1` = prior shot in the sequence (camera/motion reference)
**Settings:** 720p · 16:9 · 8s · audio on

**Technique notes:**
- `@Video1` is assigned an explicit role ("camera movement and lighting") rather than just listed as an input
- The character description is intentionally light here — the visual identity is already carried by the prior clip; only the new beat needs full description
- This is the pattern to reach for whenever a shot needs to feel continuous with the one before it, rather than starting a new scene from scratch

---

## Example 7 — Video Editing (Targeted Change)

**Formula:** Recreate + the one change / Keep + the invariants
**Mode:** Reference-to-Video (video-edit pattern)
**Best for:** Fixing or altering one element of an existing clip without regenerating the whole shot

**Prompt:**
```
Recreate the scene from @Video1 but replace the cracked stone altar
with the runed obsidian pedestal from @Image1. Keep the sorceress's
performance, the candlelight, and the camera framing exactly as they
were.
```

**References:** `@Video1` = the clip being edited · `@Image1` = the new prop/set element
**Settings:** 720p · 16:9 · match source duration · audio: preserve original where possible

**Technique notes:**
- The change is named first, the invariants second — this is the order the model weighs most reliably
- Only one change is requested (the altar). A second simultaneous change (say, also swapping the lighting) should be a separate follow-up pass, not bundled into the same edit
- Restating the invariants explicitly, even though they'd arguably be "kept" by default, meaningfully reduces drift
