import json
import requests

from abc import ABC, abstractmethod
from notifcraft.settings import env, JellyfinSettings


class DiscordMessageBuilder(ABC):
    def __init__(self, webhook_url: str, context: dict, template: str):
        self._message = env.get_template(template).render(self.build_context(context))
        self._wehbook_url = webhook_url

    def send(self):
        response = requests.post(self._wehbook_url, json=json.loads(self._message))
        response.raise_for_status()

    @abstractmethod
    def _build_context(self, context: dict):
        return


class BazarrDiscordMessageBuilder(DiscordMessageBuilder):
    def __init__(self, webhook_url: str, context: dict, template: str):
        super().__init__(webhook_url, context, template)
