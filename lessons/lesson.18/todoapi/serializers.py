from rest_framework import serializers

from .models import Author, ToDoItem


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = 'id', 'name'
        view_name = 'author'


class ToDoItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ToDoItem
        fields = 'id', 'title', 'done', 'author', 'author_id'
        view_name = 'todo'
        # exclude =
    # id = serializers.IntegerField()
    # title = serializers.CharField()
    # done = serializers.BooleanField()
    # author = AuthorSerializer()
