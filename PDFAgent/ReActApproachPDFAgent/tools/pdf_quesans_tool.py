from langchain_core.tools import tool
from langchain_community.vectorstores import Chroma
# from pdf_retriever_build import build_retriever
# from config import chat_model
from langchain.retrievers.multi_query import MultiQueryRetriever
from config import chat_model
from langchain_community.vectorstores import Chroma


def build_retriever(vectordb:Chroma):
    """Creates an MMR + MultiQuery to answer asked question retriever."""

    print("⚙ Building advanced retriever...")
    vectordb_retriever = vectordb.as_retriever(search_type="mmr", search_kwargs={"k": 5})

    multiquery_retriever = MultiQueryRetriever.from_llm(retriever=vectordb_retriever, llm=chat_model) 
    
    return multiquery_retriever


@tool("answer_question")
def answer_question(vectordb:Chroma,user_query:str):
    """
    Answer a user question using PDF content stored in a vector database.

    Args:
        vectordb (Chroma): A Chroma vector database containing embedded PDF chunks.
        user_query (str): The question asked by the user.

    Returns:
        str: A natural language answer generated from the most relevant PDF content.

    Use this tool when you want to answer a question directly from the PDF. 
    It uses advanced retrieval (MMR + MultiQuery) to fetch the best matching chunks 
    before generating the answer.
    """
    print("Answering Question from PDF")
    retriever = build_retriever(vectordb)
    docs = retriever.get_relevant_documents(user_query)
    context = "\n\n".join([d.page_content for d in docs])
    question = user_query

    prompt = f"Answer the question using the following context:\n\n{context}\n\nQuestion: {question}"
    return chat_model.invoke(prompt).content
