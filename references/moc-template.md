# Master MOC Template

The Master MOC (Map of Content) is the user's entry point. It's the first thing they open, every time.

Filename: `🗺️ <Subject> - Master MOC.md` inside `00 - MOC/`. The emoji is intentional — it makes the file visually jump out in the file explorer and distinguishes it from regular notes.

## Full template

```markdown
---
tags: [moc, index, navigation]
topic: <Subject> - Master Index
created: <YYYY-MM-DD>
---

# 🗺️ <Subject> — Master MOC

> **Entry point for the entire <Subject> knowledge base.** All roads lead here.

## Subject Overview
One short paragraph — what this subject is about, what it covers, what it's useful for. Written for the user a month from now who's forgotten half of it.

## Topic Map

### Module 1 — <Module Title>
Short description (1 line).
- Summary: [[Lec 1 - ...]]
- Key concepts: [[Concept A]], [[Concept B]], [[Concept C]]

### Module 2 — <Module Title>
...

(Repeat for every module.)

## Source Materials
- [[Lec 1 - ...]] — original: `Lec 1.pdf`
- [[Lec 2 - ...]] — original: `Lec 2.pdf`
- ...

## Exam Prep
- [[Exam Cheat Sheet - All <Subject>]]
- [[Exam Q&A - Modules 1-2 ...]]
- [[Exam Q&A - Modules 3-4 ...]]
- [[Exam Q&A - Modules 5-8 ...]]

## Key Assumptions / Recurring Traps
A short list of assumptions or common confusions that apply across the whole subject. Example:
- > ⚠️ All models assume profit maximisation unless stated
- > ⚠️ "Bertrand with differentiated products" is NOT the Bertrand Paradox

## How to use this vault
1. Click into a Module in the Topic Map above
2. Read the summary note for context
3. Drill into individual concept notes via wikilinks
4. Use the Cheat Sheet + Q&A for exam prep
5. Use Obsidian's graph view (Ctrl/Cmd+G) to see the whole structure
```

## Why the MOC matters

Without a MOC, a vault of 100+ atomic notes is unnavigable. With one, the user has a stable address — they always know where to start. Every other note in the vault should be reachable from the MOC in ≤2 clicks.

## Rules

- **Every concept note must appear somewhere on the MOC** — either directly under a module or linked from a summary linked from the MOC. If a note isn't reachable, it's effectively lost.
- **Module order matches the course order.** Don't reorder by topic similarity.
- **Keep the MOC skimmable.** Don't write paragraphs under each module — just a one-liner plus the links.
- **Update the MOC last**, after all summaries and concepts exist, so every link resolves.

## Optional overlays — Bases and Canvas

Once the MOC exists, two Obsidian features can layer on top of it:

- **`obsidian:obsidian-bases`** — invoke to create a `.base` file that shows, e.g., every `#concept` note in a module as a sortable/filterable table, or every Q&A grouped by difficulty. Bases are live views over the vault's YAML frontmatter, so the tags and `module` field you set in every note pay off here.
- **`obsidian:json-canvas`** — invoke to create a `.canvas` file with a visual map of how concepts relate (e.g. a flowchart showing how Cournot leads to Stackelberg leads to Bertrand). Especially useful when the user says "I want to see how these ideas connect."

Add links to any Bases or Canvases you create into the Master MOC under a new "Visual Overlays" section so they're discoverable.

## Sub-MOCs (optional)

If a subject has > 50 concepts or very distinct sub-areas, make sub-MOCs:

- `00 - MOC/Module 5 - Variety and Quality MOC.md`
- `00 - MOC/Module 6 - Advertising MOC.md`

Link them from the Master MOC. Each sub-MOC follows the same pattern but scoped to its module.
