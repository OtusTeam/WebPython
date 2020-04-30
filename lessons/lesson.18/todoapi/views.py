from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView, Response
from rest_framework.viewsets import ModelViewSet

from .models import Author, ToDoItem
from .serializers import AuthorSerializer, ToDoItemSerializer


class ToDoItemListView(APIView):
    def get(self, request):
        items = ToDoItem.objects.all()
        serializer = ToDoItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ToDoItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ToDoItemDetailView(APIView):
    def get(self, request, pk):
        todo = get_object_or_404(ToDoItem, pk=pk)
        serializer = ToDoItemSerializer(todo)
        return Response(serializer.data)

    def delete(self, request, pk):
        todo = get_object_or_404(ToDoItem, pk=pk)
        serializer = ToDoItemSerializer(todo)
        data = serializer.data
        todo.delete()
        return Response(data)


class ToDoItemViewSet(ModelViewSet):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
