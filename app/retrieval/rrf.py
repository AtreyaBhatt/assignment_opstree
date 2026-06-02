class ReciprocalRankFusion:
    def __init__(self, k: int = 60):
        self.k = k

    def fuse(
        self,
        dense_results: list[dict],
        sparse_results: list[dict],
    ) -> list[dict]:

        scores = {}

        for rank, doc in enumerate(
            dense_results,
            start=1,
        ):
            scores.setdefault(
                doc["chunk_id"],
                {
                    "score": 0.0,
                    "doc": doc,
                },
            )

            scores[doc["chunk_id"]]["score"] += (
                1 / (self.k + rank)
            )

        for rank, doc in enumerate(
            sparse_results,
            start=1,
        ):
            scores.setdefault(
                doc["chunk_id"],
                {
                    "score": 0.0,
                    "doc": doc,
                },
            )

            scores[doc["chunk_id"]]["score"] += (
                1 / (self.k + rank)
            )

        ranked = sorted(
            scores.values(),
            key=lambda x: x["score"],
            reverse=True,
        )

        return [
            item["doc"]
            for item in ranked
        ]
