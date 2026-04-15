# Exam Prep — Phase 7

Exam prep is what makes the vault a study tool rather than an encyclopedia. Two artefacts live in `03 - Exam Prep/`.

## Artefact 1 — Cheat Sheet

Filename: `Exam Cheat Sheet - All <Subject>.md`

A single dense page. Maximum information density, minimum prose. Think: the one-page summary you'd smuggle into an exam if allowed.

### Structure

```markdown
---
tags: [exam, cheat-sheet, reference]
created: <YYYY-MM-DD>
---

# Exam Cheat Sheet — All <Subject> Models

> See also: [[🗺️ <Subject> - Master MOC]]

## Module 1: <Title>

**<Model/Concept Name>**
- Setup: $P = a - bQ$, $MC = c$, $N$ firms
- Key formula: $Q^* = \frac{a - c}{b(N+1)}$
- Decision rule: produce while MR > MC
- Welfare: DWL = $\frac{1}{2} \cdot \text{gap} \cdot \text{quantity}$

**<Next Concept>**
- ...

## Module 2: <Title>
...
```

### Rules for the cheat sheet

- **No paragraphs.** Bullets and formulas only.
- **Every formula names its variables** inline or in a compact "where:" line.
- **Group by module in course order.** Let the user's eye travel the same path as in lectures.
- **Include decision rules** (when to use each model) not just formulas. A formula is useless if the user can't tell when it applies.
- **Aim for 1–3 pages max** when rendered. If it's longer, split by module (one cheat sheet per module) and link them from a cheat sheet MOC.

## Artefact 2 — Q&A Files

Filename: `Exam Q&A - Modules X-Y <Topic Range>.md` (one per module cluster — don't make one giant file).

Each file contains 10–20 exam-style questions with full worked solutions.

### Question format

```markdown
---
tags: [exam, Q&A, practice, module-<N>]
created: <YYYY-MM-DD>
---

# Exam Q&A — Modules X–Y: <Topic Range>

> See also: [[Exam Cheat Sheet - All <Subject>]] | [[🗺️ <Subject> - Master MOC]]

---

## MODULE X: <Module Title>

---

**Q1.** <Question text with all required numerical parameters stated explicitly.>

**A:**
- Step 1: identify the relevant model/formula
- Step 2: plug in numbers, show the arithmetic
- Step 3: interpret the result
- Final answer: **<value>** ✅

---

**Q2.** ...

**A:** ...

---
```

### Rules for Q&A

- **One question per `Q<N>`, heading-marked.** Use `---` horizontal rules between questions so they're visually separated.
- **Every answer ends with the final numerical or conceptual result in bold, followed by ✅.** This visual marker makes the vault scannable when revising.
- **Show every step.** No "algebra omitted". The value of this file is the worked intermediate steps.
- **Mix question types**: numerical, conceptual ("explain why..."), comparative ("what happens if..."), decision ("should the firm..."). Don't make them all plug-and-chug.
- **Draw questions from the whole module**, not just one lecture. The user should be able to work through all Q&A for a module and feel prepared.
- **Tag appropriately** in YAML: `[exam, Q&A, practice, module-N]`.

### How to generate Q&A

1. Read every atomic note in the module
2. For each note's **Formula**, write a numerical question that uses it
3. For each note's **Intuition**, write a short-answer conceptual question
4. For each note's **Common Pitfalls**, write a "spot the error" or "what happens if" question
5. Cover edge cases (what if demand shifts? what if MC rises? what if N→∞?)

Aim for roughly 1.5× as many Q&A as atomic notes in the module — enough coverage to feel thorough without bloating.

## Why two separate artefacts?

- **Cheat sheet** = compressed recall. Use in the final 24 hours before the exam.
- **Q&A** = applied practice. Use in the week before the exam to build fluency.

They serve different cognitive jobs. Keeping them separate keeps each one fit for its purpose.
