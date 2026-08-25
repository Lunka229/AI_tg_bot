from src.config import AI_MODEL
from src.prompts import SYSTEM_PROMPT

import ollama


async def generate_response(prompt: str) -> str:

    try:
        response = ollama.chat(
            model=AI_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            options={
                "num_ctx": 2048,
                #"num_predict": 500,
                "temperature": 0.3
            },
            think=False
        )

        print(f"AI response: {response.message.content!r}")
        #print(response)

        content = response.message.content

        if not content:
            return "Не удалось получить ответ от модели."

        return content

    except Exception as error:
        print(f"Ollama error: {error}")
        return "Произошла ошибка при обращении к AI."