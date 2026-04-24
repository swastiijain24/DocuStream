import os

import google.generativeai as genai
from dotenv import load_dotenv


INDEX_DIR = "faiss_index"
EMBEDDING_MODEL = "models/embedding-001"
CHAT_MODEL = "gemini-pro"


def configure_environment() -> str:
    """Load environment variables and configure Gemini SDK."""
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError("GOOGLE_API_KEY is missing. Add it to your .env file.")

    genai.configure(api_key=api_key)
    return api_key
