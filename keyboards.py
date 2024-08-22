from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Клавиатура для команды /start
start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Привет"), KeyboardButton(text="Пока")]
    ],
    resize_keyboard=True
)

# Клавиатура для команды /links
links_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Новости", url="https://news.yandex.ru")],
    [InlineKeyboardButton(text="Музыка", url="https://music.yandex.ru")],
    [InlineKeyboardButton(text="Видео", url="https://www.rutube.ru")]
])

# Клавиатура для команды /dynamic
dynamic_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Показать больше", callback_data="show_more")]
])

# Клавиатура после "Показать больше"
dynamic_more_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Опция 1", callback_data="option_1")],
    [InlineKeyboardButton(text="Опция 2", callback_data="option_2")]
])
