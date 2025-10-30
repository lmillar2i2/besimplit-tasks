# tasks/forms.py
from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    """Formulario para crear y editar tareas"""
    
    class Meta:
        model = Task
        fields = ['title', 'description']
        labels = {
            'title': 'Título de la tarea',
            'description': 'Descripción (opcional)',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-colors',
                'placeholder': 'Ej: Registrar tareas de la semana',
                'maxlength': '255',
                'required': True,
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-colors resize-none',
                'placeholder': 'Agrega detalles adicionales sobre esta tarea...',
                'rows': 3,
            }),
        }
        error_messages = {
            'title': {
                'required': 'El título es obligatorio.',
                'max_length': 'El título no puede exceder 255 caracteres.',
            },
        }
    
    def clean_title(self):
        """Validación  para el título"""
        title = self.cleaned_data.get('title')
        
        if title:
            # Elimina espacios en blanco extra
            title = ' '.join(title.split())
            
            # Valida longitud mínima
            if len(title) < 3:
                raise forms.ValidationError(
                    'El título debe tener al menos 3 caracteres.'
                )
            
            # Valida que no sea solo números
            if title.isdigit():
                raise forms.ValidationError(
                    'El título no puede contener solo números.'
                )
        
        return title
    
    def clean_description(self):
        """Validación para la descripción"""
        description = self.cleaned_data.get('description')
        
        if description:
            # Elimina espacios en blanco extra
            description = ' '.join(description.split())
            
            # Limita longitud máxima (opcional)
            if len(description) > 500:
                raise forms.ValidationError(
                    'La descripción no puede exceder 500 caracteres.'
                )
        
        return description or ''  # Devuelve string vacío si es None
    
    def __init__(self, *args, **kwargs):
        """Inicialización personalizada del formulario"""
        super().__init__(*args, **kwargs)
        
        # Agrega asterisco a campos requeridos
        for field_name, field in self.fields.items():
            if field.required:
                field.label = f"{field.label} *"
        
        # Configuración adicional para cada campo
        self.fields['title'].help_text = 'Mínimo 3 caracteres'
        self.fields['description'].required = False
        self.fields['description'].help_text = 'Máximo 500 caracteres'