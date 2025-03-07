import ollama
from os import environ as env
from src.ai_models.model_interface import ModelInterface

class OllamaModel(ModelInterface):
    desiredModel = env['OLLAMA_MODEL']
    ollama_api_url = env['OLLAMA_API_URL']
    oClient = ollama.Client(host=ollama_api_url)
    
    def get_response(self, input: str) -> list:
        res = self.oClient.chat(model=self.desiredModel, messages=[
        {"role": "user", "content": input}
        ])
        
        return res