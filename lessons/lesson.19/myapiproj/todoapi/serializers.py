from rest_framework import serializers

from . import models


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Author
        fields = 'id', 'name'


class ToDoItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ToDoItem
        fields = 'id', 'title', 'done', 'author', # 'author_id'

    author = AuthorSerializer(many=False)
    # author = AuthorSerializer
    # author = serializers.PrimaryKeyRelatedField(many=False, queryset=models.Author.objects.all())
