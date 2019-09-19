from flask import request, jsonify
from flask_restful import Resource
from marca.models import Marca
from database import db
from http import HTTPStatus


class MarcaView(Resource):

    def put(self, marca_id):
        try:
            marca_json = request.get_json()
            if 'nome' not in marca_json:
                response = jsonify({'errors': 'Favor enviar o novo nome da marca.'})
                response.status_code = HTTPStatus.BAD_REQUEST
                return response
            marca = Marca.query.get(marca_id)
            marca.nome = marca_json['nome']
            db.session.add(marca)
            db.session.commit()
            return 'Registro alterado.'
        except:
            flask_response = jsonify({'errors': 'Ocorreu um erro genérico'})
            flask_response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            return flask_response

    def get(self, marca_id):
        try:
            marca = Marca.query.get(marca_id)
            return jsonify(marca)
        except:
            flask_response = jsonify({'errors': 'Ocorreu um erro genérico'})
            flask_response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            return flask_response


class MarcasView(Resource):
    def post(self):
        try:
            marca_json = request.get_json()
            marca = Marca()
            marca.nome = marca_json['nome']
            db.session.add(marca)
            db.session.commit()
            return "Ok"
        except:
            flask_response = jsonify({'errors': 'Ocorreu um erro genérico'})
            flask_response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            return flask_response

    def get(self):
        try:
            marcas = Marca.query.all()
            return jsonify(marcas)
        except:
            flask_response = jsonify({'errors': 'Ocorreu um erro genérico'})
            flask_response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            return flask_response
