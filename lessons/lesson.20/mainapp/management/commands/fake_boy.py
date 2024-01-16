from django.core.management.base import BaseCommand
from mainapp.models import Food, Category, Animal
import factory


class Command(BaseCommand):
    help = "Fake data with boy"

    def handle(self, *args, **options):

        class CategoryFactory(factory.Factory):
            class Meta:
                model = Category

            name = 'Fixed name'

        category = CategoryFactory()
        print(category.name)

        category = CategoryFactory(name='Other name')
        print(category.name)
        print(category.id)
        print(type(category))
        # category.save()

        Category.objects.all().delete()

        class CategoryFactory(factory.django.DjangoModelFactory):
            class Meta:
                model = Category

            name = factory.Faker('name')

        category = CategoryFactory(name='Other name')
        print(category.name)
        print(category.id)

        category = CategoryFactory.create()
        print(category.name)
        print(category.id)

        category = CategoryFactory.build()
        print(category.name)
        print(category.id)

        class AnimalFactory(factory.django.DjangoModelFactory):
            class Meta:
                model = Animal

            name = factory.Faker('name')
            category = factory.SubFactory(CategoryFactory)

        animal = AnimalFactory.create()
        print(animal)
        print(animal.category.name)
        print(animal.name)