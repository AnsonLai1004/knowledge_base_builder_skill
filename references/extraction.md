# Extraction — Phase 3

The user's sources are in formats you can't read directly. Extract them to plain text in a temporary working folder, then read from there.

## Where to put extracted text

Use a scratch folder inside the current session's working directory — **not** inside the user's vault. Extracted text is a working artefact, not a deliverable.

```
/sessions/<session-id>/extracted/
├── Lec 1.txt
├── Lec 2.txt
└── ...
```

## PDF — `pymupdf`

`pymupdf` (aka `fitz`) is the fastest and cleanest extractor for most academic PDFs. Install:

```bash
pip install pymupdf --break-system-packages
```

Use the bundled `scripts/extract_pdf.py`:

```bash
python scripts/extract_pdf.py --input "<source-folder>" --output "/sessions/<session-id>/extracted"
```

The script walks the input folder for `.pdf` files, extracts page-by-page text, and saves one `.txt` per PDF preserving filenames.

### If pymupdf struggles

Some PDFs (scanned, image-based) won't yield text via pymupdf. Signs:
- Extracted text is empty or gibberish
- Page count high, character count low

For these, fall back to the `pdf` skill (which has OCR options) or tell the user the PDF is image-based and ask if they want OCR.

## DOCX — `python-docx` or the `docx` skill

```python
from docx import Document
doc = Document("<file>.docx")
text = "\n".join(p.text for p in doc.paragraphs)
```

Or invoke the bundled `docx` skill which handles richer structure (tables, headings). For a knowledge base build, plain paragraph text is usually enough.

## PPTX — `python-pptx` or the `pptx` skill

```python
from pptx import Presentation
prs = Presentation("<file>.pptx")
text = []
for slide in prs.slides:
    for shape in slide.shapes:
        if shape.has_text_frame:
            text.append(shape.text_frame.text)
text = "\n---\n".join(text)
```

Use `---` as a slide separator so you can still see where slides break when reading the extracted text.

## Markdown and text — read directly

No extraction needed. Use the `Read` tool.

## URL sources — `obsidian:defuddle`

If a source is a web URL (blog post, online textbook chapter, lecture notes hosted on a university site), **invoke the `obsidian:defuddle` skill** rather than WebFetch. Defuddle strips navigation/ads/boilerplate and produces clean Markdown — which saves tokens and gives you readable content to process like any other source. Save the defuddled output to the `/sessions/<session-id>/extracted/` folder alongside text from PDFs.

## What to do with extracted text

You're **not** copying extracted text into notes. You're reading it to understand the content, then writing notes in your own words.

- Read each extraction fully before writing the summary for it
- Identify distinct concepts — each becomes a candidate for an atomic note
- Note every formula, decision rule, and worked example
- Cross-reference across sources: the same concept might appear in multiple lectures; it gets one atomic note, linked from multiple summaries

## Cleanup

The extraction folder is disposable. Don't clean it up mid-build (you may need to re-read). Once the vault is delivered, the session will clear it automatically.
