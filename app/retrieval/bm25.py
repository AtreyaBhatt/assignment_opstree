from rank_bm25 import BM25Okapi


class BM25Retriever:
    def __init__(self):
        self.bm25 = None
        self.chunks = []

    def build(self, chunks: list[dict]):
        self.chunks = chunks

        corpus = [
            chunk["text"].lower().split()
            for chunk in chunks
        ]

        self.bm25 = BM25Okapi(corpus)

    def search(
        self,
        query: str,
        top_k: int = 20,
    ) -> list[dict]:

        if self.bm25 is None:
            return []

        tokenized_query = query.lower().split()

        scores = self.bm25.get_scores(
            tokenized_query
        )

        ranked = sorted(
            zip(self.chunks, scores),
            key=lambda x: x[1],
            reverse=True,
        )

        return [
            chunk
            for chunk, _ in ranked[:top_k]
        ]
