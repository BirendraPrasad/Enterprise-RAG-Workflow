from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


def generate_answer(query, context):

    prompt = f"""
You are a helpful E-Commerce RAG Assistant.

Use ONLY the provided context to answer the question.

Rules:
- Base your answer only on the context.
- The context may contain headings, table of contents entries, and partial sentences.
- Infer the answer if the information is clearly indicated in the context.
- Do not invent facts not present in the context.
- Keep answers concise and helpful.
- If the answer truly cannot be found, reply exactly:
"I could not find relevant information in the documents."

Context:
{context}

Question:
{query}

Answer:
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=300
    )

    return response.choices[0].message.content.strip()