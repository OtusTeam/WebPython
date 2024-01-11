from rest_framework.viewsets import ModelViewSet
from mainapp.models import Category
from .serializers import CategoryModelSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
