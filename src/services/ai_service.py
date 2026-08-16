from src.services.ollama_client import generate_response

async def get_ai_response(message: str) -> str:
    response = await generate_response(message)
    return response