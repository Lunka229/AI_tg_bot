import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

AI_MODEL=os.getenv(
    "AI_MODEL",
    "qwen3:4b"
)

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не найден")