import os
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

os.environ['HF_HOME'] = 'C:/Users/Aditya/Desktop/Langchain/Langchain_Models/LOCALINSTALLEDMODELS'

chat_model=ChatGroq(model="llama3-8b-8192")

# Embeddings
embedding_model = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

# Vector DB settings
PERSIST_DIR = "./chroma_persist"
CHROMA_COLLECTION_NAME = "pdf_docs"

# Default PDF path (can change via load_pdf tool)
