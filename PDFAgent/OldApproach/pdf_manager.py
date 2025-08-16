from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain.retrievers.document_compressors import EmbeddingsFilter
from config import embedding_model, chat_model, PDF_PATH, PERSIST_DIR, CHROMA_COLLECTION_NAME
import os

from pdf_agent.retriever_tool import build_retriever

class PDFManager:
    def __init__(self):
        self.full_text = None
        self.retriever = None
        self.vectordb = None
        self.loaded = False
        self.PDF_PATH = PDF_PATH

    def load_pdf(self):
        """Load, split, embed, and store retriever (only once per file)."""
        if self.loaded:
            return

        if not os.path.exists(self.PDF_PATH):
            raise FileNotFoundError(f"PDF file '{self.PDF_PATH}' not found.")

        loader = PyPDFLoader(self.PDF_PATH)
        docs = loader.load()
        self.full_text = "\n".join([doc.page_content for doc in docs])

        if os.path.exists(PERSIST_DIR) and os.listdir(PERSIST_DIR):
            self.vectordb = Chroma(
                persist_directory=PERSIST_DIR,
                embedding_function=embedding_model,
                collection_name=CHROMA_COLLECTION_NAME
            )
        else:
            splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            chunks = splitter.split_documents(docs)
            self.vectordb = Chroma.from_documents(
                chunks,
                embedding_model,
                persist_directory=PERSIST_DIR,
                collection_name=CHROMA_COLLECTION_NAME
            )
            self.vectordb.persist()

        self.retriever = build_retriever(self.vectordb)

        self.loaded = True

    def get_full_text(self):
        if not self.loaded:
            self.load_pdf()
        return self.full_text

    def get_retriever(self):
        if not self.loaded:
            self.load_pdf()
        return self.retriever

# Singleton instance
pdf_manager = PDFManager()
