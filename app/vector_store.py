from langchain.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from app.config import EMBEDDING_MODEL, INDEX_DIR


def _embeddings():
    return GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL)


def build_and_save_vector_store(text_chunks) -> None:
    store = FAISS.from_texts(text_chunks, embedding=_embeddings())
    store.save_local(INDEX_DIR)


def load_vector_store():
    return FAISS.load_local(
        INDEX_DIR,
        _embeddings(),
        allow_dangerous_deserialization=True,
    )


def similarity_search(question: str):
    store = load_vector_store()
    return store.similarity_search(question)
