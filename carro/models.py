from database import db


class Carro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String)
    modelo = db.Column(db.String)
    preco = db.Column(db.Float)
