# 📄 PDF RAG Application using Qdrant & OpenRouter

A Retrieval-Augmented Generation (RAG) application built with Python that answers user questions from PDF documents using semantic search and a Large Language Model (LLM).

## 🚀 Features

- Extracts text from PDF documents
- Generates semantic embeddings using Sentence Transformers
- Stores embeddings in a local Qdrant vector database
- Retrieves the most relevant document chunks
- Uses OpenRouter LLM to generate context-aware answers
- Displays document name and page number as citations
- Responds with:
  > "The information is not available in the supplied documents."
  when the answer is not found in the uploaded PDFs.

---

## 🛠️ Tech Stack

- Python 3.11+
- PyMuPDF
- Sentence Transformers
- Qdrant (Local Vector Database)
- OpenRouter API
- python-dotenv

---

## 📁 Project Structure

```
project/
│
├── data/                  # PDF files
├── qdrant_db/             # Local Qdrant storage
├── utils/
│   └── pdf_loader.py
│
├── app.py                 # Chat application
├── ingest.py              # PDF indexing script
├── config.py              # Configuration
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/pdf-rag.git
cd pdf-rag
```

### 2. Create a virtual environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
OPENROUTER_API_KEY=your_openrouter_api_key
```

---

## 📥 Add PDF Documents

Place all PDF files inside the `data/` folder.

Example:

```
data/
├── document1.pdf
├── document2.pdf
└── notes.pdf
```

---

## 📚 Index the PDFs

Run:

```bash
python ingest.py
```

Expected output:

```
Indexed XXXX pages successfully.
```

---

## 💬 Run the Chat Application

```bash
python app.py
```

Example:

```
Ask a question:

> What is Retrieval-Augmented Generation?
```

Output:

```
ANSWER
--------------------------------

RAG combines document retrieval with an LLM to generate
answers grounded in the supplied documents.

CITATIONS
--------------------------------

Document: AI_Guide.pdf
Page: 12
```

---

## 🧠 How It Works

1. PDFs are loaded from the `data/` folder.
2. Text is extracted using PyMuPDF.
3. Sentence Transformer generates embeddings.
4. Embeddings are stored in Qdrant.
5. User query is embedded.
6. Top matching document chunks are retrieved.
7. Retrieved context is sent to the OpenRouter LLM.
8. The generated answer and citations are displayed.

---

## 📦 Dependencies

```
PyMuPDF
sentence-transformers
qdrant-client
openai
python-dotenv
pydantic
```

---

## 📌 Future Improvements

- Streamlit Web Interface
- Multi-PDF Collections
- Conversation Memory
- Metadata Filtering
- Hybrid Search
- Docker Support
- FastAPI REST API

---

## 👨‍💻 Author

**Shivendra Pratap Singh**

Python Developer | AI & Machine Learning Enthusiast

GitHub: https://github.com/yourusername

LinkedIn: https://linkedin.com/in/yourprofile

---

## 📄 License

This project is developed for educational and learning purposes.