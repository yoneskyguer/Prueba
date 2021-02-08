from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT, jwt_required

from segurity import authenticate, identity
from Controllers.user import User_register
from Controllers.product import Products, ProductList
from Controllers.category import Categories, CategoryList

app = Flask(__name__)
app.secret_key = 'Laura'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_AUTH_USERNAME_KEY'] = "user"
app.config['JWT_AUTH_PASSWORD_KEY'] = "password"
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(Products, '/product')
api.add_resource(ProductList, '/products')
api.add_resource(Categories, '/category')
api.add_resource(CategoryList, '/categories')


api.add_resource(User_register, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=4000, debug=True)