from flask import Flask
from flask_restful import Api
from carro import Carro, Carros
from flask_cors import CORS


app = Flask(__name__)
api = Api(app)
CORS(app)


api.add_resource(Carros, '/carros/')
api.add_resource(Carro, '/carros/<int:codigo>')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
