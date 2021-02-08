from flask_restful import Resource, reqparse
from Models.product import ProductModel
from flask_jwt import jwt_required
from flask import request
from seed import product

class Products(Resource):
    parser = reqparse.RequestParser()

    @jwt_required()
    def get(self, name):
        name = ProductModel(name)
        if name:
            return name.json()
        return {'message': 'Name not found'}

    def post(self):
        data = request.get_json()
        name = data.get('name', None)
        size = data.get('size', None)

        if (ProductModel.find_by_name(name)):
            return {'message': "Product already registered"}, 500

        product = ProductModel(data['name'], data['size'])
        product.save_to_db()

        return {'message': f'Successfully created the product {name}', 'product': product.json() }

    def delete(self):
        data = request.get_json()
        id = data.get('id', None)
        product = ProductModel.find_by_id(id)

        if not product:
            return {"message": "Product does not exist"}, 500

        product.delete_from_db()
        return {'message': 'Removed.'}

    def put(self):
        data = request.get_json()
        name = data.get('name', None)
        id = data.get('id', None)

        if (not name):
            return {"message": "Name is needed"}, 500

        product = ProductModel.find_by_id(id)

        if not product:
            return {"message": "Product does not exist"}, 500

        product.name = name
        product.save_to_db()

        return {"message": "Updated product", "product": product.json()}


class ProductList(Resource):
    @jwt_required()
    def get(self):
        return {'Product': list(map(lambda x: x.json(), ProductModel.query.all()))}