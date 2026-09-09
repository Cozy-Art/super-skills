# sora-v2 — build notes

Human-facing build notes.

---

## Version History

### v1.0.0 (2026-02-25)
- Initial SKILL creation for Sora 2 (Standard and Pro)
- Covers text-to-video, image-to-video, and audio sync workflows
- MARS-LSP timestamped prompting documentation (Pro only)
- Platform API paths for OpenAI, Azure, Replicate, sora.com
- Sequential prompt technique for character consistency
- Editing tools reference (Re-Cut, Blend, Loop, Storyboard, Remix)
- 6 example input/output pairs across complexity levels

## Platform-Specific API Paths

### OpenAI API (Official)
```
POST https://api.openai.com/v1/videos/generations
Authorization: Bearer {API_KEY}
Content-Type: application/json

Models: "sora-2", "sora-2-pro"
```

### Azure AI Foundry (Microsoft)
```
POST https://{endpoint}/openai/deployments/sora/videos/generations
api-key: {API_KEY}
Content-Type: application/json

Available via Azure AI Foundry preview
```

### Sora Web Interface
```
Access via sora.com (requires Plus or Pro subscription)
Direct prompt input with editing tools:
- Re-Cut, Blend, Loop, Storyboard, Remix
No API key needed — subscription-based
```

### Replicate
```
POST https://api.replicate.com/v1/predictions
Model: openai/sora-2
Model: openai/sora-2-pro
Authorization: Bearer {API_TOKEN}
```

---

---

## Metadata
- **Model:** OpenAI Sora 2
- **Model Family:** Sora 2 (Standard, Pro)
- **SKILL Version:** 1.0.0
- **API Version:** Sora 2 (September 2025 launch)
- **Last Updated:** 2026-02-25
- **Status:** production
- **Category:** video-generation

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
