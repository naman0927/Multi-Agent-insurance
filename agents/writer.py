import json
from agents.base_agent import BaseAgent


class WriterAgent(BaseAgent):
    def run(self, state: dict):
        research_data = state.get("research_data", "")

        # Convert dict JSON to string if needed
        if isinstance(research_data, dict):
            research_data = json.dumps(research_data, indent=2)

        prompt = f"""
You are a professional insurance advisor.

Using the research data below, create a clear and structured
insurance comparison report.

Include:

1. Policy types explanation
2. Hospital network info
3. Claim process
4. Claim rejection reasons
5. Exclusions explanation
6. Policy comparison

Write professionally in paragraphs.

Research Data:
{research_data}
"""

        final_report = self.llm_service.generate(prompt)
        state["final_report"] = final_report

        return state
