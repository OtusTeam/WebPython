from django.core.management.base import BaseCommand
from mixer.backend.django import mixer, Mixer, GenFactory
from mainapp.models import Food, Category, Animal


class Command(BaseCommand):
    help = "Fake data with mixer"

    def handle(self, *args, **options):
        Category.objects.all().delete()
        category = mixer.blend(Category)
        animal = mixer.blend(Animal)
        print('A Animal:')
        print(animal.a)
        print(animal.name)
        print(animal.category.name)
        print(animal.id)

        for i in range(5):
            category = mixer.blend(Category, name=lambda: f'category{i}')
            print(category.name)

        mixer.cycle(4).blend(Category, name=(
            name for name in ('Piter', 'John', 'Leo', 'Max', 'Five'))
        )

        categories = mixer.cycle(4).blend(Category, name=mixer.sequence(
            lambda category: f"category_{category}")
        )

        print('SEQUENCE')
        for category in categories:
            print(category.name)

        categories = mixer.cycle(4).blend(
            Category, name=mixer.sequence("{0}_test_{0}")
        )

        print('SEQUENCE 0')
        for category in categories:
            print(category.name)

        #
        # category = mixer.blend(Category, score=mixer.RANDOM)
        # client.score  # Some like: --> 456

        animal = mixer.blend(Animal, a=mixer.RANDOM)
        print('A Animal:')
        print(animal.a)

        print(Category.objects.all().values_list('id'))

        animal = mixer.blend(Animal)

        print(animal.category.id)

        animal = mixer.blend(Animal, category=mixer.SELECT)

        print(animal.category.id)

        lang_mixer = Mixer(locale='ar_AA')
        category = lang_mixer.blend(Category)
        print(category.name)

        factory = GenFactory()
        build_mixer = Mixer(commit=False, factory=factory)
        category = build_mixer.blend(Category)
        print(category.name)
        print(category.id)


