#!/bin/sh

if [[ ! -d templates ]]; then
    mkdir templates
fi

rsync --recursive --ignore-existing base_templates/ templates/base

poetry run gunicorn -w 4 --bind 0.0.0.0:80 --log-level info notifcraft.app:app
