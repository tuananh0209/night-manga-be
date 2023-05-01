python manage.py collectstatic --noinput
python manage.py migrate
gunicorn config.wsgi -b 0.0.0.0:8000
