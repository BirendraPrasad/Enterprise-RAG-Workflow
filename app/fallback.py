def fallback_answer(query, docs):

    answer = docs[0][:1000]

    return f"""
Top Retrieved Context:

{answer}
"""