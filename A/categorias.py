from db import db


class CategoriaModel(db.Model):
    __tablename__ = 'categorias'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    valor = db.Column(db.Float(precision=2))

    def __init__(self, name, valor):
        self.name = name
        self.valor = valor

    def json(self):
        return {'name': self.name, 'valor': self.valor}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()