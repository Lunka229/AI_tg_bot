import ollama

async def get_ai_response(message: str) -> str:
    response = ollama.chat(
        model = "qwen3:4b",
        messages =[
            {
                "role":"user",
                "content":message
            }
        ]
    )
    return response["message"]["content"]