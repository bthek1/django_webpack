from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)  # Optional description
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # Automatically set on creation
    updated_at = models.DateTimeField(auto_now=True)  # Automatically set on update

    def __str__(self):
        return self.title
