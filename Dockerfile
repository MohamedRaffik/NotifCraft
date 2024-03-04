FROM python:3.9-alpine

ARG JELLYFIN_API_KEY
ARG JELLYFIN_DISCORD_WEBHOOK_URL
ARG JELLYFIN_URL
ARG PUID=1000
ARG PGID=1000

RUN addgroup --gid ${PGID} -S notifcraft && \
    adduser --uid ${PUID} --ingroup notifcraft -S notifcraft
USER notifcraft
ENV PATH="${PATH}:/home/notifcraft/.local/bin"

RUN pip install --user poetry

WORKDIR /app
COPY --chown=${PUID}:${PGID} . .
RUN poetry config virtualenvs.in-project true
RUN poetry install
ENTRYPOINT [ "poetry", "run", "gunicorn", "-w", "4", "--bind", "0.0.0.0:80", "notifcraft.app:app" ]
