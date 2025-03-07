
class ModelService:
    model = None
    def __init__(self, modeName: str):
        if modeName.lower() == "ollama":
            from src.ai_models.ollama_model import OllamaModel
            self.model = OllamaModel()
        else:
            raise ValueError("Model not found")
       

    def get_response(self, input: str) -> list:
        return self.model.get_response(input)