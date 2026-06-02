from app.embeddings.embedder import Embedder
from app.retrieval.bm25 import BM25Retriever
from app.retrieval.hyde import HyDEGenerator
from app.retrieval.rrf import ReciprocalRankFusion
from app.retrieval.reranker import Reranker
from app.retrieval.vector_store import VectorStore
from app.core.state import (
    embedder,
    bm25,
    vector_store,
)


class HybridRetriever:
    def __init__(self):
        self.embedder = embedder

        self.bm25 = bm25

        self.vector_store = vector_store

        self.hyde = HyDEGenerator()

        self.rrf = ReciprocalRankFusion()

        self.reranker = Reranker()

    def retrieve(
        self,
        query: str,
    ):

        sparse_results = self.bm25.search(
            query
        )

        hypothetical_doc = (
            self.hyde.generate(query)
        )

        query_embedding = (
            self.embedder.embed_query(
                hypothetical_doc
            )
        )

        dense_results = (
            self.vector_store.search(
                query_embedding
            )
        )

        fused = self.rrf.fuse(
            dense_results,
            sparse_results,
        )

        print(
            f"BM25={len(sparse_results)} "
            f"Dense={len(dense_results)} "
            f"Fused={len(fused)}"
        )

        reranked = (
            self.reranker.rerank(
                query,
                fused,
            )
        )

        print(
            f"Final={len(reranked)}"
        )

        return reranked
