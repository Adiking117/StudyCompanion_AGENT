from langchain_community.vectorstores import Chroma
from config import embedding_model, PERSIST_DIR, CHROMA_COLLECTION_NAME
import os
from langchain_core.tools import tool


@tool("embed_pdf")
def embed_pdf(chunks:list)->Chroma:
    """
    Create or load a vector database for PDF content.

    Args:
        chunks (list): A list of document chunks obtained after splitting the PDF.

    Returns:
        Chroma: A Chroma vector database containing embeddings of the chunks.

    Use this tool when you want to store or search PDF content in vector form 
    for semantic search, question answering, or retrieval.
    """
    print("Embedding pdf")
    if os.path.exists(PERSIST_DIR) and os.listdir(PERSIST_DIR):
        print("Vector DB Exist, using that")
        vectordb = Chroma(
            persist_directory=PERSIST_DIR,
            embedding_function=embedding_model,
            collection_name=CHROMA_COLLECTION_NAME
        )
    else:
        print("Vector DB does not exist, creating one")
        vectordb = Chroma.from_documents(
            chunks,
            embedding_model,
            persist_directory=PERSIST_DIR,
            collection_name=CHROMA_COLLECTION_NAME
        )
        vectordb.persist()

    return vectordb
