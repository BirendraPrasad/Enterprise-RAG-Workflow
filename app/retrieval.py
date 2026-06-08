from app.embeddings import model
from app.vectordb import collection


def search_docs(query, n_results=20):

    query_embedding = model.encode(
        [query]
    ).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=n_results
    )

    return results