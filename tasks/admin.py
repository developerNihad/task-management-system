from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'status')  # Show owner
    list_filter = ('user',)  # Add user filter

admin.site.register(Task, TaskAdmin)