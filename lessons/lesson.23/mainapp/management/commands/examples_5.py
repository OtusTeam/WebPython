from rest_framework import serializers
from python_models import Family, FamilyCard, Kind, Food


class FamilySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    max_age = serializers.IntegerField()


class FamilyCardSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=1024)
    family = FamilySerializer()


class FoodSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    families = FamilySerializer(many=True)


class KindSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    family = FamilySerializer()


family1 = Family('Медведь', 50)
serializer = FamilySerializer(family1)
print(serializer.data)  # {'name': 'Медведь', 'max_age': 50}

card = FamilyCard('Текст карточки', family1)
serializer = FamilyCardSerializer(card)
print(
    serializer.data)  # {'text': 'Текст карточки', 'family': OrderedDict([('name', 'Медведь'), ('max_age', 50)])}

kind = Kind('Бурый', family1)
serializer = KindSerializer(kind)  # {'name': 'Бурый', 'family': OrderedDict([('name', 'Медведь'), ('max_age', 50)])}
print(serializer.data)
#
family2 = Family('Тигр', 30)
food = Food('мясо', [family1, family2])
#
serializer = FoodSerializer(food)
print(serializer.data)
# {'name': 'мясо', 'families': [OrderedDict([('name', 'Медведь'), ('max_age', 50)]), OrderedDict([('name', 'Тигр'), ('max_age', 30)])]}
