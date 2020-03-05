from faker import Faker
from mixer.backend.django import mixer
from django.core.management import BaseCommand

from factoriesapp.models import Group, User

fake = Faker()


def create_all():
    group = mixer.blend(Group)
    print(group)

    user = mixer.blend(User)
    print(user, user.group)

    user = mixer.blend(User, group__name='grp_name_custom')
    print(user, user.group)

    user = mixer.blend(User, username=fake.user_name)
    print(user)

    users = mixer.cycle(3).blend(User)
    print(users)

    groups = mixer.cycle(3).blend(
        Group,
        name=(n for n in ('grp1', 'grp2')),
    )
    print(groups)

    users = mixer.cycle(3).blend(
        User,
        username=(n for n in ('jack', 'john', 'ben')),
    )
    print(users)

    groups = mixer.cycle(3).blend(Group, name=mixer.sequence('grp1', 'grp2', 'grp3'))
    print(groups)

    groups = mixer.cycle(3).blend(Group, name=mixer.sequence(lambda c: f'group_{c}'))
    print(groups)

    user = mixer.blend(User, username='custom', nickname=mixer.MIX.username)
    print(user)



class Command(BaseCommand):

    def handle(self, *args, **options):
        create_all()
