# DocuStream

DocuStream is a Streamlit app for asking natural-language questions across multiple uploaded PDF documents. It uses Gemini for embeddings and answer generation, plus FAISS for local similarity search.

## What Changed

This project now uses a modular architecture instead of one large script.

- Cleaner separation of concerns for indexing, retrieval, and QA.
- Environment validation on startup.
- Updated UI labels and application identity.

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
2. DocuStream extracts text and splits it into chunks.
3. Chunks are embedded and stored in a local FAISS index.
4. Your question is matched against relevant chunks.
5. Gemini generates an answer from retrieved context only.

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Create a `.env` file at the project root:

```env
GOOGLE_API_KEY=your_google_api_key
```

3. Run the app:

```bash
streamlit run chatapp.py
```

## Notes

- The FAISS index is saved in `faiss_index/` after document processing.
- If no key is found, the app stops and shows a configuration error.

## License

This project is distributed under the MIT License. See LICENSE for details.
