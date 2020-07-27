from rest_framework import serializers
from .models import Author, ToDoItem


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = 'id', 'name'


class ToDoItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToDoItem
        fields = 'id', 'title', 'done', 'author', 'author_id'

    author = AuthorSerializer()
    # title = serializers.CharField()
    # done = serializers.BooleanField()
