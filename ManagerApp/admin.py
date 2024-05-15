from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')  # Specify the fields to display in the list view
    search_fields = ('text',)      # Add a search field for the 'text' field
