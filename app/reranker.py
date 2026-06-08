from flashrank import Ranker, RerankRequest

ranker = Ranker()


def rerank_results(query, documents):

    passages = []

    for i, doc in enumerate(documents):

        passages.append({
            "id": i,
            "text": doc
        })

    request = RerankRequest(
        query=query,
        passages=passages
    )

    results = ranker.rerank(request)

    return results