from rest_framework import serializers

from .models import Author, ToDoItem


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = "id", "name", "username"
        view_name = "authors"


class ToDoItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ToDoItem
        fields = "id", "title", "done", "dt_created", "author", "author_id"
        view_name = "todos"

    # id = serializers.IntegerField()
    # title = serializers.CharField()
    # author = AuthorSerializer()
