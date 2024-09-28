import logging
import sys
from core.config import settings
import asyncio
from aiogram import Dispatcher, Bot
from aiogram.types import Message
from aiogram.filters import Command

bot = Bot(token=settings.bot.token)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Hello world!")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except KeyboardInterrupt: print("Exit")











