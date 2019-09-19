from flask.json import JSONEncoder
from carro.models import Carro


class CarroEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Carro):
            return {
                'codigo': obj.id,
                'marca': obj.marca.nome,
                'modelo': obj.modelo,
                'preco': obj.preco
            }
        return super(CarroEncoder, self).default(obj)
