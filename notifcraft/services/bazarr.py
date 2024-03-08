from notifcraft.settings import ServiceSettings
from notifcraft.utils.discord import BaseDiscordMessageBuilder


class BazarrSettings(ServiceSettings):
    BAZARR_DISCORD_WEBHOOK_URL: str
    BAZARR_TEMPLATE: str = "bazarr.jinja"


class DiscordMessageBuilder(BaseDiscordMessageBuilder):
    def __init__(self, context: dict):
        settings = BazarrSettings()
        super().__init__(
            settings.BAZARR_DISCORD_WEBHOOK_URL, context, settings.BAZARR_TEMPLATE
        )

    def _build_context(self, context: dict):
        content: str = context.get("message")
        if ":" in content:
            last_index = 0
            for i in range(len(content) - 1, -1, -1):
                if content[i] == ":":
                    last_index = i
                    break
            media = content[:last_index]
            message = content[last_index + 1 :]
            return {"media": media.strip(), "message": message.strip()}
        return {"media": context.get("title"), "message": context.get("message")}
