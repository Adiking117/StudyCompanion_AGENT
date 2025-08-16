from langchain_core.tools import tool
from pdf_manager import pdf_manager
import os
from config import PDF_PATH

@tool("load_pdf")
def load_pdf(file_path: str) -> str:
    """
    Load a PDF into memory for all future operations.
    - If pdf is already loaded dont do it again
    - If not just pass the file name or full path 
    """
    if not os.path.exists(file_path):
        return f"⚠ File '{file_path}' not found."

    pdf_manager.full_text = None
    pdf_manager.loaded = False
    pdf_manager.PDF_PATH = file_path
    pdf_manager.load_pdf()

    return f"✅ PDF '{file_path}' loaded successfully."
