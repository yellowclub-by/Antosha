from aiogram import types, Router, F

group_router = Router()

ban_words = ["c++", "пупс", "степан"]


@group_router.message(F.text)
async def cleaner(message: types.Message):
    words_lst = message.text.split(" ")
    for word in words_lst:
        if word.lower() in ban_words:
            await message.answer(f"{message.from_user.first_name} Ваше сообщение удалено, соблюдайте правила чата.")
            await message.delete()
