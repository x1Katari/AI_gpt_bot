from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo


def get_web_app_markup():
    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Выбрать персонажа', web_app=WebAppInfo(
url=f'https://amadeusx.ru/choose-character'))]])
