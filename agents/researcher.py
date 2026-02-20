import json
from agents.base_agent import BaseAgent


class ResearcherAgent(BaseAgent):
    def run(self, state: dict):
        user_query = state.get("user_query", "")

        prompt = f"""
You are an insurance research expert.

Analyze the following query and extract:

- insurance_type
- available_policy_types
- network_hospitals
- claim_process
- claim_rejection_reasons
- exclusions
- comparison_points

Return ONLY valid JSON.
No explanation, no markdown, no extra text.
Just a pure JSON object.

Query:
{user_query}
"""

        research_data = self.llm_service.generate(prompt)

        # Safely parse JSON
        try:
            state["research_data"] = json.loads(research_data)
        except Exception:
            state["research_data"] = research_data

        return state
