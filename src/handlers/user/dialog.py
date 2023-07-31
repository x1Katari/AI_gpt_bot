import openai
from aiogram import Router, types, Bot

from db.db_utils import get_current_character, get_messages, get_character_settings, save_message, send_amplitude_event, add_user
from utils.keyboards import get_web_app_markup
from configuration import config
from aiogram.utils.chat_action import ChatActionSender

dialog_router = Router(name="dialog")


async def send_msg_to_gpt(data):
    openai.api_key = config.gpt_token.get_secret_value()
    model = 'gpt-3.5-turbo'
    response = openai.ChatCompletion.create(model=model, messages=data)
    return response.choices[0].message.content


async def create_msg_to_gpt(user_id, character_id, new_msg):
    data = [{'role': 'system',
             'content': await get_character_settings(character_id)}]

    messages = await get_messages(user_id, character_id)
    messages = messages.split(' &&& ')
    for msg in messages:
        if msg.strip().startswith('@@@'):
            data.append({
                'role': 'user',
                'content': msg.strip()[3:]
            })
        if msg.strip().startswith('###'):
            data.append({
                'role': 'assistant',
                'content': msg.strip()[3:]
            })
    data.append({
        'role': 'user',
        'content': new_msg
    })
    return data


@dialog_router.message()
async def dialog(message: types.Message, bot: Bot):
    async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
        user_id = message.from_user.id
        await send_amplitude_event(user_id, 'Send_request')
        
        user = await add_user(message.from_user.id, message.from_user.username, message.from_user.first_name,
                              message.from_user.last_name)
        if not user.current_character:
            return await message.answer(
                'Привет, друг!\nЧтобы пообщаться с ботом, выбери персонажа по кнопке ниже',
                reply_markup=get_web_app_markup())
        else:
            current_character = await get_current_character(user_id)
            await save_message(user_id, current_character, message.text, from_user=True)
    
            data = await create_msg_to_gpt(user_id, current_character, message.text)
            answer = await send_msg_to_gpt(data)
            await send_amplitude_event(user_id, 'Get_answer')
            await save_message(user_id, current_character, answer, from_user=False)
    
            await message.answer(text=answer)
            return await send_amplitude_event(user_id, 'Send_answer')
