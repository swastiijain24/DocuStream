from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
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
    return load_qa_chain(model, chain_type="stuff", prompt=prompt)


def answer_question(question: str, docs):
    chain = build_qa_chain()
    response = chain(
        {"input_documents": docs, "question": question},
        return_only_outputs=True,
    )
    return response["output_text"]
