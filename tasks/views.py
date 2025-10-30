# tasks/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, View
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm
import csv


# LISTAR TAREAS
class TaskListView(ListView):
    """Vista principal que lista todas las tareas"""
    model = Task
    template_name = "tasks/index.html"
    context_object_name = "tasks"

    def get_queryset(self):
        """Filtra tareas según parámetro 'filter' en la URL"""
        qs = super().get_queryset().order_by('-created_at')
        filter_type = self.request.GET.get('filter', 'all')

        if filter_type == 'pending':
            qs = qs.filter(completed=False)
        elif filter_type == 'completed':
            qs = qs.filter(completed=True)
        return qs

    def get_context_data(self, **kwargs):
        """Agrega contadores al contexto"""
        context = super().get_context_data(**kwargs)
        all_tasks = Task.objects.all()
        context['completed_count'] = all_tasks.filter(completed=True).count()
        context['pending_count'] = all_tasks.filter(completed=False).count()
        return context

    def get_template_names(self):
        """Si es una petición HTMX, devuelve solo el partial de la lista"""
        if self.request.headers.get('HX-Request'):
            return ["tasks/partials/task_list_partial.html"]
        return [self.template_name]


# CREAR TAREA
class TaskCreateView(CreateView):
    """Vista para crear una nueva tarea"""
    model = Task
    form_class = TaskForm
    template_name = "tasks/partials/task_form_partial.html"

    def form_valid(self, form):
        self.object = form.save()

        if self.request.headers.get('HX-Request'):
            # Renderizar la nueva tarea
            task_html = render_to_string(
                "tasks/partials/task_row_partial.html",
                {'task': self.object},
                request=self.request
            )
            
            # Devolver formulario limpio + nueva tarea
            response = HttpResponse(task_html)
            # Trigger para actualizar estadísticas
            response['HX-Trigger'] = 'taskChanged'
            return response

        return redirect(reverse_lazy('tasks:index'))

    def form_invalid(self, form):
       
        if self.request.headers.get('HX-Request'):
            html = render_to_string(
                self.template_name,
                {'form': form},
                request=self.request
            )
            response = HttpResponse(html)  # 200 para que HTMX haga swap
            response['HX-Retarget'] = '#task-create-form'  # reemplaza el propio form
            response['HX-Reswap'] = 'outerHTML'
            return response
        return super().form_invalid(form)


# TOGGLE COMPLETADO
class TaskToggleView(View):
    """Vista para marcar/desmarcar tarea como completada"""
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.completed = not task.completed
        task.save()

        html = render_to_string(
            "tasks/partials/task_row_partial.html",
            {'task': task},
            request=request
        )
        response = HttpResponse(html)
        response['HX-Trigger'] = 'taskChanged'
        return response


# ELIMINAR TAREA
class TaskDeleteView(View):
    """Vista para eliminar una tarea"""

    def post(self, request, pk):
       
        task = get_object_or_404(Task, pk=pk)
        task.delete()
      
        response = HttpResponse("")
        response['HX-Trigger'] = 'taskChanged'
        return response

    
    def delete(self, request, pk):
        return self.post(request, pk)


# MOSTRAR FORMULARIO DE EDICIÓN
class TaskEditFormView(View):
    """Vista que devuelve el formulario de edición inline"""
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(instance=task)

        html = render_to_string(
            "tasks/partials/task_edit_form_partial.html",
            {'form': form, 'task': task},
            request=request
        )
        return HttpResponse(html)


#ACTUALIZAR TAREA
class TaskUpdateView(UpdateView):
    """Vista para actualizar una tarea existente"""
    model = Task
    form_class = TaskForm
    template_name = "tasks/partials/task_edit_form_partial.html"

    def form_valid(self, form):
        self.object = form.save()

        if self.request.headers.get('HX-Request'):
            html = render_to_string(
                "tasks/partials/task_row_partial.html",
                {'task': self.object},
                request=self.request
            )
            response = HttpResponse(html)
            response['HX-Trigger'] = 'taskChanged'
            return response

        return redirect(reverse_lazy('tasks:index'))

    def form_invalid(self, form):
        if self.request.headers.get('HX-Request'):
            html = render_to_string(
                self.template_name,
                {'form': form, 'task': self.object},
                request=self.request
            )
            return HttpResponse(html, status=400)
        return super().form_invalid(form)


# DETALLE (para cancelar edición)
class TaskDetailView(View):
    """Vista para volver al modo lectura luego de editar"""
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        html = render_to_string(
            "tasks/partials/task_row_partial.html",
            {'task': task},
            request=request
        )
        return HttpResponse(html)


# STATS PARCIAL PARA CONTADORES
class TaskStatsView(View):
    """Devuelve el parcial con los contadores de tareas"""
    def get(self, request):
        all_tasks = Task.objects.all()
        context = {
            'total_count': all_tasks.count(),
            'completed_count': all_tasks.filter(completed=True).count(),
            'pending_count': all_tasks.filter(completed=False).count(),
        }
        html = render_to_string(
            "tasks/partials/stats_partial.html",
            context,
            request=request
        )
        return HttpResponse(html)


#EXPORTAR CSV
class TaskExportCSVView(View):
    """Exporta todas las tareas en formato CSV"""
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="tasks_export.csv"'

        writer = csv.writer(response)
        writer.writerow(['id', 'title', 'description', 'completed', 'created_at'])
        for task in Task.objects.all().order_by('-created_at'):
            writer.writerow([
                task.id,
                task.title,
                task.description,
                'true' if task.completed else 'false',
                task.created_at.isoformat(),
            ])

        return response
