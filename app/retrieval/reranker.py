from sentence_transformers import CrossEncoder

from app.core.config import settings


class Reranker:
    def __init__(self):
        self.model = CrossEncoder(
            settings.RERANKER_MODEL
        )

    def rerank(
        self,
        query: str,
        chunks: list[dict],
        top_k: int = 5,
    ) -> list[dict]:

        pairs = [
            (query, chunk["text"])
            for chunk in chunks
        ]

        scores = self.model.predict(
            pairs
        )

        ranked = sorted(
            zip(chunks, scores),
            key=lambda x: x[1],
            reverse=True,
        )

        return [
            chunk
            for chunk, _ in ranked[:top_k]
        ]
