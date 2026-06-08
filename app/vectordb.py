import chromadb


client = chromadb.PersistentClient(
    path="vector_db"
)


collection = client.get_or_create_collection(
    name="ecommerce_rag"
)


def store_chunks(
    chunks,
    embeddings,
    source_file
):

    ids = []

    metadatas = []

    for i in range(
        len(chunks)
    ):

        ids.append(
            f"{source_file}_{i}"
        )

        metadatas.append(
            {
                "source":
                source_file,

                "chunk_no":
                i
            }
        )

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas
    )


def count_documents():

    return collection.count()