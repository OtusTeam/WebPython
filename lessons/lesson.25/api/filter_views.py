from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from .filters import CategoryFilter
from mainapp.models import Category
from .serializers import CategoryModelSerializer


class CategoryQuerysetFilterViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryModelSerializer
    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Category.objects.all()

    def get_queryset(self):
        return Category.objects.filter(name__contains='ед')
        # return Category.objects.filter(user=self.request.user)


class CategoryKwargsFilterView(ListAPIView):
    serializer_class = CategoryModelSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return Category.objects.filter(name__contains=name)


class CategoryParamFilterViewSet(viewsets.ModelViewSet):
    # http://127.0.0.1:8000/filters/param/?name=ур
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', '')
        categorys = Category.objects.all()
        if name:
            categorys = categorys.filter(name__contains=name)
        return categorys


class CategoryDjangoFilterViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    filterset_fields = ['name']


class CategoryCustomDjangoFilterViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    filterset_class = CategoryFilter
