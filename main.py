from fastapi import FastAPI, UploadFile, File
import shutil

from app.retrieval import search_docs
from app.reranker import rerank_results
from app.guardrails import validate_query
from app.llm import generate_answer

from app.ingestion import extract_pdf_text
from app.chunking import chunk_text
from app.embeddings import generate_embeddings
from app.vectordb import store_chunks

from app.crud import (
    list_documents,
    delete_document
)

app = FastAPI(
    title="Enterprise RAG Assistant"
)


@app.get("/")
def home():

    return {
        "message": "RAG Backend Running"
    }


@app.post("/query")
def query_docs(query: str):

    # Guardrails check
    if not validate_query(query):

        return {
            "status": "blocked",
            "message": "Unsafe query detected"
        }

    # Retrieve documents
    results = search_docs(query)

    docs = results["documents"][0]

    # Rerank documents
    reranked = rerank_results(
        query,
        docs
    )

    # Use Top 5 chunks instead of Top 3
    top_docs = reranked[:10]

    # Build context for LLM
    context = "\n\n".join(
        [
            str(item["text"])
            for item in top_docs
        ]
    )

    # Generate final answer
    answer = generate_answer(
        query,
        context
    )

    return {
        "query": query,
        "answer": answer,
        "sources": [
            {
                "score": float(item["score"]),
                "text": item["text"][:300]
            }
            for item in top_docs
        ]
   }


@app.post("/upload")
async def upload_pdf(
    file: UploadFile = File(...)
):

    file_path = f"data/{file.filename}"

    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    # Extract text
    text = extract_pdf_text(
        file_path
    )

    if not text:

        return {
            "status": "error",
            "message": "No text found in PDF"
        }

    # Create chunks
    chunks = chunk_text(
        text
    )

    # Generate embeddings
    embeddings = generate_embeddings(
        chunks
    )

    # Store in ChromaDB
    store_chunks(
        chunks,
        embeddings,
        file.filename
    )

    return {
        "status": "success",
        "filename": file.filename,
        "chunks_stored": len(chunks)
    }


@app.get("/documents")
def get_documents():

    return {
        "documents": list_documents()
    }


@app.delete("/documents/{filename}")
def remove_document(
    filename: str
):

    success = delete_document(
        filename
    )

    if success:

        return {
            "status": "deleted",
            "filename": filename
        }

    return {
        "status": "not found"
    }