from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.api import TaskViewSet
# api_urls.py: enrutamiento de la API (DRF).
# Registra el ViewSet de tareas en un router para crear rutas REST automáticamente.

router = DefaultRouter()
router.register('tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
]


