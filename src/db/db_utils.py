from .models import User, Character, Dialog
import aiohttp
import json


async def send_amplitude_event(id, event):
    url = 'https://api2.amplitude.com/2/httpapi'
    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*'
    }
    data = {
        "api_key": "73a37614caeb42834b0a083b84c6bd53",
        "events": [{
            "device_id": f"{id}",
            "event_type": f"{event}"
        }]
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=json.dumps(data), ssl=False) as response:
            if response.status == 200:
                print("Success:", await response.json())
            else:
                print("Error:", await response.text())


async def add_user(user_id: int, username: str, name: str, surname: str):
    user = await User.get_or_none(id=user_id)
    if not user:
        user = await User.create(id=user_id, username=username, name=name, surname=surname)
        await send_amplitude_event(user_id, 'Registration')
    return user


async def set_character(user_id: int, character_id: int) -> None:
    user = await User.get(id=user_id)
    character = await Character.get(id=character_id)
    if user:
        user.current_character = character
        await user.save()
        await send_amplitude_event(user_id, 'Choose_character')
    else:
        raise Exception(f'Пользователь {user_id} отсутствует в базе, но пытается выбрать персонажа')


async def get_current_character(user_id: int):
    user = await User.get_or_none(id=user_id).prefetch_related('current_character')
    if user:
        return user.current_character.id
    else:
        return None


async def get_character_greetings(char_id: int):
    character = await Character.get_or_none(id=char_id)
    if character:
        return character.greetings
    else:
        raise Exception(f'Персонажа с id={char_id} не существует')


async def get_character_settings(char_id: int):
    character = await Character.get_or_none(id=char_id)
    if character:
        return character.settings
    else:
        raise Exception(f'Персонажа с id={char_id} не существует')


async def save_message(user_id, character_id, message, from_user=False):
    dialog = await Dialog.get_or_none(user_id=user_id, character_id=character_id)
    character = await Character.get(id=character_id)
    user = await User.get(id=user_id)
    if not dialog:
        return await Dialog.create(user_id=user, character_id=character, messages=f'@@@{message} &&& ')
    else:
        if from_user:
            dialog.messages += f'@@@{message} &&& '
            await dialog.save()
        else:
            dialog.messages += f'###{message} &&& '
            await dialog.save()


async def get_messages(user_id: int, character_id: int) -> str:
    user = await User.get(id=user_id)
    character = await Character.get(id=character_id)
    dialog = await Dialog.get(user_id=user, character_id=character)
    if dialog:
        return dialog.messages
    else:
        raise Exception(f'Ошибка получения истории сообщений')
