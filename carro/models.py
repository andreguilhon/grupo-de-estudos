from database import db


class Carro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String)
    preco = db.Column(db.Float)
    id_marca = db.Column(db.Integer, db.ForeignKey('marca.id'))
    marca = db.relationship('Marca', backref='marca', lazy=True)


class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, unique=True)
