from agent_tools import build_react_agent

if __name__ == "__main__":
    agent = build_react_agent()
    print("🤖 PDF Agent Ready! Ask me things like:")
    while True:
        query = input("\nYou: ")
        if query.lower() in ["exit", "quit"]:
            break
        response = agent.invoke({"input":query})
        print("\nAgent:", response['output'])
