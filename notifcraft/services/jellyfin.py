from notifcraft.settings import ServiceSettings
from notifcraft.utils.discord import BaseDiscordMessageBuilder


class JellyfinSettings(ServiceSettings):
    JELLYFIN_DISCORD_WEBHOOK_URL: str
    JELLYFIN_TEMPLATE: str = "jellyfin.jinja"


class DiscordMessageBuilder(BaseDiscordMessageBuilder):
    def __init__(self, context: dict):
        settings = JellyfinSettings()
        super().__init__(
            settings.JELLYFIN_DISCORD_WEBHOOK_URL, context, settings.JELLYFIN_TEMPLATE
        )

    def _build_context(self, context: dict):
        runtime = context.get("RunTime")
        if runtime:
            parts = runtime.split(":")
            seconds = parts.pop()
            minutes = f"{int(parts.pop())}m"
            hours = ""
            if parts:
                hour_part = int(parts.pop())
                if hour_part:
                    hours = f"{hour_part}h"
            cleaned_runtime = f"{hours}{minutes}"
            context["RunTime"] = cleaned_runtime

        subtitles = set()
        for key in context.keys():
            if key.startswith("Subtitle") and key.endswith("Language"):
                subtitles.add(context[key])
        context["Subtitles"] = ", ".join(list(subtitles))

        audio = set()
        for key in context.keys():
            if key.startswith("Subtitle") and key.endswith("Language"):
                audio.add(context[key])
        context["Audio"] = ", ".join(list(audio))
        return context
