#!/usr/bin/env python3
"""
Batch-extract text from every PDF in a folder using pymupdf.

Usage:
    python extract_pdf.py --input <source-folder> --output <dest-folder>

The script recursively walks <source-folder>, extracts text from every .pdf,
and writes one .txt per PDF into <dest-folder>, preserving the base filename.

It preserves page breaks with a `\n\n--- Page N ---\n\n` separator so you can
locate which page content came from when writing notes.
"""

import argparse
import sys
from pathlib import Path


def extract_one(pdf_path: Path, out_path: Path) -> tuple[int, int]:
    """Extract text from pdf_path, write to out_path. Return (pages, chars)."""
    import fitz  # pymupdf

    out_path.parent.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(str(pdf_path))
    parts = []
    for i, page in enumerate(doc, start=1):
        parts.append(f"\n\n--- Page {i} ---\n\n")
        parts.append(page.get_text())
    text = "".join(parts)
    out_path.write_text(text, encoding="utf-8")
    return doc.page_count, len(text)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", required=True, help="Folder containing PDFs (searched recursively)")
    ap.add_argument("--output", required=True, help="Folder to write .txt files to")
    args = ap.parse_args()

    src = Path(args.input).expanduser().resolve()
    dst = Path(args.output).expanduser().resolve()

    if not src.is_dir():
        print(f"ERROR: input folder not found: {src}", file=sys.stderr)
        return 1

    try:
        import fitz  # noqa: F401
    except ImportError:
        print(
            "ERROR: pymupdf is not installed. Install with:\n"
            "    pip install pymupdf --break-system-packages",
            file=sys.stderr,
        )
        return 1

    pdfs = sorted(src.rglob("*.pdf")) + sorted(src.rglob("*.PDF"))
    pdfs = sorted(set(pdfs))
    if not pdfs:
        print(f"No PDFs found in {src}")
        return 0

    print(f"Found {len(pdfs)} PDF(s). Extracting to {dst} ...")
    total_pages = 0
    total_chars = 0
    failed = []
    for pdf in pdfs:
        out = dst / (pdf.stem + ".txt")
        try:
            pages, chars = extract_one(pdf, out)
            total_pages += pages
            total_chars += chars
            print(f"  OK  {pdf.name}  ({pages} pages, {chars:,} chars)")
        except Exception as e:  # noqa: BLE001
            failed.append((pdf, e))
            print(f"  FAIL {pdf.name}  ({e})")

    print(
        f"\nDone. {len(pdfs) - len(failed)}/{len(pdfs)} succeeded. "
        f"{total_pages} pages, {total_chars:,} chars total."
    )
    if failed:
        print("Failures:")
        for pdf, err in failed:
            print(f"  - {pdf}: {err}")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
