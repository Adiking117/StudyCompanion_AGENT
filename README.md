# 📘 PDF Chatbot with LangGraph  

An intelligent PDF Question Answering (QA) system built using **LangGraph**, **LangChain**, and **HuggingFace embeddings**.  
This project allows you to:  

- Ask **questions** directly from a PDF (`qa`)  
- **Summarize** an entire PDF (`summpdf`)  
- Generate a **quiz** from the entire PDF (`quizpdf`)  
- Summarize a **specific topic** from the PDF (`summtopic`)  
- Generate a **topic-specific quiz** (`quiztopic`)  

All powered by a **state-driven graph** that dynamically routes queries based on classification.  

---

## ⚡️ Approach  

### 1. **State Management**  
We define a central `PDFChatState` that holds all intermediate values:  

```python
class PDFChatState(TypedDict):
    pdfpath: str
    pdf: List[Any]
    userQuery: str
    userQueryCategory: Literal["qa", "summpdf", "quizpdf", "summtopic", "quiztopic"]
    extracted_text: str
    splitted_text: List[Any]
    vectordb: Chroma
    similar_pages: List[Any]
    similar_pages_content: str
    answer: str
