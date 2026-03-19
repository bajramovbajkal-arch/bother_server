import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message,
from aiogram.filters import CommandStart, Command

import os
from dotenv import load_dotenv
load_dotenv()
#aadilbek
pp = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='_Kanallar_')],
        [KeyboardButton(text='_Botlar_')]
    ],
    resize_keyboard=True
)

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    print('bot ishladi')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
