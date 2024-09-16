from ninja import NinjaAPI
from django.shortcuts import get_object_or_404
from .models import Usuario
from .schemas import UsuarioSchema, UsuarioCreateSchema, UsuarioUpdateSchema

api = NinjaAPI()

@api.post("/usuarios/")
def crear_usuario(request, payload: UsuarioCreateSchema):
    usuario = Usuario.objects.create(**payload.dict())
    return {"success": True, "usuario_id": usuario.id}

@api.get("/usuarios/{usuario_id}/", response=UsuarioSchema)
def obtener_usuario(request, usuario_id: int):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    return usuario

@api.put("/usuarios/{usuario_id}/", response=UsuarioSchema)
def modificar_usuario(request, usuario_id: int, payload: UsuarioUpdateSchema):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    for attr, value in payload.dict().items():
        setattr(usuario, attr, value)
    usuario.save()
    return usuario

@api.delete("/usuarios/{usuario_id}/")
def eliminar_usuario(request, usuario_id: int):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario.delete()
    return {"success": True}
