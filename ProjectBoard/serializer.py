from ProjectBoard.models import TaskModel, Boardmodel
from rest_framework import serializers

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boardmodel
        fields = ['id', 'name', 'description', 'creationtime', 'team', 'status']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ['id', 'title', 'description', 'user_id', 'creationtime', 'status']
