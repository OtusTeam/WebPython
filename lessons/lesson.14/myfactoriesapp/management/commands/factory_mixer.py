from faker import Faker
from mixer.backend.django import mixer
from django.core.management import BaseCommand

from myfactoriesapp.models import Group

fake = Faker()


def create_all():
    group = mixer.blend(Group)
    print(group)

    group = mixer.blend(Group, name='test')
    print(group)

    group = mixer.blend(Group, name=fake.word)
    print(group)

    groups = mixer.cycle(3).blend(Group, name=mixer.sequence('grp1', 'grp2', 'grp3'))
    print(groups)

    groups = mixer.cycle(3).blend(Group, name=mixer.sequence(lambda c: f"group_{c}"))
    print(groups)


class Command(BaseCommand):
    def handle(self, *args, **options):
        create_all()
