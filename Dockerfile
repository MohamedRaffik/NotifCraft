FROM python:3.9-alpine

ARG JELLYFIN_API_KEY
ARG JELLYFIN_DISCORD_WEBHOOK_URL
ARG JELLYFIN_URL
ARG PUID=1000
ARG PGID=1000

RUN apk add bash && \
    apk add rsync
RUN addgroup --gid ${PGID} -S notifcraft && \
    adduser --uid ${PUID} --ingroup notifcraft -s /bin/bash -S notifcraft
USER notifcraft
ENV PATH="${PATH}:/home/notifcraft/.local/bin"

RUN pip install --user poetry

WORKDIR /app
COPY --chown=${PUID}:${PGID} pyproject.toml pyproject.toml
COPY --chown=${PUID}:${PGID} poetry.lock poetry.lock
RUN poetry config virtualenvs.in-project true
RUN poetry install --no-root
COPY --chown=${PUID}:${PGID} . .
RUN chmod +x init.sh
ENTRYPOINT [ "./init.sh" ]
