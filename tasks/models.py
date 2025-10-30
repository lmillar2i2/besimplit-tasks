from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name='Título')
    description = models.TextField(blank=True, verbose_name='Descripción')
    completed = models.BooleanField(default=False, verbose_name='Completada')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')

    class Meta:
        
        verbose_name = 'Tarea'
        verbose_name_plural = 'Lista de Tareas'
        ordering = ['-created_at']
        
    def __str__(self):
        return self.title
