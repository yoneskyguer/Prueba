from werkzeug.security import safe_str_cmp
from Models.user import UserModel

def authenticate(user, password):
    user = UserModel.find_by_user(user)

    if user and safe_str_cmp(user.password, password):
        return user
    return None

def identity(payload):
    id_user = payload['identity']
    return UserModel.find_by_id(id_user)