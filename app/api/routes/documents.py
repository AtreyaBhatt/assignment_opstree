from pathlib import Path

from fastapi import APIRouter, UploadFile, File

from app.services.document_service import DocumentService

router = APIRouter(
    prefix="/documents",
    tags=["documents"],
)

service = DocumentService()


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...)
):
    uploads_dir = Path("data/uploads")

    uploads_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    file_path = (
        uploads_dir / file.filename
    )

    with open(file_path, "wb") as f:
        f.write(
            await file.read()
        )

    chunks = service.process_document(
        str(file_path)
    )

    return {
        "filename": file.filename,
        "chunks": len(chunks),
    }


@router.get("")
async def list_documents():
    uploads_dir = Path(
        "data/uploads"
    )

    if not uploads_dir.exists():
        return []

    return [
        {
            "filename": f.name
        }
        for f in uploads_dir.iterdir()
        if f.is_file()
    ]
