import os

from jinja2 import Environment, FileSystemLoader
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    LOG_FILE: str = os.path.join(os.path.dirname(__file__), "../logs/flask.log")
    PORT: int = 5000
    DEBUG: int = 0


settings = Settings()

env = Environment(
    loader=FileSystemLoader(
        os.path.join(
            os.path.dirname(__file__),
            "../base_templates" if settings.DEBUG else "../templates",
        )
    )
)


class SettingsBase(BaseSettings):
    DISCORD_WEBHOOK_URL: str
