import re
from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.Serializer):
    todo_title = serializers.CharField(max_length=100)
    todo_description = serializers.CharField()
    is_done = serializers.BooleanField(default=False)
    uid = serializers.UUIDField(read_only=True)
  


    def validate_todo_title(self, value):
        if value:
            todo_title = value
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

            if len(todo_title) < 3:
                raise serializers.ValidationError('Todo title must be more than 3 characters')
            if regex.search(todo_title) is not None:
                raise serializers.ValidationError('Todo title cannot contain special characters')
        return value

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.todo_title = validated_data.get('todo_title', instance.todo_title)
        instance.todo_description = validated_data.get('todo_description', instance.todo_description)
        instance.is_done = validated_data.get('is_done', instance.is_done)
        instance.save()
        return instance
