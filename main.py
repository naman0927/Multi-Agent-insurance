import json
from services.llm_services import LLMService
from agents.researcher import ResearcherAgent
from agents.writer import WriterAgent


def main():
    llm_service = LLMService(model_name="llama3")

    researcher = ResearcherAgent(llm_service)
    writer = WriterAgent(llm_service)

    user_query = input("Enter your insurance query: ")
    state = {"user_query": user_query}

    print("\nResearch Agent Working...")
    state = researcher.run(state)

    print("\n=== Research JSON Output ===")
    if isinstance(state["research_data"], dict):
        print(json.dumps(state["research_data"], indent=2))
    else:
        print(state["research_data"])

    print("\nWriter Agent Working...")
    state = writer.run(state)

    print("\n=== Final Insurance Report ===")
    print(state["final_report"])

    with open("final_insurance_report.txt", "w", encoding="utf-8") as f:
        f.write(state["final_report"])

    print("\nReport saved as final_insurance_report.txt")


if __name__ == "__main__":
    main()
