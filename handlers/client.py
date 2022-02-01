from aiogram import Dispatcher, types
from create_bot import dp as dp
from keyboards import client_kb


#@dp.message_handler(commands=['start', 'help'])
async def commands_start(message : types.Message):
    await message.answer('Вот что я умею:', reply_markup = client_kb.kb_client)

#@dp.message_handler(commands=['Записать_на_курс'])
async def marmedasha_add_course_command(message : types.Message):
    await message.answer('Форма записи на курс')

#@dp.message_handler(commands=['Ближайшая_свободная_дата'])
async def marmedasha_date_command(message : types.Message):
    await message.answer('Ближайшая свободная дата: 03/0/2022' )

#@dp.message_handler(commands=['Тарифы'])
async def marmedasha_rates_command(message : types.Message):
    await message.answer('Вывод тарифных планов')

#dp.message_handler(command=['Меню'])
#async def marmedasha_menu_command(message : types.Message):
#    for ret in cur.execute('SELECT * FROM menu').fetchall():
#        await bot.send_photo(message.from_user.id, ret[0], f'{ret')

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(marmedasha_add_course_command, commands=['Записать_на_курс'])
    dp.register_message_handler(marmedasha_date_command, commands=['Ближайшая_свободная_дата'])
    dp.register_message_handler(marmedasha_rates_command, commands=['Тарифы'])