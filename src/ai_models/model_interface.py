from abc import ABC, abstractmethod

class ModelInterface(ABC):
    @abstractmethod
    def get_response(self, input: str) -> list:
        pass