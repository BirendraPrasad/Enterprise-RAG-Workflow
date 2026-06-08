from app.retrieval import search_docs
from app.reranker import rerank_results
from app.llm import generate_answer

query = "What is intrusion detection system?"

results = search_docs(query)

docs = results["documents"][0]

reranked = rerank_results(
    query,
    docs
)

context = ""

for item in reranked[:3]:

    context += (
        item["text"] + "\n\n"
    )

answer = generate_answer(
    query,
    context
)

print(answer)