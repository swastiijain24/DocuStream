import streamlit as st

from app.config import configure_environment
from app.pdf_processing import extract_pdf_text, split_text
from app.qa_chain import answer_question
from app.vector_store import build_and_save_vector_store, similarity_search


def process_uploaded_docs(pdf_docs) -> None:
    raw_text = extract_pdf_text(pdf_docs)
    if not raw_text.strip():
        raise ValueError("No readable text found in the uploaded PDFs.")

    text_chunks = split_text(raw_text)
    build_and_save_vector_store(text_chunks)


def render_sidebar() -> None:
    with st.sidebar:
        st.write("---")
        st.title("Document Ingestion")
        pdf_docs = st.file_uploader(
            "Upload one or more PDF files, then click Process Documents.",
            accept_multiple_files=True,
            type=["pdf"],
        )
        if st.button("Process Documents"):
            if not pdf_docs:
                st.warning("Please upload at least one PDF before processing.")
            else:
                with st.spinner("Building searchable index..."):
                    process_uploaded_docs(pdf_docs)
                st.session_state["index_ready"] = True
                st.success("Documents indexed successfully.")


def render_main_panel() -> None:
    st.title("DocuStream")
    st.caption("Conversational Q&A across your uploaded PDF collection.")

    user_question = st.text_input("Ask a question about your documents")
    if not user_question:
        return

    if not st.session_state.get("index_ready"):
        st.info("Upload and process documents first.")
        return

    docs = similarity_search(user_question)
    answer = answer_question(user_question, docs)
    st.write("Answer:")
    st.write(answer)


def main():
    st.set_page_config(page_title="DocuStream", page_icon=":books:")
    try:
        configure_environment()
    except RuntimeError as exc:
        st.error(str(exc))
        st.stop()

    st.session_state.setdefault("index_ready", False)
    render_sidebar()
    render_main_panel()

if __name__ == "__main__":
    main()
