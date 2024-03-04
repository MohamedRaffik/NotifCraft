#!/bin/sh

if [[ ! -d notifcraft/templates ]]; then
    mkdir notifcraft/templates
fi

cp -r notifcraft/base_templates notifcraft/templates

poetry run gunicorn -w 4 --bind 0.0.0.0:80 notifcraft.app:app
