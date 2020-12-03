from flask_restful import Resource, reqparse
from A.categorias import CategoriaModel


class Categorias(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('valor',
                        type=float,
                        required=True,
                        help="Este espacio no puede estar vacío."
                        )

    def get(self, name):
        name = CategoriaModel(name)
        if name:
            return name.json()
        return {'message': 'Artículo no encontrado'}

    def post(self):
        data = Categorias.parser.parse_args()

        name = CategoriaModel(data['name'], data['valor'])
        name.save_to_db()

        return {'message': 'Creado.'}

    def delete(self):
        name = CategoriaModel(data['name'])
        if name:
            name.delete_from_db()
            return {'message': 'Eliminado.'}
        return {'message': 'Artículo no encontrado.'}, 404

    def put(self, name):
        data = Categorias.parser.parse_args()

        name = CategoriaModel(name)

        if name is None:
            name.name = data['name']
        else:
            name = CategoriaModel(name, **data)

        name.save_to_db()

        return name.json()
                

class CategoriaList(Resource):
    def get(self):
        return {'productos': list(map(lambda x: x.json(), CategoriaModel.query.all()))}