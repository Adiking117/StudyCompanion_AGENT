from langchain_core.tools import tool
from config import chat_model

@tool("summarize_text")
def summarize_text(input_text: str):
    """
    Summarize a given text into a concise and detailed summary.

    Args:
        input_text (str): The raw text to summarize (can be extracted from a PDF).

    Returns:
        str: A detailed summary of the input text.

    Use this tool when you need to create a summary of PDF content 
    (e.g., after extracting text from the entire PDF or specific sections).
    """
    
    prompt = f"Summarize the following content in detail:\n\n{input_text}"
    return chat_model.invoke(prompt).content