from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from app.config import CHAT_MODEL


PROMPT_TEMPLATE = """
Answer the question as thoroughly as possible using only the provided context.
If the answer cannot be found in the context, say:
"answer is not available in the context"

Context:
{context}

Question:
{question}

Answer:
"""


def build_qa_chain():
    model = ChatGoogleGenerativeAI(model=CHAT_MODEL, temperature=0.3)
    prompt = PromptTemplate(
        template=PROMPT_TEMPLATE,
        input_variables=["context", "question"],
    )
    return prompt | model | StrOutputParser()


def answer_question(question: str, docs):
    chain = build_qa_chain()
    context = "\n\n".join(
        doc.page_content if hasattr(doc, "page_content") else str(doc)
        for doc in docs
    )
    return chain.invoke({"context": context, "question": question})
