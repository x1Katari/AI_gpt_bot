from pydantic import SecretStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
  DB_URL_ORM: SecretStr
  bot_token: SecretStr
  admin_id: SecretStr
  gpt_token: SecretStr
  logging_level: int
  POSTGRES_DB: SecretStr
  POSTGRES_USER: SecretStr
  POSTGRES_PASSWORD: SecretStr
  POSTGRES_PORT: SecretStr
  POSTGRES_HOST: SecretStr
  

  class Config:
    env_file = '.env'
    env_file_encoding = 'utf-8'

config = Settings()
