from flask_restful import Resource, reqparse
from Models.producto import ProductoModel
from flask import request

class Productos(Resource):
    def get(self, producto):
        producto = Productos(producto)
        if producto:
            return producto.json()
        return {'message': 'Artículo no encontrado'}

    def post(self):
        data = request.get_json()
        producto = ProductoModel(data['name'], data['valor'], data.get('category_id'))
        if not producto:
            return {'message': 'Ocurrio un error al ingresar el artículo.'}, 500
        producto.save_to_db()

        return producto.json(), 201

    def delete(self, producto):
        producto = Productos(producto)
        if producto:
            producto.delete_from_db()
            return {'message': 'Eliminado.'}
        return {'message': 'Artículo no encontrado.'}, 404

    def put(self, name):
        data = Productos.parser.parse_args()
        name = ProductoModel(name)
        if name is None:
            name.name = data['name']
        else:
            name = ProductoModel(name, **data)
        name.save_to_db()
        return name.json()


class ProductoList(Resource):
    def get(self):
        return {'productos': list(map(lambda x: x.json(), ProductoModel.query.all()))}