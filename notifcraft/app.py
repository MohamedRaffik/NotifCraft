from flask import Flask, Response, Blueprint, request
from pydantic import ValidationError

from notifcraft.utils.discord import DiscordMessageBuilder
from notifcraft.settings import JellyfinSettings, Settings
from notifcraft.utils.utils import create_jellyfin_message_context

app = Flask(__name__)

notify_bp = Blueprint("notify", __name__, url_prefix="/notify")


settings = Settings()


@notify_bp.post("/jellyfin")
def jellyfin_notifier():
    try:
        settings = JellyfinSettings()
        context = create_jellyfin_message_context(request.json)
        builder = DiscordMessageBuilder(
            webhook_url=settings.DISCORD_WEBHOOK_URL,
            context=context,
            template="jellyfin.jinja",
        )
        builder.send()
        return Response(response="Message sent.", status=200)
    except ValidationError as e:
        app.logger.info(f"Jellyfin Settings Not Configured: {e.json()}")
        return Response(response=e.json(), status=400)
    except Exception as e:
        app.logger.info(e)
        return Response(response="Failed to send message.", status=400)


app.register_blueprint(notify_bp)

if __name__ == "__main__":
    app.run(debug=settings.DEBUG, host="0.0.0.0", port=settings.PORT)
