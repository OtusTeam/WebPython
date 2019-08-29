from rest_framework import serializers

from .models import ToDoItem


# def text_not_empty(value):
#     if not value:
#         raise serializers.ValidationError('This field cannot be empty.')

class ToDoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = 'id', 'text', 'done'
        # exclude = 'comment',

    # text = serializers.CharField(validators=(text_not_empty, ))
    text = serializers.CharField()
    done = serializers.BooleanField(required=False)

    # id = serializers.IntegerField()
    # text = serializers.CharField()
    # done = serializers.BooleanField()
