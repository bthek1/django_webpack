from django.shortcuts import render
from django.http import JsonResponse
from .models import Todo


from rest_framework import viewsets
from .models import Todo
from .serializers import TodoListSerializer, TodoDetailSerializer, TodoCreateSerializer, TodoUpdateSerializer, TodoPartialUpdateSerializer, TodoDestroySerializer 

class TodoViewSet(viewsets.ModelViewSet):
    """
    A viewset for managing To-Do items with separate serializers for each action.
    """
    queryset = Todo.objects.all()

    def get_serializer_class(self):
        """
        Return the appropriate serializer class based on the action.
        """
        if self.action == 'list':
            return TodoListSerializer
        elif self.action == 'retrieve':
            return TodoDetailSerializer
        elif self.action == 'create':
            return TodoCreateSerializer
        elif self.action == 'update':
            return TodoUpdateSerializer
        elif self.action == 'partial_update':
            return TodoPartialUpdateSerializer
        elif self.action == 'destroy':
            return TodoDestroySerializer
        return TodoListSerializer  # Default fallback

def index(request):
    """
    Render the main page for the To-Do app.
    """
    return render(request, "todo/index.html")

def todo_list(request):
    """
    Return the list of To-Do items as JSON.
    """
    todos = list(Todo.objects.values())  # Convert QuerySet to a list of dictionaries
    return JsonResponse(todos, safe=False)
