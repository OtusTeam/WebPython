from django.core.management.base import BaseCommand, CommandError
from mainapp.models import Food, Category, Animal, HomeAnimal, LoggingAnimal

class Command(BaseCommand):
    help = "Get all animals"

    def handle(self, *args, **options):
        animals = Animal.objects.all()
        for animal in animals:
            print(animal.name)
            animal.get_category_name()

        print('HOME')
        animals = HomeAnimal.objects.all()
        for animal in animals:
            print(animal.name)

        print('L Animals')
        animals = LoggingAnimal.objects.all()
        for animal in animals:
            print(animal.name)
            animal.get_category_name()
