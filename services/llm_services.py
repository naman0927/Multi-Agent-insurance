from langchain_ollama import ChatOllama

class LLMService:
    def __init__(self, model_name="llama3"):
        self.llm = ChatOllama(
            model=model_name,
            temperature=0.7
        )

    def generate(self, prompt: str):
        response = self.llm.invoke(prompt)
        return response.content