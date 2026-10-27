# FLUX 3 Image — Continuity & References

FLUX 3 has no seed, no conversation thread and no "previous generation ID". **Continuity is carried entirely by the images you send back in.** Treat your approved outputs as the source of truth.

## 1. Housekeeping That Makes Continuity Possible

- Download every approved result immediately — `result.sample` URLs expire after ~1 hour.
- Keep a local library: `identity/`, `wardrobe/`, `locations/`, `style/`, `approved-shots/`.
- Record the prompt **and** the returned `result.prompt` with each keeper.

## 2. Reference Role Assignment

Up to 10 references, but explicit roles matter more than count. Every image gets a job.

```
Use the person from image 1, the jacket from image 2, and the kitchen from image 3.
Preserve the face and hairstyle from image 1 exactly. Take only the lighting and
palette from image 4 — not its subject or composition.
```

| Slot | Typical role |
|---|---|
| image 1 | Base scene **or** identity master (drives `auto` ratio; strongest anchor) |
| image 2–3 | Wardrobe, full-body proportions, side profile |
| image 4–5 | Location / set |
| image 6 | Style frame (lighting, palette, texture only) |
| image 7+ | Props, secondary characters |

Prose refs are **1-based** ("image 1"). Box refs are **0-based** (`ref_image_0`). Don't mix them up.

## 3. Character Consistency Protocol

1. Generate an **identity master**: unobstructed face, recognizable hair, signature wardrobe, neutral even light, plain backdrop, 4:5 or 1:1 at `2k`.
2. Optional supporting refs: full-body, side profile, signature prop.
3. Keep the identity master in the **same slot** (usually image 1) across the whole sequence.
4. Repeat a compact **identity block** in every prompt — textually identical:
   ```
   IDENTITY: Mara Venn — early thirties, sharp oval face, dark brown eyes,
   jaw-length black bob, thin silver scar through left eyebrow.
   ```
5. State what may change and what must stay exact ("She now wears… Preserve her facial structure, scar, hair and age.").
6. Keep ratio, palette, medium and style vocabulary constant.
7. Change **one** major variable per request: pose, location, costume or lighting.
8. Feed approved shots forward rather than re-describing them.

## 4. Style Lock

A reusable block, pasted verbatim into every prompt in the project:

```
STYLE LOCK: photographed as a restrained 35mm science-fiction drama; practical
sets, cool green shadows, amber utility lights, natural skin texture, subtle
film grain, low saturation, matte surfaces.
```

For stronger control, add one approved style frame and say it supplies **only** lighting, palette, texture and photographic treatment.

Pair with `grounding: false` so web search doesn't pull the look toward real-world imagery.

## 5. Multi-Shot / Storyboard Sequencing

- Establish a hero frame for every recurring character and location before shooting coverage.
- For each new shot: image 1 = previous approved frame (or the cleanest master), then identity/wardrobe/location refs.
- Define each shot by framing, lens, action and **screen direction**; keep left-to-right movement and eyelines consistent across cuts.
- Branch new shots from the cleanest master — long edit chains accumulate drift.
- Use bounding boxes for recurring spatial anchors (doorway, vehicle, title region) so they land in the same place shot to shot.
- Read `result.prompt` after each shot; if the model expanded something you didn't want, pin it down in the next prompt.

**Shot template:**
```
[Shot size + angle + lens]. The same woman from image 1 [action, screen direction].
[IDENTITY block]. She stands in [location from image 3]. [Lighting matching ref].
[STYLE LOCK].
```

## 6. Edit Continuity

- Edit from the approved image as image 1, `aspect_ratio: "auto"`.
- Natural language for broad changes; bounding-box edit rows when one element must move/change and everything else must hold.
- Anchor (`kind: "anchor"`) the elements that must not move.
- After 3–4 sequential edits, regenerate from the master with the accumulated changes stated in one prompt.

## 7. Resolution Handoff

Draft → final is not an upscale; it's a new roll. To keep a draft's composition at `2k`/`4k`, pass the draft as image 1 and say "Recreate image 1 at higher fidelity, preserving composition, identity, lighting and palette exactly."

## 8. Handoff to Video

FLUX 3 Image outputs no video. Approved stills are ideal first/last/intermediate keyframes for FLUX 3 Video or any image-to-video model. Generate keyframes with the same identity block, style lock and screen direction so the video model inherits consistent anchors.
