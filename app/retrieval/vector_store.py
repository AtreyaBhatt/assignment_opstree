from pymilvus import MilvusClient

from app.core.config import settings


class VectorStore:
    def __init__(self):
        self.client = MilvusClient(
            uri=settings.MILVUS_URI
        )

        self.collection_name = (
            settings.MILVUS_COLLECTION
        )

    def create_collection(
        self,
        dimension: int,
    ):
        collections = (
            self.client.list_collections()
        )

        if self.collection_name in collections:
            self.client.load_collection(
                collection_name=self.collection_name
            )
            return

        self.client.create_collection(
            collection_name=self.collection_name,
            dimension=dimension,
        )

        self.client.load_collection(
            collection_name=self.collection_name
        )

    def load_collection(self):
        self.client.load_collection(
            collection_name=self.collection_name
        )

    def insert(
        self,
        chunks: list[dict],
        embeddings: list[list[float]],
    ):
        data = []

        for idx, (
            chunk,
            embedding,
        ) in enumerate(
            zip(chunks, embeddings)
        ):
            data.append(
                {
                    "id": idx,
                    "vector": embedding,
                    "text": chunk["text"],
                    "filename": chunk["filename"],
                    "page_number": chunk[
                        "page_number"
                    ],
                    "chunk_id": chunk[
                        "chunk_id"
                    ],
                }
            )

        self.client.insert(
            collection_name=self.collection_name,
            data=data,
        )

    def search(
        self,
        query_embedding: list[float],
        top_k: int = 20,
    ):
        self.load_collection()

        results = self.client.search(
            collection_name=self.collection_name,
            data=[query_embedding],
            limit=top_k,
            output_fields=[
                "text",
                "filename",
                "page_number",
                "chunk_id",
            ],
        )

        chunks = []

        for hit in results[0]:

            entity = hit.get(
                "entity",
                hit,
            )

            chunks.append(
                {
                    "chunk_id": entity.get(
                        "chunk_id",
                        str(hit["id"]),
                    ),
                    "text": entity["text"],
                    "filename": entity[
                        "filename"
                    ],
                    "page_number": entity[
                        "page_number"
                    ],
                }
            )

        return chunks
