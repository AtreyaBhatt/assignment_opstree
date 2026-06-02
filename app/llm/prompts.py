HYDE_PROMPT = """
Given the question below, generate a hypothetical document
that would likely contain the answer.

Question:
{question}

Hypothetical Document:
"""


RAG_PROMPT = """
You are a helpful assistant.

Answer ONLY using the provided context.

If the answer cannot be found, say:
"I could not find this information in the uploaded documents."

Context:
{context}

Question:
{question}

Answer:
"""
