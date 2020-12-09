from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT

from seguridad import authenticate, identity
from B.usuario2 import Registro_de_usuario
from B.categorias2 import Categorias, CategoriaList
from B.producto2 import Productos, ProductoList

app = Flask(__name__)
app.secret_key = 'Laura'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_AUTH_USERNAME_KEY'] = "usuario"
app.config['JWT_AUTH_PASSWORD_KEY'] = "contrasena"
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(Productos, '/producto/<string:name>')
api.add_resource(Categorias, '/categorias/<string:name>')
api.add_resource(CategoriaList, '/productos')

api.add_resource(Registro_de_usuario, '/registro')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=4000, debug=True)