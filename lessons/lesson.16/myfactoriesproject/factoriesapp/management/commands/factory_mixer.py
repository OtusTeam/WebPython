from faker import Faker
from mixer.backend.django import mixer

from django.core.management import BaseCommand

from factoriesapp.models import Group, User

fake = Faker()


def create_all():
    group = mixer.blend(Group, name=fake.word)
    print(group)

    user = mixer.blend(User, birth_month=mixer.MIX.birth_date.month)
    print(user, user.group)

    groups = mixer.cycle(3).blend(Group, name=mixer.sequence('grp1', 'grp2', 'grp3'))
    print(groups)

    groups = mixer.cycle(3).blend(Group, name=mixer.sequence(lambda c: f"group_{c + 1}"))
    print(groups)

    user = mixer.blend(User, lang=mixer.RANDOM('RU', 'EN', 'FR'), username="superuser", group__name="admin")
    print(user, user.group)


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Starting with mixer!")
        create_all()
