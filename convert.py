#!/usr/bin/env python3
"""Convert every PDF in input/ to Markdown in output/."""

from pathlib import Path

from docling.document_converter import DocumentConverter

ROOT = Path(__file__).resolve().parent
INPUT_DIR = ROOT / "input"
OUTPUT_DIR = ROOT / "output"


def main() -> None:
    INPUT_DIR.mkdir(exist_ok=True)
    OUTPUT_DIR.mkdir(exist_ok=True)

    pdfs = sorted(INPUT_DIR.glob("*.pdf"))
    if not pdfs:
        raise SystemExit(f"Tidak ada PDF di {INPUT_DIR}")

    converter = DocumentConverter()
    for pdf in pdfs:
        result = converter.convert(pdf)
        out = OUTPUT_DIR / f"{pdf.stem}.md"
        out.write_text(result.document.export_to_markdown(), encoding="utf-8")
        print(f"{pdf.name} -> {out.name}")


if __name__ == "__main__":
    main()
