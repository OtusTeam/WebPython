from django.core.management.base import BaseCommand, CommandError
from mainapp.models import Food, Category, Animal, WildAnimal


class Command(BaseCommand):
    help = "Fill db with test data"

    def handle(self, *args, **options):
        print('Delete categories')
        Category.objects.all().delete()

        print('Create categories...')
        bear = Category.objects.create(name='Медведь')
        tiger = Category.objects.create(name='Тигр')

        print('Delete food')
        Food.objects.all().delete()

        print('Create food...')
        banana = Food.objects.create(name='Банан')
        meat = Food.objects.create(name='Мясо')
        honey = Food.objects.create(name='Мёд')

        print('Create animals...')

        for _ in range(10):
            leo = WildAnimal.objects.create(name='Leo', category=tiger, age=1)
            leo_tiger = WildAnimal.objects.create(name='Tiger Leo', category=tiger, age=2)
            boris = WildAnimal.objects.create(name='Boris', category=bear, age=5)

        # Many to Many
        leo.food.add(banana)
        leo.food.add(meat)
        leo.save()

        boris.food.add(meat)
        boris.food.add(honey)
        boris.save()

        print('Update...')
        leo.name = 'Tiger Leo'
        leo.save()

        print('Get all')
        animals = WildAnimal.objects.all()

        print(len(animals))
        for animal in animals:
            print(animal.name)
            print(animal.category.name)
            for food in animal.food.all():
                print(food.name)

        print('Get one')
        print('First')
        first_animal = WildAnimal.objects.filter(id=leo.id).first()
        print(first_animal)

        print('Get')
        get_animal = WildAnimal.objects.get(id=leo.id)
        print(get_animal)

        #
        self.stdout.write(
            self.style.SUCCESS('Done')
        )
        #
        #
        # self.stdout.write(
        #     self.style.ERROR('error')
        # )