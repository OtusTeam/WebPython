from rest_framework import serializers
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):

        class FamilySerializer(serializers.Serializer):
            name = serializers.CharField(max_length=128)
            max_age = serializers.IntegerField()
            # max_age = serializers.IntegerField()

            def validate_max_age(self, value):
                print('validate max age')
                if value < 0:
                    raise serializers.ValidationError('Максимальный возраст не может быть отрицательным')
                return value

            def validate(self, attrs):
                print('validate')
                if attrs['name'] == 'Медведь' and attrs['max_age'] < 3:
                    raise serializers.ValidationError('Медведи живут больше')
                return attrs

        data = {'name': 'Тигр', 'max_age': 30}
        serializer = FamilySerializer(data=data)
        print(serializer.is_valid())

        data = {'name': 'Черепаха', 'max_age': -10}
        serializer = FamilySerializer(data=data)
        print(serializer.is_valid())

        print(serializer.errors)

        data = {'name': 'Медведь', 'max_age': 2}
        serializer = FamilySerializer(data=data)
        print(serializer.is_valid())

        print(serializer.errors)
