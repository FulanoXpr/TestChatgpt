# RAG System Template

This repository contains starter templates for building a Retrieval-Augmented Generation (RAG) system in Python.

## Key Files

- `data_loader.py`: Loads documents from a directory.
- `embedding_model.py`: Generates embeddings for text.
- `index_builder.py`: Builds a FAISS vector index.
- `vector_store.py`: Handles queries to the vector index.
- `retriever.py`: Retrieves relevant documents for a query.
- `generator.py`: Uses OpenAI GPT to generate answers.
- `rag_pipeline.py`: Orchestrates the full RAG workflow.
- `config.py`: Stores configuration.
- `utils.py`: Utility functions.

## Setup

1. Install dependencies:
    ```bash
    pip install sentence-transformers faiss-cpu openai
    ```
2. Set your OpenAI API key in `config.py`.
3. Place your `.txt` documents in the `data/` directory.

## Usage

Run the pipeline:
```python
from rag_pipeline import rag_pipeline
from embedding_model import EmbeddingModel
from data_loader import load_documents
from index_builder import build_index
from vector_store import VectorStore
from config import DATA_DIR, MODEL_NAME, OPENAI_KEY, TOP_K

docs = load_documents(DATA_DIR)
embedding_model = EmbeddingModel(MODEL_NAME)
embeddings = embedding_model.encode(docs)
index = build_index(embeddings)
vector_store = VectorStore(index)

query = "Your question here"
answer = rag_pipeline(query, DATA_DIR, embedding_model, vector_store, docs, OPENAI_KEY)
print(answer)
```