from rest_framework.decorators import api_view, renderer_classes
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from mainapp.models import Category
from .serializers import CategoryModelSerializer
import random


class CategoryAPIVIew(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategoryModelSerializer(categories, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def category_view(request):
    categories = Category.objects.all()
    serializer = CategoryModelSerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def random_number(request):
    return Response({'random_number': random.randint(1, 2)})