from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import TaskSerializer

from .models import Task

class TaskList(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = TaskSerializer
    def get_queryset(self):
        return Task.objects.filter(user = self.request.user).order_by("-id")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    

class TaskDetail(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self,pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data, partial = True)
        if request.user != task.user:
            return Response(data={'details':'This task belongs to other user'},status=status.HTTP_403_FORBIDDEN)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        if request.user == task.user:
            task.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(data={'details':'This task belongs to other user'},status=status.HTTP_403_FORBIDDEN)
        
        