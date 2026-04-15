---
name: knowledge-base-builder
description: Build a complete Obsidian-style "Second Brain" knowledge base from a folder of source materials (PDFs, slides, lecture notes, textbooks, readings). Use this skill WHENEVER the user asks to "build a knowledge base", "create study notes", "make a second brain", "set up an Obsidian vault", "organise my course materials", "make a notetaking system", "summarise my lecture PDFs into notes", "turn these readings into a vault", or provides a folder of study materials and asks for structured notes. Also trigger on phrases like "help me study X", "prep for my exam using these sources", "process these lecture slides into atomic notes", or any request to transform raw source documents into a linked, searchable, exam-ready knowledge base with summaries, atomic concept notes, MOCs, and exam prep materials.
---

# Knowledge Base Builder

Transform a folder of raw source materials (PDFs, slides, docs, notes) into a complete, linked, Obsidian-compatible **Second Brain** optimised for study, review, and exam preparation.

## Purpose

When a user points to a folder of course/study materials, produce a knowledge base that is:

- **Atomic** — one concept per note, so each idea can be recombined, linked, and reviewed independently
- **Linked** — every note connects to related notes via `[[wikilinks]]`, forming a navigable knowledge graph
- **Progressive** — navigable from high-level maps (MOCs) down to single formulas, without ever getting lost
- **Exam-ready** — includes cheat sheets and worked Q&A so the vault isn't just a reference but a study tool
- **Reproducible** — the same folder should always yield the same structure and conventions

The user should be able to open the output folder in Obsidian and immediately navigate, search, and study.

## When to Use

Trigger this skill whenever:

- A user gives a folder of study materials and asks for notes, a knowledge base, a vault, a Second Brain, or help studying
- A user asks to process lecture PDFs/slides into structured notes
- A user mentions Obsidian, atomic notes, Zettelkasten, MOCs, or wants a searchable note system built from source docs
- A user asks for exam prep generated from course materials

Do **not** use this skill for one-off summaries of a single document (use the relevant document skill), or when the user wants raw text extraction without structure.

## High-Level Workflow

The full workflow proceeds through seven phases. Each phase has its own detail file in `references/` that you should read before executing that phase.

1. **Discover** — scan the user's folder, identify all source files, detect any existing vault
2. **Plan** — propose the vault structure and confirm scope with the user
3. **Extract** — pull text from every source (PDFs, docx, pptx) into readable form
4. **Architect** — create the folder skeleton and the Master MOC
5. **Summarise** — produce one detailed summary note per source file
6. **Atomise** — produce atomic concept notes for every distinct idea across all sources
7. **Exam Prep** — produce cheat sheets and worked Q&A for each module/topic

At every phase, files use consistent YAML frontmatter and `[[wikilinks]]`. The patterns are in `references/note-templates.md` — **read this before writing any note**.

> 🔗 **Always pair with the Obsidian marketplace skills.** Before writing any note, invoke `obsidian:obsidian-markdown` for wikilink/callout/frontmatter syntax. If the vault already exists, invoke `obsidian:obsidian-cli` during Discover. If the user wants tabular views or visual maps of the vault, invoke `obsidian:obsidian-bases` or `obsidian:json-canvas` in the appropriate phase. See the "Required companion skills" section below for the full invocation pattern.

## Phase 1 — Discover

Read `references/discovery.md` for the full procedure. In short:

- Confirm the target folder with the user (use `ls` via Bash on the folder they named)
- Recursively list all source files. Supported: `.pdf`, `.docx`, `.pptx`, `.md`, `.txt`
- Check for an existing Obsidian vault by looking for a `.obsidian/` directory at or above the target
- If a vault exists, work inside it and respect its conventions; if not, create a fresh one
- Group sources by topic/module if filenames suggest a structure (e.g. "Lec 1", "Lec 2", "Week 3")

Report back what you found before proceeding: number of sources, detected structure, whether a vault exists.

## Phase 2 — Plan

Briefly propose the output structure to the user and get a green light. Default skeleton:

```
<vault-root>/
├── 00 - MOC/                        # Maps of Content (navigation hubs)
├── 01 - Summaries/                  # One file per source document
├── 02 - Concepts/                   # Atomic notes (one idea each)
├── 03 - Exam Prep/                  # Cheat sheets + Q&A
└── <original source folders>/       # Leave source files untouched
```

The numeric prefixes force useful ordering in Obsidian's file explorer. Let the user override folder names if they want (e.g. they may prefer "Notes" over "Concepts").

## Phase 3 — Extract

Source files are useless until their text is readable. Read `references/extraction.md` for the full procedure and the `scripts/extract_pdf.py` helper.

- PDFs: use `pymupdf` (install with `pip install pymupdf --break-system-packages` if missing). The bundled `scripts/extract_pdf.py` batches a whole folder
- DOCX: use `python-docx` or the `docx` skill
- PPTX: use `python-pptx` or the `pptx` skill
- Save extracted text to a temporary working folder (in `/sessions/*/` — not in the user's vault) so you can read it without cluttering their files

You are writing the notes yourself, not copying extracted text. Extraction is just to let you read the content.

## Phase 4 — Architect

Create the folder skeleton, then build the **Master MOC** — a single file named `🗺️ <Subject> - Master MOC.md` at the top of `00 - MOC/`. This is the entry point a user lands on when they open the vault.

The Master MOC must contain:

- A one-paragraph subject overview
- A **topic map** — sections for each module/topic, each linking (via wikilinks) to the relevant summary and key concept notes
- A **source index** — one bullet per source file, linking to its summary note
- An **exam prep index** — links to the cheat sheet and all Q&A files
- A **key assumptions / common pitfalls** section if the subject has recurring traps

See `references/moc-template.md` for the full template.

## Phase 5 — Summarise

For every source file, produce one summary note in `01 - Summaries/` named after the source (e.g. `Lec 1 - Perfect Competition & Monopoly.md`). Each summary contains:

- YAML frontmatter: `tags`, `source`, `module`, `created`
- A top link back to the Master MOC
- **Key Takeaways** (3–6 bullets, at the top, for fast review)
- **Core Content** (structured by sub-topic, with formulas, diagrams-as-text, intuitions)
- **Worked Examples** if the source contains any
- **Common Pitfalls** drawn from the source
- **Related Notes** — wikilinks to every atomic concept note that originates from this source

The summary is the "expanded view" of a source — detailed enough to revise from without opening the PDF, but not a transcript.

## Phase 6 — Atomise

This is the most important phase and the one that makes the vault valuable. For every distinct idea across all sources, create one small note in `02 - Concepts/`.

**Atomic note rules** (read `references/note-templates.md` for the full template):

- **One concept per note.** A concept is something you could define in a sentence and test on an exam in one question
- Filename = the concept name in natural case (e.g. `Bertrand Paradox.md`, `Dorfman-Steiner Condition.md`)
- Every note follows the structure: **Definition → Intuition → Formula/Key Points → Example → Common Pitfalls → Related Notes**
- Every note has at least 2 outgoing `[[wikilinks]]` to other concept notes and a link back to its source summary
- YAML frontmatter: `tags`, `topic`, `module`, `created`. Use tags like `concept`, `formula`, `exam`, `important`

Before writing each note, ask: "Is this one idea, or am I smuggling several in?" If several, split them.

Aim for ~15–30 atomic notes per typical lecture PDF depending on density.

## Phase 7 — Exam Prep

Create `03 - Exam Prep/` with at minimum:

- **One cheat sheet** — `Exam Cheat Sheet - All <Subject>.md` — a single page with every formula, model, and decision rule in the course, organised by module. No prose, maximum density
- **Q&A files, one per module cluster** — `Exam Q&A - Modules X-Y <Topic>.md` — a sequence of exam-style questions with full step-by-step worked solutions, each answer ending with a ✅ on the final result

Read `references/exam-prep.md` for the exact format and examples.

## Conventions That Apply Everywhere

These are not optional; they are what makes the vault coherent.

### YAML frontmatter
Every note starts with frontmatter. At minimum:

```yaml
---
tags: [type, topic, exam, important]
topic: <Topic Name>
module: <Number or name>
created: <YYYY-MM-DD>
---
```

`type` is one of: `concept`, `formula`, `summary`, `moc`, `exam`, `Q&A`.

### Wikilinks
Always use `[[Exact Note Title]]`. Never use bare text for concept references; every mention of a concept that has its own note should link to that note. This is what produces the knowledge graph — it's the whole point.

### Headings
`# Title` once at the top (may match filename). `##` for section headings. Never skip levels.

### Formulas
Inline with `$...$`, display with `$$...$$`. Always name the variables directly below the formula.

### Tone
Brief, precise, no filler. Study material, not a blog post.

## Why This Structure Works

This structure encodes how expert learners actually study:

- **MOCs** give a mental model of the whole subject
- **Summaries** are the "long form" review layer — what you re-read a week before the exam
- **Atomic notes** are the "flashcard" layer — what you drill
- **Exam prep** is the "night-before" layer — maximum density, maximum recall cues

By linking all four layers together, the user can zoom from any level to any other in one click. That's what a Second Brain is for.

## Tools & Dependencies

### Required companion skills (always use alongside this skill)

This skill produces Obsidian-compatible output, so you **must** invoke the Obsidian marketplace skills whenever they apply — they encode Obsidian-specific syntax and behaviours that this skill relies on. Treat them as part of the toolchain, not optional add-ons.

- **`obsidian:obsidian-markdown`** — **invoke this before writing ANY `.md` note in the vault**. It covers wikilinks `[[...]]`, embeds `![[...]]`, callouts `> [!note]`, frontmatter properties, tags, and block references. Every note in every phase goes through Obsidian Flavored Markdown, so loading this skill's conventions first is non-negotiable.
- **`obsidian:obsidian-cli`** — invoke when you need to read, search, create, or manage notes in an existing vault programmatically (e.g. checking for existing notes before creating duplicates, searching the vault for a concept that may already exist, running vault-wide operations). Use during Phase 1 (Discover) when a vault already exists.
- **`obsidian:obsidian-bases`** — invoke in Phase 4 (Architect) or Phase 7 (Exam Prep) if the user wants table/card views over their notes (e.g. a Base that shows all `#concept` notes in one module as a table). Great for building "all formulas in one view" or "all Q&A by difficulty" overlays.
- **`obsidian:json-canvas`** — invoke if the user wants a visual canvas/mind-map of a topic (e.g. a flowchart of how Cournot → Stackelberg → Bertrand relate). Optional but powerful for concept maps that go beyond linear notes.
- **`obsidian:defuddle`** — invoke when a source is a URL (blog post, online textbook chapter, web article) rather than a local file. Defuddle cleans the page into readable markdown so you can process it like any other source.

**Default invocation pattern for a typical build:**

1. Phase 1 Discover → optionally `obsidian:obsidian-cli` if vault exists
2. Phase 3 Extract → `obsidian:defuddle` for any URL sources; `pdf`/`docx`/`pptx` skills for files
3. Phases 4–7 (every note write) → `obsidian:obsidian-markdown` for syntax; `obsidian:obsidian-bases` if tabular views requested; `obsidian:json-canvas` if visual maps requested

If you skip `obsidian:obsidian-markdown`, you will produce plain Markdown that misses Obsidian's power features. Always load it before the writing phases.

### Python libraries

- `pymupdf` for PDF extraction (`pip install pymupdf --break-system-packages`)
- Optionally `python-docx`, `python-pptx` for Office files

### Bundled

- `scripts/extract_pdf.py` — batch PDF → text extractor

## Detail References

Read the appropriate reference file before starting each phase:

- `references/discovery.md` — Phase 1 procedure and vault detection
- `references/note-templates.md` — YAML frontmatter, atomic note structure, summary structure (read before Phase 5 or 6)
- `references/moc-template.md` — Master MOC template (read before Phase 4)
- `references/exam-prep.md` — Cheat sheet and Q&A format (read before Phase 7)
- `references/extraction.md` — How to extract text from each source format (read before Phase 3)

## Final Deliverable

When done, present the user with:

- A link to the Master MOC (their entry point)
- A brief summary: X source files processed, Y atomic notes, Z exam Q&A
- A suggestion to open the folder in Obsidian to see the graph view

Do not dump the contents of every note into chat — the files are the deliverable.
