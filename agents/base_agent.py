class BaseAgent:
    def __init__(self, llm_service):
        self.llm_service = llm_service

    def run(self, state: dict):
        raise NotImplementedError("Subclasses must implement run()")