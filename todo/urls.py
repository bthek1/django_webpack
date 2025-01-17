from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index, todo_list, TodoViewSet

# Define app_name for reverse lookups
app_name = "todo"

# Create a router and register the Todo viewset
router = DefaultRouter()
router.register(r"todos", TodoViewSet, basename="todo")


urlpatterns = [
    path("api/", include(router.urls)),  # Include router-generated URLs
    path("", index, name="index"),  # Main To-Do page
    path("list", todo_list, name="lists"),  # API endpoint for To-Do items
]
