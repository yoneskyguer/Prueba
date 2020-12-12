from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT, jwt_required

from seguridad import authenticate, identity
from Controllers.usuario import Registro_de_usuario
from Controllers.categorias import Categorias, CategoriaList
from Controllers.producto import Productos, ProductoList
from Controllers.productos import productos

app = Flask(__name__)
app.secret_key = 'Laura'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_AUTH_USERNAME_KEY'] = "usuario"
app.config['JWT_AUTH_PASSWORD_KEY'] = "contrasena"
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(Productos, '/producto')
api.add_resource(ProductoList, '/productos')
api.add_resource(Categorias, '/categoria')
api.add_resource(CategoriaList, '/categorias')
api.add_resource(productos, '/productos')

api.add_resource(Registro_de_usuario, '/registro')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=4000, debug=True)