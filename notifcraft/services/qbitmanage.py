from notifcraft.settings import ServiceSettings
from notifcraft.utils.discord import BaseDiscordMessageBuilder


class QbitManageSettings(ServiceSettings):
    QBITMANAGE_DISCORD_WEBHOOK_URL: str
    QBITMANAGE_TEMPLATE: str = "qbitmanage.jinja"


class DiscordMessageBuilder(BaseDiscordMessageBuilder):
    def __init__(self, context: dict):
        settings = QbitManageSettings()
        super().__init__(
            settings.QBITMANAGE_DISCORD_WEBHOOK_URL,
            context,
            settings.QBITMANAGE_TEMPLATE,
        )

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
            message = message.replace("\n", "\n\n").strip()
        return {"title": title, "message": message}
