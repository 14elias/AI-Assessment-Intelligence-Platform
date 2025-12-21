# app/core/config.py
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    APP_NAME: str = "AlignEd"
    ENV: str = "development"

    DATABASE_URL: str = Field(
        default="sqlite+aiosqlite:///./aligned.db"
    )

    DATABASE_SYNC_URL: str = "sqlite:///./aligned.db" 

    class Config:
        env_file = ".env"

settings = Settings()
