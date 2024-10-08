# sitio de usuarios

Este proyecto consiste en una aplicación de Django que proporciona una API REST para gestionar usuarios y un sitio web que permite la carga masiva de datos de usuarios mediante archivos CSV. El proyecto se divide en dos aplicaciones: `api_usuarios` para la API REST y `sitio_usuarios` para la interfaz web.

## Características

- **API REST con Django-Ninja**: Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los usuarios.
- **Sitio Web para Carga Masiva**: Permite la carga de usuarios mediante un archivo CSV, validando y procesando los datos.

## Tecnologías Utilizadas

- Python 3.9
- Django 4.x
- Django-Ninja
- HTML y CSS para la interfaz web

## Estructura del Proyecto

- `gestion_usuarios/`: Proyecto principal de Django.
- `api_usuarios/`: Aplicación que contiene la lógica de la API REST.
- `sitio_usuarios/`: Aplicación que contiene la interfaz web para la carga de usuarios.

## Instalación y Configuración

Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local.

### Prerrequisitos

- Python 3.9 o superior
- pip (Python package installer)
- Virtualenv (opcional, pero recomendado)

### Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/oscarPyth/sitio_usuarios
   cd gestion_usuarios/gestion_usuarios
   ```

2. **Crear un entorno virtual (opcional, pero recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa venv\\Scripts\\activate
   ```

3. **Instalar las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplicar las migraciones de la base de datos:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crear un superusuario para acceder al admin de Django:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Ejecutar el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```

### Uso de la API REST

La API REST está disponible en la ruta `/api/`. Aquí tienes las principales rutas:

- **Crear un usuario:**
  ```
  POST /api/usuarios/
  ```
  Cuerpo de la solicitud (JSON):
  ```json
  {
      \"nombre\": \"Juan\",
      \"apellido_paterno\": \"Pérez\",
      \"apellido_materno\": \"García\",
      \"edad\": 30,
      \"nombre_cuenta\": \"juanp\",
      \"contraseña\": \"password\"
  }
  ```

- **Obtener un usuario por ID:**
  ```
  GET /api/usuarios/{usuario_id}/
  ```

- **Modificar un usuario:**
  ```
  PUT /api/usuarios/{usuario_id}/
  ```

- **Eliminar un usuario:**
  ```
  DELETE /api/usuarios/{usuario_id}/
  ```

### Uso del Sitio Web para la Carga Masiva de Usuarios

El sitio web para la carga masiva está disponible en la ruta `/cargar_usuarios/`. Para cargar usuarios:

1. Navega a `/cargar_usuarios/`.
2. Selecciona un archivo CSV con los datos de los usuarios. ( se encuentra en la raiz del proyecto) El CSV debe tener el siguiente formato:
   ```csv
   nombre,apellido_paterno,apellido_materno,edad,nombre_cuenta,contraseña
   Juan,Pérez,García,30,juanp,password
   María,López,Hernández,25,mlopez,password
   Carlos,Fernández,Martínez,28,carlosf,password
   ```
3. Haz clic en el botón \"Cargar\".

### Notas Adicionales

- Asegúrate de que los `nombre_cuenta` sean únicos para evitar errores de duplicados al cargar datos.
- Los mensajes de éxito o error se mostrarán después de la carga del archivo CSV.
- Si subes nombres que ya existen se omitira esa carga



