---
name: adr-capture
description: Capture architectural decisions as lightweight ADRs in the project's decisions directory. Use when the user says things like "we decided X", "let's go with Y over Z", "locked decision", "ADR", or when an architectural trade-off is being resolved. Also use at phase-close to record what was settled during the phase. Can retroactively draft an ADR from a memory entry, changelog note, or commit.
allowed-tools: Read, Edit, Write, Glob, Grep, Bash
---

# adr-capture

## What this is

A skill for writing and maintaining **Architectural Decision Records (ADRs)**. ADRs capture *why* a decision was made, not just *what* was decided — they survive code rewrites and personnel changes and answer "why didn't we do it the other way?" questions that come up six months later.

## When to trigger

**Proactively** when the user or conversation signals a decision is being made:

- Direct cues: "we decided", "let's go with", "locked decision", "I want to commit to", "the choice is".
- Framing cues: "X over Y", "instead of", "we're not going to", "trade-off".
- Structural cues: picking between two architectures, adopting a convention, retiring a pattern.

**On explicit request:** "write an ADR", "document this decision", "add decision 0014".

**At phase close:** scan the phase's plan file and session summaries for decisions that didn't get recorded yet.

**SKIP** when:
- The "decision" is a one-off implementation choice with no architectural impact (what to name a local variable, which util to call).
- You're just summarizing past work — if nothing new was decided, there's nothing to ADR.

## Where ADRs live

**First, find the project's decisions directory.** Glob for an existing `**/decisions/INDEX.md` or `**/adr*/` and use whatever the project already has. If there is none, ask where it should go — common choices are `docs/decisions/`, `Resources/decisions/`, or `.claude/decisions/`. The examples below use `<decisions>/` for that directory.

```
<decisions>/
  INDEX.md                              ← table of contents
  _TEMPLATE.md                          ← MADR-lite structure
  0001-<kebab-title>.md
  0002-<kebab-title>.md
  ...
```

Numbers are **immutable**. If a decision is reversed, write a new ADR marked `Status: Supersedes NNNN` and update the old one to `Status: Superseded by MMMM` — never renumber or rewrite history.

## The template

Open `<decisions>/_TEMPLATE.md` before writing (create it from the structure below if the project has none). Structure:

```
# NNNN — <Title>

**Status:** Proposed | Accepted | Superseded by NNNN | Deprecated
**Date:** YYYY-MM-DD
**Deciders:** <names or roles>

## Context
## Decision
## Consequences  (Positive / Negative / Neutral)
## Alternatives considered
## References
```

Writing guidelines:

- **Title:** noun phrase describing the chosen path. "One authorization checkpoint for every route" not "Authorization" and not "Use the auth middleware".
- **Context:** why is this decision needed *now*? What constraint or incident forced it? Keep to 3–6 sentences.
- **Decision:** state the choice in the *present tense*. "We use X." not "We will use X."
- **Consequences:** include the **negative / accepted trade-offs**. Every real decision has downsides; recording them forces honesty and helps future-you recognize when the trade-off has shifted.
- **Alternatives:** at least one. If you can't name one, you didn't have a real decision — you had a default.

## Workflow

### Path A — Capture a new decision (live)

1. **Pick the next number:** read `<decisions>/INDEX.md`. Take the highest existing `NNNN` + 1.
2. **Draft the title** as a kebab slug. Keep under ~60 chars. Filename: `NNNN-<slug>.md`.
3. **Write the ADR** from the `_TEMPLATE.md` shape. Fill in every section — skipping "Alternatives considered" is the usual smell that means this isn't ADR-worthy.
4. **Update `INDEX.md`:** add a row to the table. Keep the table sorted ascending by `#`.
5. **Link from the active phase or plan file** if the project tracks work that way and the decision belongs to one (→ its Decisions section).
6. **Mention in the session summary** under "### Decisions (link ADRs if any)".

### Path B — Retroactive capture

When the user points at an existing memory entry, changelog paragraph, or commit and says "turn this into an ADR":

1. Read the source material. Extract: what was the problem, what was chosen, what was rejected.
2. If `Alternatives considered` can't be reconstructed, ask the user for one concrete alternative before writing. Don't fabricate.
3. Use the original decision's date (not today's). The ADR is a record of what happened then.
4. Otherwise follow Path A (new number, write file, update index, link back).

## Sizing

ADRs are *small on purpose*. Target 40–120 lines. If the draft is bigger:

- Move detailed implementation notes into the project's phase or plan file and link from the ADR.
- Cut the history lesson. Context should motivate the decision, not re-summarize the project.

## Don'ts

- **Don't ADR every commit.** Code-level choices belong in commit messages and comments. ADRs are reserved for decisions you'd want to explain to a new engineer.
- **Don't rewrite old ADRs.** Supersede them.
- **Don't leave `Status: Proposed` indefinitely.** Either accept it (change status + date) or delete the file. A proposed-forever ADR is architectural clutter.
- **Don't forget to update `INDEX.md`.** An ADR with no index entry is invisible.
- **Don't hide dissent.** If a decision was controversial, say so in Context. The ADR is for future readers, including future-you.

## What a good ADR looks like

Read a few existing ADRs in `<decisions>/` before writing your first one — match their voice and length. The four shapes worth recognizing:

- **One rule, enforced everywhere** — a single chokepoint replaces scattered ad-hoc checks (e.g. `0001-single-authorization-checkpoint.md`).
- **Infrastructure choice with clear trade-offs** — picking a queue, a database, a hosting target (e.g. `0002-managed-queue-for-async-jobs.md`).
- **Small decision, tight doc** — a naming or file-layout convention worth writing down once (e.g. `0003-naming-convention-for-design-tokens.md`).
- **Process or IA decision, not code** — how the team plans, reviews, or organizes docs (e.g. `0004-plan-decomposition-by-phase-file.md`).

Those filenames are illustrative, not real files — number and name your own from the project's index.

## Cross-references

- Template: `<decisions>/_TEMPLATE.md`
- Index: `<decisions>/INDEX.md`
- Related skills: `code-documentation-standards` (for code-level comments), `project-docs` (for user-facing docs)

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
