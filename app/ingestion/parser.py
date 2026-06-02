from pathlib import Path

import fitz
from docx import Document


class DocumentParser:
    SUPPORTED_EXTENSIONS = {".pdf", ".docx", ".txt"}

    def parse(self, file_path: str) -> list[dict]:
        path = Path(file_path)

        suffix = path.suffix.lower()

        if suffix == ".pdf":
            return self._parse_pdf(path)

        if suffix == ".docx":
            return self._parse_docx(path)

        if suffix == ".txt":
            return self._parse_txt(path)

        raise ValueError(f"Unsupported file type: {suffix}")

    def _parse_pdf(self, path: Path) -> list[dict]:
        doc = fitz.open(path)

        pages = []

        for page_num, page in enumerate(doc):
            pages.append(
                {
                    "text": page.get_text(),
                    "page_number": page_num + 1,
                }
            )

        return pages

    def _parse_docx(self, path: Path) -> list[dict]:
        doc = Document(path)

        text = "\n".join(
            p.text
            for p in doc.paragraphs
            if p.text.strip()
        )

        return [
            {
                "text": text,
                "page_number": 1,
            }
        ]

    def _parse_txt(self, path: Path) -> list[dict]:
        text = path.read_text(encoding="utf-8")

        return [
            {
                "text": text,
                "page_number": 1,
            }
        ]
