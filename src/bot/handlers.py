from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from src.services.ai_service import get_ai_response


router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "Привет! Я AI Bot \n\n"
        "Напиши мне сообщение."
    )

@router.message()
async def message_handler(message: Message):
    if not message.text:
        return
    
    response = await get_ai_response(message.text)    

    await message.answer(response)