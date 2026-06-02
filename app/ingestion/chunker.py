from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.core.config import settings


class Chunker:
    def __init__(self):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP,
        )

    def chunk_document(
        self,
        pages: list[dict],
        filename: str,
    ) -> list[dict]:

        chunks = []

        chunk_counter = 0

        for page in pages:

            page_chunks = self.splitter.split_text(
                page["text"]
            )

            for chunk in page_chunks:

                chunks.append(
                    {
                        "chunk_id": f"{filename}_{chunk_counter}",
                        "filename": filename,
                        "page_number": page["page_number"],
                        "text": chunk,
                    }
                )

                chunk_counter += 1

        return chunks
