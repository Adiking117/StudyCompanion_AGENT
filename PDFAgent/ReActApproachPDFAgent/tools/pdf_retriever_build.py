from langchain.retrievers.multi_query import MultiQueryRetriever
from config import chat_model
from langchain_community.vectorstores import Chroma


def build_retriever(vectordb:Chroma):
    """Creates an MMR + MultiQuery to answer asked question retriever."""

    print("⚙ Building advanced retriever...")
    vectordb_retriever = vectordb.as_retriever(search_type="mmr", search_kwargs={"k": 5})

    multiquery_retriever = MultiQueryRetriever.from_llm(retriever=vectordb_retriever, llm=chat_model) 
    
    return multiquery_retriever