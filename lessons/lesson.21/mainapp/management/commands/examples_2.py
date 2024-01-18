from rest_framework import serializers
from python_models import Family


class FamilySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    max_age = serializers.IntegerField()

    def create(self, validated_data):
        return Family(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.max_age = validated_data.get('max_age', instance.max_age)
        return instance


data = {'name': 'Медведь', 'max_age': 50}
serializer = FamilySerializer(data=data)
serializer.is_valid()
family = serializer.save()
print(family)
print(type(family))

data = {'name': 'Тигр', 'max_age': 50}
serializer = FamilySerializer(family, data=data)
serializer.is_valid()
updated_family = serializer.save()
print(updated_family)
print(family is updated_family)

data = {'max_age': 30}
serializer = FamilySerializer(updated_family, data=data, partial=True)
# serializer = FamilySerializer(updated_family, data=data)
serializer.is_valid()
family = serializer.save()

print(family.max_age, family.name)
