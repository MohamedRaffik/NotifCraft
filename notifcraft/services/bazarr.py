from pydantic_settings import SettingsConfigDict

from notifcraft.utils.discord import BaseDiscordMessageBuilder
from notifcraft.settings import BaseServiceSettings


class BazarrSettings(BaseServiceSettings):
    model_config = SettingsConfigDict(env_prefix="BAZARR_")

    TEMPLATE: str = "bazarr.jinja"


class DiscordMessageBuilder(BaseDiscordMessageBuilder):
    def __init__(self, context: dict):
        settings = BazarrSettings()
        super().__init__(settings.DISCORD_WEBHOOK_URL, context, settings.TEMPLATE)

    def _build_context(self, context: dict):
        content: str = context.get("message")
        if ":" in content:
            last_index = 0
            for i in range(len(content) - 1, -1):
                if content[i] == ":":
                    last_index = i
            media = content[:last_index]
            message = content[last_index + 1 :]
            return {"media": media.strip(), "message": message.strip()}
        return {"media": context.get("title"), "message": context.get("message")}
