import os

import streamlit as st
from dotenv import load_dotenv


INDEX_DIR = "faiss_index"
EMBEDDING_MODEL = "models/gemini-embedding-001"
CHAT_MODEL = "gemini-3.6-flash"


@st.cache_resource(show_spinner=False)
def configure_environment() -> str:
    """Load env vars and configure Gemini once, cached for the app lifetime."""
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError("GOOGLE_API_KEY is missing")
    return api_key
