"""
URL configuration for gestion_usuarios project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from api_usuarios.api import api  # Asegúrate de importar el objeto api, no el módulo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),  # Incluye correctamente las URLs del objeto NinjaAPI
    path('', include('sitio_usuarios.urls')),  # Incluye las URLs de sitio_usuarios
]
