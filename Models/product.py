from db import db


class ProductModel(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    size = db.Column(db.String(80))

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def json(self):
        return {'id': self.id, 'name': self.name, 'size': self.size}

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