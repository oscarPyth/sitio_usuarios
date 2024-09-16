from ninja import Schema


class UsuarioSchema(Schema):
    id: int
    nombre: str
    apellido_paterno: str
    apellido_materno: str
    edad: int
    nombre_cuenta: str


class UsuarioCreateSchema(Schema):
    nombre: str
    apellido_paterno: str
    apellido_materno: str
    edad: int
    nombre_cuenta: str
    contraseña: str


class UsuarioUpdateSchema(Schema):
    nombre: str = None
    apellido_paterno: str = None
    apellido_materno: str = None
    edad: int = None
    nombre_cuenta: str = None
    contraseña: str = None
