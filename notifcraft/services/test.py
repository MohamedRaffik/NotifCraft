import pprint

from notifcraft.settings import ServiceSettings
from notifcraft.utils.discord import BaseDiscordMessageBuilder


class TestServiceSettings(ServiceSettings):
    TEST_DISCORD_WEBHOOK_URL: str
    TEST_TEMPLATE: str = "test.jinja"


class DiscordMessageBuilder(BaseDiscordMessageBuilder):
    def __init__(self, context: dict, remote_addr: str):
        settings = TestServiceSettings()
        self._remote_addr = remote_addr
        super().__init__(
            settings.TEST_DISCORD_WEBHOOK_URL,
            context,
            settings.TEST_TEMPLATE,
        )

    def _build_context(self, context: dict[str, str]):
        message = pprint.pformat(context, indent=2)
        return {"message": message, "source": self._remote_addr}
