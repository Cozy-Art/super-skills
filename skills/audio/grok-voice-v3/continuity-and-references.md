# Grok Voice 3.0 — Continuity & Persona Consistency

A live voice agent has no seed and no reference-audio input per turn. **Continuity is carried by five things:** the pinned model ID, the `voice` ID, the versioned `instructions`, the session config (speed, `replace`, `keyterms`, tools), and — within a 30-minute window — session resumption. Anything not locked in those drifts.

## 1. The Agent Manifest

One per agent, versioned like code. Change one line per version and re-run the test script.

```
AGENT: harbor-dental-frontdesk   v1.4
MODEL: grok-voice-3.0            (pinned — not grok-voice-latest)
VOICE: ara                       (fallback: celeste)
SPEED: 0.95
REASONING: none
TURN_DETECTION: server_vad · idle_timeout_ms 8000
AUDIO: in pcm 24000 / out pcm 24000 (web) · pcmu 8000 (SIP)
LANGUAGE_HINT: en
KEYTERMS: Harbor Dental, Dr. Okafor, Invisalign, Delta Dental
REPLACE: {"Okafor": "oh-KAH-for"}
TOOLS: check_availability, book_slot, transfer_call
INSTRUCTIONS: prompts/frontdesk_v1.4.md   (sha / date)
RESUMPTION: enabled
```

Log per call: manifest version, `conversation.id`, transcript, tool calls, outcome, failure tag.

## 2. Persona Bible

Kept outside the prompt; the prompt carries a compressed version.

```
MIRA (Harbor Dental front desk)
Disposition: warm, unhurried, lightly dry; never chirpy
Vocabulary: "absolutely" ✗  "sure thing" ✓  "let me check" ✓
Turn length: 1 sentence default, 2 max
Signature phrases: "Let me take a look." / "You're all set." / "Anything else I can sort out?"
Never says: "As an AI language model", "per our policy"
Disclosure: "I'm the practice's AI assistant." when asked or at transfer
Escalation line: "I'll get you to someone at the front desk — one moment."
```

Rule: give the persona **sample phrases**, not adjectives alone. The model copies phrasing more reliably than it interprets "warm".

## 3. Same Persona, Many Sessions

- **Pin the model.** `grok-voice-latest` was silently moved to 3.0 on 14 Oct 2026; it will move again. Pin `grok-voice-3.0` in production, test the alias in staging.
- **Store instructions as a file**, inject at connect via `session.update`. Never hand-edit in a console for one session.
- **Same voice ID everywhere** — web, mobile, SIP. If SIP needs `pcmu` 8 kHz, the voice is the same but will sound band-limited; audition it on a phone line.
- **Same `replace` and `keyterms`** in every channel, or names will sound and be heard differently per channel.
- **Personalisation without drift:** keep the persona static; inject per-user facts in a clearly bounded block at the end of `instructions` ("## Caller Context: name, last visit, open balance"), or via a read-only tool. Don't rewrite persona text per user.

## 4. Within a Session

- `session.update` is allowed mid-call (instructions, `language_hint`, `keyterms`, `replace`, tools). Change only the field you need — e.g. add a caller's surname to `keyterms` once you learn it.
- **One-turn overrides** (`response.create` with `response.instructions`) for a single deviation — a summary, a language switch, a compliance read — then the session prompt resumes automatically. Prefer this to rewriting session instructions.
- **Verbatim lines** (recording notice, legal disclaimer): `force_message` with `interruptible: false`. Same text every call, no paraphrase drift.
- Phase changes in complex flows: keep all phases in one prompt (Goal / How to respond / Exit when) rather than swapping instructions per phase — swaps can lose context the model already built.

## 5. Across a Dropped Connection (Resumption)

1. `resumption.enabled: true` on the first session.
2. Save `conversation.created.conversation.id`.
3. On drop, reconnect `wss://api.x.ai/v1/realtime?conversation_id=<id>` with resumption enabled again.
4. Re-send the same `session.update` (manifest unchanged) — only transcripts, tool calls and function outputs are documented as replayed.
5. After **30 min** of inactivity the history is gone: start fresh and, if needed, inject a short summary into Caller Context.

For multi-day continuity (a tutor that remembers last week), resumption is the wrong tool — persist your own summary and pass it in Caller Context or via a `get_user_history` tool.

## 6. Brand Voice via Custom Voices

- One clone per brand persona, recorded in the **register the agent will use** (support-call calm, not an ad read — delivery style is cloned).
- 90–120 s, single speaker, quiet room, WAV 16-bit mono 24 kHz. Background noise and lossy artifacts get cloned.
- The ID is permanent for that audio; re-recording means a new ID → bump the manifest version and re-test.
- Console: 30 voices per team, free; API creation is Enterprise-only; US-only (not Illinois). Clone only voices you have consent and rights to use.
- Keep a built-in fallback voice in the manifest in case the custom voice is deleted or unavailable in a region.

## 7. Matching Live and Scripted Audio

When the same character appears in live calls (S2S) and pre-rendered prompts (TTS — hold messages, IVR menus, trailers): use the same `voice` / `voice_id`, the same `replace` map and the same `speed`. TTS adds speech tags (`<soft>`, `[sigh]`) that live replies don't reliably have — keep scripted lines in the same emotional range as the live persona, or the hand-off is audible. Same-voice consistency between S2S and TTS output is not documented — audition side by side (unverified).

## 8. Migrating from grok-voice-2.0

xAI states the endpoint, session parameters and events are unchanged, and the price is the same.

1. Change `?model=grok-voice-2.0` → `?model=grok-voice-3.0` (or rely on the alias). Nothing else is required.
2. Re-run your test script — 3.0's vendor-reported gains are in turn-taking/interruptions (Full Duplex Bench 95.1% → 97.0%) and support-call tasks (τ-Voice 56.5% → 71.6%), so behaviour **will** shift even with identical prompts.
3. Watch for: shorter or longer turns, different tool-call eagerness, changed handling of barge-in. Fix with prompt bullets, not by staying on 2.0 (deprecated).
4. Recheck `reasoning.effort` — if you used `"none"` on 2.0 for speed, test whether `"high"` now fits your latency budget.
5. Don't assume features you see in current docs (custom voices, `replace`, binary transport, resumption) are new in 3.0 — they're platform features available to both.
6. Bump the manifest version; keep the 2.0 transcripts as a baseline for comparison.
