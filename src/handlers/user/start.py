from aiogram import Router, types
from aiogram.filters import CommandStart

from db.db_utils import add_user
from utils.keyboards import get_web_app_markup

start_router = Router(name="start")


@start_router.message(CommandStart())
async def start(message: types.Message):
    await add_user(message.from_user.id, message.from_user.username, message.from_user.first_name,
                   message.from_user.last_name)
    
    return await message.answer(
        'Привет, друг!\nЯ универсальный искусственный интеллект и могу быть как Марио, так и Альбертом Эйнштейном, выбери с кем ты хочешь поговорить, по кнопке ниже',
        reply_markup=get_web_app_markup())

    
