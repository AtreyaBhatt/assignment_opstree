# scripts/test_bm25.py

from app.services.document_service import DocumentService
from app.retrieval.bm25 import BM25Retriever

service = DocumentService()

chunks = service.process_document(
    "sample_documents/assignment.pdf"
)

retriever = BM25Retriever()

retriever.build(chunks)

results = retriever.search(
    "multiple"
)

print(results[0]["text"])
