FROM python:3.9-alpine

ARG JELLYFIN_API_KEY
ARG JELLYFIN_DISCORD_WEBHOOK_URL
ARG JELLYFIN_URL

RUN pip install poetry
WORKDIR /app
COPY . .
RUN poetry install
ENTRYPOINT [ "poetry run python -m app.app" ]
