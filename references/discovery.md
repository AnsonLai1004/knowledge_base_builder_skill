# Discovery — Phase 1

Before touching anything, understand what the user has.

## Step 1: Confirm the target folder

The user will usually point to a folder like "my Industrial Organisation course folder" or give a path. Confirm the path with `ls` (via Bash) so you know exactly what's there. If the path is ambiguous, ask once — then proceed.

## Step 2: Recursively list every source

```bash
find "<target-folder>" -type f \( -iname "*.pdf" -o -iname "*.docx" -o -iname "*.pptx" -o -iname "*.md" -o -iname "*.txt" \) | sort
```

Record this list. Every item on it will become at least one summary note.

## Step 3: Detect an existing Obsidian vault

Look for a `.obsidian/` directory at the target or any ancestor:

```bash
# From target folder, walk up until we hit one or reach root
dir="<target-folder>"
while [ "$dir" != "/" ]; do
  if [ -d "$dir/.obsidian" ]; then echo "VAULT: $dir"; break; fi
  dir=$(dirname "$dir")
done
```

**If a vault exists**: work inside it. Respect any existing folder conventions (if they already have `Notes/` or `Concepts/`, use those names). Don't duplicate what's there.

> 🔗 When a vault already exists, invoke the **`obsidian:obsidian-cli`** skill. It lets you search existing notes, check for name collisions before creating new atomic notes, and respect the vault's existing tag taxonomy. Skipping this step risks creating duplicate notes under slightly different names (e.g. `Bertrand Paradox.md` vs `bertrand-paradox.md`), which fragments the knowledge graph.

**If no vault exists**: treat the target folder itself as the new vault root and build the skeleton inside it. You don't need to create a `.obsidian/` directory — Obsidian generates it on first open.

## Step 4: Infer topical structure

Look at the filenames. Common patterns:

- `Lec 1 - X.pdf`, `Lec 2 - Y.pdf` → lecture-based course; use "Lecture" / "Module" numbering
- `Week 1.pdf`, `Week 2.pdf` → weekly structure
- `Chapter 1.pdf`, `Chapter 2.pdf` → book/reader
- Unnumbered topical names → infer topic clusters by content after extraction

Use whatever numbering the source uses. Don't renumber.

## Step 5: Report to the user

Before proceeding to Phase 2, tell the user:

- The vault root you detected or will create
- How many source files, broken down by type
- The structure you inferred (e.g. "9 lecture PDFs numbered 1–9")

This prevents you from charging ahead with the wrong target.

## Common surprises

- **Duplicates across folders** — a user may have the same PDFs in two places (e.g. Downloads + a course folder). Prefer the course folder; note the duplication
- **Non-source files mixed in** — the folder may also contain old notes, assignment submissions, solutions. Flag them but don't process them as sources unless the user asks
- **Protected/encrypted PDFs** — `pymupdf` will complain. Skip and report; the user can decrypt and retry
