import os

from app.ingestion import (
    extract_pdf_text
)

from app.chunking import (
    chunk_text
)

from app.embeddings import (
    generate_embeddings
)

from app.vectordb import (
    store_chunks
)


DATA_FOLDER = "data"


for file in os.listdir(
    DATA_FOLDER
):

    if file.endswith(".pdf"):

        pdf_path = os.path.join(
            DATA_FOLDER,
            file
        )

        print(
            f"\nProcessing: {file}"
        )

        text = extract_pdf_text(
            pdf_path
        )

        if not text:

            print(
                "No text found."
            )

            continue

        chunks = chunk_text(
            text
        )

        embeddings = (
            generate_embeddings(
                chunks
            )
        )

        store_chunks(
            chunks,
            embeddings,
            file
        )

        print(
            f"Stored {len(chunks)} chunks"
        )

print(
    "\nIndexing Completed"
)