from flask_restful import Resource, reqparse
from Models.producto import ProductoModel
from flask_jwt import jwt_required
from flask import request
from productos import productos

class Productos(Resource):

    @jwt_required()
    def get(self, producto):
        producto = Productos(producto)
        if producto:
            return producto.json()
        return {'message': 'Artículo no encontrado'}

    def addProductos():
        nuevo_producto = {
            "name": request.json['name'],
            "valor": request.json['valor'],
            "cantidad": request.json['cantidad']
        }
        productos.append(nuevo_producto)
        return jsonify({"message": "Producto agregado con éxito", "Productos": Productos})

    def post(self):
        data = request.get_json()
        producto = ProductoModel(data['name'], data['valor'], data.get('category_id'))
        if not producto:
            return {'message': 'Ocurrio un error al ingresar el artículo.'}, 500
        producto.save_to_db()

        return producto.json(), 201

    def delete(self):
        data = request.get_json()
        id = data.get('id', None)
        producto = ProductoModel.find_by_id(id)

        if not producto:
            return {'message': 'Producto no existe.'}, 500

        producto.delete_from_db()
        return {'message': 'Eliminado.'}, 404

    def put(self):
        data = request.get_json()
        name = data.get('name', None)
        id = data.get('id', None)

        if (not name):
            return {"message": "Es necesario name."}, 500

        producto = ProductoModel.find_by_id(id)

        if not producto:
            return {"message": "Producto no existe."}, 500

        producto.name = name
        producto.save_to_db()

        return {"message": "Producto editado", "Producto": producto.json()}


class ProductoList(Resource):
    @jwt_required()
    def get(self):
        return {'productos': list(map(lambda x: x.json(), ProductoModel.query.all()))}