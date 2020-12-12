from db import db
from .categorias import CategoriaModel

class ProductoModel(db.Model):
    __tablename__ = 'producto'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    valor = db.Column(db.Float(precision=2))
    category_id = db.Column(db.Integer, db.ForeignKey('categoria.id'))

    def __init__(self, name, valor, category_id):
        self.name = name
        self.valor = valor
        self.category_id = category_id

    def json(self):
        return {'producto': self.name, 'valor': self.valor, 'category_id': self.category_id, 'id': self.id, 'categoria': CategoriaModel.find_by_id(self.category_id).json() if self.category_id else None}

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