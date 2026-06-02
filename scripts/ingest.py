from app.services.document_service import DocumentService

service = DocumentService()

chunks = service.process_document(
    "sample_documents/assignment.pdf"
)

print(f"Chunks: {len(chunks)}")

print(chunks[0])
