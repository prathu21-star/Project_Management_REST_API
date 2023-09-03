from django.contrib import admin
from ProjectBoard.models import TaskModel, Boardmodel

@admin.register(Boardmodel)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'creationtime', 'team', 'status']

@admin.register(TaskModel)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'user_id', 'creationtime', 'status']

