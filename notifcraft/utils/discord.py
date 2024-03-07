import json
import requests

from abc import ABC, abstractmethod
from jinja2 import TemplateNotFound
from notifcraft.settings import templates, base_templates


class BaseDiscordMessageBuilder(ABC):
    def __init__(self, webhook_url: str, context: dict, template: str):
        try:
            template = templates.get_template(template)
        except TemplateNotFound:
            template = base_templates.get_template(template)
        self._message = template.render(self._build_context(context))
        self._wehbook_url = webhook_url

    def send(self):
        if self._message:
            response = requests.post(
                self._wehbook_url, json=json.loads(self._message, strict=False)
            )
            response.raise_for_status()

    @abstractmethod
    def _build_context(self, context: dict):
        return
