import json

from django.core.management import BaseCommand

from django.contrib.auth import get_user_model
from users.models import User as u


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            u.objects.get(email='admin@admin.com').delete()
        except:
            pass
        get_user_model().objects.create_superuser(
            email='admin@admin.com', password='1', username='admin', is_staff=True, is_superuser=True)
