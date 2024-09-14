from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TaskBoard(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    assigned_users = models.ManyToManyField(User, related_name='task_boards')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    STATUS_CHOICES = [
        ('TODO', 'To Do'),
        ('IN_PROGRESS', 'In Progress'),
        ('DONE', 'Done')
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    task_board = models.ForeignKey(
        TaskBoard, related_name='tasks', on_delete=models.CASCADE)
    assigned_users = models.ManyToManyField(User, related_name='tasks')
    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default='TODO')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
