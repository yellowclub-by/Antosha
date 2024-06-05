from aiogram import types, Router, F
from aiogram.types import FSInputFile

menu_router = Router()


@menu_router.message(F.text.lower() == 'перепелиные')
async def egg_perepeliniye(message: types.Message):
    photo = FSInputFile('img\menu\Перепелиные.jpg')
    await message.answer_photo(photo, caption='Перепелиные яйца')


@menu_router.message(F.text.lower() == "куриные")
async def egg_kyriniye(message: types.Message):
    photo = FSInputFile('img\menu\Куриные.jpg')
    await message.answer_photo(photo, caption="Куриные яйца")


@menu_router.message(F.text.lower() == "сырые")
async def egg_Ciriye(message: types.Message):
    photo = FSInputFile('img\menu\Сырые.jpeg')
    await message.answer_photo(photo, caption="Сырые яйца")


@menu_router.message(F.text.lower() == "готовые")
async def egg_gotoviye(message: types.Message):
    photo = FSInputFile('img\menu\Готовые.jpg')
    await message.answer_photo(photo, caption="Готовые яйца")
