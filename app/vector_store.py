import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from app.config import EMBEDDING_MODEL, INDEX_DIR, configure_environment


@st.cache_resource(show_spinner=False)
def _embeddings():
    """Create the embedding model once and reuse across all calls."""
    api_key = configure_environment()
    return GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL,
        google_api_key=api_key,
    )


def build_and_save_vector_store(text_chunks) -> None:
    store = FAISS.from_texts(text_chunks, embedding=_embeddings())
    store.save_local(INDEX_DIR)
    # Clear the cached store so the next search loads the fresh index
    _load_vector_store.clear()


@st.cache_resource(show_spinner=False)
def _load_vector_store():
    """Load FAISS index from disk once and keep it in memory."""
    return FAISS.load_local(
        INDEX_DIR,
        _embeddings(),
        allow_dangerous_deserialization=True,
    )


def similarity_search(question: str):
    store = _load_vector_store()
    return store.similarity_search(question)
