from langchain_community.document_loaders import PyPDFLoader
# from config import PDF_PATH
import os
from langchain_core.tools import tool


@tool("load_pdf")
def load_pdf(file_path: str) -> list:
    """
    Load a PDF file from the given file path.

    Args:
        file_path (str): Path to the PDF file.

    Returns:
        list: A list of LangChain Document objects, each representing one page of the PDF.

    Use this tool when you need to load a PDF into memory for further processing 
    such as splitting, embedding, text extraction, summarization, or question answering.
    """
    print(f"Loading PDF at {file_path}")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"PDF file '{file_path}' not found.")

    loader = PyPDFLoader(file_path)
    docs = loader.load()
    return docs


