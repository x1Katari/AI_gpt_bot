from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "character" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(32) NOT NULL,
    "greetings" TEXT NOT NULL,
    "settings" TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "user" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(32),
    "name" VARCHAR(32),
    "surname" VARCHAR(32),
    "create_date" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "update_date" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "current_character_id" BIGINT REFERENCES "character" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "dialog" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "messages" TEXT NOT NULL,
    "character_id_id" BIGINT NOT NULL REFERENCES "character" ("id") ON DELETE CASCADE,
    "user_id_id" BIGINT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
