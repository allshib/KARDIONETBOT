from create_bot import bot, dp
from aiogram import types, Dispatcher
from handlers import config
from handlers.connect import plots, CreateDiag, UseProgramNew
from keyboards.keyb import start_kb


async def starts(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет, для начала обследования введите /st1', reply_markup=start_kb)


async def St1(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет', reply_markup=start_kb)


# начало отрывка из start.py
def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(starts, commands=['start', 'help'])
    dp.register_message_handler(St1, commands=['st'])
# конец отрывка из start.py
