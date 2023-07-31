from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.BigIntField(pk=True, index=True)  # id в телеграме
    username = fields.CharField(max_length=32, null=True)  # username в телеграме
    name = fields.CharField(max_length=32, null=True)  # Имя в телеграме
    surname = fields.CharField(max_length=32, null=True)  # Фамилия в телеграме
    create_date = fields.DatetimeField(auto_now_add=True)  # первое использование бота
    update_date = fields.DatetimeField(auto_now=True)  # последнее использование бота
    current_character = fields.ForeignKeyField("models.Character", null=True)  # последний выбранный персонаж

    def __str__(self) -> str:
        return f'<User id:{self.id} | Username:{self.username}>'


class Dialog(Model):
    id = fields.BigIntField(pk=True, index=True)
    user_id = fields.ForeignKeyField("models.User", related_name="dialogs")
    character_id = fields.ForeignKeyField("models.Character")
    messages = fields.TextField()  # История общения с ботом


class Character(Model):
    id = fields.BigIntField(pk=True, index=True)
    name = fields.CharField(max_length=32)  # Имя персонажа
    greetings = fields.TextField()  # Приветствие персонажа
    settings = fields.TextField()  # Настройки личности персонажа