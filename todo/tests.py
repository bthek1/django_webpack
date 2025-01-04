import pytest
from django.urls import reverse
from django.http import JsonResponse
from django.test import Client
from .models import Todo

from rest_framework.test import APIClient

@pytest.mark.django_db
def test_index_view(client):
    """
    Test the index view for rendering the main page.
    """
    response = client.get(reverse("todo:index"))  # Use reverse for URL resolution
    assert response.status_code == 200
    assert b"<!DOCTYPE html>" in response.content  # Check if the response contains HTML content

@pytest.mark.django_db
def test_todo_list_view(client):
    """
    Test the todo_list view for returning a JSON response.
    """
    # Create some test data
    Todo.objects.create(title="Task 1", completed=False)
    Todo.objects.create(title="Task 2", completed=True)

    response = client.get(reverse("todo:todo_list"))
    assert response.status_code == 200
    assert isinstance(response, JsonResponse)

    data = response.json()
    assert len(data) == 2
    assert data[0]["title"] == "Task 1"
    assert data[1]["completed"] is True




@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
class TestTodoAPI:
    """
    Test suite for the To-Do API endpoints.
    """

    def test_todo_list_api(self, api_client):
        """
        Test the API endpoint for listing To-Do items.
        """
        # Create some test data
        Todo.objects.create(title="Task 1", completed=False)
        Todo.objects.create(title="Task 2", completed=True)

        response = api_client.get("/api/todos/")
        assert response.status_code == 200

        data = response.json()
        assert len(data) == 2
        assert data[0]["title"] == "Task 1"
        assert data[1]["completed"] is True

    def test_todo_detail_api(self, api_client):
        """
        Test the API endpoint for retrieving a single To-Do item.
        """
        todo = Todo.objects.create(title="Task 1", completed=False)
        response = api_client.get(f"/api/todos/{todo.id}/")
        assert response.status_code == 200

        data = response.json()
        assert data["title"] == "Task 1"
        assert data["completed"] is False

    def test_todo_create_api(self, api_client):
        """
        Test the API endpoint for creating a new To-Do item.
        """
        payload = {"title": "New Task", "completed": False}
        response = api_client.post("/api/todos/", payload, format="json")
        assert response.status_code == 201

        data = response.json()
        assert data["title"] == "New Task"
        assert data["completed"] is False

    def test_todo_update_api(self, api_client):
        """
        Test the API endpoint for updating an existing To-Do item.
        """
        todo = Todo.objects.create(title="Old Task", completed=False)
        payload = {"title": "Updated Task", "completed": True}
        response = api_client.put(f"/api/todos/{todo.id}/", payload, format="json")
        assert response.status_code == 200

        data = response.json()
        assert data["title"] == "Updated Task"
        assert data["completed"] is True

    def test_todo_partial_update_api(self, api_client):
        """
        Test the API endpoint for partially updating a To-Do item.
        """
        todo = Todo.objects.create(title="Task 1", completed=False)
        payload = {"completed": True}
        response = api_client.patch(f"/api/todos/{todo.id}/", payload, format="json")
        assert response.status_code == 200

        data = response.json()
        assert data["completed"] is True

    def test_todo_delete_api(self, api_client):
        """
        Test the API endpoint for deleting a To-Do item.
        """
        todo = Todo.objects.create(title="Task to Delete", completed=False)
        response = api_client.delete(f"/api/todos/{todo.id}/")
        assert response.status_code == 204

        # Check that the item was deleted
        assert not Todo.objects.filter(id=todo.id).exists()
