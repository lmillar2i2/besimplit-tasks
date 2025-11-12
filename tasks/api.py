from rest_framework import serializers, viewsets, mixins
from tasks.models import Task
# api.py: API básica con Django REST Framework.
# Expone endpoints para listar y crear tareas.


class TaskSerializer(serializers.ModelSerializer):
    """Serializador de Task que controla cómo viajan los datos por la API."""
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'created_at']
        read_only_fields = ['id', 'created_at']


class TaskViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    """ViewSet
       GET /tasks/ lista tareas (ordenadas por creación)
       POST /tasks/ crea una nueva tarea"""
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer


