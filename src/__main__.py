import asyncio
import logging

from aiogram import Bot, Dispatcher
from tortoise import Tortoise

from configuration import config
from handlers import setup_routers
from utils.commands import set_commands


DATABASE_CONFIG = {
    "connections": {"default": 'postgres://postgres:postgres@ai_db:5432/test'},
    "apps": {
        "models": {
            "models": ["db.models", "aerich.models"],
            "default_connection": "default",
        },
    }
}



async def main():
    await Tortoise.init(config=DATABASE_CONFIG)

    bot = Bot(config.bot_token.get_secret_value(), parse_mode="HTML")
    await set_commands(bot)
    dp = Dispatcher()

    dp.include_router(setup_routers())

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types(), skip_updates=True)


if __name__ == "__main__":
    logging.basicConfig(level=config.logging_level)
    asyncio.run(main())
