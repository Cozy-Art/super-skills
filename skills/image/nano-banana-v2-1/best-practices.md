# Nano Banana 2.1 — Best Practices

## 1. Write a Brief, Not a Tag List

Google's guidance for the Nano Banana family: a coherent scene description beats disconnected keywords. Google's text-to-image formula is **[Subject] + [Action] + [Location/context] + [Composition] + [Style]**; for references it is **[Reference images] + [Relationship instruction] + [New scenario]**.

| Weak | Better |
|---|---|
| `coffee shop, cozy, vintage, Edison bulbs` | `A cozy vintage coffee shop with exposed beams; warm Edison bulbs hang over a long oak counter while morning light slants across the floor` |
| `cinematic` | `Low-angle 35mm still, hard cyan backlight, deep amber practical lamps` |
| `highly detailed` | `Rain droplets catch the shop light; individual wool fibres visible on the coat` |
| `professional product photo` | `Studio product photograph, softbox above-left, long highlight along the rim, gentle contact shadow` |

Name the **purpose** — "a premium skincare launch ad", "a storyboard frame for a chase" — it gives the model a design goal, not just an object list.

## 2. Positive Language

No negative-prompt field exists. Describe what occupies the space.

| Instead of | Write |
|---|---|
| no cars | an empty, deserted street |
| no text | clean, unmarked surfaces |
| no clutter | a plain seamless warm-gray backdrop |
| not blurry | crisp focus on the eyes, fine skin texture |

A short exclusion still helps for asset hygiene ("the label carries no other text", "no extra bicycles"), but positive description does the work.

## 3. Composition by Shot Type

- **Portraits / characters:** shot size + identity first; end with 3–6 identity anchors (face shape, scar, hair streak, garment construction). If clothing changes, replace it explicitly, or the model treats the outfit as identity.
- **Landscapes:** scale and layers — foreground anchor, middle-ground subject, background geography, horizon placement, weather, light direction.
- **Action stills:** the decisive instant — body mechanics, direction of travel, what is frozen (droplets, dust) and what blurs.
- **Layouts:** state the grid before the content; walk through it in reading order.
- **Negative space:** name the empty region and its purpose — "the right half stays uncluttered for later headline placement".
- **Counts:** "exactly four", "each appears once". Combine left/right with thirds and landmarks; left/right swaps are a known failure.

## 4. Camera Language for Stills

There are no camera controls; write intent. Movement words produce the *look* of motion, not motion.

```
eye-level close-up · low-angle hero · overhead flat lay · aerial oblique
24mm wide · 35mm documentary · 50mm natural · 85mm portrait · 200mm compressed
shallow depth of field · deep focus · foreground occlusion · dutch angle
tracking-shot aesthetic · panning blur · shutter-drag trails · frozen splash
```

"A still with the energy of a handheld tracking shot: runner sharp, stalls streaked behind her." Add "a single photographic frame" if the model drifts toward storyboard panels.

**One medium, one era, one supporting effect.** For illustration, swap lens language for material, line, texture and shading ("gouache on cold-press paper, dry-brush edges").

## 5. Typography and Layout

2.1's headline gain is text and infographic accuracy — use it deliberately.

- **Quote every literal string**, exact capitalization and punctuation. Unquoted copy gets paraphrased.
- Give each string a **position, relative size, weight and type class**: `"SUMMER SALE" in heavy condensed sans across the top third; "Ends Sunday" small, light, centred below`.
- Describe the type style or name a font family ("a geometric sans like Futura").
- For repeated panels use **parallel sentences**: "Panel 1: number "1", laptop icon, heading "Start online", caption "…"."
- **Localize:** write the prompt in one language and ask for the text in another ("set all copy in Japanese").
- **Text-first:** for important copy, settle the wording in conversation first, then ask for the image with that exact text.
- Use `high` thinking and `2K` for menus, dense infographics and multi-string layouts; fix one wrong string per follow-up edit.

## 6. Editing

Editing is a different mindset: say **what changes and what stays**.

```
Change only [X] from [before] to [after]. Keep [face, pose, hands, background,
camera position, lighting, text] unchanged.
```

- **Keep-lists must be concrete** — name the elements from the actual frame, not "everything else".
- **Removal (semantic masking):** "Remove the man on the left and continue the brick wall and pavement behind him." Name what fills the gap.
- **Inserts:** describe interaction with the scene — contact shadow, reflection, spill light, occlusion — or it looks pasted on.
- **Style transfer:** "Restyle this photo as a Van Gogh-style oil painting with swirling impasto skies; keep the street layout and figures."
- **Aspect ratio:** edits usually follow the source shape; set the ratio in settings if you need a change.
- **One conceptual change per turn.** Chains of redraws accumulate drift.

## 7. Search Grounding

Turn search grounding on only when the image depends on facts that change — forecasts, scores, current products, recent events. Prompt shape: **[what to look up] + [what to analyse] + [how to visualise it]**: "Look up the current five-day forecast for Lisbon and render it as a clean modern weather card with one clothing icon per day." Keep it off for fiction and controlled art direction. Verify grounded facts before publishing.

## 8. Choosing the Thinking Level

| Level | Use for |
|---|---|
| `minimal` | Fast drafts, simple single-subject shots, high-volume jobs |
| `medium` (default) | Routine scenes, ordinary edits |
| `high` | Dense text, infographics, multi-reference composites, groups, strict placement, body mechanics |

Thinking costs tokens and latency. Higher thinking and higher resolution don't fix a vague or contradictory prompt.

## 9. Panoramas and Extreme Ratios

For `4:1`, `8:1`, `1:4`, `1:8`: describe the frame as **bands in reading order** — "from left to right: harbour cranes, the old town on the hill, the cathedral spire at the right edge". Give every section something to do or it fills with repetition. Render at `2K`/`4K`; 2.1 fixes the tiling seams Nano Banana 2 had there.

## 10. Video and PDF as Context

Attach a video or PDF to get a still from it: "From the attached product video, design a YouTube thumbnail: the moment the lid opens, the product large on the right, headline "UNBOXED" on the left." This is understanding, not image-to-video.

## 11. Common Mistakes

| Mistake | Result | Fix |
|---|---|---|
| Keyword soup | Incoherent choices | Ordered sentences with relationships |
| Unscoped style reference | Subjects from the style image leak in | "Use only the palette and grain; take nothing else" |
| Identity in text only | Face/product drift | Clean reference + 3–6 identity anchors |
| No counts or positions | Duplicates, missing items | "Exactly once", thirds, landmarks |
| Unquoted copy | Paraphrased or misspelled text | Quote + position + type role, `high` thinking |
| Vague keep statement | Edit changes unrelated regions | Concrete keep-list from the frame |
| Removal without fill | Odd smears | Describe what continues behind |
| Contradictions (close-up + full body, noon + dusk) | Muddled image | One shot size, one final light model |
| Asking for a camera move | Storyboard panels or confusion | Describe the still-frame evidence |
| Lowercase `2k` / `512px` | Rejected request | `1K` `2K` `4K` |
| Leaving thinking at default after migration | Slower, costlier jobs | Set `minimal` explicitly where it suffices |
| Long edit chain | Accumulated drift | Restart from master, replay approved edits |
| Unused references attached | Ambiguity, cost | Attach only what the shot uses |
