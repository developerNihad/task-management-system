from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from rest_framework import filters
from rest_framework.exceptions import PermissionDenied


class TaskListCreateView(generics.ListCreateAPIView):

    filter_backends = [filters.SearchFilter]
    search_fields = ['status']

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Task.objects.all()
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        if not self.request.user.is_staff and 'user' in serializer.validated_data:
            if serializer.validated_data['user'] != self.request.user:
                raise PermissionDenied("You can only create tasks for yourself")
        serializer.save()
    

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)