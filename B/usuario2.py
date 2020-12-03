from flask_restful import Resource, reqparse
from A.usuario import UserModel


class Registro_de_usuario(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('usuario',
                        type=str,
                        required=True,
                        help="Este espacio no puede estar vacío."
                        )
    parser.add_argument('contrasena',
                        type=str,
                        required=True,
                        help="Este espacio no puede estar vacío."
                        )

    def post(self):
        data = Registro_de_usuario.parser.parse_args()

        if UserModel.find_by_usuario(data['usuario']):
            return {"message": "Ya existe este usuario."}, 400

        usuario = UserModel(data['usuario'], data['contrasena'])
        usuario.save_to_db()

        return {"message": "Usuario creado con éxito."}, 201