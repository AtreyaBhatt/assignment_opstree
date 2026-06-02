from uuid import uuid4


def create_chunk_id() -> str:
    return str(uuid4())
