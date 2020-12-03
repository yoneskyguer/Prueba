from flask_restful import Resource, reqparse
from A.producto import ProductoModel


class Productos(Resource):
    def get(self, producto):
        producto = Productos(producto)
        if producto:
            return producto.json()
        return {'message': 'Artículo no encontrado'}

    def post(self):
        data = Productos.parser.parse_args()

        """if ProductoModel.find_by_usuario(name):
            return {'message': 'Ya exite un artículo con este usuario.'.format(name)}, 400"""

        name = ProductoModel(data['name'], data['valor'])
        name.save_to_db()

        return {'message': 'Ocurrio un error al ingresar el artículo.'}, 500

        return name.json(), 201

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
        return {'productos': list(map(lambda x: x.json(), CategoriaModel.query.all()))}