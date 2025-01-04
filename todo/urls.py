from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="todo-index"),         # Main To-Do page
    path("list", views.todo_list, name="todo-list"),  # API endpoint for To-Do items
]
