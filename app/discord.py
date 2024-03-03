import json
import requests

from app.settings import env


class DiscordMessageBuilder:
    def __init__(self, webhook_url: str, context: dict, template: str):
        self._message = env.get_template(template).render(context=context)
        self._wehbook_url = webhook_url

    def send(self):
        response = requests.post(self._wehbook_url, json=json.loads(self._message))
        print(response.content)
        response.raise_for_status()
