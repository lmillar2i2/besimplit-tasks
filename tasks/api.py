from rest_framework import serializers, viewsets, mixins
from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'created_at']
        read_only_fields = ['id', 'created_at']


class TaskViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer


