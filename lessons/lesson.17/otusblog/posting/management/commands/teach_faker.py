import faker
from django.core.management import BaseCommand
from faker_music import MusicProvider


faker_inst = faker.Faker('ru_ru')
faker_inst.seed_instance(100)


def example_1():
    print('first_name', faker_inst.first_name())
    print('last_name', faker_inst.last_name())
    print('user_name', faker_inst.user_name())
    print('email', faker_inst.email())
    print('address', faker_inst.address())
    print('rgb_color', faker_inst.rgb_color())
    print('color', faker_inst.color(hue='red', color_format='rgb'))


def example_2():
    faker_inst.add_provider(MusicProvider)
    print('music_genre', faker_inst.music_genre())
    print('music_instrument', faker_inst.music_instrument())


class Command(BaseCommand):

    def handle(self, *args, **options):
        example_1()
        example_2()
