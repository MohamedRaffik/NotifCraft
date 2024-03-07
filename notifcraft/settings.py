import os

from jinja2 import Environment, FileSystemLoader
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PORT: int = 5000
    DEBUG: int = 0


class BaseServiceSettings(BaseSettings):
    DISCORD_WEBHOOK_URL: str
    TEMPLATE: str

    model_config = SettingsConfigDict(
        toml_file=os.path.join(os.path.dirname(__file__), "../config/config.toml")
    )


settings = Settings()

templates = Environment(
    loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), "../templates"))
)
base_templates = Environment(
    loader=FileSystemLoader(
        os.path.join(os.path.dirname(__file__), "../base_templates")
    )
)
