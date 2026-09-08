# Phota — Edit, Enhance & Workflow Examples

Examples covering Edit mode (expression fixes, lighting adjustments, compositing, memory rescue), Enhance mode (zero-prompt quality improvement), and multi-step production workflows.

---

## EXPRESSION FIXES

### Example 1: Smile Correction — Subtle
```
Prompt: Keep the same person [[profile_id_1]] and identity exactly. 
Adjust only the facial expression: soften into a natural relaxed smile 
with slight eye crinkle. Keep eyes and face shape consistent. 
Preserve the lighting, background, camera angle, and crop unchanged. 
Photoreal, realistic skin and teeth, no exaggerated makeover.

Mode: Edit
Input Images: 1 (original headshot with neutral expression)
Resolution: 4K
Aspect Ratio: auto
Profiles Referenced: [profile_id_1]

Director's Notes: Single-variable edit — expression only. Everything 
else explicitly locked. "Subtle eye crinkle" makes the smile genuine 
(Duchenne smile) rather than forced. "No exaggerated makeover" prevents 
AI beautification drift. Profile reference ensures identity doesn't 
shift during the expression change.
```

---

### Example 2: Gaze Redirect
```
Prompt: Keep [[profile_id_1]]'s identity, expression, lighting, 
background, and framing exactly the same. Change only the eye gaze 
direction: redirect eyes to look directly at camera instead of 
off to the left. Keep head position and angle unchanged.

Mode: Edit
Input Images: 1 (portrait with off-camera gaze)
Resolution: 4K
Aspect Ratio: auto
Profiles Referenced: [profile_id_1]

Director's Notes: Extremely precise single-variable edit — only the 
eye gaze direction changes. Head position explicitly locked to 
prevent the model from rotating the entire head. This is a common 
production fix for portraits where the subject wasn't looking at 
the lens.
```

---

## LIGHTING ADJUSTMENTS

### Example 3: Flat to Dramatic Lighting
```
Prompt: Keep [[profile_id_1]]'s identity, expression, and pose 
exactly the same. Change only the lighting: replace flat frontal 
lighting with dramatic Rembrandt lighting from the upper left. 
Allow natural shadow to fall on the right side of the face, with 
the characteristic triangle of light on the shadow-side cheek. 
Maintain the same background. Photoreal.

Mode: Edit
Input Images: 1 (headshot with flat lighting)
Resolution: 4K
Aspect Ratio: auto
Profiles Referenced: [profile_id_1]

Director's Notes: Lighting-only edit. "Rembrandt lighting" is specific 
enough for the model — includes the triangle highlight reference 
in case the model needs reinforcement. Identity and expression 
explicitly locked. This converts a casual snapshot into a dramatic 
portrait without reshooting.
```

---

### Example 4: Color Temperature Shift
```
Prompt: Keep [[profile_id_1]]'s identity, expression, pose, and 
composition unchanged. Shift the overall color temperature from cool 
daylight to warm golden hour. Add subtle warm amber tones to highlights 
and skin, keep shadows with a slight warm cast. Maintain natural 
skin rendering. Photoreal, no artificial color grading.

Mode: Edit
Input Images: 1 (portrait shot in cool daylight)
Resolution: 4K
Aspect Ratio: auto
Profiles Referenced: [profile_id_1]

Director's Notes: Color temperature shift without affecting identity 
or composition. "No artificial color grading" prevents over-processed 
Instagram-filter look. This simulates a time-of-day change — as if 
the same photo was taken during golden hour instead of midday.
```

---

## BACKGROUND AND SETTING CHANGES

### Example 5: Studio to Environmental
```
Prompt: Keep [[profile_id_1]]'s identity, expression, and pose exactly 
the same. Replace the studio background with a blurred outdoor park 
scene: autumn foliage in warm gold and russet tones, soft natural 
daylight. Add subtle warm rim light on the right side of the face to 
match the new outdoor setting. Maintain chest-up framing. Photoreal, 
natural light integration.

Mode: Edit
Input Images: 1 (studio headshot on gray background)
Resolution: 4K
Aspect Ratio: auto
Profiles Referenced: [profile_id_1]

Director's Notes: Background swap with lighting integration — the key 
instruction is adding rim light that connects the subject to the new 
environment. Without this, the subject looks pasted. "Autumn foliage 
in warm gold and russet" is specific enough to get consistent seasonal 
rendering.
```

---

## GROUP SHOT COMPOSITING

### Example 6: Two-Person Composite from Separate Photos (Shadows of Ashford)
```
Prompt: Create a single group photo combining [[profile_id_1]] from 
Image 1 and [[profile_id_2]] from Image 2. Match the lighting, 
background, and perspective of Image 1. Position [[profile_id_2]] 
standing to the right of [[profile_id_1]], slightly turned toward 
them. Both should appear naturally lit as if photographed together 
in the same moment. Both looking at camera. Photoreal, natural 
shadows consistent with a single overhead key light, no compositing 
artifacts.

Mode: Edit
Input Images: 2 (separate individual portraits)
Resolution: 4K
Aspect Ratio: 16:9
Profiles Referenced: [profile_id_1, profile_id_2]

Director's Notes: Multi-person compositing from separate source photos. 
The critical instructions: "Match lighting of Image 1" (picks the 
primary), "naturally lit as if photographed together" (prevents 
pasted look), and "natural shadows consistent with single source" 
(forces unified lighting logic). Both profiles referenced to lock 
both identities.
```

---

### Example 7: Remove Person from Group Shot
```
Prompt: Convert to a solo portrait of [[profile_id_1]]. Remove all 
other people from the frame. Keep the background, lighting, and 
framing the same. Fill the space where the removed person was 
standing with natural continuation of the background. Maintain 
[[profile_id_1]]'s exact expression and pose. Photoreal.

Mode: Edit
Input Images: 1 (group photo with multiple people)
Resolution: 4K
Aspect Ratio: auto
Profiles Referenced: [profile_id_1]

Director's Notes: Person removal with background inpainting. Profile 
reference ensures the kept subject's identity is preserved. 
"Natural continuation of the background" prevents obvious clone 
stamp artifacts. Only the target profile is referenced — the 
removed people are simply not profiled.
```

---

## MEMORY RESCUE

### Example 8: Restoring a Faded Photo
```
Prompt: Restore this photo of [[profile_id_1]]. Preserve the original 
composition, setting, and moment exactly as captured. Fix the 
technical quality only: correct the faded colors, restore natural 
color balance, reduce the yellowing, improve sharpness, and remove 
compression artifacts. Keep the person's identity, expression, and 
pose exactly as in the original. Photoreal, period-appropriate 
color rendering.

Mode: Edit
Input Images: 1 (faded, yellowed old photograph)
Resolution: 4K
Aspect Ratio: auto
Output Format: png
Profiles Referenced: [profile_id_1]

Director's Notes: Memory rescue workflow. The profile locks identity 
even from a degraded source — Phota's trained model knows what the 
person looks like regardless of the photo's condition. "Period-
appropriate color rendering" prevents the model from applying modern 
color grading to a photo from the 1980s. PNG output preserves 
maximum quality for archival.
```

---

### Example 9: Deblurring with Identity Lock
```
Prompt: Fix the motion blur in this photo of [[profile_id_1]]. 
Sharpen the face and body while preserving the original composition, 
background, lighting, and moment. The person's identity and 
expression must match their profile exactly — use the profile as 
the ground truth for facial features that the blur has obscured. 
Photoreal, natural sharpness without over-sharpening artifacts.

Mode: Edit
Input Images: 1 (motion-blurred photo)
Resolution: 4K
Aspect Ratio: auto
Profiles Referenced: [profile_id_1]

Director's Notes: This is where Phota's profile system provides 
a real advantage over general enhancement tools. The profile 
acts as "ground truth" for what the person looks like, so the 
deblurring process can recover facial features accurately rather 
than hallucinating generic features. "Without over-sharpening 
artifacts" prevents halo effects.
```

---

## ENHANCE MODE (ZERO PROMPT)

### Example 10: Album Consistency Pass
```
Mode: Enhance
Input Images: [Batch of 12 photos from the same event/session]
Resolution: 4K
Output Format: jpeg
No prompt required.

Director's Notes: Enhance mode runs automatic quality improvement 
across all photos: exposure correction, noise reduction, sharpness 
improvement, color consistency. No risk of identity drift because 
no prompt is involved — the model improves technical quality only. 
This is the fastest way to make an entire photo album visually 
consistent. Process each image individually through the Enhance 
endpoint. Ideal as a final pass after Generate or Edit workflows 
to polish the entire output set.
```

---

## MULTI-STEP PRODUCTION WORKFLOW

### Example 11: Full Headshot Production Pipeline

**Step 1: Generate base headshot**
```
Prompt: Professional studio headshot of [[profile_id_1]], chest up. 
Clean neutral gray background. Soft key light from upper left, 
rim light on hair. Confident expression, direct gaze. 85mm lens 
look, shallow depth of field. Photoreal.

Mode: Generate
Resolution: 4K
Num Images: 4
→ Select best of 4 variations
```

**Step 2: Fix expression (if needed)**
```
Prompt: Keep everything identical. Soften the expression slightly — 
make the smile warmer and more approachable. Eyes remain the same. 
Preserve identity exactly.

Mode: Edit
Input Images: 1 (selected from Step 1)
```

**Step 3: Adjust lighting (if needed)**
```
Prompt: Keep identity, expression, and background unchanged. Add a 
subtle warm fill light from the right to open up the shadow side 
slightly. Keep the overall mood professional.

Mode: Edit
Input Images: 1 (result from Step 2)
```

**Step 4: Final quality polish**
```
Mode: Enhance
Input Image: (result from Step 3)
Resolution: 4K
→ Final output
```

```
Director's Notes: Four-step pipeline demonstrating one-change-per-pass 
discipline. Each step modifies exactly one variable: Step 1 = base, 
Step 2 = expression, Step 3 = lighting fill, Step 4 = quality polish. 
The profile locks identity through all four passes. This is more 
reliable than attempting all changes in a single complex prompt.
```

---

## Version Information

- **Examples Version:** 1.0
- **Covers:** Phota Edit, Enhance, and multi-step workflows
- **Last Updated:** 2026-04-18
- **Maintained By:** Visual Horizon Studio
