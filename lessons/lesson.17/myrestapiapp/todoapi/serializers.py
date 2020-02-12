from rest_framework import serializers

from .models import TodoItem, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = 'id', 'name'


# class TodoItemSerializer(serializers.ModelSerializer):
class TodoItemSerializer(serializers.HyperlinkedModelSerializer):
# class TodoItemSerializer(serializers.SlugRelatedField):
    class Meta:
        model = TodoItem
        fields = 'id', 'title', 'done', 'author', 'author_id'
        # exclude =

    # id = serializers.IntegerField()
    # title = serializers.CharField()
    # done = serializers.BooleanField()
