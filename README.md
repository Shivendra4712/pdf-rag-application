# PDF RAG Application using Qdrant & OpenRouter

A simple Retrieval-Augmented Generation (RAG) application built with Python that answers questions from PDF documents using semantic search and an OpenRouter LLM.

## Architecture

PDFs → Text Extraction (PyMuPDF) → Chunking → Embeddings (BAAI/bge-small-en-v1.5) → Qdrant Vector DB → Semantic Retrieval → OpenRouter LLM → Answer + Citation

## Tech Stack

- Python 3.11+
- PyMuPDF
- Sentence Transformers
- Qdrant (Local)
- OpenRouter API
- python-dotenv

## Embedding Model

**BAAI/bge-small-en-v1.5**

## Assumptions

- PDFs contain selectable text.
- Local Qdrant is used for vector storage.
- Only free OpenRouter models are used.
- Answers are generated only from retrieved document context.

## Installation

Clone the repository:

```bash
git clone https://github.com/Shivendra4712/pdf-rag-application.git
cd pdf-rag-application
```

Create a virtual environment:

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
```

Place all PDF files inside the `data/` folder.

Index the PDFs:

```bash
python ingest.py
```

Run the application:

```bash
python app.py
```

## Example Output

**Question**

```
What is Retrieval-Augmented Generation?
```

**Answer**

```
RAG combines document retrieval with a language model to generate answers grounded in the supplied documents.
```

**Citation**

```
Document: AI_Guide.pdf
Page: 12

Retrieved Text:
"Retrieval-Augmented Generation (RAG) combines retrieval of relevant documents with a language model..."
```

**Unknown Question**

```
Question:
Who won IPL 2025?

Answer:
The information is not available in the supplied documents.
```

## Libraries Used

- PyMuPDF
- sentence-transformers
- qdrant-client
- openai
- python-dotenv

## Author

**Shivendra Pratap Singh**

GitHub: https://github.com/Shivendra4712
## 📄 License

This project is developed for educational and learning purposes.
