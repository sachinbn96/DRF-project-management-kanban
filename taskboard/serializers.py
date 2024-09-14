from rest_framework import serializers
from django.contrib.auth.models import User

from .models import (Task, TaskBoard)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class TaskSerializer(serializers.ModelSerializer):
    assigned_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'task_board',
                  'assigned_users', 'status', 'created_at', 'updated_at', 'due_date']
        read_only_fields = ['created_at', 'updated_at']


class TaskBoardSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    assigned_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = TaskBoard
        fields = ['id', 'title', 'description', 'assigned_users',
                  'tasks', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
