import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message,ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart, Command

import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TOKEN")

bot= Bot(token=TOKEN)
dp= Dispatcher()

@dp.message(CommandStart())
async def g(a:Message):
    await a.answer('salam')
@dp.message(Command('adil'))
async def g(a:Message):
    await a.answer('xaw')

async def main():
    print('bot ishladi')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
