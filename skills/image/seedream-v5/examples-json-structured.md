# Seedream 5.0 — JSON Structured Prompt Examples

JSON structured prompts are Seedream 5.0 Lite's unique capability for precise multi-subject placement, per-element color control, and commercial art direction. Use JSON mode when plain text can't provide the positional precision your shot requires.

**When to use JSON mode:**
- Multi-subject scenes with 3+ elements needing specific placement
- Per-element HEX color control for brand accuracy
- Commercial art direction with precise layout
- Product flat lays with defined spatial arrangement
- Poster/UI layouts requiring compositional precision

**When to stay with plain text:**
- Single-subject scenes
- Creatively open prompts
- Emotional/artistic content where rigid positioning would harm the result

---

## PRODUCT FLAT LAYS

### Example 1: Fragrance Collection — Overhead Layout (Aurelia)

**JSON Prompt:**
```json
{
  "scene": "Overhead flat lay on raw white Carrara marble surface with subtle grey veining, luxury editorial product photography",
  "subjects": [
    {
      "description": "Sculptural glass perfume bottle with Art Deco gold cap, containing amber-gold liquid, light refracting through faceted cuts",
      "position": "center",
      "color": "#D4A574"
    },
    {
      "description": "Three white peony blooms, petals slightly open, with two dark green leaves",
      "position": "upper left"
    },
    {
      "description": "Folded cream silk scarf with subtle gold thread edge detail",
      "position": "lower right"
    },
    {
      "description": "Small brass Art Deco mirror, round, reflecting warm light",
      "position": "upper right",
      "color": "#C5973A"
    },
    {
      "description": "Thin trail of golden perfume droplets on the marble surface",
      "position": "lower left",
      "color": "#D4A574"
    }
  ],
  "style": "Luxury editorial flat lay, Vogue still life aesthetic",
  "lighting": "Soft natural window light from the top, creating gentle shadows beneath each object, warm color temperature",
  "camera": {
    "angle": "directly overhead",
    "lens": "35mm wide, f/5.6 for edge-to-edge sharpness"
  }
}
```

```
Variant: Seedream 5.0 Lite
Image Size: square_hd
Seed: null

Director's Notes: JSON mode chosen for precise 5-element placement on flat lay. 
HEX #D4A574 locks the amber-gold brand color across bottle and droplets. Overhead 
angle with 35mm keeps all elements in plane. Marble surface specified by name 
(Carrara) for authentic veining pattern.
```

---

### Example 2: Prop Table — Evidence Spread (Shadows of Ashford)

**JSON Prompt:**
```json
{
  "scene": "Overhead view of a 1940s detective's desk, dark stained oak surface with ring stains and cigarette burns, noir atmosphere",
  "subjects": [
    {
      "description": "Open manila case file folder with typed pages visible, stamped 'CONFIDENTIAL' in red ink",
      "position": "center left"
    },
    {
      "description": "Black-and-white surveillance photograph of a woman in a fur coat entering a building, slightly blurry, 3x5 inches",
      "position": "upper right"
    },
    {
      "description": "Glass ashtray with two crushed cigarette butts and grey ash",
      "position": "lower right"
    },
    {
      "description": "Snub-nosed revolver with worn wooden grip",
      "position": "lower left"
    },
    {
      "description": "Half-empty tumbler of whiskey catching amber light",
      "position": "upper left",
      "color": "#B8860B"
    },
    {
      "description": "Folded newspaper with visible headline, yellowed edges",
      "position": "center right"
    }
  ],
  "style": "Cinematic still life, noir detective aesthetic, black and white with selective amber tones",
  "lighting": "Single desk lamp from upper left casting harsh directional light with deep shadows, the rest of the desk falling into darkness",
  "camera": {
    "angle": "slightly overhead, approximately 60 degrees",
    "lens": "50mm, f/4"
  }
}
```

```
Variant: Seedream 5.0 Lite
Image Size: landscape_16_9
Seed: null

Director's Notes: Six elements precisely placed to create a narrative evidence 
spread. JSON mode prevents subject overlap and ensures readable composition. 
Selective amber color on whiskey creates the classic noir color accent against 
monochrome. 60-degree angle (not flat overhead) adds depth and shadow drama.
```

---

## BRAND AND COMMERCIAL

### Example 3: Brand Color Palette Card (Aurelia)

**JSON Prompt:**
```json
{
  "scene": "Minimalist brand identity color palette card on clean white background, luxury fashion branding aesthetic",
  "subjects": [
    {
      "description": "Large circle swatch of rich amber gold",
      "position": "upper left",
      "color": "#D4A574"
    },
    {
      "description": "Large circle swatch of deep burgundy",
      "position": "upper center",
      "color": "#722F37"
    },
    {
      "description": "Large circle swatch of soft ivory cream",
      "position": "upper right",
      "color": "#FFFFF0"
    },
    {
      "description": "Large circle swatch of charcoal graphite",
      "position": "lower left",
      "color": "#36454F"
    },
    {
      "description": "Large circle swatch of rose gold metallic",
      "position": "lower center",
      "color": "#B76E79"
    }
  ],
  "style": "Clean graphic design, Swiss design principles, precise geometry",
  "lighting": "Even, flat lighting with no shadows",
  "camera": {
    "angle": "flat, perpendicular to surface",
    "lens": "standard"
  }
}
```

```
Variant: Seedream 5.0 Lite
Image Size: landscape_4_3
Seed: null

Director's Notes: HEX color control is essential here — each swatch must match 
the exact brand color specification. JSON positioning ensures clean grid layout. 
Flat lighting and perpendicular angle eliminate any dimensional distortion. 
This is pure graphic design, not photography.
```

---

### Example 4: Neon Sign Mockup — Music Venue (Neon Pulse)

**JSON Prompt:**
```json
{
  "scene": "Exterior brick wall of an underground music venue at night, aged red brick with moisture, urban gritty atmosphere",
  "subjects": [
    {
      "description": "Large neon sign reading \"NEON PULSE\" in a bold angular typeface, glowing intensely with slight flickering quality",
      "position": "center",
      "color": "#FF006E"
    },
    {
      "description": "Smaller neon sign below reading \"LIVE TONIGHT\" in a simpler block font",
      "position": "lower center",
      "color": "#00F5FF"
    },
    {
      "description": "Metal door painted black, partially open, warm amber light spilling from inside",
      "position": "lower left"
    },
    {
      "description": "Wet pavement reflecting the neon colors in elongated streaks",
      "position": "lower third"
    }
  ],
  "style": "Urban nightlife photography, cyberpunk practical lighting",
  "lighting": "Neon signs as primary light sources, creating colored pools on the brick wall and pavement. No other artificial lighting.",
  "camera": {
    "angle": "straight on, eye level",
    "lens": "35mm, f/2.0, CineStill 800T film stock"
  }
}
```

```
Variant: Seedream 5.0 Lite
Image Size: portrait_16_9
Seed: null

Director's Notes: Text rendering in JSON mode — both neon signs have text in 
quotation marks within the description field. HEX colors lock the brand pink 
(#FF006E) and cyan (#00F5FF). CineStill 800T produces characteristic halation 
glow around the neon tubes. Portrait orientation for venue entrance/poster format.
```

---

## MULTI-SUBJECT SCENES

### Example 5: Space Station Control Room — Discovery Moment (Stellar Drift)

**JSON Prompt:**
```json
{
  "scene": "Interior of a derelict space station control room, consoles dark except for one bank of screens that has just flickered to life, dust particles floating in zero gravity, cables hanging weightlessly",
  "subjects": [
    {
      "description": "Female astronaut in a worn EVA suit, cropped dark hair visible through scratched helmet visor, leaning forward toward the active console with one hand reaching out, expression of shock and wonder",
      "position": "center left"
    },
    {
      "description": "Bank of three CRT-style monitors displaying green-on-black scrolling data, the central screen showing a star map with a pulsing red marker",
      "position": "center right",
      "color": "#00FF41"
    },
    {
      "description": "Floating debris field — a clipboard, two pens, and a photograph — suspended in zero gravity between the astronaut and the console",
      "position": "center"
    },
    {
      "description": "Emergency lighting strip along the floor casting dim red uplight",
      "position": "lower third",
      "color": "#FF0000"
    }
  ],
  "style": "Cinematic science fiction, Alien (1979) production design aesthetic",
  "lighting": "CRT screens as primary light source casting green glow on astronaut's face and visor. Emergency red strip as secondary fill from below. No other light sources — deep shadow everywhere else.",
  "camera": {
    "angle": "medium shot, slight low angle",
    "lens": "28mm anamorphic, f/2.8"
  }
}
```

```
Variant: Seedream 5.0 Lite
Image Size: landscape_16_9
Seed: null

Director's Notes: Four-element scene with competing light sources (green CRT vs 
red emergency strip) that would be difficult to describe precisely in plain text. 
JSON ensures the floating debris occupies the spatial gap between astronaut and 
console. Alien (1979) reference anchors the retro-futurist production design. 
Anamorphic lens produces characteristic oval bokeh and horizontal flares.
```

---

### Example 6: War Council Table (Iron Crown)

**JSON Prompt:**
```json
{
  "scene": "Interior of a medieval great hall, a massive round stone table with a carved map of a fantasy kingdom etched into its surface, torchlight from iron sconces on the walls",
  "subjects": [
    {
      "description": "An aging king in tarnished silver armor with a fur-lined cloak, standing with both hands planted on the table, looking down at the map with grim determination, battle scars across his left cheek",
      "position": "center, behind the table"
    },
    {
      "description": "A hooded female advisor in dark green robes, pointing at a position on the carved map, her face partially in shadow",
      "position": "right side of table"
    },
    {
      "description": "A young knight in polished steel plate armor, arms crossed, skeptical expression, standing apart from the table",
      "position": "left side, slightly back"
    },
    {
      "description": "The carved stone map on the table surface, showing mountain ranges, rivers, and castle positions, with small iron game pieces placed at strategic points",
      "position": "center foreground, on table surface"
    }
  ],
  "style": "Epic fantasy cinematography, Game of Thrones production quality, warm and cold light mixing",
  "lighting": "Warm orange torchlight from wall sconces at left and right. Cold blue moonlight filtering through a narrow arched window behind the king, creating rim light on his silhouette.",
  "camera": {
    "angle": "low angle from table level, looking slightly up at the king",
    "lens": "24mm wide angle, deep focus"
  }
}
```

```
Variant: Seedream 5.0 Lite
Image Size: landscape_16_9
Seed: null

Director's Notes: Three characters plus the map table as a fourth "subject" — 
JSON prevents spatial confusion in this complex multi-figure scene. Each character 
has distinct visual identity (tarnished armor vs green robes vs polished steel) 
to aid differentiation. Mixed warm/cold lighting creates visual tension matching 
the narrative tension. Low angle from table level makes the king dominant.
```

---

## POSTER AND TYPOGRAPHY LAYOUTS

### Example 7: Festival Poster with Typography Hierarchy (Neon Pulse)

**JSON Prompt:**
```json
{
  "scene": "Large-format event poster with dark background gradient from midnight black to deep electric blue",
  "subjects": [
    {
      "description": "Bold condensed sans-serif text reading \"NEON PULSE\" in glowing hot pink, largest element",
      "position": "upper center",
      "color": "#FF006E"
    },
    {
      "description": "Elegant thin sans-serif text reading \"Electronic Music Festival 2026\" in white",
      "position": "center, below title"
    },
    {
      "description": "Three DJ names in medium weight: \"SYNTHWAVE COLLECTIVE\" \"DIGITAL NOMAD\" \"CHROME HEARTS\" stacked vertically in cyan",
      "position": "lower center",
      "color": "#00F5FF"
    },
    {
      "description": "Stylized geometric waveform pattern running horizontally across the poster, thin lines",
      "position": "center, behind text",
      "color": "#6B2FA0"
    },
    {
      "description": "Date and venue text: \"JULY 18-20 • WAREHOUSE DISTRICT\" in small caps white",
      "position": "bottom center"
    }
  ],
  "style": "Contemporary electronic music event design, Swiss grid layout, clean typography hierarchy",
  "lighting": "Self-illuminated text elements, no external light source, glow effects on primary colors",
  "camera": {
    "angle": "flat, perpendicular",
    "lens": "standard"
  }
}
```

```
Variant: Seedream 5.0 Lite
Image Size: portrait_16_9
Seed: null

Director's Notes: Five text elements with strict typographic hierarchy — JSON 
positioning ensures clean stacking. HEX colors lock brand pink (#FF006E), 
cyan (#00F5FF), and purple (#6B2FA0) for the three-color palette. All literal 
text in quotation marks within description fields. Portrait orientation for 
poster format.
```

---

### Example 8: Documentary Chapter Card (Forgotten Waters)

**JSON Prompt:**
```json
{
  "scene": "Minimalist documentary chapter title card, horizontal format",
  "subjects": [
    {
      "description": "Large serif text reading \"CHAPTER THREE\" in thin weight, muted white with slight transparency",
      "position": "upper center"
    },
    {
      "description": "Bold serif text reading \"The Last Net\" in solid white, larger than chapter number",
      "position": "center"
    },
    {
      "description": "Background photograph of an abandoned fishing net draped over wooden posts on a dried lakebed, desaturated, slightly blurred",
      "position": "full frame background"
    }
  ],
  "style": "Documentary title card, Ken Burns aesthetic, restrained typography",
  "lighting": "Overcast natural light in the background image, even and soft, no dramatic shadows",
  "camera": {
    "angle": "straight on",
    "lens": "standard"
  }
}
```

```
Variant: Seedream 5.0 Lite
Image Size: landscape_16_9
Seed: null

Director's Notes: Three-layer composition: background photo → chapter number → 
chapter title. JSON ensures text hierarchy with proper layering. Ken Burns 
reference anchors the restrained, classical documentary typography. Background 
specified as "slightly blurred" to ensure text readability.
```

---

## TECHNICAL / DATA VISUALIZATION

### Example 9: Sci-Fi UI Console Display (Stellar Drift)

**JSON Prompt:**
```json
{
  "scene": "Futuristic holographic heads-up display floating in space, dark background with subtle star field, science fiction UI design",
  "subjects": [
    {
      "description": "Circular radar-style display with concentric rings and three blinking dots representing ship positions",
      "position": "center left",
      "color": "#00FF41"
    },
    {
      "description": "Rectangular status panel reading \"HULL INTEGRITY: 47%\" with a horizontal bar graph, warning state",
      "position": "upper right",
      "color": "#FF4136"
    },
    {
      "description": "Navigation coordinates panel reading \"SECTOR 7-G • LAT 42.7 • DRIFT 0.03\" in monospace font",
      "position": "lower left",
      "color": "#00F5FF"
    },
    {
      "description": "Small circular portrait frame showing the astronaut's face, labeled \"CPT. VASQUEZ\"",
      "position": "upper left"
    },
    {
      "description": "Central crosshair reticle with distance markers",
      "position": "center",
      "color": "#FFFFFF"
    }
  ],
  "style": "Sci-fi UI design, translucent holographic elements, Minority Report aesthetic",
  "lighting": "Self-illuminated UI elements, no external light, elements cast subtle glow on each other",
  "camera": {
    "angle": "straight on, as if viewed by the pilot",
    "lens": "standard"
  }
}
```

```
Variant: Seedream 5.0 Lite
Image Size: landscape_16_9
Seed: null

Director's Notes: Five UI elements with text rendering (coordinates, status 
readouts, labels) — Seedream's typography strength makes this feasible. HEX 
colors differentiate functional zones: green for radar, red for warnings, cyan 
for navigation, white for targeting. JSON prevents element overlap on the 
complex display layout.
```

---

### Example 10: Brand Mood Board Grid (Aurelia)

**JSON Prompt:**
```json
{
  "scene": "Professional mood board layout on a neutral warm grey background, luxury branding presentation format",
  "subjects": [
    {
      "description": "Top-left panel: close-up of golden honey dripping from a wooden dipper, warm backlighting, macro photography",
      "position": "upper left"
    },
    {
      "description": "Top-right panel: aerial view of a baroque marble floor pattern in cream and gold, architectural photography",
      "position": "upper right"
    },
    {
      "description": "Bottom-left panel: close-up of white peony petals with morning dew, soft focus, botanical photography",
      "position": "lower left"
    },
    {
      "description": "Bottom-right panel: texture swatch of raw silk fabric in champagne color with visible weave, fabric photography",
      "position": "lower right"
    },
    {
      "description": "Center overlay: small brand logo text reading \"AURELIA\" in elegant thin serif, gold on translucent white",
      "position": "center",
      "color": "#C5973A"
    }
  ],
  "style": "Brand mood board, luxury fashion aesthetic, cohesive warm golden palette across all panels",
  "lighting": "Each panel has its own natural lighting appropriate to its subject, unified by warm color temperature",
  "camera": {
    "angle": "flat, grid layout",
    "lens": "various per panel"
  }
}
```

```
Variant: Seedream 5.0 Lite
Image Size: landscape_4_3
Seed: null

Director's Notes: Multi-panel mood board as a single generation — JSON ensures 
four quadrant panels plus center logo don't overlap. Each panel is a different 
photographic subject but unified by warm golden palette and luxury material 
focus (honey, marble, petals, silk). Brand name in quotation marks for text 
rendering. HEX #C5973A locks the gold brand color.
```

---

## Version Information

- **Examples Version:** 1.0
- **Covers:** Seedream 5.0 Lite JSON Structured Prompts
- **Last Updated:** 2026-04-18
- **Maintained By:** Visual Horizon Studio
