# Suno v6 — Parameters & Specs

Suno is a consumer web/mobile app (suno.com). There is no official public API documented in Suno's help center; third-party "Suno API" wrappers are unofficial and their field names are not Suno syntax.

*Verified against help.suno.com (v6 FAQ, Current Models, How long will my song be, Creative Sliders, Exclude, Voices FAQ, Custom Models, Upload Audio, Replace Section, Remaster, Get Stems, Download types) and suno.com/blog/introducing-v6, October 2026.*

## Models

| Model | Plan | Character | Best use |
|---|---|---|---|
| `v6` | Pro, Premier | Flagship: reliable, precise, polished, strongest prompt control | Finals, client work, structured songs, faithful covers |
| `v6-wild` | Pro, Premier | Less predictable, more varied; outputs can be taken into v6 to refine | Ideation, genre collisions, unexpected arrangements |
| `v6-mini` | All plans (incl. free) | Fastest, most efficient | Sketches, volume exploration |
| Custom Model | Pro, Premier | Private model trained on ≥6 tracks you own; existing ones auto-upgraded to v6 | Recurring catalog sound |

Released September 9, 2026. **All pre-v6 models are retired** for new generations; older songs remain playable, shareable, remasterable and coverable, but new iterations use v6-family models.

## Create Form Fields

| Field | Surface | Notes |
|---|---|---|
| Brief / description | Simple mode | Natural language; can combine Suno songs, playlists, audio uploads, images, video. v6 infers cover / remix / extend / edit / sample / mashup from plain language. |
| Lyrics | Custom mode | Words + `[section]` tags. Composer counter shows **5,000** chars (observed in live UI; unverified as a fixed spec). |
| Style (Style of Music) | Custom mode | Producer brief. Counter shows **1,000** chars (observed; unverified as fixed). Aim 300–700. |
| Exclude (Exclude Styles) | Custom → Advanced/More Options | Unwanted instruments, styles, vocal traits. Shown back as minus-prefixed terms after the style text. No published limit. |
| Title | Custom mode | Metadata only. |
| Instrumental | Toggle | Disables lyric-led vocals. |
| Vocal Gender | More Options | Present in UI; options/behaviour not documented (unverified). |
| Personalize / My Taste | More Options | Present in UI; behaviour not documented (unverified). |

## Sliders & Toggles

| Control | Range / default | Effect | Starting point |
|---|---|---|---|
| **Variety** (new in v6) | UI slider; Suno documents only `0`; no published max/default | Adjusts/updates your style prompt; higher = takes diverge more | **0** for strict briefs and A/B tests; raise to explore |
| **Weirdness** | Safe → Chaos; 50% described as baseline | More unusual musical choices | 20–40% controlled · ~50% general · 60%+ experiments |
| **Style Influence** | Loose → Strong; third-party reports 50% default (unverified) | Adherence to Style text | High/Strong for production briefs; lower for reinterpretation |
| **Audio Influence** | Appears only with an audio upload / Voice; no published range | Closeness to uploaded audio or Voice | Raise when melody or singer identity drifts |
| **Max Mode** | On / Off; costs more credits | More compute per generation | On for songs > 2 min, close covers, style transfer, vocal/style consistency over a full track |
| **Remaster Variation** | Subtle · Normal (default) · High | Deviation during Remaster | Subtle = polish · Normal = refresh · High = may change musical elements and vocals |

No seed control exists. Reuse Prompt repopulates Lyrics/Style/Title only.

## Duration

- Up to **8 minutes** per generation on v6, v6-wild and v6-mini. This is a ceiling, not a target.
- Length is driven by lyric length, tempo, section count, instrumental passages and the ending instruction. To aim, write a target into Style: `Target 2:15. Eight-bar intro, two verses, two choruses, bridge, final chorus, four-bar resolved ending.`
- Extend continues from a chosen point; **Get Whole Song** stitches it to the original.
- Suno Scenes (mobile): video in → two 30-second songs.

## Credits

| Action | Cost |
|---|---|
| Standard generation (2 songs) | 10 credits (same as prior models) |
| Max Mode | More than standard (shown before generating) |
| Many images/videos in a prompt | Increases cost |
| Auto Split stems (up to 12) | 50 credits per extraction |
| Split from Mix (1 stem + complement) | 10 credits per stem |
| Advanced Split (~100 instrument choices, Premier) | 10 credits per stem |

## Uploads

| Plan | Audio upload length |
|---|---|
| Free (Basic) | up to 60 s |
| Pro / Premier | up to 8 min (full songs) |

An older Upload Audio article still lists 6–60 s and 120 s for subscribers — limits may differ by surface; trust the upload dialog. Uploads can be Extended, Covered and referenced. Studio accepts WAV, MP3, MIDI.

## Downloads & Stems

| Output | Plan |
|---|---|
| MP3 | All plans, web + mobile |
| WAV | Pro / Premier, on suno.com (mobile defaults to MP3) |
| Stems (Get Stems) | Pro / Premier; Advanced Split Premier only |
| MIDI | Premier, songs made in Studio |
| Studio multitrack / range / full-mix export | Studio; high-quality WAV (Studio 2.0 lists 32-bit WAV for Premier multitrack — confirm on your export dialog) |

## Editing Tools

| Tool | Plan | Behaviour |
|---|---|---|
| Replace Section | Pro / Premier | Highlight a region + new lyrics/instructions → two options → new whole-song version |
| Plain-language edit (v6) | — | "Change only the second chorus lyric to…" in Simple mode |
| Extend | All | Continue from a timestamp; Get Whole Song to stitch |
| Cover | All | Re-perform a song in a new style/voice |
| Remaster | — | Subtle/Normal/High variation of an existing clip |
| Song Editor / Studio | Studio features vary by plan | Section rearranging, stems, timing |

## Recommended Combinations

| Goal | Model | Variety | Weirdness | Style Influence | Max Mode |
|---|---|---:|---:|---|---|
| Controlled final song | v6 | 0 | 20–40% | Strong | On if > 2 min |
| Fast concept sweep | v6-mini | low–med | 40–55% | Medium | Off |
| Experimental discovery | v6-wild | med–high | 55–80% | Loose–med | Off |
| Faithful cover / style transfer | v6 | 0 | 10–30% | Strong | On |
| Reference-led soundtrack | v6 | 0–low | 25–45% | Strong; raise Audio Influence | On for long cues |

These are workflow starting points, not Suno presets. Change one control per run.

## v5.5 → v6 Migration

| Old habit | v6 |
|---|---|
| Comma tag cloud (`dark, synthwave, 80s, male vocals`) | Ordered producer-brief sentences |
| Picking Cover / Remix / Extend manually | Still available; Simple mode can infer from plain language |
| One audio reference | Songs, playlists, uploads, images and video together, each with a role |
| Regenerate to fix a lyric | Replace Section or single-lyric plain-language edit |
| Elaborate metatag recipes | Short section tags + composite cues; v6 reads natural language |
| "no X" in style | Exclude field |
| Selecting v4.5/v5/v5.5 | Retired; pick v6 / v6-wild / v6-mini |
| v5.5 Custom Model | Auto-upgraded to v6 — re-test its identity |
| Voices on v5.5 | Voices FAQ still says to select v5.5; v6 Voices compatibility **unverified — check the model dropdown** |

To revisit an old song, Cover or Remaster it rather than rebuilding from text.
