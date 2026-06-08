from app.retrieval import search_docs

results = search_docs(
    "How do I charge Galaxy Watch 5 Pro?",
    n_results=10
)

for i, doc in enumerate(results["documents"][0]):
    print("\n" + "=" * 50)
    print(f"RESULT {i+1}")
    print(doc[:1000])