from pathlib import Path
from pypdf import PdfReader


def chunk_text(text, chunk_size=300, overlap=50):
    words = text.split()
    chunks = []

    step = chunk_size - overlap

    for i in range(0, len(words), step):
        chunk = " ".join(words[i:i + chunk_size])
        if chunk.strip():
            chunks.append(chunk)

    return chunks


def load_pdfs(folder="data"):
    documents = []

    pdf_files = Path(folder).glob("*.pdf")

    for pdf in pdf_files:

        print(f"Loading {pdf.name}")

        reader = PdfReader(pdf)

        for page_num, page in enumerate(reader.pages, start=1):

            text = page.extract_text()

            if not text:
                continue

            for chunk in chunk_text(text):

                documents.append(
                    {
                        "text": chunk,
                        "document": pdf.name,
                        "page": page_num,
                    }
                )

    return documents