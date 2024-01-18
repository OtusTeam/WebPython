from django.core.management.base import BaseCommand, CommandError
from mainapp.models import Food, Category, Animal, WildAnimal


class Command(BaseCommand):
    help = "Query examples"

    def handle(self, *args, **options):

        print('All animals')
        animals = Animal.objects.all()

        for item in animals:
            print(item)

        print('Simple filter')
        # Все животные с именем Tiger Leo

        leos = Animal.objects.filter(name='Tiger Leo')
        print(len(leos))
        print(type(leos))
        print(leos.first().name)

        # найти животное с возрастом меньше 5
        print('Age animals')

        age_animals = WildAnimal.objects.filter(age__lt=5)
        # age_animals = Animal.objects.filter(age__lte=5)
        # age_animals = Animal.objects.filter(age__gt=5)
        for item in age_animals:
            print(item.name)
            print(item.age)

        # найти животное у которого имя содержит leo
        # 1. с учетом регистра
        # 2. без учета регистра

        print('name filter')

        animals = Animal.objects.filter(name__icontains='leo')
        # age_animals = Animal.objects.filter(age__lte=5)
        # age_animals = Animal.objects.filter(age__gt=5)
        for item in animals:
            print(item.name)

        # найти животное с категорией название которой начинается на Т

        t_category = Category.objects.filter(name__startswith='Т')
        print(t_category)

        animals = Animal.objects.filter(category=t_category.first())
        print(animals.order_by('-id'))

        animals = Animal.objects.filter(category__name__startswith='Т')
        print(animals.order_by('-id'))

        # количество животных
        # не очень хорошо
        print(len(animals))

        # лучше
        print(animals.count())

        # есть ли животное с именем содержащим leo
        animals = Animal.objects.filter(name__icontains='leo')
        # animals = animals.filter(name__icontains='l')

        print(len(animals) != 0)
        print(animals.count() != 0)
        print(animals.exists())