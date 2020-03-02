from django.core.management import BaseCommand
from django.db import transaction
from faker import Faker

from otusblog.models import Tag

fake = Faker()


@transaction.atomic
def create_tags():
    for _ in range(10):
        Tag.objects.create(name=fake.word())


class Command(BaseCommand):
    help = 'Creates Tag fixtures, deletes existing'

    def handle(self, *args, **options):
        Tag.objects.all().delete()
        create_tags()
        print('Done!')
