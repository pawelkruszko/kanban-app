from rest_framework import generics
from kanban.tasks.models import Tasks
from kanban.tasks.serializers import TaskSerializer

class TaskList(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer