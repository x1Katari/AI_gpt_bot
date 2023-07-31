from aiogram import Bot
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse, JSONResponse
from starlette.staticfiles import StaticFiles
from tortoise.contrib.fastapi import register_tortoise

from ..configuration import config
from ..db.db_utils import set_character, get_character_greetings

app = FastAPI()
app.mount("/static", StaticFiles(directory="src/backend/templates"))
templates = Jinja2Templates(directory="src/backend/templates")


@app.get('/choose-character', response_class=HTMLResponse)
async def choose_character(request: Request):
    print(request.url)
    return templates.TemplateResponse("index.html", {"request": request})


@app.post('/set-character')
async def set_character_endpoint(character_id: int, user_id: int):
    try:
        await set_character(user_id=user_id, character_id=character_id)

        bot = Bot(token=config.bot_token.get_secret_value())

        greetings = await get_character_greetings(character_id)
        await bot.send_message(chat_id=user_id, text=greetings)

        return JSONResponse({"message": "Character set successfully"})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=404)


DATABASE_CONFIG = {
    "connections": {"default": 'postgres://postgres:postgres@ai_db:5432/test'},
    "apps": {
        "models": {
            "models": ["src.db.models", "aerich.models"],
            "default_connection": "default",
        },
    }
}

register_tortoise(
    app,
    config=DATABASE_CONFIG,
)
