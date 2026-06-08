from app.retrieval import search_docs
from app.reranker import rerank_results

query = "What is intrusion detection system?"

results = search_docs(query)

docs = results["documents"][0]

reranked = rerank_results(
    query,
    docs
)

for item in reranked[:3]:

    print("\nScore:", item["score"])
    print(item["text"][:300])