from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain.retrievers.document_compressors import EmbeddingsFilter
from config import embedding_model,chat_model

def build_retriever(vectordb):
    """Creates an MMR + MultiQuery + Contextual Compression retriever."""
    print("⚙ Building advanced retriever...")
    base_retriever = vectordb.as_retriever(search_type="mmr", search_kwargs={"k": 5})

    multiquery = MultiQueryRetriever.from_llm(retriever=base_retriever, llm=chat_model) 
    embeddings_filter = EmbeddingsFilter(embeddings=embedding_model, similarity_threshold=0.76)

    retriever = ContextualCompressionRetriever(
        base_compressor=embeddings_filter,
        base_retriever=multiquery
    )
    return retriever
