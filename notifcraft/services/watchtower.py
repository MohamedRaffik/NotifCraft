from notifcraft.settings import ServiceSettings
from notifcraft.utils.discord import BaseDiscordMessageBuilder


class WatchtowerSettings(ServiceSettings):
    WATCHTOWER_DISCORD_WEBHOOK_URL: str
    WATCHTOWER_TEMPLATE: str = "watchtower.jinja"


class DiscordMessageBuilder(BaseDiscordMessageBuilder):
    def __init__(self, context: dict):
        settings = WatchtowerSettings()
        super().__init__(
            settings.WATCHTOWER_DISCORD_WEBHOOK_URL,
            context,
            settings.WATCHTOWER_TEMPLATE,
        )

    def _build_context(self, context: dict):
        title = context.get("title")
        message = context.get("message")
        return {"title": title, "message": message}
