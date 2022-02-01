from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

bttn_1 = KeyboardButton('/Записать_на_курс')
bttn_2 = KeyboardButton('/Ближайшая_свободная_дата')
bttn_3 = KeyboardButton('/Тарифы')
bttn_4 = KeyboardButton('/Меню')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(bttn_1).add(bttn_2).row(bttn_3,bttn_4)