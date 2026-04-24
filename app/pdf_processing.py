from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter


def extract_pdf_text(pdf_docs) -> str:
    """Extract text from one or more uploaded PDFs."""
    text = ""
    for pdf in pdf_docs:
        reader = PdfReader(pdf)
        for page in reader.pages:
            page_text = page.extract_text() or ""
            text += page_text
    return text


def split_text(text: str):
    splitter = RecursiveCharacterTextSplitter(chunk_size=50000, chunk_overlap=1000)
    return splitter.split_text(text)
