from aiogram import Router, F, types
from aiogram.filters import Command

from utils.keyboards import get_web_app_markup

from db.db_utils import get_current_character, add_user

menu_router = Router(name="menu")


@menu_router.message(Command(commands="menu"))
async def menu(message: types.Message):
    user = await add_user(message.from_user.id, message.from_user.username, message.from_user.first_name,
                   message.from_user.last_name)
    if not user.current_character:
        return await message.answer(
            'Привет, друг!\nЧтобы пообщаться с ботом, выбери персонажа по кнопке ниже',
            reply_markup=get_web_app_markup())
    else:
        return await message.answer(
            'Привет, друг!\nЧтобы поменять себоседника – жми на кнопку 😉',
            reply_markup=get_web_app_markup())
