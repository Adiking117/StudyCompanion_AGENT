from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.tools import tool

@tool("split_pdf")
def split_pdf(docs:list) -> list:
    """
    Split PDF documents into smaller text chunks.

    Args:
        docs (list): A list of LangChain Document objects (usually loaded from a PDF).

    Returns:
        list: A list of smaller Document chunks, ready for embedding or retrieval.

    Use this tool when you need to break long PDF content into smaller chunks 
    so they can be embedded in a vector database or used for retrieval-based Q&A.
    """
    print("Splitting text from PDF")
    splitter = RecursiveCharacterTextSplitter(chunk_size=10, chunk_overlap=2)
    chunks = splitter.split_documents(docs)
    return chunks