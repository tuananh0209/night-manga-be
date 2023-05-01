#!/bin/sh

if [ -z ${ENVIRONMENT} ]
then 
    export ENVIRONMENT=development
fi

if [ -z ${DATABASE_URL} ]
then 
    export DATABASE_URL="postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@postgres:5432/${POSTGRES_DB}"
fi


# python manage.py create_user
# python manage.py migrate
# python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8000 --settings=config.$ENVIRONMENT
