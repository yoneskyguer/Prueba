from db import db
from .product import ProductModel

class CategoryModel(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    quantity = db.Column(db.Float(precision=2))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))

    def __init__(self, name, quantity, product_id):
        self.name = name
        self.quantity = quantity
        self.product_id = product_id

    def json(self):
        return {'category': self.name, 'quantity': self.quantity, 'product_id': self.product_id, 'id': self.id, 'product': ProductModel.find_by_id(self.product_id).json() if self.product_id else None}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()