from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from . import models, serializers


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class AuthorViewSet(ModelViewSet):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['id', 'name']
    pagination_class = StandardResultsSetPagination


class ToDoItemViewSet(ModelViewSet):
    queryset = models.ToDoItem.objects.all()
    serializer_class = serializers.ToDoItemSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['id', 'title', 'author__name']


class ExampleView(APIView):
    def get(self, request):
        # serializer = serializers.AuthorSerializer(instance=author).data
        item = {"foo": "bar"}
        return Response(item)

    def post(self, request: Request):
        return Response({
            "data": request.data,
        })


class SecretView(APIView):
    permission_classes = IsAdminUser,
    # permission_classes = IsAuthenticated,

    def get(self, request):
        item = {"secret message": "spam and eggs"}
        return Response(item)

