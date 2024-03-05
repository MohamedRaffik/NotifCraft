from pydantic_settings import SettingsConfigDict

from notifcraft.utils.discord import DiscordMessageBuilder
from notifcraft.settings import SettingsBase


class BazarrSettings(SettingsBase):
    model_config = SettingsConfigDict(env_prefix="BAZARR_")

    URL: str
    TEMPLATE: str = "bazarr.jinja"


class BazarrDiscordMessageBuilder(DiscordMessageBuilder):
    def __init__(self, context: dict):
        settings = BazarrSettings()
        super().__init__(settings.DISCORD_WEBHOOK_URL, context, settings.TEMPLATE)

    def _build_context(self, context: dict):
        content = context.get("message")
        if ":" in content:
            media, message = content.split(":")
            return {"media": media.strip(), "message": message.strip()}
        return {"media": context.get("title"), "message": context.get("message")}
