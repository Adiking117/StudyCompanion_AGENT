from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
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

    # Custom ReAct prompt
    custom_prompt = PromptTemplate.from_template("""
    You are a specialized PDF assistant.

    You have access to the following tools:
    {tools}

    Valid tool names you can call: {tool_names}

    Workflows:
    1. For answering a question about PDF content:
    - Call load_pdf → split_pdf → embed_pdf → answer_question
    2. For summarization:
    - Call load_pdf → text_extract → summarize_text
    3. For quiz generation:
    - Call load_pdf → text_extract → generate_quiz

    Rules:
    - Always follow the workflows exactly.
    - Do NOT output code examples.
    - Use ONLY this format:
    Thought: reasoning
    Action: tool name
    Action Input: tool input
    - After observations, end with:
    Final Answer: your final answer

    User question: {input}

    {agent_scratchpad}
    """)

    # ✅ Create ReAct agent with parser
    agent = create_react_agent(
        llm=chat_model,
        tools=tools,
        prompt=custom_prompt,
    )

    return AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        handle_parsing_errors=True  # still good to keep
    )
