from rest_framework.serializers import ModelSerializer, Serializer
from mainapp.models import Category
from .v1.serializers import CategoryModelSerializer
from .v2.serializers import CategoryModelSerializer as CategoryModelSerializerV2

# class CategoryModelSerializer(ModelSerializer):
#
#     class Meta:
#         model = Category
#         fields = '__all__'
#
#
# class CategoryModelSerializerOther(ModelSerializer):
#
#     class Meta:
#         model = Category
#         exclude = ('create_duplicated',)

serializers = {
    'v1': CategoryModelSerializer,
    'v2': CategoryModelSerializerV2
}


def get_serializer(version):
    return serializers.get(version, CategoryModelSerializer)
