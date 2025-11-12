from django.db import models
# models.py, define el modelo principal de la app (Task).


class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name='Título')
    category = models.models.ForeignKey("Category", verbose_name=_("categoría"), on_delete=models.CASCADE)
    description = models.TextField(blank=True, verbose_name='Descripción')
    completed = models.BooleanField(default=False, verbose_name='Completada')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')

    class Meta:
        # nombres legibles en admin y orden por defecto
        verbose_name = 'Tarea'
        verbose_name_plural = 'Lista de Tareas'
        ordering = ['-created_at']
        
    def __str__(self):
        # representación corta y útil en admin y logs
        return self.title
    
    
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre categoría")
    
