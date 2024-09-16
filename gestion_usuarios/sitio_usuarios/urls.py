from django.urls import path
from .views import cargar_usuarios_csv

urlpatterns = [
    path('cargar_usuarios/', cargar_usuarios_csv, name='cargar_usuarios_csv'),
]
