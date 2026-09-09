# seedream-v4 — build notes

Human-facing build notes.

---

## Version History

### v1.0.0 (2026-02-25)
- Initial SKILL creation for Seedream 4.5
- Covers text-to-image, image-to-image, multi-image, and editing workflows
- Platform API paths for BytePlus, Segmind, Freepik, Scenario, Fal.ai
- 6 example input/output pairs across complexity levels
- JSON schema with full parameter validation

## Platform-Specific API Paths

### BytePlus (Official)
```
POST https://api.byteplus.com/modelark/v1/images/generations
Authorization: Bearer {API_KEY}
Content-Type: application/json
```

### Segmind
```
POST https://api.segmind.com/v1/seedream-4
x-api-key: {API_KEY}
Content-Type: application/json
```

### Freepik
```
Access via Freepik Spaces interface
Model selection: Seedream 4.0 / 4.5
No direct API — use Freepik's generation UI
```

### Scenario
```
Access via Scenario workspace
Model selection: Seedream 4.x under "Models" panel
Supports reference images and sequence mode
```

### Fal.ai
```
POST https://fal.run/fal-ai/seedream-4
Authorization: Key {API_KEY}
Content-Type: application/json
```

---

## Metadata
- **Model:** ByteDance Seedream 4.5
- **Model Family:** Seedream 4.x
- **SKILL Version:** 1.0.1
- **API Version:** Seedream 4.5 (December 2025)
- **Last Updated:** 2026-07-23 - Dropped "2.39:1 composition" from the "cinematic" style expansion so aspect ratio no longer leaks into prompt prose.
- **Status:** production
- **Category:** image-generation

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
