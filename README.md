# DocuStream

DocuStream is a Streamlit-based multi-document Q&A application that lets you upload PDF files and ask natural-language questions grounded in document content.

Repository: https://github.com/swastiijain24/DocuStream
Maintainer: Swasti Jain

## Overview

DocuStream combines retrieval-augmented generation (RAG) with a clean Streamlit interface:

- PDF parsing with PyPDF2
- Text chunking with LangChain text splitters
- Embedding generation using Google Gemini embeddings
- Local semantic retrieval with FAISS
- Answer generation with Gemini chat models

## Project Structure

```text
.
|-- app/
|   |-- __init__.py
|   |-- config.py
|   |-- pdf_processing.py
|   |-- qa_chain.py
|   |-- vector_store.py
|-- chatapp.py
|-- requirements.txt
|-- img/
|-- docs/
```

## How It Works

1. Upload one or more PDF files from the sidebar.
2. Text is extracted and split into searchable chunks.
3. Chunks are converted to embeddings and stored in a local FAISS index.
4. A similarity search retrieves the most relevant context for each question.
5. Gemini generates a context-grounded answer.

## Features

- Multi-PDF ingestion in one session
- Local vector index creation for fast retrieval
- Context-constrained answering flow
- Modular codebase under `app/` for maintainability
- Streamlit UI for quick local deployment

## Setup

1. Clone the repository:

```bash
git clone https://github.com/swastiijain24/DocuStream.git
cd DocuStream
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file at the project root:

```env
GOOGLE_API_KEY=your_google_api_key
```

4. Run the app:

```bash
streamlit run chatapp.py
```

## Usage

1. Open the app in your browser.
2. Upload one or more PDF documents.
3. Click Process Documents to build the search index.
4. Ask questions in the input box.

## Configuration Notes

- The FAISS index is saved in `faiss_index/` after document processing.
- If no key is found, the app stops and shows a configuration error.

## License

This project is distributed under the MIT License. See LICENSE for details.
