# PixVerse V6 — Parameters Reference

---

## V6 API Parameters (WaveSpeed — Most Complete V6 Schema)

| Parameter | Type | Required | Default | Range / Values | Notes |
|-----------|------|----------|---------|---------------|-------|
| `image` | string | Yes (I2V) | — | URL or file | Reference image to animate |
| `prompt` | string | Yes | — | ≤ 2,048 chars | Motion, camera style, scene atmosphere |
| `resolution` | string | No | `720p` | `360p`, `540p`, `720p`, `1080p` | 360p/540p for drafts; 1080p for finals |
| `duration` | integer | No | `5` | 1–15 seconds | Full 1-second granularity in V6 |
| `generate_audio_switch` | boolean | No | `false` | `true` / `false` | AI-generated ambient SFX — not music generation |
| `thinking_type` | string | No | `auto` | `enabled`, `disabled`, `auto` | `enabled` = model rewrites/enhances; `disabled` = verbatim |
| `seed` | integer | No | random | 0–2,147,483,647 | Lock for reproducible results |
| `negative_prompt` | string | No | — | ≤ 2,048 chars | Unwanted elements; highly effective in V6 |
| `aspect_ratio` | — | — | 16:9 | 16:9, 9:16, 1:1 | Set before generation; not a crop |

---

## Character / Token Limits

| Field | Limit | Notes |
|-------|-------|-------|
| `prompt` | 2,048 characters | Required for all generation modes |
| `negative_prompt` | 2,048 characters | Optional; active across all modes |
| `lip_sync_tts_content` | ~200 characters | TTS dialogue script; no UTF-8 encoding |

Prompts under ~20 words produce highly variable, low-control outputs.

---

## Legacy Platform API Parameters (V4/V4.5 — Still Functional)

These parameters appear in the legacy `docs.platform.pixverse.ai` schema. V6-specific features are primarily via third-party APIs until official V6 API parity is published.

| Parameter | Valid Values | Notes |
|-----------|-------------|-------|
| `camera_movement` | `horizontal_left`, `horizontal_right`, `vertical_up`, `vertical_down`, `zoom_in`, `zoom_out`, `crane_up`, `quickly_zoom_in`, `quickly_zoom_out`, `smooth_zoom_in`, `camera_rotation`, `robo_arm`, `super_dolly_out`, `whip_pan`, `hitchcock`, `left_follow`, `right_follow`, `pan_left`, `pan_right`, `fix_bg` | Explicit camera control for legacy models; same terms work in V6 text prompts |
| `style` | `anime`, `3d_animation`, `day`, `cyberpunk`, `comic` | Strong genre override — avoid for photorealistic output |
| `motion_mode` | `normal`, `fast` | `fast` = 5s only; **1080p does not support `fast`** |
| `duration` | `5`, `8` | Legacy; V6 supports 1–15s |
| `quality` | `360p` (Turbo), `540p`, `720p`, `1080p` | Required field in legacy schema |

---

## V6 Cinematic Lens Controls (Web UI — 20+)

Available as explicit UI parameters in V6 — not just text-prompt hints.

| Control | Description |
|---------|-------------|
| Focal length | Wide, standard, telephoto equivalent |
| Aperture | Depth-of-field control |
| Depth of field | Bokeh intensity and range |
| Lens distortion | Fisheye, barrel, or pin-cushion effects |
| Chromatic aberration | Fringe color separation at edges |
| Vignetting | Edge darkening / vintage lens feel |
| Motion blur | Shutter-speed simulation |
| Film grain | Texture overlay for analog look |
| + 12 additional controls | Available in V6 UI |

These controls are accessible via the web UI. API equivalents are not fully documented as of April 2026 — use text prompt descriptors for API workflows.

---

## Aspect Ratio Options

| Ratio | Format | Primary Platform |
|-------|--------|-----------------|
| **16:9** | Landscape | YouTube, widescreen, desktop |
| **9:16** | Vertical | TikTok, Reels, YouTube Shorts |
| **1:1** | Square | Instagram feed, social posts |

V6 composes natively for each ratio — it is **not a crop of a single master output**. Always set aspect ratio before generation.

---

## API Pricing (WaveSpeed, V6 I2V)

| Resolution | Without Audio | With Audio |
|------------|-------------|------------|
| 360p | $0.025/s | $0.035/s |
| 540p | $0.035/s | $0.045/s |
| 720p | $0.045/s | $0.060/s |
| 1080p | $0.090/s | $0.115/s |

**Example costs:**
- 10s at 720p (no audio) = $0.45
- 15s at 1080p (with audio) = $1.73
- 5s at 360p (draft, no audio) = $0.13

**Cost strategy:**
- Draft at 360p/540p — validate before committing to 1080p
- Enable audio only after visual is finalized
- 1080p costs 2–3× more than 720p

---

## Duration Options

| Duration | Mode Support | Notes |
|----------|------------|-------|
| 1–15s | V6 full range | 1-second granularity; new in V6 |
| 5s | Fast mode (legacy) | Fast mode limited to 5s |
| 5s, 8s | Legacy platform API | V4/V4.5 only |

**1080p constraint:** Does not support `motion_mode: fast`. Use `motion_mode: normal` at 1080p.

---

## V5.6 → V6 Feature Migration

| Feature | V5.6 | V6 |
|---------|------|-----|
| Primary use case | Short stylized clips, standalone social | Production-ready narrative, commercial assets |
| Max duration | 15s (with seam artifacts) | **15s single-pass, no seam artifacts** |
| Audio | Silent output only | **Native audio: dialogue, SFX, ambient** |
| Multi-shot | Single shot only | **Native multi-shot engine** |
| Character consistency | Single reference image | **Multi-image reference (multiple angles)** |
| Camera control | Text-described or basic `camera_movement` API | **20+ explicit lens controls in UI** |
| Developer tools | REST API | CLI + agentic workflow support |
| Resolution max | 4K | **1080p with improved temporal coherence** |

> **Resolution trade-off:** V5.6 offered 4K. V6 focuses on 1080p with dramatically improved temporal stability — PixVerse made a deliberate trade of maximum resolution for production reliability.

---

## thinking_type Parameter

| Value | Behavior | When to Use |
|-------|----------|------------|
| `enabled` | Model rewrites and enhances prompt before generation | Drafting — exploring effective phrasings |
| `disabled` | Generates exactly from prompt verbatim | Production — locked prompts needing reproducibility |
| `auto` (default) | Model decides based on prompt complexity | General use; most prompts |

**Workflow:** Use `enabled` during drafts to discover effective phrasings → switch to `disabled` for reproducible finals.
