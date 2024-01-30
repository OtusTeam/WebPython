from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, \
    DestroyAPIView, UpdateAPIView
from rest_framework.renderers import JSONRenderer
from mainapp.models import Category
from .serializers import CategoryModelSerializer


class CategoryCreateAPIView(CreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class CategoryListAPIView(ListAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class CategoryRetrieveAPIView(RetrieveAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class CategoryDestroyAPIView(DestroyAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class CategoryUpdateAPIView(UpdateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer

# Есть и другие, которые являются комбинацией этих
