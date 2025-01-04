from rest_framework import serializers
from .models import Todo


# Serializer for list view
class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'completed']

# Serializer for detailed (retrieve) view
class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'completed']

# Serializer for create view
class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['title', 'completed']  # No `id` in the POST request