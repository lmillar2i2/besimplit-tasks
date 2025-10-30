# Besimplit Tasks

Aplicación de tareas con Django + HTMX + Tailwind + DRF (SQLite).
Entorno de desarrollo WSL2 - UBUNTU


## ✨ Features Principales

- **CRUD completo sin recargas** - Gracias a HTMX
- **Filtros interactivos** - Todas/Pendientes/Completadas
- **Export CSV** - Descarga de tareas  en CSV
- **UI moderna** - Tailwind CSS con animaciones suaves
- **API REST** - Endpoints DRF para integración externa
- **Datos demo** - Command management para testing rápido
- **Stats simple** - Total, completadas, pendientes

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


## Trade-offs y decisiones

- Simplicidad primero por lo que se prioriza velocidad de entrega sobre funcionalidades avanzadas.
- SQLite en desarrollo, fácil y sin configuración.
- Tailwind vía CDN (sin build) para desarrollo y arranque rápido.
- API DRF mínima y sin autenticación ideal para el desafío pero no apto para producción sin seguridad, auth, permisos, rate limiting,etc.
- Sin paginación ni filtros avanzados en API, pero puede generar problemas rendimiento con grandes volúmenes de datos.
- Exportación CSV generada en servidor sin colas de forma simple pero puede bloquear o tardar con datasets grandes.
- Validación y manejo de errores básicos suficientes para el desafío pero faltan mensajes y validacions más extra.
- Sin pruebas por tiempo. 
- CBV/GCBV sobre FBV, menos código y mayor reutilización y rapidez (ListView/CreateView/UpdateView/View)
- POST para toggle/eliminar/crear/editar en UI HTMX, simplifica formularios y CSRF pero no cumple reglas de REST puras estricta.
- Entorno de desarrollo con venv en vez de Docker. Más rápido para desarrollo local y menor fricción pero menor reproducibilidad entre distintos equipos.

### Próximas mejoras sugeridas
- Stats enriquecido y creación de dashboard con`pandas y `Chart.js o Plotly en frontend.
- Django auth para UI y JWT/Token para API (DRF), permisos por vista y rate limiting.
- API más robusta con paginación, filtros, ordenamiento, validación avanzada.
- Exportación asíncrona de tal forma mover CSV a tareas en segundo plano usando Celery.
- Uso de contenedores Docker y Docker Compose con Postgres y Redis para mejorar compativilidad en producción y desarrollo y tener alta escalabilidad.
