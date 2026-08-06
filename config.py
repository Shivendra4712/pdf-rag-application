import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenRouter API Key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Collection name for Qdrant Local
COLLECTION_NAME = "pdf_rag"
