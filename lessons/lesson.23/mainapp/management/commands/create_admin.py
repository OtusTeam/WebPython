from django.core.management.base import BaseCommand, CommandError
from userapp.models import MyUser
from django.db.utils import IntegrityError


class Command(BaseCommand):
    help = "Fill db with test data"

    def handle(self, *args, **options):
        try:
            MyUser.objects.create_superuser('admin', 'admin@admin.com', 'admin')
        except IntegrityError:
            self.stdout.write(
                self.style.SUCCESS('Already Exists')
            )
        else:
            self.stdout.write(
                self.style.SUCCESS('Done')
            )

        # MyUser.objects.create_superuser('admin', 'admin@admin.com', 'admin')
