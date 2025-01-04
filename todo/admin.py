from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'completed')  # Columns to display in the admin list view
    list_filter = ('completed',)                # Filters on the right side of the admin page
    search_fields = ('title',)                  # Search bar for the title field
    ordering = ('id',)                          # Default ordering
