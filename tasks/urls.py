from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.TaskListView.as_view(), name="index"),
    path("create/", views.TaskCreateView.as_view(), name="create"),
    path("toggle/<int:pk>/", views.TaskToggleView.as_view(), name="toggle"),#url para toggle
    path("delete/<int:pk>/", views.TaskDeleteView.as_view(), name="delete"),
    path("update/<int:pk>/", views.TaskUpdateView.as_view(), name="update"),
    path("edit-form/<int:pk>/", views.TaskEditFormView.as_view(), name="edit-form"),
    path("detail/<int:pk>/", views.TaskDetailView.as_view(), name="detail"),
    path("stats/", views.TaskStatsView.as_view(), name="stats"),
    path("export/csv/", views.TaskExportCSVView.as_view(), name="export-csv"),
]
