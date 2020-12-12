from flask_restful import Resource, reqparse
from Models.categorias import CategoriaModel
from flask_jwt import jwt_required
from flask import request

class Categorias(Resource):
    parser = reqparse.RequestParser()

    @jwt_required()
    def get(self, name):
        name = CategoriaModel(name)
        if name:
            return name.json()
        return {'message': 'Artículo no encontrado'}

    def post(self):
        data = request.get_json()
        name = data.get('name', None)

        if (CategoriaModel.find_by_name(name)):
            return {'message': "Categoria ya registrada"}, 500

        categoria = CategoriaModel(data['name'])
        categoria.save_to_db()

        return {'message': f'Creado con éxito la categoria {name}', 'categoria': categoria.json() }

    def delete(self):
        data = request.get_json()
        id = data.get('id', None)
        categoria = CategoriaModel.find_by_id(id)

        if not categoria:
            return {"message":"categoria no existe"}, 500

        categoria.delete_from_db()
        return {'message': 'Eliminado.'}

    def put(self):
        data = request.get_json()
        name = data.get('name', None)
        id = data.get('id', None)

        if (not name):
            return {"message":"Se necesita name"}, 500

        categoria = CategoriaModel.find_by_id(id)

        if not categoria:
            return {"message":"categoria no existe"}, 500

        categoria.name = name
        categoria.save_to_db()

        return {"message": "categoria actualizada", "categoria": categoria.json()}


class CategoriaList(Resource):
    @jwt_required()
    def get(self):
        return {'categorias': list(map(lambda x: x.json(), CategoriaModel.query.all()))}