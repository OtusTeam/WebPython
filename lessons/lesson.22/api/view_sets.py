from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from mainapp.models import Category
from .serializers import CategoryModelSerializer


class CategoryViewSet(viewsets.ViewSet):
    # renderer_classes = [JSONRenderer]

    # extra action
    # http://127.0.0.1:8000/viewsets/base/1/category_text_only/
    @action(detail=True, methods=['get'])
    def category_text_only(self, request, pk=None):
        category = get_object_or_404(Category, pk=pk)
        return Response({'category.full_name': category.title_name})

    def list(self, request):
        categories = Category.objects.all()
        serializer = CategoryModelSerializer(categories, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategoryModelSerializer(category)
        return Response(serializer.data)


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    # renderer_classes = [JSONRenderer]
    serializer_class = CategoryModelSerializer


class CategoryCustomViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.DestroyModelMixin,
        viewsets.GenericViewSet,
    ):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
