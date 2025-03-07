from fastapi import APIRouter
from ...services.model_service import ModelService
router = APIRouter(
    prefix="/model",
    tags=["ai model"],
)

modelService = ModelService("ollama")

@router.post("/ask")
async def ask(question:dict) -> list:
    print(question['prompt'])
    return modelService.get_response(question['prompt'])