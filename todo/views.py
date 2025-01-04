from django.shortcuts import render
from django.http import JsonResponse
from .models import Todo

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
