import os

from jinja2 import Environment, PackageLoader
from pydantic_settings import BaseSettings, SettingsConfigDict

env = Environment(loader=PackageLoader(__name__))


class Settings(BaseSettings):
    DEBUG: bool
    LOG_FILE: str = os.path.join(os.path.dirname(__file__), "../logs/flask.log")
    PORT: int = 5000


class SettingsBase(BaseSettings):
    DISCORD_WEBHOOK_URL: str


class JellyfinSettings(SettingsBase):
    model_config = SettingsConfigDict(env_prefix="JELLYFIN_")

    URL: str
    API_KEY: str
