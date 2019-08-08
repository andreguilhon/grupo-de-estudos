import os
from flask import json, request
from flask_restful import Resource
from carro.models import Carro
from database import db

filedb = os.path.join('./', 'data', 'carrodb.json')


class CarrosView(Resource):
    def get(self):
        carros = Carro.query.all()
        carros_list = []
        for carro in carros:
            carros_list.append({'codigo': carro.id,
                                'marca': carro.marca,
                                'modelo': carro.modelo,
                                'preco': carro.preco
                                })
        return carros_list

    def post(self):
        carro_json = request.get_json()
        carro = Carro()
        carro.marca = carro_json['marca']
        carro.modelo = carro_json['modelo']
        carro.preco = carro_json['preco']
        db.session.add(carro)
        db.session.commit()
        return 'ok'


class CarroView(Resource):
    def get(self, codigo):
        carro = Carro.query.get(codigo)
        carro_json = {'codigo': carro.id,
                      'marca': carro.marca,
                      'modelo': carro.modelo,
                      'preco': carro.preco}
        return carro_json

    def put(self, codigo):
        carro_request = request.get_json()
        carro = Carro.query.get(codigo)
        if 'marca' in carro_request:
            carro.marca = carro_request['marca']
        if 'modelo' in carro_request:
            carro.modelo = carro_request['modelo']
        if 'preco' in carro_request:
            carro.preco = carro_request['preco']

        db.session.add(carro)
        db.session.commit()

        return "OK"

    def delete(self, codigo):
        carro = Carro.query.get(codigo)
        db.session.delete(carro)
        db.session.commit()
        return "Ok"
