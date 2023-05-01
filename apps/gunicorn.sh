#!/bin/sh

if [ -z ${ENVIRONMENT} ]; then export ENVIRONMENT=local; fi

# build static assets
python /usr/src/apps/manage.py collectstatic --noinput --settings=config.$ENVIRONMENT

# start api with gunicorn
/usr/src/apps/virtualenv/bin/gunicorn config.wsgi -b 0.0.0.0:8000 --chdir=/usr/src/apps
