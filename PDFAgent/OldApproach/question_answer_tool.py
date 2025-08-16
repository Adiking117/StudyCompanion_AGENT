from langchain_core.tools import tool
from config import chat_model
from pdf_manager import pdf_manager

@tool("answer_question")
def answer_question_tool(input_text: str) -> str:
    """
    Answer a question based on input text from the loaded PDF.
    - always ask input_text to be retrieved from PDF.
    """
    retriever = pdf_manager.get_retriever()
    docs = retriever.get_relevant_documents(input_text)
    context = "\n\n".join([d.page_content for d in docs])
    question = input_text

    prompt = f"Answer the question using the following context:\n\n{context}\n\nQuestion: {question}"
    return chat_model.invoke(prompt).content
