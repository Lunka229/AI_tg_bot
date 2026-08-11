from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "Привет! Я AI Bot \n\n"
        "Напиши мне сообщение."
    )

@router.message()
async def message_handler(message: Message):
    await message.answer(
        f'Вы написали:\n\n{message.text}'
    )