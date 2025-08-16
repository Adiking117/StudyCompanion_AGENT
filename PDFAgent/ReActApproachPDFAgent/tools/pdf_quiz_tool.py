from langchain_core.tools import tool
from config import chat_model

@tool("generate_quiz")
def generate_quiz(full_text: str):
    """
    Generate a 10-question quiz (with answers) from the provided text.

    Args:
        full_text (str): The text content to generate questions from.

    Returns:
        str: A quiz with 10 questions and their corresponding answers.

    Use this tool when you want to test understanding of PDF content 
    by creating practice questions and answers.
    """
    prompt = (
        "Based on the following content, create a quiz of 10 questions "
        "with answers at the end:\n\n"
        f"{full_text}"
    )
    return chat_model.invoke(prompt).content