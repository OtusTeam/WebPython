from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.views import APIView, Response

from .models import TodoItem, Author
from .serializers import TodoItemSerializer, AuthorSerializer


class TodoItemListView(APIView):

    def get(self, request):
        items = TodoItem.objects.all()
        serializer = TodoItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class TodoItemDetailView(APIView):

    def get(self, request, pk):
        todo = get_object_or_404(TodoItem, pk=pk)
        serializer = TodoItemSerializer(todo)
        return Response(serializer.data)

    def delete(self, request, pk):
        todo = get_object_or_404(TodoItem, pk=pk)
        serializer = TodoItemSerializer(todo)
        data = serializer.data
        todo.delete()
        return Response(data)


class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
