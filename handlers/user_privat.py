from aiogram.filters import CommandStart, Command
from aiogram import types, Router, F

user_router = Router()

@user_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Привет это бот по продаже свежих яиц!!")

@user_router.message(F.text.lower() == 'меню')
@user_router.message(Command('menu'))
async def menu(message: types.Message):
    await message.answer("Вот наше меню")

@user_router.message(F.text.lower() == 'о нас')
@user_router.message(Command('about'))
async def about(message: types.Message):
    await message.answer("Продаем свежие яйца!!")

@user_router.message(F.text.lower() == 'контакты')
@user_router.message(Command('contacts'))
async def contacts(message: types.Message):
    await message.answer("+37592384")

@user_router.message(F.text.lower() == 'филиалы')
@user_router.message(Command('adreses'))
async def adreses(message: types.Message):
    await message.answer("Улица Пушкина Дом Колотушкина")


# @user_router.message(F.text)
# @user_router.message(F.photo)
# @user_router.message(F.text.lower() == 'доставка')
# @user_router.message(F.text.lower().contains('достав'))
# @user_router.message(F.text.lower().startswith('как'))
# @user_router.message(F.text.lower().endswith('?'))
# @user_router.message(F.text.lower().startswith('как'), F.text.lower().endwiths('?'))
# @user_router.message((F.text.lower().contains('стоимост')) | (F.text.lower().contains('цен')))


async def echo(message: types.Message):
    await message.answer("Сработал магический фильтр!!!")


