from django.shortcuts import render, redirect
from django.contrib import messages
import csv
from api_usuarios.models import Usuario

def cargar_usuarios_csv(request):
    if request.method == "POST":
        try:
            csv_file = request.FILES['file']
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'Por favor, sube un archivo CSV.')
                return redirect('cargar_usuarios_csv')

            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)

            usuarios_creados = 0
            usuarios_omitidos = 0

            for row in reader:
                # Verificar si el nombre_cuenta ya existe
                if Usuario.objects.filter(nombre_cuenta=row['nombre_cuenta']).exists():
                    usuarios_omitidos += 1  # Contador para los omitidos
                    continue  # Salta este registro

                # Crear el usuario si no hay duplicado
                Usuario.objects.create(
                    nombre=row['nombre'],
                    apellido_paterno=row['apellido_paterno'],
                    apellido_materno=row['apellido_materno'],
                    edad=int(row['edad']),
                    nombre_cuenta=row['nombre_cuenta'],
                    contraseña=row['contraseña']
                )
                usuarios_creados += 1  # Contador para los creados

            messages.success(request, f'Usuarios creados: {usuarios_creados}. Usuarios omitidos por duplicados: {usuarios_omitidos}.')
        except Exception as e:
            messages.error(request, f'Error al procesar el archivo: {e}')

    return render(request, 'sitio_usuarios/cargar_usuarios.html')
