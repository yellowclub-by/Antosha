import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

TOKEN = "7024143256:AAGV9L3F6nUCu6L4MWTILS7dWQuzElRB9Tk"
bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Привет это бот по продаже свежих яиц!!")


@dp.message()
async def echo(message: types.Message):
    # await message.answer("Бот находится в разработке.")
    user_text = message.text
    await message.answer(user_text)


async def main():
    print("Бот запущен")
    await dp.start_polling(bot)


asyncio.run(main())
