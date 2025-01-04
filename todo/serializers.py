from rest_framework import serializers
from .models import Todo


# Serializer for the list view
class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id", "title", "completed"]


# Serializer for the retrieve (detailed) view
class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id", "title", "description", "completed", "created_at", "updated_at"]


# Serializer for create
class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["title", "description", "completed"]  # No `id` in the input


# Serializer for update
class TodoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["title", "description", "completed"]


# Serializer for partial update
class TodoPartialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["title", "description", "completed"]


# Serializer for destroy (optional, for confirmation messages)
class TodoDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id", "title"]  # Minimal fields for confirmation or logging
