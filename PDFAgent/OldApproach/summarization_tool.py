from langchain_core.tools import tool
from config import chat_model
from pdf_manager import pdf_manager

@tool("summarize_text")
def summarize_text(input_text: str) -> str:
    """
    Summarize text or PDF.
    - If pdf is loaded ,summarize from that PDF
    - If input_text is empty, summarize the loaded PDF.
    - If input_text contains content, summarize that.
    """
    prompt = f"Summarize the following content in detail:\n\n{input_text}"
    return chat_model.invoke(prompt).content
