FROM python:3.9-alpine

ARG JELLYFIN_API_KEY
ARG JELLYFIN_DISCORD_WEBHOOK_URL
ARG JELLYFIN_URL
ARG PUID=1000
ARG GUID=1000

RUN pip install poetry
RUN addgroup --gid ${GUID} -S notifcraft && \
    adduser --uid ${PUID} --ingroup notifcraft -S notifcraft
USER notifcraft
WORKDIR /app
COPY . .
RUN poetry install
ENTRYPOINT [ "/bin/bash", "-c", "poetry run python -m app.app" ]
