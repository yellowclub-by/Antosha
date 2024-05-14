from aiogram.filters import CommandStart, Command
from aiogram import types, Router

user_router = Router()



@user_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Привет это бот по продаже свежих яиц!!")

@user_router.message(Command('menu'))
async def menu(message: types.Message):
    await message.answer("Вот наше меню")

@user_router.message(Command('about'))
async def about(message: types.Message):
    await message.answer("Продаем свежие яйца!!")

@user_router.message(Command('contacts'))
async def contacts(message: types.Message):
    await message.answer("+37592384")

@user_router.message(Command('adreses'))
async def adreses(message: types.Message):
    await message.answer("Улица Пушкина Дом Колотушкина")









@user_router.message()
async def echo(message: types.Message):
    # await message.answer("Бот находится в разработке.")
    user_text = message.text
    await message.answer(user_text)

