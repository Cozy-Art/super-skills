# Veo 3.1 - Best Practices Guide

## The Five-Part Formula (Mandatory)

Every Veo 3.1 prompt MUST include all five elements:

**[Cinematography] + [Subject] + [Action] + [Context] + [Style & Ambiance]**

This is not optional. Missing any element results in degraded quality.

---

## Optimal Prompt Length: 100-180 Words

### ✅ GOOD: 125 words
```
A low-angle tracking shot follows a lone astronaut walking through an abandoned lunar colony. 
The astronaut moves slowly, dust kicking up with each step, examining broken solar panels 
and shattered windows. The setting is a grey lunar surface with Earth visible in the dark sky, 
harsh sunlight creating deep shadows between structures. Film grain aesthetic with desaturated 
colors and cool blue undertones creates an isolating, melancholic atmosphere. The astronaut 
whispers, "Base seventeen... There's no one here." SFX: Radio static crackling. Ambient noise: 
the dull hum of a dying life support system.
```
**Includes:** All five elements + audio specifications

### ❌ TOO SHORT: 35 words
```
An astronaut walks through an abandoned base on the moon. Sad mood. 
They say "nobody here" and it's quiet.
```
**Problem:** Missing cinematography, vague descriptions, no audio detail

### ❌ TOO LONG: 250+ words
```
[Extended rambling prompt with excessive detail...]
```
**Problem:** Model loses focus, conflicting instructions, diminishing returns

---

## The Five Elements Explained

### 1. Cinematography (Camera Work)

**Always specify:**
- Shot type (close-up, medium, long shot)
- Camera movement (dolly, pan, tracking, crane)
- Lens characteristics (if relevant)

**✅ Good examples:**
- "A medium tracking shot follows..."
- "Crane shot starting low and ascending..."
- "Handheld POV from behind the character..."
- "Static wide shot establishes..."
- "Slow dolly-in on the subject's face..."

**❌ Avoid:**
- No camera mention at all
- Generic "cinematic shot"
- Conflicting movements ("pan left while tracking right")

---

### 2. Subject (Who/What)

**Be specific about:**
- Physical characteristics
- Clothing/appearance
- Distinctive features
- Age, gender, species (if relevant)

**✅ Good examples:**
- "A weathered detective in a brown trench coat"
- "A miniature dragon with iridescent blue scales"
- "An elderly craftsman with calloused hands"

**❌ Avoid:**
- "A person"
- "Someone cool"
- "A thing"

---

### 3. Action (What's Happening)

**Focus on:**
- Clear verbs describing movement
- Emotional state
- Interaction with environment
- Progressive action (moments in progress)

**✅ Good examples:**
- "walks with calm, deliberate steps"
- "carefully extracts a data chip from a panel"
- "gazes upward with wonder and fear"

**❌ Avoid:**
- Static descriptions ("stands there")
- Complete story arcs ("finds treasure, defeats enemy, celebrates")
- Overly complex simultaneous actions

---

### 4. Context (Where/When)

**Include:**
- Physical environment
- Time of day
- Weather/atmospheric conditions
- Spatial relationships

**✅ Good examples:**
- "rain-slicked street in a forgotten city, shrouded in twilight"
- "sunlit workshop at dawn, dust motes visible in light beams"
- "deep space nebula with stars scattered across darkness"

**❌ Avoid:**
- "A place"
- "Somewhere nice"
- No location specified

---

### 5. Style & Ambiance (Mood/Aesthetic)

**Specify:**
- Lighting quality
- Color palette
- Artistic style
- Emotional tone

**✅ Good examples:**
- "film noir style with deep shadows and high contrast"
- "warm golden hour glow, nostalgic and peaceful"
- "ethereal dreamlike quality with soft focus and pastel hues"

**❌ Avoid:**
- "Looks good"
- "Cool style"
- Conflicting styles ("minimalist but very detailed")

---

## Audio Best Practices

### Dialogue Rules

**Format:**
```
Speaker + verb + "quoted dialogue"
```

**✅ Good:**
```
The detective murmurs, "This must be it. The secret code."
```

**Best Practices:**
- **1-2 lines maximum** per 8-second clip
- **Show the mouth** - frame shots to include speaker's face
- **Name the speaker** explicitly
- **Use action verbs** - murmurs, shouts, whispers, declares
- **Keep it short** - lip-sync accuracy decreases with length

**❌ Avoid:**
- Long monologues
- Multiple speakers in one clip (unless brief)
- Off-screen dialogue without visible speakers

---

### Sound Effects (SFX)

**Format:**
```
SFX: specific description
```

**✅ Good examples:**
- "SFX: thunder cracks in the distance"
- "SFX: glass shattering"
- "SFX: footsteps echoing on metal floor"
- "SFX: engine roaring to life"

**Be specific about:**
- Type of sound
- Intensity/volume
- Distance (near/far)
- Character (sharp, dull, echoing)

---

### Ambient Noise

**Format:**
```
Ambient noise: soundscape description
```

**✅ Good examples:**
- "Ambient noise: the quiet hum of a starship bridge"
- "Ambient noise: city traffic and distant sirens"
- "Ambient noise: wind howling through abandoned corridors"
- "Ambient noise: gentle rain on leaves"

**Purpose:** Sets the environmental sound bed beneath dialogue and SFX

---

## Camera Terminology That Works

### Shot Types (Distance)
- **Extreme close-up (ECU)**: Eyes, hands, specific details
- **Close-up (CU)**: Face, shoulders
- **Medium close-up (MCU)**: Waist up
- **Medium shot (MS)**: Knees up
- **Medium long shot (MLS)**: Full body with some space
- **Long shot (LS)**: Full body in environment
- **Extreme long shot (ELS)**: Tiny figure in vast landscape
- **Establishing shot**: Wide view showing location

### Camera Movements
- **Dolly in/out**: Camera moves toward/away from subject
- **Tracking shot**: Camera follows subject's movement
- **Pan left/right**: Camera rotates horizontally on axis
- **Tilt up/down**: Camera rotates vertically on axis
- **Crane shot**: Camera moves vertically (ascending/descending)
- **Arc shot**: Camera circles around subject
- **Whip pan**: Extremely fast pan creating blur
- **Handheld**: Naturalistic camera shake

### Camera Angles
- **Eye-level**: Standard, neutral perspective
- **Low-angle**: Camera below subject, looking up (power)
- **High-angle**: Camera above subject, looking down (vulnerability)
- **Bird's-eye view**: Directly overhead
- **Dutch angle**: Tilted horizon (unease, tension)
- **POV (Point of view)**: Camera is character's eyes

### Lens Effects
- **Shallow depth of field**: Subject sharp, background blurred
- **Deep focus**: Everything sharp front to back
- **Rack focus**: Focus shifts from one subject to another
- **Lens flare**: Light artifacts from bright sources
- **Wide-angle**: Exaggerated perspective, more in frame
- **Telephoto**: Compressed perspective, isolated subject

---

## Motion and Action Guidelines

### Design "Moments in Progress"

**✅ Good approach:**
Focus on ongoing action rather than complete story arcs.

```
A thief carefully picks a lock, sweat beading on their forehead, 
glancing nervously over their shoulder as footsteps approach...
```

**❌ Avoid:**
Complete narratives within 8 seconds.

```
A thief breaks into a vault, steals the diamond, gets caught by police, 
escapes through window, and rides away on motorcycle...
```

### Use Clear Motion Phrases

- "slow camera drift"
- "gentle character movement"
- "smooth continuous motion"
- "deliberate steps"
- "flowing gesture"

### Include Emotional Descriptors

- calm, tense, dreamlike, mysterious, hopeful
- anxious, triumphant, melancholic, energetic
- serene, ominous, playful, contemplative

---

## Reference Image Strategy

### When to Use References

**Character Consistency:**
- Multi-shot sequences with same character
- Dialogue scenes requiring facial consistency
- Narrative projects with recurring characters

**Style/Environment Consistency:**
- Location establishing shots
- Brand-specific visual style
- Matching existing footage aesthetic

### How to Use References

**Number of Images:** 1-3 per generation
- 1 image: Single character or primary style reference
- 2-3 images: Multiple characters or style + character

**Quality Requirements:**
- High resolution
- Good lighting
- Clear subject visibility
- Front-facing for characters (best results)

**Reference Types:**
- `"character"`: People, creatures - maintains identity
- `"asset"`: Objects, props, environments

**Consistency Workflow:**
1. Upload references with initial generation
2. Use **same references** across all related shots
3. Keep **character descriptions consistent** in text
4. Use **same seed** when possible
5. Maintain **style language** (lighting, mood) identically

---

## Video Extension Workflow

### When to Use Extension

- Building sequences longer than 8 seconds
- Creating narrative continuity
- Multi-shot scene construction

### Extension Process

**Step 1:** Generate initial 8s clip at **720p** (extension requires 720p)

**Step 2:** Extend by describing next action:
```
The detective stands from the desk, walks slowly toward the window, 
and peers out at the rainy street below...
```

**Step 3:** Repeat up to 20 times for ~148 seconds total

**Important Notes:**
- Only works with Veo-generated videos
- Must be 720p resolution
- Videos stored 2 days (timer resets when referenced)
- Each extension adds ~7 seconds

---

## Resolution Strategy

| Resolution | Generation Time | Cost | Extension | Best For |
|------------|----------------|------|-----------|----------|
| **720p** | Fastest | Lowest | ✅ Yes | Iteration, extension workflows |
| **1080p** | Moderate | Medium | ❌ No | Professional deliverables, client review |
| **4K** | Slowest | Highest | ❌ No | Final hero shots, maximum quality |

**Recommended Workflow:**
1. **Concept:** 720p for rapid testing
2. **Review:** 720p with references for approval
3. **Extend:** 720p for longer sequences if needed
4. **Final:** 1080p or 4K for deliverables

---

## Common Mistakes & Fixes

| Mistake | Problem | Solution |
|---------|---------|----------|
| **Missing cinematography** | Static, boring shots | Always specify shot type + movement |
| **Vague descriptions** | Generic results | Be specific in all five elements |
| **Too much dialogue** | Poor lip-sync | 1-2 short lines maximum per 8s |
| **Complete story arcs** | Abrupt, rushed feel | Focus on ongoing moments |
| **No audio specified** | Wasted native audio capability | Always add dialogue/SFX/ambient |
| **Conflicting instructions** | Confused output | One dominant style, clear direction |
| **Using "no" or "don't"** | May be ignored | Use positive exclusions in negativePrompt |
| **Ignoring references** | Inconsistent characters | Use 1-3 references consistently |

---

## Negative Prompts (What NOT to Show)

**Don't use "no" or "don't" in main prompt.**

Instead, use the `negativePrompt` parameter with positive descriptions:

**❌ In main prompt:**
```
"no walls" or "don't show buildings"
```

**✅ In negativePrompt parameter:**
```
"wall, frame, urban background, man-made structures"
```

**Common negative prompt uses:**
- Removing unwanted objects: "table, chair, furniture"
- Simplifying scenes: "clutter, decoration, ornaments"
- Controlling environment: "people, crowds, vehicles"
- Style exclusions: "cartoon, anime, illustration"

---

## Timestamp Prompting (Advanced)

For complex timing within 8 seconds:

```
[00:00-00:02] Medium shot. A detective sits at a dimly lit desk, 
examining a photograph with a magnifying glass.

[00:02-00:04] The detective's hand sets down the magnifying glass. 
SFX: glass clicking on wooden desk.

[00:04-00:06] Close-up on the detective's face as realization dawns. 
The detective whispers, "It was her all along."

[00:06-00:08] Slow dolly-out as the detective leans back in chair, 
processing the revelation.
```

**When to use:**
- Complex multi-shot sequences
- Precise timing requirements
- Specific audio timing

**Note:** This is an advanced feature; start with single-shot prompts first.

---

## Quick Reference Checklist

Before submitting, verify your prompt includes:

- [ ] **Cinematography**: Shot type + movement
- [ ] **Subject**: Specific, detailed description
- [ ] **Action**: Clear verbs and emotional state
- [ ] **Context**: Environment, time, weather
- [ ] **Style & Ambiance**: Lighting, mood, aesthetic
- [ ] **Audio**: Dialogue (in quotes), SFX, ambient
- [ ] **Length**: 100-180 words
- [ ] **References**: 1-3 images if consistency needed
- [ ] **Parameters**: Resolution, duration, aspect ratio

---

## Template Structures

### Dialogue Scene
```
[Shot type + movement] follows [subject description] as they [action] 
in [context location]. [Subject] [speaks with emotion], "[dialogue]." 
[Style and lighting]. SFX: [sound]. Ambient noise: [soundscape].
```

### Action Scene
```
[Dynamic camera movement] captures [subject] [action verb] through 
[context environment]. [Motion description] as [additional action]. 
[Style and mood]. SFX: [action sounds]. Ambient noise: [environment].
```

### Establishing Shot
```
[Wide camera shot] reveals [environment description] during [time of day]. 
[Weather/atmospheric conditions] create [mood]. [Subject appears] in 
[location within frame]. [Style and lighting]. Ambient noise: [soundscape].
```

---

**Remember:** Veo 3.1 excels when given complete information. The five-part formula + audio specifications + 100-180 words = optimal results.
