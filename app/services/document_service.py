from pathlib import Path

from app.embeddings.embedder import (
    Embedder,
)

from app.ingestion.chunker import (
    Chunker,
)

from app.ingestion.parser import (
    DocumentParser,
)

from app.retrieval.bm25 import (
    BM25Retriever,
)

from app.retrieval.vector_store import (
    VectorStore,
)

from app.core.state import (
    embedder,
    vector_store,
    bm25,
)

from app.core.state import (
    all_chunks,
)

class DocumentService:

    def __init__(self):

        self.parser = DocumentParser()

        self.chunker = Chunker()

        self.embedder = embedder
        self.vector_store = vector_store
        self.bm25 = bm25

    def process_document(
        self,
        file_path: str,
    ):

        filename = Path(
            file_path
        ).name

        pages = self.parser.parse(
            file_path
        )

        chunks = (
            self.chunker.chunk_document(
                pages,
                filename,
            )
        )

        embeddings = (
            self.embedder.embed_documents(
                [
                    chunk["text"]
                    for chunk in chunks
                ]
            )
        )

        self.vector_store.create_collection(
            len(embeddings[0])
        )

        self.vector_store.insert(
            chunks,
            embeddings,
        )

        all_chunks.extend(chunks)

        self.bm25.build(all_chunks)

        return chunks
