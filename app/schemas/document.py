from pydantic import BaseModel


class DocumentMetadata(BaseModel):
    filename: str
    page_number: int
    chunk_id: str
