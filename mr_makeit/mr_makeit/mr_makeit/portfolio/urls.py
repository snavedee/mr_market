from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),  # List all projects
    # Add detail view later if needed: path('<int:pk>/', views.project_detail, name='project_detail'),
]