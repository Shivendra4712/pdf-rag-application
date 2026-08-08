# PDF RAG Application

A simple Retrieval-Augmented Generation (RAG) application built with Python that answers questions using only the supplied PDF documents.

## Architecture

```text
PDF Documents
     ↓
PyMuPDF → Text Chunking
     ↓
Sentence Transformer
(all-MiniLM-L6-v2)
     ↓
Qdrant Vector Database
     ↓
Semantic Retrieval (Top 5)
     ↓
OpenRouter Free LLM
     ↓
Answer + Citation
```

## Libraries & Technologies

- Python 3.11+
- PyMuPDF — PDF text extraction
- Sentence Transformers — document/query embeddings
- Qdrant — vector database
- OpenRouter — free LLM inference
- python-dotenv — environment variables

## Embedding Model

```text
all-MiniLM-L6-v2
```

The model generates 384-dimensional embeddings used for semantic similarity search.

## Project Structure

```text
pdf-rag-application/
│
├── data/
├── utils/
│   └── pdf_loader.py
├── app.py
├── ingest.py
├── config.py
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run

### 1. Clone Repository

```bash
git clone https://github.com/Shivendra4712/pdf-rag-application.git
cd pdf-rag-application
```

### 2. Create Virtual Environment

**Windows**

```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure OpenRouter

Create a `.env` file in the project root:

```text
OPENROUTER_API_KEY=your_openrouter_api_key
```

### 5. Add Documents

Place the supplied PDF documents inside:

```text
data/
```

### 6. Index Documents

```bash
python ingest.py
```

### 7. Run Application

```bash
python app.py
```

The application retrieves the top 5 relevant chunks and generates an answer using only the retrieved PDF context.

## Citations

Every generated answer displays:

```text
Document
Page
Similarity
Retrieved Text
```

Example:

```text
Document: document.pdf
Page: 17
Similarity: 0.78

Retrieved Text:
"Relevant text retrieved from the document..."
```

## Unknown Questions

If the requested information is not present in the supplied documents, the application returns:

```text
The information is not available in the supplied documents.
```

The LLM is instructed not to use external knowledge or fabricate answers.

## Assumptions

- PDFs contain selectable text.
- Qdrant is used locally for vector storage.
- `all-MiniLM-L6-v2` is used for embeddings.
- The top 5 relevant chunks are passed to the LLM.
- Only retrieved PDF context is used for answer generation.

## Author

**Shivendra Pratap Singh**

GitHub: https://github.com/Shivendra4712
