
# Create your views here.
from rest_framework import viewsets, permissions
from .models import TaskBoard, Task
from .serializers import TaskBoardSerializer, TaskSerializer


class TaskBoardViewSet(viewsets.ModelViewSet):
    queryset = TaskBoard.objects.all()
    serializer_class = TaskBoardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        task_board = serializer.save()
        task_board.assigned_users.add(self.request.user)

    def perform_update(self, serializer):
        task_board = serializer.save()
        if 'assigned_users' in self.request.data:
            task_board.assigned_users.set(self.request.data['assigned_users'])


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        task = serializer.save()
        task.assigned_users.add(self.request.user)

    def perform_update(self, serializer):
        task = serializer.save()
        if 'assigned_users' in self.request.data:
            task.assigned_users.set(self.request.data['assigned_users'])
