from langchain_core.tools import tool

@tool("text_extract")
def text_extract(docs:list) -> str:
    """
    Extract raw text from PDF documents.

    Args:
        docs (list): A list of LangChain Document objects.

    Returns:
        str: The concatenated full text of the entire PDF.

    Use this tool when you need the full plain text of the PDF 
    without chunking or embeddings (e.g., for summarization or quiz generation).
    """
    full_text = "\n".join([doc.page_content for doc in docs])
    return full_text