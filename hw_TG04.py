import logging
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from config import TOKEN
from keyboards import start_keyboard, links_keyboard, dynamic_keyboard, dynamic_more_keyboard

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
router = Router()
dp = Dispatcher()


# Команда /start
@router.message(Command('start'))
async def send_welcome(message: Message):
    await message.answer("Добро пожаловать! Выберите действие:", reply_markup=start_keyboard)


# Команда /help
@router.message(Command('help'))
async def send_help(message: Message):
    help_text = (
        "Команды бота:\n"
        "/start - Показать меню с кнопками 'Привет' и 'Пока'.\n"
        "/links - Показать кнопки с URL-ссылками.\n"
        "/dynamic - Показать динамическую клавиатуру.\n"
        "/help - Показать это сообщение помощи."
    )
    await message.answer(help_text)


# Обработка кнопки "Привет"
@router.message(lambda message: message.text == "Привет")
async def greet_user(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}!")


# Обработка кнопки "Пока"
@router.message(lambda message: message.text == "Пока")
async def farewell_user(message: Message):
    await message.answer(f"До свидания, {message.from_user.first_name}!")


# Команда /links
@router.message(Command('links'))
async def send_links(message: Message):
    await message.answer("Выберите ссылку:", reply_markup=links_keyboard)


# Команда /dynamic
@router.message(Command('dynamic'))
async def send_dynamic_keyboard(message: Message):
    await message.answer("Нажмите кнопку ниже:", reply_markup=dynamic_keyboard)


# Обработка нажатий на инлайн-кнопки
@router.callback_query(lambda callback: True)
async def process_callback_button(callback_query: CallbackQuery):
    if callback_query.data == "show_more":
        await bot.edit_message_text(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            text="Выберите опцию:",
            reply_markup=dynamic_more_keyboard
        )
    elif callback_query.data == "option_1":
        await callback_query.answer("Выбор опции 1")
        await bot.send_message(callback_query.from_user.id, "Вы выбрали Опцию 1")
    elif callback_query.data == "option_2":
        await callback_query.answer("Выбор опции 2")
        await bot.send_message(callback_query.from_user.id, "Вы выбрали Опцию 2")


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
