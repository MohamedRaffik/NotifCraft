from flask import Flask, Response, Blueprint, request
from pydantic import ValidationError

from notifcraft.settings import settings
from notifcraft.services.bazarr import BazarrDiscordMessageBuilder
from notifcraft.services.jellyfin import JellyfinDiscordMessageBuilder
from notifcraft.utils.discord import DiscordMessageBuilder

app = Flask(__name__)

notify_bp = Blueprint("notify", __name__, url_prefix="/notify")


def notifier(Builder: DiscordMessageBuilder):
    try:
        builder = Builder(context=request.json)
        builder.send()
        return Response(response="Message sent.", status=200)
    except ValidationError as e:
        message = f"{type(Builder).__name__} Settings Not Configured"
        app.logger.error(message)
        app.logger.error(e.json())
        return Response(
            {"message": message, "errors": e.json()},
            status=400,
        )
    except Exception as e:
        app.logger.error(e)
        app.logger.debug(request.json)
        return Response(response="Failed to send message.", status=400)


@notify_bp.post("/jellyfin")
def jellyfin_notifier():
    return notifier(JellyfinDiscordMessageBuilder)


@notify_bp.post("/bazarr")
def bazarr_notifier():
    return notifier(BazarrDiscordMessageBuilder)


app.register_blueprint(notify_bp)

if __name__ == "__main__":
    app.run(debug=settings.DEBUG, host="0.0.0.0", port=settings.PORT)
