from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn

class Settings(BaseSettings):
    DB_HOST: str = "127.0.0.1"
    DB_PORT: str = "5432"
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "1234"
    DB_NAME: str = "test_db"
    DB_SSLMODE: str = "require"
    # DATABASE_URI: Optional[PostgresDsn] = None

    model_config = SettingsConfigDict(case_sensitive=True, env_file=".env")


settings = Settings()
