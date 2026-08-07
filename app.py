import logging

from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from openai import OpenAI

from config import OPENROUTER_API_KEY, COLLECTION_NAME


# ---------------- Logging ---------------- #

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------- Embedding Model ---------------- #

model = SentenceTransformer("all-MiniLM-L6-v2")

# ---------------- Qdrant ---------------- #

client = QdrantClient(path="./qdrant_db")

# ---------------- OpenRouter ---------------- #

llm = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

print("\n========================================")
print("      PDF RAG Chat Assistant")
print("========================================")

while True:

    question = input("\nAsk a question (or type exit): ")

    if question.lower() == "exit":
        print("\nGoodbye!")
        break

    logging.info(f"Question: {question}")

    try:

        embedding = model.encode(question).tolist()

        results = client.search(
            collection_name=COLLECTION_NAME,
            query_vector=embedding,
            limit=3,
        )

    except Exception as e:

        print(f"\nVector Search Error: {e}")
        continue

    if len(results) == 0 or results[0].score < 0.55:

        print("\nThe information is not available in the supplied documents.")
        continue


    context = ""

    for r in results:

        context += (
            f"\nDocument: {r.payload['document']}"
            f"\nPage: {r.payload['page']}"
            f"\nText: {r.payload['text']}\n"
        )

    prompt = f"""
You are a helpful assistant.

Answer ONLY using the provided context.

Do NOT use any external knowledge.

If the answer is not explicitly present in the context, reply exactly:

"The information is not available in the supplied documents."

Context:
{context}

Question:
{question}

Answer:
"""

    try:
        response = llm.chat.completions.create(
        model="meta-llama/llama-3.3-8b-instruct:free",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0,
        )

        answer = response.choices[0].message.content

    except Exception as e:

        print(f"\nLLM Error: {e}")
        continue

    print("\n========================================")
    print("ANSWER")
    print("========================================")
    print(answer)

    print("\n========================================")
    print("CITATIONS")
    print("========================================")

    for r in results:

        print(f"\nDocument : {r.payload['document']}")
        print(f"Page     : {r.payload['page']}")
        print(f"Retrieved Text:\n{r.payload['text'][:500]}")

    print("\n----------------------------------------")