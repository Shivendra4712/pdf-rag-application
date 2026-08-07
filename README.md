# PDF RAG Application using Qdrant & OpenRouter

A simple Retrieval-Augmented Generation (RAG) application built with Python that answers questions from PDF documents using semantic search and an OpenRouter Large Language Model (LLM).

## Architecture

PDF Documents → PyMuPDF → Text Chunking → Embeddings (all-MiniLM-L6-v2) → Qdrant Vector Database → Semantic Retrieval → OpenRouter LLM → Answer with Citations

## Tech Stack

- Python 3.11+
- PyMuPDF
- Sentence Transformers
- Qdrant (Local Vector Database)
- OpenRouter API
- python-dotenv

## Embedding Model

**all-MiniLM-L6-v2**

## Assumptions

- PDFs contain selectable text.
- Local Qdrant is used for vector storage.
- Only free OpenRouter models are used.
- Answers are generated only from the retrieved document context.
- If the requested information is not present in the supplied PDFs, the application returns that the information is unavailable.

## Installation

### Clone the Repository

```bash
git clone https://github.com/Shivendra4712/pdf-rag-application.git
cd pdf-rag-application
```

### Create a Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create a `.env` File

```env
OPENROUTER_API_KEY=your_openrouter_api_key
```

## Usage

Place all PDF documents inside the `data/` folder.

Index the PDFs:

```bash
python ingest.py
```

Run the application:

```bash
python app.py
```

## Example

**Question**

```text
What is Retrieval-Augmented Generation?
```

**Answer**

```text
RAG combines document retrieval with a language model to generate answers grounded in the supplied documents.
```

**Citation**

```text
Document: AI_Guide.pdf
Page: 12

Retrieved Text:
"Retrieval-Augmented Generation (RAG) combines retrieval of relevant documents with a language model..."
```

**Unknown Question**

```text
Question:
Who won IPL 2025?

Answer:
The information is not available in the supplied documents.
```

## Project Structure

```text
project/
│
├── data/
├── utils/
│   └── pdf_loader.py
├── app.py
├── ingest.py
├── config.py
├── requirements.txt
└── README.md
```

## Author

**Shivendra Pratap Singh**

GitHub: https://github.com/Shivendra4712

LinkedIn: https://linkedin.com/in/shivendra-pratap-singh-85258b314
