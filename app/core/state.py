from app.embeddings.embedder import Embedder
from app.retrieval.bm25 import BM25Retriever
from app.retrieval.vector_store import VectorStore

embedder = Embedder()

bm25 = BM25Retriever()

vector_store = VectorStore()

all_chunks = []
