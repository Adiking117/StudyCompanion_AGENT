from agent_tools import build_react_agent

if __name__ == "__main__":
    agent = build_react_agent()
    print("🤖 PDF Agent Ready! Ask me things like:")
    # print(" - load_pdf sp.pdf")
    # print(" - summarize_text")
    # print(" - generate_quiz")
    # print(" - answer_question What is the topic of page 3?")
    # print(" - Give me a summary then make a quiz from it")
    
    while True:
        query = input("\nYou: ")
        if query.lower() in ["exit", "quit"]:
            break
        response = agent.invoke({"input":query})
        print("\nAgent:", response['output'])
