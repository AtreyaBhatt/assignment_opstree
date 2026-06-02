from app.llm.gemini import GeminiClient
from app.llm.prompts import RAG_PROMPT

from app.retrieval.hybrid import HybridRetriever


class ChatService:
    def __init__(self):
        self.retriever = HybridRetriever()
        self.llm = GeminiClient()

    def ask(self, question: str):

        chunks = self.retriever.retrieve(
            query=question
        )

        if not chunks:
            return {
                "answer": (
                    "I could not find relevant "
                    "information in the uploaded "
                    "documents."
                ),
                "sources": [],
            }

        context = "\n\n".join(
            chunk["text"]
            for chunk in chunks
        )

        prompt = RAG_PROMPT.format(
            context=context,
            question=question,
        )

        answer = self.llm.generate(prompt)

        sources = []
        seen = set()

        for chunk in chunks:

            key = (
                chunk["filename"],
                chunk["page_number"],
            )

            if key not in seen:

                seen.add(key)

                sources.append(
                    {
                        "filename": chunk["filename"],
                        "page_number": chunk["page_number"],
                    }
                )

        return {
            "answer": answer,
            "sources": sources,
        }
