from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Меню'),
            KeyboardButton(text='О нас')
        ],
        [
            KeyboardButton(text='Контакты'),
            KeyboardButton(text='Филиалы')

        ]

    ],
    resize_keyboard=True,
    input_field_placeholder='Категории'

)


back_btn = KeyboardButton(text='Назад')

menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Перепелиные'),
            KeyboardButton(text='Куриные')
        ],
        [KeyboardButton(text='Сырые'),
        KeyboardButton(text='Готовые')
         ],
        [back_btn

        ]

    ],
    resize_keyboard=True,
)
kontackts_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Продаем яйца'),
            KeyboardButton(text='+33783488')
        ],
        [KeyboardButton(text='Находимся улица пушкина дом колотушкина'),
        KeyboardButton(text='Степа Пупс')
         ]


    ],
    resize_keyboard=True,
)