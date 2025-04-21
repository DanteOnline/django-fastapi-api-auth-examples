from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Create Users"


    def handle(self, *args, **options):
        User.objects.all().delete()
        User.objects.create_user('user', 'user@user.com', 'user123')
        User.objects.create_superuser('admin', 'admin@user.com', 'admin123')
        print('USERS CREATED')
