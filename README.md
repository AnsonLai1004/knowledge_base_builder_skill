# knowledge-base-builder

A Claude skill that turns a folder of raw source materials (PDFs, slides, lecture notes, textbooks, readings) into a complete, linked, Obsidian-compatible **Second Brain** optimised for study, review, and exam preparation.

## What it does

Given a folder of course or study materials, this skill produces:

- **Atomic concept notes** — one idea per note, following a `Definition → Intuition → Formula → Example → Common Pitfalls → Related Notes` structure
- **Source summaries** — one detailed summary per source document with key takeaways, worked examples, and links to every atomic note derived from it
- **A Master MOC** (Map of Content) — a navigation hub linking every summary, concept, and exam artefact
- **Exam prep** — a dense cheat sheet plus worked Q&A for each module

Everything is plain Markdown with YAML frontmatter and `[[wikilinks]]`, so it opens natively in Obsidian.

## How to install

Copy the `knowledge-base-builder/` folder into your Claude skills directory:

```bash
cp -r knowledge-base-builder ~/.claude/skills/
```

Once installed, trigger the skill with prompts like:

- "Build a knowledge base from this folder"
- "Turn these lecture PDFs into study notes"
- "Set up an Obsidian vault from my course materials"
- "Create a Second Brain for <subject>"
- "Organise these readings into atomic notes"

## What's inside

```
knowledge-base-builder/
├── SKILL.md                    # Main skill instructions (triggering + 7-phase workflow)
├── references/
│   ├── discovery.md            # Phase 1: folder scan + vault detection
│   ├── extraction.md           # Phase 3: PDF/DOCX/PPTX/URL extraction
│   ├── moc-template.md         # Phase 4: Master MOC template
│   ├── note-templates.md       # Phase 5-6: atomic + summary note templates
│   └── exam-prep.md            # Phase 7: cheat sheet + Q&A format
└── scripts/
    └── extract_pdf.py          # Batch PDF -> text extractor (pymupdf)
```

## Workflow

The skill runs through seven phases:

1. **Discover** — scan the folder, identify sources, detect any existing vault
2. **Plan** — propose the vault structure and confirm scope
3. **Extract** — pull text from every source (PDFs, docx, pptx, URLs)
4. **Architect** — build the folder skeleton and Master MOC
5. **Summarise** — one detailed summary per source file
6. **Atomise** — one note per distinct concept across all sources
7. **Exam Prep** — cheat sheet plus worked Q&A per module

## Companion skills

This skill pairs with the Obsidian marketplace skills and uses them automatically:

- `obsidian:obsidian-markdown` — wikilinks, callouts, frontmatter syntax
- `obsidian:obsidian-cli` — vault search and deduplication when a vault exists
- `obsidian:obsidian-bases` — tabular / card views over `#concept` notes
- `obsidian:json-canvas` — visual concept maps
- `obsidian:defuddle` — clean extraction for URL sources

## Dependencies

- Python 3 with `pymupdf` (`pip install pymupdf --break-system-packages`)
- Optional: `python-docx`, `python-pptx` for Office files

## License

MIT
