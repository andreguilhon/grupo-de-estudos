import os
from flask import json, request
from flask_restful import Resource

filedb = os.path.join('./', 'data', 'carrodb.json')


class Carros(Resource):
    def get(self):
        with open(filedb) as carrodb:
            return json.load(carrodb)

    def post(self):
        carro = request.get_json()
        with open(filedb) as carrodb:
            lista_carro = json.load(carrodb)
            lista_carro.append(carro)
        with open(filedb, 'w') as carrodbrw:
            json.dump(lista_carro, carrodbrw)
        return 'Ok'


class Carro(Resource):
    def get(self, codigo):
        with open(filedb) as carrodb:
            lista_carros = json.load(carrodb)
            for carro in lista_carros:
                if carro['codigo'] == codigo:
                    return carro
            return 'boca mole'

    def put(self, codigo):
        carro_request = request.get_json()
        with open(filedb) as carrodb:
            lista_carros = json.load(carrodb)
            for carro in lista_carros:
                if carro['codigo'] == codigo:
                    carro_tmp = carro
                    lista_carros.remove(carro)
                    if 'marca' in carro_request:
                        carro_tmp['marca'] = carro_request['marca']
                    if 'modelo' in carro_request:
                        carro_tmp['modelo'] = carro_request['modelo']
                    if 'preco' in carro_request:
                        carro_tmp['preco'] = carro_request['preco']
                    lista_carros.append(carro_tmp)
        with open(filedb, 'w') as carrodbrw:
            json.dump(lista_carros, carrodbrw)

        return "OK"

    def delete(self, codigo):
        with open(filedb) as carrodb:
            lista_carros = json.load(carrodb)
            for carro in lista_carros:
                if carro['codigo'] == codigo:
                    lista_carros.remove(carro)
        with open(filedb, 'w') as carrodbrw:
            json.dump(lista_carros, carrodbrw)
        return "Ok"
