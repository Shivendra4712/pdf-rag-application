import logging
import uuid

from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

from utils.pdf_loader import load_pdfs
from config import COLLECTION_NAME


# ---------------- Logging ---------------- #

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------- Embedding Model ---------------- #

model = SentenceTransformer("all-MiniLM-L6-v2")

# ---------------- Qdrant ---------------- #

client = QdrantClient(path="./qdrant_db")

# ---------------- Create Collection ---------------- #

try:

    collections = [c.name for c in client.get_collections().collections]

    if COLLECTION_NAME not in collections:

        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE,
            ),
        )

        logging.info(f"Collection '{COLLECTION_NAME}' created.")

    else:

        logging.info(f"Collection '{COLLECTION_NAME}' already exists.")

except Exception as e:

    print(f"Collection Error : {e}")
    exit()

# ---------------- Load PDFs ---------------- #

try:

    logging.info("Loading PDF files...")

    documents = load_pdfs("data")

    logging.info(f"Loaded {len(documents)} text chunks.")

except Exception as e:

    print(f"PDF Loading Error : {e}")
    exit()

# ---------------- Generate Embeddings ---------------- #

points = []

logging.info("Generating embeddings...")

for doc in documents:

    try:

        embedding = model.encode(doc["text"]).tolist()

        points.append(
            PointStruct(
                id=str(uuid.uuid4()),
                vector=embedding,
                payload={
                    "text": doc["text"],
                    "document": doc["document"],
                    "page": doc["page"],
                },
            )
        )

    except Exception as e:

        logging.warning(
            f"Skipping page {doc['page']} of {doc['document']} : {e}"
        )

# ---------------- Upload ---------------- #

try:

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points,
    )

    logging.info("Upload completed successfully.")

except Exception as e:

    print(f"Upload Error : {e}")
    exit()

print("\n========================================")
print(f"Indexed {len(points)} chunks successfully.")
print("========================================")