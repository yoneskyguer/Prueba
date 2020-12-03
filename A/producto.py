from db import db


class ProductoModel(db.Model):
    __tablename__ = 'productos'

    id = db.Column(db.Integer, primary_key=True)
    producto = db.Column(db.String(80))
    valor = db.Column(db.Float(precision=2))

    def __init__(self, producto, valor):
        self.producto = producto
        self.valor = valor

    def json(self):
        return {'producto': self.producto, 'categorias': [name.json() for name in self.producto.all()]}    

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()