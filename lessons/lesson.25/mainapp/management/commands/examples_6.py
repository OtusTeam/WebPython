from rest_framework import serializers
from django.core.management.base import BaseCommand
from mainapp.models import Category, Animal, AnimalCard, Food


class Command(BaseCommand):

    def handle(self, *args, **options):
        class FamilySerializer(serializers.ModelSerializer):
            class Meta:
                model = Category
                fields = '__all__'

        class FoodSerializer(serializers.ModelSerializer):
            class Meta:
                model = Food
                fields = '__all__'

        class AnimalCardSerializer(serializers.ModelSerializer):
            class Meta:
                model = AnimalCard
                fields = ['text']

        # class AnimalSerializer(serializers.ModelSerializer):
        #     category = FamilySerializer()
        #
        #     class Meta:
        #         model = Animal
        #         #exclude = ['name']
        #         fields = '__all__'



        class AnimalSerializer(serializers.ModelSerializer):
            # food = serializers.StringRelatedField(many=True)
            food = FoodSerializer(many=True)
            """
                1. StringRelatedField — представляет объект методом __str__.
                2. PrimaryKeyRelatedField — представляет объект его id (используется по умолчанию).
                3. HyperlinkedRelatedField — представляет объект гипперссылкой. Обычно она ведёт на страницу detail этого объекта.
                4. SlugRelatedField — позволяет указать несколько полей для отображения объекта.
            """
            category = FamilySerializer()
            # kind = serializers.SlugRelatedField(
            #     many=False,
            #     slug_field='full_name',
            #     read_only=True
            # )

            class Meta:
                model = Animal
                fields = '__all__'

        """
                {'id': 4, 'foods': ['Мясо', 'Мед'], 
                'kind': OrderedDict([('id', 3), ('family', OrderedDict([('id', 4), ('name', 'Медведь')])), 
                ('image',
                 None), 
                 ('full_name', None)]), 'name': 'Борис', 'create': '2022-01-13T18:04:04.772142Z', 
                 'update': '2022-01-13T18:04:05.142244Z', 'card': 2}
                """

        class_list = [Animal, Category, AnimalCard, Food]
        for item in class_list:
            item.objects.all().delete()

        family = Category.objects.create(name='Медведь')
        serializer = FamilySerializer(family)
        print(serializer.data)

        # kind = Kind.objects.create(name='Бурый', family=family, full_name='Бурый Медведь')
        # serializer = KindSerializer(kind)
        # print(serializer.data)

        food1 = Food.objects.create(name='Мясо')
        serializer = FoodSerializer(food1)
        print(serializer.data)

        # animal_card = AnimalCard.objects.create(text='Карточка Медведя')
        # serializer = AnimalCardSerializer(animal_card)
        # print(serializer.data)

        animal = Animal.objects.create(name='Борис', category=family)
        food2 = Food.objects.create(name='Мед')
        animal.food.add(food1)
        animal.food.add(food2)
        animal.save()
        serializer = AnimalSerializer(animal)
        print(serializer.data)
