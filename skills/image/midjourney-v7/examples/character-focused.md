# Character-Focused Examples - Midjourney v7

Midjourney v7 introduces **Omni Reference (`--oref`)** for character consistency. These examples show how to create and maintain character continuity across multiple scenes.

---

## Example 1: Establishing a Character

### Initial Character Creation

**Prompt (28 words):**
```
A cyberpunk detective with silver undercut hair, leather coat with neon circuits, 
cybernetic eye implant, standing in neon-lit alley --ar 3:4 --s 250
```

**Notes:**
- Establish distinctive features: silver hair, leather coat, cybernetic eye
- Use specific details that are visually memorable
- Standard quality first generation
- Save the URL of the best result for Omni Reference

---

## Example 2: Character in Different Scene (Using Omni Reference)

### Same Character, New Location

**Prompt (22 words):**
```
The silver-haired detective examines holographic evidence in a high-tech police 
station, blue ambient lighting --oref [URL] --ow 250 --ar 16:9
```

**Configuration:**
- `--oref [URL]` points to best image from Example 1
- `--ow 250` moderate weight for character similarity
- New scene description, but character maintained
- Different aspect ratio for scene variety

---

## Example 3: Character Action Sequence

### Scene 1: Investigation
```
Cyberpunk detective crouches examining crime scene, rain-soaked street, 
neon reflections --oref [URL] --ow 280 --ar 16:9
```

### Scene 2: Chase
```
The detective runs through narrow alley, motion blur, neon signs streaking 
past --oref [URL] --ow 280 --ar 21:9 --s 300
```

### Scene 3: Confrontation
```
Detective faces suspect across rooftop, city skyline background, tense standoff 
--oref [URL] --ow 280 --ar 16:9 --s 250
```

**Notes:**
- Same `--oref` URL and `--ow` value across all three
- Each scene focuses on different action/composition
- Consistent character throughout sequence

---

## Example 4: Fantasy Character - Multiple Angles

### Establishing Shot
```
A fierce elven warrior with braided silver hair, ornate leather armor with 
green accents, forest setting --ar 3:4 --s 200
```

### Close-Up Portrait
```
Close-up portrait of the elven warrior, fierce expression, dappled forest 
light through leaves --oref [URL] --ow 300 --ar 3:4
```

### Action Shot
```
The warrior draws bow mid-leap through ancient forest, dynamic action 
pose --oref [URL] --ow 300 --ar 16:9 --s 250
```

### Different Lighting
```
Same warrior at campfire at night, warm firelight illuminating face, 
contemplative mood --oref [URL] --ow 280 --ar 4:3
```

---

## Example 5: Character with Props/Costume Changes

### Base Character
```
A steampunk inventor in workshop, goggles on forehead, leather apron, 
brass gadgets around --ar 3:4 --s 220
```

### Same Character, Different Context
```
The inventor at formal gala, Victorian suit instead of apron, still 
recognizable face --oref [URL] --ow 320 --ar 3:4 --s 220
```

**Note:** Higher `--ow 320` to maintain face despite costume change

---

## Example 6: Age Variations (Same Character)

### Young Adult
```
A space captain in their 20s, confident stance, sleek uniform, on bridge 
of starship --ar 3:4 --s 250
```

### Middle Age
```
The same captain now in their 40s, weathered but determined, same uniform 
style --oref [URL] --ow 200 --ar 3:4
```

**Note:** Lower `--ow 200` allows aging while maintaining core features

---

## Example 7: Emotional Range - Same Character

### Neutral
```
A young mage with auburn hair and green robes, standing in stone tower, 
neutral expression --ar 3:4 --s 200
```

### Focused/Intense
```
The mage casting powerful spell, intense concentration, magical energy 
swirling --oref [URL] --ow 300 --ar 3:4 --s 250
```

### Serene
```
Same mage meditating in garden, peaceful expression, soft morning light 
--oref [URL] --ow 280 --ar 4:3
```

---

## Example 8: Group Shot Maintaining Individual Characters

### Establish Individual Characters First

**Character A:**
```
A grizzled space marine with scarred face, heavy armor, battle-worn 
--ar 3:4 --s 200
```

**Character B:**
```
A tech specialist with short blue hair, glasses, tactical vest with 
equipment --ar 3:4 --s 200
```

### Combined Scene
```
The marine and tech specialist planning mission around holographic table 
--oref [URL-A] --oref [URL-B] --ow 250 --ar 16:9
```

**Note:** Can use multiple `--oref` URLs for group consistency

---

## Example 9: Character Interaction

### Character 1 Established
```
A knight in silver armor with red cape, noble bearing, castle courtyard 
--ar 3:4 --s 220
```

### Two-Character Scene
```
The silver-armored knight shakes hands with visiting diplomat, formal greeting 
in throne room --oref [URL] --ow 300 --ar 16:9
```

**Note:** Omni Reference maintains your knight while generating new diplomat

---

## Example 10: Style Consistency with Character

### Establishing with Style
```
A jazz musician in 1920s attire, art deco style, vintage poster aesthetic 
--ar 2:3 --s 300
```

### Maintaining Character and Style
```
The same musician performing on stage, art deco theatrical setting 
--oref [URL] --ow 280 --sref [art-deco-sref] --ar 16:9 --s 300
```

**Note:** Combines `--oref` (character) with `--sref` (style) for dual consistency

---

## Omni Weight (`--ow`) Guidelines

| Value | Character Adherence | When to Use |
|-------|-------------------|-------------|
| `--ow 100-150` | Loose inspiration | Different age, major costume changes |
| `--ow 200-250` | Moderate similarity | New poses, different lighting |
| `--ow 280-320` | Strong adherence | Standard consistency needs |
| `--ow 350-400` | Maximum (limit) | Exact replication required |

**IMPORTANT:** Keep `--ow` below 400. Values above 400 can cause artifacts or over-rigid results.

---

## Multi-Scene Character Workflow

### Step 1: Create Hero Shot
```
[Detailed character description] --ar 3:4 --s 250 --q 2
```
Generate multiple variations, pick the absolute best.

### Step 2: Save URL
Copy URL of chosen image for Omni Reference.

### Step 3: Generate Scene Variations
```
[Scene description] --oref [saved-URL] --ow 280 --ar [appropriate] --s [appropriate]
```

### Step 4: Iterate Within Scenes
If character drifts, adjust `--ow`:
- **Too different?** Increase `--ow` (e.g., 280 → 320)
- **Too rigid?** Decrease `--ow` (e.g., 300 → 250)

### Step 5: Maintain Consistency
Use same `--oref` URL and `--ow` range across entire scene sequence.

---

## Character Description Best Practices

### Distinctive Features to Emphasize
- **Hair:** Color, style, length (e.g., "silver undercut," "long braided red hair")
- **Facial Features:** Unique marks, scars, piercings, tattoos
- **Clothing:** Signature outfit elements (e.g., "red leather jacket," "ornate armor")
- **Accessories:** Memorable items (e.g., "round glasses," "silver medallion")
- **Build/Posture:** Body type, stance characteristics

### What Works
✅ "A warrior with braided silver hair, green eyes, ornate leather armor"
✅ "Cyberpunk hacker with neon pink mohawk, facial tattoos, leather jacket"
✅ "Victorian gentleman with monocle, top hat, burgundy waistcoat"

### What Doesn't Work
❌ "A person in an outfit"
❌ "Someone cool-looking"
❌ "A character with style"

---

## Troubleshooting Character Consistency

### Issue: Character Looks Different Each Time

**Solutions:**
1. Increase `--ow` value (try +50 increments)
2. Be more specific in original character description
3. Ensure saved URL is from best hero shot
4. Reduce `--c` chaos if using it
5. Use `--seed` for additional reproducibility

### Issue: Character Too Rigid/Unnatural

**Solutions:**
1. Decrease `--ow` value
2. Don't exceed `--ow 400`
3. Allow natural variation in poses/expressions
4. Use lower `--s` for more natural results

### Issue: Face Maintains But Outfit Doesn't

**Expected behavior:** Omni Reference focuses on facial features/body.
**Solution:** Re-describe outfit in each prompt if consistency needed.

---

## Character Prompt Template

```
A [character type] with [distinctive hair], [unique facial features], 
[signature clothing/armor], [environment context] --ar [ratio] --s [stylize]

# Then for subsequent scenes:
[Character action/pose], [new environment], [lighting] --oref [URL] --ow 280 --ar [ratio]
```

---

**Pro Tip:** Generate your hero character shot at `--q 2` quality and save multiple good variations. Different scenes may work better with slightly different reference angles or expressions.
