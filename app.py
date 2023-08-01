from aiogram import types
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import ReplyKeyboardRemove
from aiogram import executor
from logging import basicConfig, INFO
import handlers
from loader import db, bot
from data.config import ADMINS
from loader import dp


user_message = 'Пользователь'
admin_message = 'Админ'


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await message.answer('''Привет! 👋

🤖 Я бот-магазин по продаже товаров любой категории.

🛍️ Чтобы перейти в каталог и выбрать приглянувшиеся 
товары, воспользуйтесь командой /menu.

❓ Возникли вопросы? Не проблема! Команда /sos поможет 
связаться с админами, которые постараются как можно быстрее откликнуться.
    ''')



# @dp.message_handler(text=admin_message)
# async def admin_mode(message: types.Message):
#     cid = message.chat.id
#     if cid not in ADMINS:
#         ADMINS.append(cid)
#
#     await message.answer('Включен админский режим.',
#                          reply_markup=ReplyKeyboardRemove())
#
#
# @dp.message_handler(text=user_message)
# async def user_mode(message: types.Message):
#     cid = message.chat.id
#     if cid in ADMINS:
#         ADMINS.remove(cid)
#
#     await message.answer('Включен пользовательский режим.',
#                          reply_markup=ReplyKeyboardRemove())

async def on_startup(dp):
    basicConfig(level=INFO)
    db.create_tables()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=False)
