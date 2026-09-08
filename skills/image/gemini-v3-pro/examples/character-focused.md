# Character-Focused Examples - Gemini 3 Pro

This file contains examples optimized for creating and maintaining character consistency across multiple image generations.

---

## Example 1: Character Introduction - Professional Portrait

### Scenario
Establishing a main character for a corporate video series.

### Prompt
```
Create a photorealistic medium shot portrait of a confident businesswoman in her early 40s 
with silver-streaked black hair styled in a modern bob, warm brown eyes, and subtle smile 
lines. She wears a tailored charcoal blazer over a crisp white blouse with minimal jewelry—
just small gold hoop earrings. She is looking directly at the camera with an approachable, 
competent expression. Set in a modern glass-walled office with soft-focus city skyline 
visible through windows behind her. Illuminated by soft diffused daylight from camera left 
mixed with warm interior lighting. Shot with 85mm lens at f/2.8 for shallow depth of field, 
keeping face sharp while background blurs. 3:4 portrait orientation. The mood is professional, 
trustworthy, and inspiring.
```

### Configuration Notes
- **Resolution:** 2K for client review, 4K for final
- **Aspect Ratio:** 3:4 (standard portrait)
- **Reference Images:** None (initial character creation)

### Follow-up Iteration (If needed)
```
Same character, but adjust the expression to be slightly more serious and 
authoritative. Keep all facial features, hair, outfit, and lighting identical.
```

---

## Example 2: Character Consistency - Multi-Scene Story

### Scenario
Creating a series of images showing the same character in different situations for a brand story.

### Scene 1: Morning Coffee Shop
```
Create a photorealistic portrait of a young woman in her late 20s with shoulder-length 
curly auburn hair, fair skin with freckles across her nose and cheeks, bright green eyes, 
and wearing round tortoiseshell glasses. She's wearing a cream cable-knit sweater and 
vintage denim jacket. She is sitting by a window in a cozy coffee shop, holding a ceramic 
mug with both hands, looking thoughtfully out the window with a gentle smile. Morning 
sunlight streams through the window, creating warm golden highlights in her hair. Shot with 
50mm lens, shallow depth of field with the background softly blurred. 4:5 portrait orientation. 
The mood is peaceful, contemplative, and warm.
```

### Scene 2: Same Character, Park Walking (Multi-Turn)
```
Show the same character from the previous image, now walking through an autumn park with 
fallen leaves on the ground. She's looking up at trees with sunlight filtering through 
branches, still wearing the cream sweater and denim jacket. Maintain her exact facial 
features: curly auburn hair, freckles, green eyes, tortoiseshell glasses. Keep identical 
hair texture and color. Medium shot from slightly behind and to the side. Golden hour 
lighting creates warm backlighting. 16:9 landscape orientation. Mood: serene and reflective.
```

### Scene 3: Same Character, Evening Reading (Multi-Turn)
```
Same character from previous images, now sitting in a comfortable reading nook at home 
in the evening, holding an open book, wearing the same cream sweater. Keep her curly 
auburn hair, freckles, green eyes, and tortoiseshell glasses identical to previous 
generations. She's illuminated by warm lamplight from a vintage brass reading lamp 
beside her. Cozy interior with bookshelves visible in soft-focus background. Close-up 
portrait, 3:4 orientation. Mood: cozy, intimate, peaceful.
```

### Configuration Notes
- **Method:** Multi-turn conversation mode (leverages 1M token context)
- **Resolution:** 2K for all scenes
- **Preservation Strategy:** Explicit feature references + "same character from previous image"

---

## Example 3: Character with Reference Image

### Scenario
Using a reference photo to maintain exact likeness across generated scenes.

### Prompt with Reference
```
Using Image 1 as the character reference, create a professional headshot of this person 
in a modern studio setting. The person should maintain their exact facial features, skin 
tone, eye color, and hair style from the reference image. They are now wearing a navy 
blue suit with a white shirt, looking confidently at the camera with a slight smile. 
Studio lighting setup: key light from camera left at 45 degrees, soft fill light from 
right, subtle rim light from behind. Shot with 85mm lens at f/1.8 for creamy background 
bokeh. 3:4 portrait orientation. Professional, clean aesthetic with neutral gray background.
```

### Configuration Notes
- **Reference Images:** 1 (human reference)
- **Resolution:** 4K (for professional headshot quality)
- **Aspect Ratio:** 3:4
- **Key Instruction:** "Maintain exact facial features... from the reference image"

---

## Example 4: Multiple Characters with Distinct Features

### Scenario
Creating a group shot with three distinct characters who need to remain consistent.

### Initial Prompt
```
Create a photorealistic medium shot of three friends sitting together at an outdoor café 
table. From left to right: 

Character 1: A man in his early 30s with dark curly hair, thick eyebrows, olive skin, 
wearing a forest green henley shirt.

Character 2: A woman in her mid-20s with straight platinum blonde hair in a ponytail, 
pale skin, blue eyes, wearing a light pink cardigan over a white t-shirt.

Character 3: A man in his late 20s with shaved head, dark brown skin, well-groomed beard, 
wearing a burgundy flannel shirt.

All three are laughing together, coffee cups on the table. Natural afternoon sunlight 
with dappled shade from a tree overhead. Shot with 35mm lens capturing all three 
comfortably in frame. 16:9 landscape orientation. The mood is friendly, warm, and genuine.
```

### Follow-up: Reframe Same Characters
```
Show the same three characters from the previous image, but now in a closer composition 
focusing just on their faces as they lean in together. Maintain exact facial features, 
hair, skin tones, and clothing for all three: the man with curly dark hair in green 
henley, the woman with platinum blonde ponytail in pink cardigan, and the man with 
shaved head and beard in burgundy flannel. Same outdoor setting with natural light. 
Intimate close-up shot. 1:1 square format. Keep the genuine, friendly connection.
```

### Configuration Notes
- **Method:** Multi-turn conversation
- **Challenge:** Maintaining three separate characters
- **Strategy:** Detailed individual descriptions + explicit reference in follow-up

---

## Example 5: Character Age Progression

### Scenario
Showing the same character at different life stages.

### Age 20s
```
Create a photorealistic portrait of a woman in her mid-20s with long wavy dark brown 
hair, hazel eyes, olive skin, and a bright enthusiastic smile showing teeth. She's 
wearing a casual yellow sundress. Natural outdoor lighting on a sunny day. Her face 
has youthful smooth skin, bright eyes full of optimism. Shot with 85mm lens, shallow 
depth of field. 3:4 portrait orientation. Mood: energetic, hopeful, carefree.
```

### Same Character - Age 40s
```
Show the same woman from the previous image, but now in her early 40s. Maintain the 
same core facial structure, hazel eyes, and olive skin tone. Her dark brown hair now 
has subtle gray strands at the temples and is styled in a sophisticated shoulder-length 
cut. Her face shows natural aging with gentle laugh lines around eyes and mouth, 
slightly more defined bone structure. She wears a tailored burgundy blouse. Her 
expression is warm but more measured—mature confidence instead of youthful enthusiasm. 
Same lighting style and 85mm lens. 3:4 portrait orientation. Mood: wise, grounded, 
accomplished.
```

### Same Character - Age 60s
```
Show this same woman now in her mid-60s. Keep the same hazel eyes and bone structure. 
Her hair is now silver-gray with elegant natural waves, worn shorter. More pronounced 
smile lines and gentle wrinkles that speak to a life well-lived. She wears a soft 
cream cashmere sweater. Her expression radiates quiet contentment and deep wisdom. 
Same photorealistic style and lighting approach. 3:4 portrait orientation. Mood: 
serene, reflective, dignified.
```

### Configuration Notes
- **Method:** Multi-turn conversation with explicit aging instructions
- **Key Strategy:** Maintain core features (eye color, bone structure) while adding age-appropriate changes
- **Resolution:** 4K for all to capture fine aging details

---

## Example 6: Character with Emotional Range

### Scenario
Same character showing different emotions for actor portfolio or character study.

### Neutral Expression
```
Create a photorealistic close-up portrait of a man in his early 30s with short dark 
hair, light stubble, blue-gray eyes, and fair skin. He wears a simple charcoal gray 
t-shirt. His expression is neutral and relaxed, looking directly at camera. Even, 
soft lighting from slightly above. Simple medium gray background. Shot with 85mm lens 
at f/2.0. 1:1 square format. Clean, actor headshot style.
```

### Same Character - Joy
```
Same character from previous image, but now with a genuine, broad smile that reaches 
his eyes, creating crow's feet at the corners. Keep identical facial features, hair, 
stubble, eye color, and clothing. His entire face is lit up with authentic happiness. 
Maintain same lighting and background. Same 85mm lens, 1:1 format.
```

### Same Character - Concern
```
Same character again, now with a concerned, worried expression. Eyebrows slightly 
furrowed, lips pressed together, eyes showing apprehension. Keep all facial features, 
hair, stubble, and clothing identical to previous images. Same studio setup and lighting. 
85mm lens, 1:1 format.
```

### Configuration Notes
- **Method:** Multi-turn conversation
- **Focus:** Emotional expression variety while maintaining physical consistency
- **Use Case:** Actor portfolios, character development, emotional storytelling

---

## Preservation Commands Reference

Use these phrases when continuing character development:

### Facial Features
- "Keep identical facial features from previous image"
- "Maintain exact same face shape and bone structure"
- "Preserve eye color, nose shape, and mouth proportions"
- "Keep the same skin tone and complexion"

### Hair
- "Identical hair color, texture, and style"
- "Same hairstyle as previous generation"
- "Keep exact hair length and styling"

### Body/Build
- "Maintain same body type and build"
- "Keep identical physique and proportions"

### Clothing
- "Same outfit as previous image"
- "Keep wearing [specific clothing items]"

### Overall Likeness
- "Same character from previous image"
- "This is the same person shown earlier"
- "Maintain this person's likeness"
- "Keep character consistency with previous generation"

---

## Advanced: Multi-Reference Character Blending

### Scenario
Creating a new character inspired by multiple reference images.

### Prompt with Multiple References
```
Using Image 1 for facial structure and Image 2 for styling aesthetic, create a new 
character portrait. Take the bone structure, face shape, and general features from 
Image 1, but apply the hairstyle, fashion sense, and color palette from Image 2. 
The result should be a cohesive new character that feels like a natural blend of 
both references. Medium shot portrait, 3:4 orientation. Natural lighting, professional 
photography style.
```

### Configuration Notes
- **Reference Images:** 2 (both human references)
- **Technique:** Feature blending with explicit attribution
- **Resolution:** 2K for initial test, 4K for final

---

## Troubleshooting Character Consistency

### If Features Drift:
1. **Reload original reference** - Go back to first successful generation
2. **Consolidate descriptions** - Combine all desired features into one comprehensive prompt
3. **Use multi-turn mode** - Leverage conversation history
4. **Add preservation commands** - Be explicit about what to maintain

### If Quality Degrades:
1. **Increase resolution** - Move from 1K to 2K or 4K
2. **Simplify the scene** - Reduce background complexity
3. **Reset lighting** - Return to simple, clean lighting setups
4. **Start fresh** - Sometimes better to begin new conversation thread

### If Clothing/Details Change:
1. **Be more specific** - Describe exact clothing items with details
2. **Reference the outfit explicitly** - "Still wearing the navy blazer and white shirt"
3. **Use preservation commands** - "Keep the same outfit"

---

**Pro Tip:** For critical character work requiring perfect consistency across many images, generate your "hero shot" first at 4K, then use that as a reference image for all subsequent generations. This gives the model a visual anchor to maintain consistency.
