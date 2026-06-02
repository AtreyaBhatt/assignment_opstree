from app.llm.gemini import GeminiClient
from app.llm.prompts import HYDE_PROMPT


class HyDEGenerator:
    def __init__(self):
        self.llm = GeminiClient()

    def generate(
        self,
        query: str,
    ) -> str:

        prompt = HYDE_PROMPT.format(
            question=query
        )

        return self.llm.generate(
            prompt
        )
