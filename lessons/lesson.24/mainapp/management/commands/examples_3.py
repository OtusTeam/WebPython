from rest_framework import serializers
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        class FamilySerializer(serializers.Serializer):
            name = serializers.CharField(max_length=128)
            max_age = serializers.IntegerField()

        data = {'name': 'Медведь', 'max_age': 30}
        serializer = FamilySerializer(data=data)
        print(serializer.is_valid())  # True

        data = {'name': 'Медведь', 'max_age': 'abc'}
        serializer = FamilySerializer(data=data)
        print(serializer.is_valid())  # False
        print(serializer.errors)  # {'max_age': [ErrorDetail(string='A valid integer is required.', code='invalid')]}

        serializer.is_valid(raise_exception=True)
