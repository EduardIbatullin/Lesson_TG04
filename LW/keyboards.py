from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Тестовая кнопка 1")],
    [KeyboardButton(text="Тестовая кнопка 2"), KeyboardButton(text="Тестовая кнопка 3")],
], resize_keyboard=True)


# ikb = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="Видео", url="https://rutube.ru/video/25b608e2bd9fdd37dfabbfda6be1943f/")]
# ])


ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Каталог", callback_data="catalog")],
    [InlineKeyboardButton(text="Новости", callback_data="news")],
    [InlineKeyboardButton(text="Профиль", callback_data="profile")],
])



test = ["Тестовая кнопка 1", "Тестовая кнопка 2", "Тестовая кнопка 3", "Тестовая кнопка 4"]


# async def test_kb():
#     kb = ReplyKeyboardBuilder()
#     for key in test:
#         kb.add(KeyboardButton(text=key))
#     return kb.adjust(2).as_markup(resize_keyboard=True)


async def test_kb():
    kb = InlineKeyboardBuilder()
    for key in test:
        kb.add(InlineKeyboardButton(text=key, url="https://rutube.ru/video/25b608e2bd9fdd37dfabbfda6be1943f/"))
    return kb.adjust(2).as_markup(resize_keyboard=True)


