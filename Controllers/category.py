from flask_restful import Resource, reqparse
from Models.category import CategoryModel
from flask_jwt import jwt_required
from flask import request
from seed import category

class Categories(Resource):

    @jwt_required()
    def get(self, category):
        category = Categories(category)
        if categories:
            return category.json()
        return {'message': 'Category not found'}

    def getCategory(): 
        return jsonify(active_categories)

        return jsonify({"message": "Category added successfully", "categories": Categories})

    def post(self):
        data = request.get_json()
        category = CategoryModel(data['name'], data['quantity'], data.get('product_id'))
        if not category:
            return {'message': 'An error occurred when entering the category.'}, 500
        category.save_to_db()

        return category.json(), 201

    def delete(self):
        data = request.get_json()
        id = data.get('id', None)
        category = CategoryModel.find_by_id(id)

        if not category:
            return {'message': 'Category not found.'}, 500

        category.delete_from_db()
        return {'message': 'Removed.'}, 404

    def put(self):
        data = request.get_json()
        name = data.get('name', None)
        id = data.get('id', None)

        if (not name):
            return {"message": "Name is required."}, 500

        category = CategoryModel.find_by_id(id)

        if not category:
            return {"message": "Category does not exist."}, 500

        category.name = name
        category.save_to_db()

        return {"message": "Updated category", "Categories": category.json()}


class CategoryList(Resource):
    @jwt_required()
    def get(self):
        return {'categories': list(map(lambda x: x.json(), CategoryModel.query.all()))}