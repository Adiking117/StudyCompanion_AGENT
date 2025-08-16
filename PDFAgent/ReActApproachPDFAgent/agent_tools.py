from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from tools.pdf_embedder_tool import embed_pdf
from tools.pdf_loader_tool import load_pdf
from tools.pdf_quesans_tool import answer_question
from tools.pdf_quiz_tool import generate_quiz
from tools.pdf_splitter_tool import split_pdf
from tools.pdf_summarize_tool import summarize_text
from tools.pdf_text_extractor_tool import text_extract

from config import chat_model

def build_react_agent():
    tools = [
        load_pdf,
        split_pdf,
        embed_pdf,
        text_extract,
        answer_question,
        summarize_text,
        generate_quiz
    ]

    prompt = hub.pull("hwchase17/react")
    
    agent = create_react_agent(
        llm=chat_model,
        tools=tools,
        prompt=prompt
    )

    return AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        handle_parsing_errors=True
    )
