from flask.json import JSONEncoder
from carro.models import Carro
from marca.models import Marca


class CarroEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Carro):
            return {
                'codigo': obj.id,
                'marca': obj.marca.nome,
                'modelo': obj.modelo,
                'preco': obj.preco
            }
        elif isinstance(obj, Marca):
            return {
                'id': obj.id,
                'nome': obj.nome
            }
        return super(CarroEncoder, self).default(obj)
