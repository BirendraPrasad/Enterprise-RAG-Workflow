# Enterprise RAG Workflow

## Project Overview

Enterprise RAG Workflow is an enterprise-grade Retrieval-Augmented Generation (RAG) application built using FastAPI, ChromaDB, FlashRank, OpenRouter, and Streamlit. The system enables intelligent document search and question answering by combining semantic retrieval with Large Language Models (LLMs).

Users can upload PDF documents, automatically index them into a vector database, retrieve relevant information using semantic search, rerank results using FlashRank, and generate accurate answers grounded in document content.

---

## Problem Statement

Organizations often store large amounts of information in PDF documents, making it difficult to quickly retrieve relevant information. Traditional keyword-based search systems fail to understand context and semantics.

This project addresses that problem by implementing a Retrieval-Augmented Generation (RAG) system that enables users to upload documents, perform semantic search, and receive accurate answers based on document content.

---

## Key Features

* PDF Upload and Indexing
* Automatic Text Extraction
* Intelligent Document Chunking
* Embedding Generation using Sentence Transformers
* ChromaDB Vector Database
* Semantic Search
* FlashRank Reranking
* OpenRouter LLM Integration
* FastAPI Backend
* Streamlit Chat Interface
* Source Chunk Display
* Query Validation Guardrails
* Document Management (Upload/Delete)
* Admin and User Role-Based Access Control (RBAC)
* Multi-Document Retrieval

---

## System Statistics

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

## Technology Stack

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

### Large Language Model

* OpenRouter

### PDF Processing

* PyMuPDF

---

## RAG Architecture

```text
User Query
      │
      ▼
Streamlit Frontend
      │
      ▼
FastAPI Backend
      │
      ▼
Guardrails Validation
      │
      ▼
ChromaDB Retrieval
      │
      ▼
FlashRank Reranking
      │
      ▼
OpenRouter LLM
      │
      ▼
Answer Generation
      │
      ▼
Source Chunk Display
```

---

## Complete Workflow

### Document Ingestion Pipeline

1. User uploads a PDF document.
2. Text is extracted using PyMuPDF.
3. The document is divided into semantic chunks.
4. Embeddings are generated using Sentence Transformers.
5. Embeddings are stored in ChromaDB.

### Query Processing Pipeline

1. User asks a question.
2. Guardrails validate the query.
3. Relevant chunks are retrieved from ChromaDB.
4. FlashRank reranks retrieved chunks.
5. Top-ranked chunks are sent to the LLM.
6. The LLM generates a grounded answer.
7. The answer and source chunks are displayed.

---

## System Prompt Strategy

The LLM is instructed to:

* Answer only using retrieved document context.
* Avoid hallucinating information.
* Provide concise and accurate responses.
* Use retrieved chunks as supporting evidence.
* Return fallback responses when context is insufficient.

---

## Role-Based Access Control (RBAC)

### Administrator

Administrators can:

* Upload PDF documents
* Delete indexed documents
* Manage the knowledge base
* Ask questions
* View retrieved source chunks

### User

Users can:

* Ask questions from indexed documents
* View generated answers
* View retrieved source chunks

Users cannot:

* Upload documents
* Delete documents
* Modify the knowledge base

---

## Why RAG?

Retrieval-Augmented Generation (RAG) combines information retrieval with language generation.

Benefits include:

* Knowledge can be updated without retraining the model.
* New PDFs can be added instantly.
* Answers are grounded in actual documents.
* Reduced hallucinations.
* Scalable knowledge management.

---

## API Endpoints

### Upload Document

```http
POST /upload
```

### Query Documents

```http
POST /query
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

## Installation Guide

### Clone Repository

```bash
git clone https://github.com/BirendraPrasad/Enterprise-RAG-Workflow.git
```

### Navigate to Project

```bash
cd Enterprise-RAG-Workflow
```

### Create Virtual Environment

```bash
python -m venv rag_env
```

### Activate Environment

#### Windows

```bash
rag_env\Scripts\activate
```

#### Linux / Mac

```bash
source rag_env/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

### Start Backend

```bash
uvicorn main:app --reload
```

Backend URL:

```text
http://localhost:8000
```

Swagger Documentation:

```text
http://localhost:8000/docs
```

### Start Frontend

```bash
streamlit run app.py
```

Frontend URL:

```text
http://localhost:8501
```
---

## Results

* Successfully indexed 35 PDF documents.
* Processed 6893+ pages.
* Generated 2989 semantic chunks.
* Implemented semantic retrieval and reranking.
* Built a complete Enterprise RAG pipeline.
* Added Admin/User Role-Based Access Control.
* Enabled document-grounded question answering.

---

## Future Enhancements

* Multi-user authentication using JWT
* Document-specific filtering
* Hybrid Search (BM25 + Vector Search)
* Conversation Memory
* Analytics Dashboard
* Cloud Deployment
* User Activity Monitoring
* Fine-tuned Domain-Specific Models

---

## Project Structure

```text
Enterprise-RAG-Workflow
│
├── app/
│   ├── chunking.py
│   ├── embeddings.py
│   ├── ingestion.py
│   ├── retrieval.py
│   ├── reranker.py
│   ├── vectordb.py
│   ├── llm.py
│   ├── guardrails.py
│
├── data/
├── vector_db/
│
├── app.py
├── main.py
├── index_documents.py
├── README.md
└── .env
```

---

## Author

**Birendra Prasad**

Enterprise Grade Retrieval-Augmented Generation (RAG) Workflow Project

Built using FastAPI, ChromaDB, FlashRank, OpenRouter, and Streamlit.
