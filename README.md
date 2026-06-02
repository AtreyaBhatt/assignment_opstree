# RAG Assistant

A Retrieval-Augmented Generation (RAG) system that enables users to upload documents and interact with them using natural language questions.

The system combines Hybrid Retrieval (BM25 + Dense Vector Search), HyDE query expansion, Reciprocal Rank Fusion (RRF), and Cross-Encoder Reranking to provide accurate, context-aware answers grounded in uploaded documents.

---

## Features

### Document Management

* Upload PDF, DOCX, and TXT documents
* View uploaded documents
* Automatic document parsing and chunking
* Metadata tracking (filename, page number, chunk ID)

### Intelligent Question Answering

* Natural language querying
* Hybrid retrieval:

  * BM25 sparse retrieval
  * Dense vector retrieval
* HyDE (Hypothetical Document Embeddings)
* Reciprocal Rank Fusion (RRF)
* Cross-Encoder reranking
* Source citations
* Gemini-powered answer generation

---

## Architecture

### Ingestion Pipeline

```text
Upload Document
        │
        ▼
Document Parsing
(PDF / DOCX / TXT)
        │
        ▼
Chunking
        │
        ▼
Chunks + Metadata
        │
        ├──────────────► BM25 Index
        │
        ▼
Embedding Model
        │
        ▼
Milvus Vector Store
```

### Query Pipeline

```text
User Question
        │
        ▼
HyDE Generation
        │
        ▼
Dense Query Embedding
        │
        ├──────────────► BM25 Retrieval
        │
        └──────────────► Vector Search
                               │
                               ▼
                    Reciprocal Rank Fusion
                               │
                               ▼
                        Cross-Encoder
                          Reranker
                               │
                               ▼
                       Context Builder
                               │
                               ▼
                          Gemini
                               │
                               ▼
                    Answer + Citations
```

---

## Technology Stack

### Backend

* FastAPI
* Pydantic

### Retrieval

* BM25 (`rank-bm25`)
* Milvus Lite
* Sentence Transformers

### Embeddings

* BAAI/bge-small-en-v1.5

### Reranking

* BAAI/bge-reranker-base

### LLM

* Gemini 2.5 Flash

### Document Processing

* PyMuPDF
* python-docx

---

## Project Structure

```text
rag-assistant/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── ingestion/
│   ├── embeddings/
│   ├── retrieval/
│   ├── llm/
│   ├── services/
│   └── schemas/
│
├── data/
│   ├── uploads/
│   └── processed/
│
├── sample_documents/
│
├── scripts/
│
├── tests/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Setup

### Clone Repository

```bash
git clone <repository-url>
cd rag-assistant
```

### Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

## Running Locally

```bash
uvicorn app.main:app --reload
```

API documentation:

```text
http://localhost:8000/docs
```

---

## Docker

Build:

```bash
docker compose build
```

Run:

```bash
docker compose up
```

API:

```text
http://localhost:8000
```

Swagger:

```text
http://localhost:8000/docs
```

---

## API Endpoints

### Upload Document

```http
POST /documents/upload
```

Form Data:

```text
file=<document>
```

Supported formats:

* PDF
* DOCX
* TXT

---

### List Documents

```http
GET /documents
```

---

### Ask Questions

```http
POST /chat
```

Request:

```json
{
  "question": "What are the responsibilities of a data science intern?"
}
```

Response:

```json
{
  "answer": "...",
  "sources": [
    {
      "filename": "internship_policy.pdf",
      "page_number": 2
    }
  ]
}
```

---

## Retrieval Strategy

The system uses a multi-stage retrieval pipeline:

### 1. HyDE

Generates a hypothetical answer document from the user query to improve semantic retrieval.

### 2. Sparse Retrieval

BM25 lexical search captures exact keyword matches.

### 3. Dense Retrieval

Semantic similarity search using vector embeddings stored in Milvus.

### 4. Reciprocal Rank Fusion

Combines sparse and dense retrieval results.

### 5. Reranking

Cross-Encoder reranker selects the most relevant chunks before generation.

---

## Assumptions

* Documents are primarily English language.
* Uploaded documents fit within available local storage.
* Milvus Lite is sufficient for assignment-scale datasets.
* Documents are uploaded before querying.
* Gemini API key is available through environment variables.

---

## Future Improvements

* Streaming responses
* Persistent BM25 index
* Authentication and user management
* OCR support for scanned PDFs
* Evaluation framework (RAGAS / DeepEval)
* Observability and tracing
* Multi-user document collections

---

## Example Workflow

1. Upload one or more documents.
2. Documents are parsed and chunked.
3. Chunks are indexed in BM25 and Milvus.
4. User submits a question.
5. Hybrid retrieval fetches relevant chunks.
6. Gemini generates a grounded answer.
7. System returns answer with source citations.

```
```
