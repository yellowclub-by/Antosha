import asyncio
from aiogram import Bot, Dispatcher, types


TOKEN = "7024143256:AAGV9L3F6nUCu6L4MWTILS7dWQuzElRB9Tk"
bot = Bot(token=TOKEN)
dp = Dispatcher()

from handlers.user_privat import user_router
from handlers.user_group import group_router
from handlers.menu import menu_router
dp.include_router(user_router)
dp.include_router(menu_router)
dp.include_router(group_router)






async def main():
    print("Бот запущен")
    await dp.start_polling(bot)




asyncio.run(main())
