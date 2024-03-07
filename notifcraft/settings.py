import os
from typing import Tuple, Type

from jinja2 import Environment, FileSystemLoader
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    TomlConfigSettingsSource,
)

TOML_CONFIG = os.path.join(os.path.dirname(__file__), "../config/config.toml")


class Settings(BaseSettings):
    PORT: int = 5000
    DEBUG: int = 0


class ServiceSettings(BaseSettings):
    model_config = SettingsConfigDict(
        toml_file=TOML_CONFIG, toml_file_encoding="utf-8", extra="allow"
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        return (TomlConfigSettingsSource(settings_cls),)


settings = Settings()

templates = Environment(
    loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), "../templates"))
)
base_templates = Environment(
    loader=FileSystemLoader(
        os.path.join(os.path.dirname(__file__), "../base_templates")
    )
)
