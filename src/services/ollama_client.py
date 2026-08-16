import ollama
from src.config import AI_MODEL

async def generate_response(
        promt:str,
        model:str = "qwen3:4b" 
) -> str:
    response = ollama.chat(
        model=AI_MODEL,
        messages=[
            {
                "role":"user",
                "content":promt
            }
        ]
    )

    return response["message"]["content"]