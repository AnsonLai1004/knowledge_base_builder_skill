# Note Templates

Use these exact templates. Consistency is what makes the vault feel like one system instead of a pile of files.

> 🔗 **Before writing any note, invoke the `obsidian:obsidian-markdown` skill.** It covers the exact syntax for wikilinks `[[...]]`, embeds `![[...]]`, callouts `> [!note]`, frontmatter properties, tags, and block references. The templates below are the shape; `obsidian:obsidian-markdown` tells you the syntax rules that make them render properly in Obsidian.

## Atomic Concept Note

Filename: `<Concept Name>.md` in `02 - Concepts/`. Use natural case (e.g. `Bertrand Paradox.md`, not `bertrand-paradox.md`).

```markdown
---
tags: [concept, <topic-tag>, exam]
topic: <Concept Name>
module: <Number>
created: <YYYY-MM-DD>
---

# <Concept Name>

## Definition
One-paragraph precise definition. Assume an intelligent reader with no prior knowledge of this concept but familiarity with the broader field.

## Intuition
Why does this concept exist? What problem does it solve? One short paragraph, plain English.

## Key Formula / Key Points
$$\text{formula here}$$

Where:
- $x$ = definition of x
- $y$ = definition of y

Or a tight bullet list of 3–6 key points if there's no formula.

## Example
A worked numerical example if the concept is quantitative, or a concrete real-world example if qualitative. Show the numbers.

## Common Pitfalls
> ⚠️ The most common mistake with this concept is...

> ⚠️ Don't confuse this with [[Related Concept]].

## Related Notes
- [[Related Concept 1]]
- [[Related Concept 2]]
- [[Lec X - Source Summary]]
```

### Atomic note rules

- **One idea only.** If you wrote "and" in the title, split it.
- **Every note has ≥2 outgoing wikilinks** to other concept notes plus a link back to its source summary. A note with zero links is not part of the knowledge graph.
- **The Definition section is self-contained** — someone should be able to read just that paragraph and leave knowing what the concept is.
- **Formulas always have variables named directly below.** Unnamed variables are forbidden.

## Summary Note

Filename: use the source's name. E.g. `Lec 1 - Perfect Competition & Monopoly.md` in `01 - Summaries/`.

```markdown
---
tags: [summary, lecture, module-<N>]
source: <original filename.pdf>
module: <N>
created: <YYYY-MM-DD>
---

# Lec <N> — <Title>

> Part of [[🗺️ <Subject> - Master MOC]]

## Key Takeaways
- Bullet 1 — the single most important idea
- Bullet 2
- Bullet 3 (aim for 3–6 total)

## <Sub-topic 1>
Prose explaining the sub-topic. Introduce concepts with [[wikilinks]] the first time they appear.

Formulas in display math:
$$P = MC$$

## <Sub-topic 2>
...

## Worked Examples
If the source has examples, reproduce one or two in full. Show the steps.

## Common Pitfalls
Anything the source warns against or that students typically get wrong.

## Related Notes
- [[Atomic Note 1]]
- [[Atomic Note 2]]
- [[Atomic Note 3]]
(All concepts that originate from this source go here.)
```

### Summary note rules

- The **Key Takeaways** are for someone revising a week before the exam — they should be enough to jog memory
- **Core Content** is for someone re-learning the material without opening the PDF — it should be detailed
- **Every concept mentioned gets its first occurrence wikilinked.** Don't link every subsequent mention
- **Related Notes at the bottom** is the authoritative list of atomic notes derived from this source

## Style rules across all notes

- **Tense**: present ("The Cournot model predicts...") not past
- **Voice**: active, second-person or neutral ("You add stores while n(n+1) < ...")
- **Math**: LaTeX — `$...$` inline, `$$...$$` display
- **Callouts**: `> ⚠️` for warnings, `> 💡` for insights, `> 📌` for definitions (use sparingly)
- **Tables**: use for side-by-side comparisons (e.g. Horizontal vs Vertical differentiation). Keep them small
- **Emoji**: only in MOC titles (🗺️) and callout markers. Never in body text unless the user's style uses them
