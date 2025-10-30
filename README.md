# Besimplit Tasks

Aplicación de tareas con Django + HTMX + Tailwind + DRF (SQLite).

## Requisitos
- Python 3.11+
- pip

## Setup

1) Entrar a la carpeta del proyecto
```bash
cd prueba_besimplit
```

2) Crear y activar entorno virtual
- Linux/Mac:
```bash
python -m venv .venv
source .venv/bin/activate
```
- Windows (PowerShell):
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

3) Instalar dependencias
```bash
pip install -r requirements.txt
```

4) Migraciones y datos demo
```bash
python manage.py migrate
python manage.py load_demo_data
```

5) Correr servidor
```bash
python manage.py runserver
```

## URLs

- UI principal (HTMX): `http://127.0.0.1:8000/`
  - Ver/filtrar/crear/editar/toggle/eliminar tareas sin recargar
  - Export CSV: botón “Exportar CSV”


- API (DRF):
  - GET `http://127.0.0.1:8000/api/tasks/`
  - POST `http://127.0.0.1:8000/api/tasks/`
    - Body JSON: `{ "title": "Texto", "description": "Opcional", "completed": false }`

## Notas
- Base de datos: SQLite (`db.sqlite3`)
- Tailwind via CDN (sin build)
- CSRF para HTMX configurado automáticamente en `tasks/templates/tasks/base.html`
