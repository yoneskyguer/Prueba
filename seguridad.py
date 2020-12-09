from werkzeug.security import safe_str_cmp
from Models.usuario import UserModel

def authenticate(usuario, contrasena):
    usuario = UserModel.find_by_usuario(usuario)

    if usuario and safe_str_cmp(usuario.contrasena, contrasena):
        return usuario
    return None

def identity(payload):
    id_usuario = payload['identity']
    return UserModel.find_by_id(id_usuario)