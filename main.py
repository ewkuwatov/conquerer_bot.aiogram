from aiogram import Bot, Dispatcher, executor, types, exceptions
import asyncio
from datetime import datetime, timedelta
from buttons.buttons import *

bot = Bot('6361087801:AAEAcbdzfe6A1FKtVBDTWKRT6ZIfdQLrTBM')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Hello conqueror', reply_markup=get_main_menu_markup)






# async def reminder(delay, user_id, message_text):
#     await asyncio.sleep(delay)
#     await bot.send_message(user_id, message_text)


# @dp.message_handler(commands=['set_reminder'])
# async def set_reminder(message: types.Message):
#     try:
#         # Разбиваем команду на части
#         command_parts = message.text.split()
#         time_str = command_parts[1]  # Время в формате "час:минута"
#         user_id = message.from_user.id
#         message_text = " ".join(command_parts[2:])
#
#         # Преобразуем строку времени в объект datetime
#         time_obj = datetime.strptime(time_str, "%H:%M")
#
#         # Вычисляем задержку до указанного времени
#         now = datetime.now()
#         target_time = datetime(now.year, now.month, now.day, time_obj.hour, time_obj.minute)
#         if now > target_time:
#             target_time += timedelta(days=1)  # Если указанное время уже прошло, добавляем 1 день
#
#         delay = (target_time - now).total_seconds()
#
#         # Создаем задачу напоминания
#         asyncio.create_task(reminder(delay, user_id, message_text))
#
#         # Отправляем ответ пользователю и ждем 3 секунды
#         reply_message = await message.reply(f'Напоминание установлено на {time_str}. Пожалуйста, подождите...')
#         await asyncio.sleep(3)
#
#         # Удаляем ответ бота
#         await bot.delete_message(chat_id=reply_message.chat.id, message_id=reply_message.message_id)
#     except (IndexError, ValueError):
#         await message.reply('Используйте команду /set_reminder <час:минута> <текст напоминания>')


if __name__ == '__main__':
    from aiogram import executor
    # loop = asyncio.get_event_loop()
    # loop.create_task(on_startup(dp))
    executor.start_polling(dp, skip_updates=True)

