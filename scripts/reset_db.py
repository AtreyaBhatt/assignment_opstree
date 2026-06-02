from app.core.state import (
    all_chunks,
    bm25,
)

all_chunks.clear()

bm25.bm25 = None
bm25.chunks = []

print("Reset complete")
