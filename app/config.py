import os

import google.generativeai as genai
from dotenv import load_dotenv


INDEX_DIR = "faiss_index"
EMBEDDING_MODEL = "models/text-embedding-004"
CHAT_MODEL = "gemini-1.5-flash"


def configure_environment() -> str:
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError("GOOGLE_API_KEY is missing")

    genai.configure(api_key=api_key)
    return api_key
