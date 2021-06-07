from django import forms
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status, filters
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Author, ToDoItem
from .serializers import AuthorSerializer, ToDoItemSerializer


class ToDoItemListView(APIView):
    def get(self, request: Request):
        items = ToDoItem.objects.all()
        serializer = ToDoItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        serializer = ToDoItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ToDoItemDetailView(APIView):
    def get(self, request, pk):
        todoitem = get_object_or_404(ToDoItem, pk=pk)
        serializer = ToDoItemSerializer(todoitem)
        return Response(serializer.data)

    def put(self, request, pk):
        ...

    def patch(self, request, pk):
        ...

    def delete(self, request, pk):
        ...


class SendEmailFeedbackForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    text = forms.CharField(widget=forms.Textarea, required=True)


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['name', 'username']
    ordering_fields = ['username', 'id']


class ToDoItemViewSet(ModelViewSet):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer

    @action(methods=["POST"], detail=False)
    def send_email_feedback(self, request: Request):
        form = SendEmailFeedbackForm(request.data)
        if not form.is_valid():
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Successfully sent!"})
