# Enterprise RAG Workflow

## Overview

Enterprise Grade Retrieval-Augmented Generation (RAG) Application built using FastAPI, ChromaDB, FlashRank, OpenRouter, and Streamlit for intelligent multi-document search and question answering.

The system allows users to upload PDF documents, automatically index them into a vector database, perform semantic retrieval, rerank results using FlashRank, and generate accurate answers using LLMs.

---

## Features

* PDF Upload and Indexing
* Automatic Text Extraction
* Intelligent Chunking
* Embedding Generation using Sentence Transformers
* ChromaDB Vector Database
* Semantic Search
* FlashRank Reranking
* OpenRouter LLM Integration
* FastAPI Backend
* Streamlit Chat Interface
* Source Chunk Display
* Guardrails for Query Validation
* Document Management (Upload/Delete)

---

## Project Statistics

| Metric          | Value            |
| --------------- | ---------------- |
| Total PDFs      | 35               |
| Total Pages     | 6893+            |
| Total Chunks    | 2989             |
| Vector Database | ChromaDB         |
| Embedding Model | all-MiniLM-L6-v2 |
| Reranker        | FlashRank        |
| Backend         | FastAPI          |
| Frontend        | Streamlit        |

---

## Architecture

User Query

↓

Streamlit Frontend

↓

FastAPI Backend

↓

Query Validation (Guardrails)

↓

ChromaDB Retrieval

↓

FlashRank Reranking

↓

OpenRouter LLM

↓

Answer Generation

↓

Response with Source Chunks

---

## Tech Stack

### Backend

* FastAPI
* Python

### Frontend

* Streamlit

### Vector Database

* ChromaDB

### Embeddings

* Sentence Transformers
* all-MiniLM-L6-v2

### Reranking

* FlashRank

### LLM

* OpenRouter

### PDF Processing

* PyMuPDF

---

## Installation

Clone Repository

```bash
git clone https://github.com/BirendraPrasad/Enterprise-RAG-Workflow.git
```

Create Virtual Environment

```bash
python -m venv rag_env
```

Activate Environment

```bash
rag_env\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run Backend

```bash
uvicorn main:app --reload
```

Run Frontend

```bash
streamlit run app.py
```

---

## API Endpoints

### Query Documents

```http
POST /query
```

### Upload PDF

```http
POST /upload
```

### List Documents

```http
GET /documents
```

### Delete Document

```http
DELETE /documents/{filename}
```

---

## Future Improvements

* Multi-user support
* Document-specific filtering
* Hybrid Search (BM25 + Vector Search)
* Conversation Memory
* Advanced Analytics Dashboard
* Cloud Deployment

---

## Author

Birendra Prasad

Enterprise Grade RAG Workflow Project
