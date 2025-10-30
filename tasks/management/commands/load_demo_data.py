from django.core.management.base import BaseCommand
from tasks.models import Task

class Command(BaseCommand):
    help = 'Crea datos demo de tasks'

    def handle(self, *args, **options):
        Task.objects.all().delete()
        demo_tasks = [
            
            {"title": "Revisar Desviación Presupuestaria", "description": "Analizar la diferencia de presupuesto."},
            {"title": "Cargar Facturas de Proveedores", "description": "Registrar los gastos en el sistema de Control."},
            
            
            {"title": "Inspeccionar Consumo Combustible", "description": "Revisar los registros de combustible."},
            {"title": "Registrar Abastecimiento Semanal de Combustible", "description": "Ingresar petróleo recibido."},

            
            {"title": "Programar Mantención Preventiva", "description": "Planificar Próximo Mantenimiento."},
            {"title": "Cerrar Orden de Trabajo", "description": "Documentar la reparación en máquina."},
        ]
        for task in demo_tasks:
            Task.objects.create(**task)
        self.stdout.write(self.style.SUCCESS('Demo tasks de gestión operacional creadas con éxito!'))
