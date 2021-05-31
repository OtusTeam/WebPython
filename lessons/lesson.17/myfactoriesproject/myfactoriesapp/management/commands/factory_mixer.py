from django.core.management import BaseCommand
from mixer.backend.django import mixer
from faker import Faker

from myfactoriesapp.models import Group, User


fake = Faker()


def create_all():
    print("Hello!")
    # print(fake.word())
    # print(fake.user_name())
    # print(fake.sentence())
    # print(fake.paragraph())
    # print(fake.words(3))
    # return

    group = mixer.blend(Group)
    print(group)

    group = mixer.blend(Group, name="news")
    print(group)

    group = mixer.blend(Group, name=fake.word)
    print(group)

    groups = mixer.cycle(3).blend(Group, name=fake.word)
    print(groups)

    groups = mixer.cycle(3).blend(Group, name=mixer.sequence("grp1", "grp2", "grp3"))
    print(groups)

    groups = mixer.cycle(3).blend(Group, name=mixer.sequence(lambda c: f"group_{c}"))
    print(groups)

    user = mixer.blend(User)
    print(user)

    user = mixer.blend(User, group=group, birth_month=mixer.MIX.birth_dt.month)
    print(user)


class Command(BaseCommand):
    help = "Create data using mixer"

    def handle(self, *args, **options):
        create_all()
