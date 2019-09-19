from flask import Flask
from flask_restful import Api
from carro.views import CarroView, CarrosView
from flask_cors import CORS
from flask_migrate import Migrate
from database import db
from utils.json_serializer import CarroEncoder


app = Flask(__name__)
app.config.from_object('config.CarrosConfig')
api = Api(app)
CORS(app)
app.json_encoder = CarroEncoder

api.add_resource(CarrosView, '/carros/')
api.add_resource(CarroView, '/carros/<int:codigo>')
db.init_app(app)

migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

