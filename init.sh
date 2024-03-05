#!/bin/sh

if [[ ! -d templates ]]; then
    mkdir templates
fi

rsync --recursive --ignore-existing base_templates/ templates/base

if [[ $DEBUG -eq 0 ]]; then
    poetry run gunicorn -w 4 --bind 0.0.0.0:80 --log-level info notifcraft.app:app
else
    poetry run gunicorn -w 4 --bind 0.0.0.0:80 --log-level debug notifcraft.app:app
fi
