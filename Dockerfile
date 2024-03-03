FROM python:3.9-alpine

ARG JELLYFIN_API_KEY
ARG JELLYFIN_DISCORD_WEBHOOK_URL
ARG JELLYFIN_URL
ARG PUID=1000
ARG GUID=1000

RUN addgroup --gid ${GUID} -S notifcraft && \
    adduser --uid ${PUID} --ingroup notifcraft -S notifcraft
USER notifcraft
ENV PATH="${PATH}:/home/notifcraft/.local/bin"

RUN pip install --user poetry
WORKDIR /app
COPY . .
RUN poetry install
ENTRYPOINT [ "poetry", "run", "python", "-m", "app.app" ]
