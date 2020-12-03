import sqlite3
from db import db


class UserModel(db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(80))
    contrasena = db.Column(db.String(80))

    def __init__(self, usuario, contrasena):
        self.usuario = usuario
        self.contrasena = contrasena

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_usuario(cls, usuario):
        return cls.query.filter_by(usuario=usuario).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()