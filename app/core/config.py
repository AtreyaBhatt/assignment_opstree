from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "RAG Assistant"

    GEMINI_API_KEY: str

    EMBEDDING_MODEL: str = "BAAI/bge-small-en-v1.5"
    RERANKER_MODEL: str = "BAAI/bge-reranker-base"

    MILVUS_URI: str = "./data/milvus.db"
    MILVUS_COLLECTION: str = "documents"

    CHUNK_SIZE: int = 800
    CHUNK_OVERLAP: int = 150

    TOP_K_DENSE: int = 20
    TOP_K_SPARSE: int = 20
    TOP_K_RERANK: int = 5

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()
