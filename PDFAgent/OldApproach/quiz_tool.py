from langchain_core.tools import tool
from config import chat_model
from pdf_manager import pdf_manager

@tool("generate_quiz")
def generate_quiz(input_text: str) -> str:
    """
    Generate a 10-question quiz from text or PDF.
    Check whether pdf is loaded or not , 
    - If not loaded , load pdf sp.pdf 
    - If pdf is loaded and there is input text given find out what it means from that pdf 
    and then generate quiz from answer retrieved from pdf 
    - 
    """
    prompt = (
        "Based on the following content, create a quiz of 10 questions "
        "with answers at the end:\n\n"
        f"{input_text}"
    )
    return chat_model.invoke(prompt).content
