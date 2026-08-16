import ollama

async def generate_response(
        promt:str,
        model:str = "qwen3:4b" 
) -> str:
    response = ollama.chat(
        model=model,
        messages=[
            {
                "role":"user",
                "content":promt
            }
        ]
    )

    return response["message"]["content"]