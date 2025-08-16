from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from summarization_tool import summarize_text
from quiz_tool import generate_quiz
from question_answer_tool import answer_question_tool
from load_pdf_tool import load_pdf
from config import chat_model


def build_react_agent():
    tools = [
        load_pdf,
        summarize_text,
        generate_quiz,
        answer_question_tool
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
