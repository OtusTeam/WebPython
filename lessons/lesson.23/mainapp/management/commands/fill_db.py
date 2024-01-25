from django.core.management.base import BaseCommand, CommandError
from mainapp.models import Food, Category, Animal, WildAnimal
from django.db.models import F, Q, Max, Min, Sum, Count, Subquery


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

        for _ in range(1):
            leo = WildAnimal.objects.create(name='Leo', category=tiger, age=1)
            leo_tiger = WildAnimal.objects.create(name='Tiger Leo', category=tiger, age=2)
            boris = WildAnimal.objects.create(name='Boris', category=bear, age=5)

        # увеличить возраст всех животных на 1
        WildAnimal.objects.all().update(age=F('age') + 1)

        for animal in WildAnimal.objects.all():
            print(animal.age)

        animals = Animal.objects.all()
        for animal in animals:
            print(animal.a)
            print(animal.b)
            print(animal.d)

        equal_dates_animals = Animal.objects.filter(a=F('b'), d=F('b'))
        print('EQUAL', equal_dates_animals)

        # Max возраст животного
        # max_age = WildAnimal.objects.aggregate(Max("age", default=0))
        # print('max_age', max_age)
        # min_age = WildAnimal.objects.aggregate(Min("age", default=0))
        # print('min_age', min_age)
        # sum_age = WildAnimal.objects.aggregate(Sum("age", default=0))
        # print('sum_age', sum_age)
        # count_age = WildAnimal.objects.aggregate(Count("age", default=0))
        # print('count_age', count_age)
        # Животное с max возрастом
        max_age = WildAnimal.objects.aggregate(Max("age", default=0))
        animal = WildAnimal.objects.filter(age=max_age['age__max']).first()
        print('MAX animal', animal.age)

        # Количество животных в каждой категории
        categories = Category.objects.annotate(
            animals_count=Count('animal'),
        )

        for category in categories:
            print(category.name, category.animals_count)
            # print(category.name, category.some_var)

        animal = Animal.objects.create(name='abc', a=2, b=3)

        duplicates_animals = Animal.objects.filter(a=animal.a, b=animal.b)
        if duplicates_animals.exists():
            duplicates_animals.update(name='duplicates')




        # wild_animal_list = []
        # for _ in range(1000):
        #     leo = WildAnimal(name='Leo', category=tiger, age=1)
        #     wild_animal_list.append(leo)
        #     leo_tiger = WildAnimal(name='Tiger Leo', category=tiger, age=2)
        #     wild_animal_list.append(leo_tiger)
        #     boris = WildAnimal(name='Boris', category=bear, age=5)
        #     wild_animal_list.append(boris)
        #
        # WildAnimal.objects.bulk_create(wild_animal_list)

        wild_animal_list = []
        for _ in range(1000):
            leo = Animal(name='Leo', category=tiger)
            wild_animal_list.append(leo)
            leo_tiger = Animal(name='Tiger Leo', category=tiger)
            wild_animal_list.append(leo_tiger)
            boris = Animal(name='Boris', category=bear)
            wild_animal_list.append(boris)

        Animal.objects.bulk_create(wild_animal_list)

        #

        # bulk update
        # Всех сделать тиграми
        Animal.objects.all().update(category=tiger)

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

        # print('Get')
        # get_animal = WildAnimal.objects.get(id=leo.id)
        # print(get_animal)

        #
        self.stdout.write(
            self.style.SUCCESS('Done')
        )
        #
        #
        # self.stdout.write(
        #     self.style.ERROR('error')
        # )