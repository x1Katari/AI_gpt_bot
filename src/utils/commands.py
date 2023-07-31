from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Команда для запуска бота'
        ),
        BotCommand(
            command='menu',
            description='Команда для смены персонажа'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
