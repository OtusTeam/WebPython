from rest_framework import serializers

from .models import ToDoItem

class ToDoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = 'id', 'text', 'done'

    # done = serializers.BooleanField(required=False, default=False)
    done = serializers.BooleanField(required=True)

    # id = serializers.IntegerField()
    # text = serializers.CharField()
    # done = serializers.BooleanField()
