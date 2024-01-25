from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import types

get_main_menu_markup = ReplyKeyboardMarkup(one_time_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text="Инструкция"),

            ],
            [
                KeyboardButton(text="Календарь"),
                KeyboardButton(text="Напоминание"),

            ],
            [
                KeyboardButton(text="Заметки"),
                KeyboardButton(text="Челлендж"),
            ],
            [
                KeyboardButton(text="План на день!"),
            ],
        ],
        row_width=2,
        resize_keyboard=True,
    )