from pydantic_settings import SettingsConfigDict

from notifcraft.utils.discord import BaseDiscordMessageBuilder
from notifcraft.settings import SettingsBase


class QbitManageSettings(SettingsBase):
    model_config = SettingsConfigDict(env_prefix="QBITMANAGE_")

    TEMPLATE: str = "qbitmanage.jinja"


class DiscordMessageBuilder(BaseDiscordMessageBuilder):
    def __init__(self, context: dict):
        settings = QbitManageSettings()
        super().__init__(settings.DISCORD_WEBHOOK_URL, context, settings.TEMPLATE)

    def _build_context(self, context: dict[str, str]):
        title = context.get("title")
        message = context.get("message")
        if not title:
            message_split = message.split("\n")
            title = message_split.pop(0)
            if message_split:
                message = "\n".join(message_split[1:])
            else:
                message = None
        elif "orphaned" in title.lower():
            message = message.replace("\n", "\n\n")
        return {"title": title, "message": message}
