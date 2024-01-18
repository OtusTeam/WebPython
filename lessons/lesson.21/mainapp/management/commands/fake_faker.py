from django.core.management.base import BaseCommand
from faker import Faker
from mainapp.models import Food


class Command(BaseCommand):
    help = "Fake data with faker"

    def handle(self, *args, **options):

        f = open('person.txt', 'a', encoding='utf-8')

        # fake = Faker(['it_IT', 'en_US', 'ja_JP', 'ar_AA'])
        # fake = Faker(['it_IT', 'en_US', 'ja_JP', 'ar_AA'])
        fake = Faker(['it_IT', 'en_US', 'ja_JP', 'ar_AA'])
        #fake = Faker(['ar_AA'])
        for _ in range(10):
            name = fake.name()
            # 'Lucy Cechtelar'
            print(name)
            f.write(f'{name}\n')

            adderss = fake.address()
            # '426 Jordy Lodge
            #  Cartwrightshire, SC 88120-6700'
            print(adderss)

            text = fake.text()
            print(text)
        f.close()

        color = fake.color(hue='blue')
        print(color)

        food_name = fake.name()
        food = Food(name=food_name)
        print(food.name)