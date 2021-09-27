from flask import Flask, request
from flask_restful import Resource, Api
from skills import Skills
import json

app = Flask(__name__)
api = Api(app)

developers = [
    {
        'id': 1,
        'nome': 'Wellisson',
        'skills': ['Python', 'Flask']
    },
    {
        'id': 1,
        'nome': 'Wellbugs',
        'skills': ['Python', 'Django']
    }
]

# devolve um desenvolvedor pelo ID, também altera e deleta um desenvolvedor
class Developer(Resource):
    def get(self, id):
        try:
            response = developers[id]
        except IndexError:
            response = {'status': 'error', 'message': 'Desenvolvedor de ID {} não existe'.format(id)}
        except Exception:
            response = {'status': 'error', 'message': 'Erro desconhecido. Procure o administrador da API'}
        return response

    def put(self, id):
        data = json.loads(request.data)
        developers[id] = data
        return data

    def delete(self, id):
        developers.pop(id)
        return {'status':'sucesso', 'mensagem':'Registro excluído'}

# Lista todos os desenvolvedor e permite registrar um novo desenvolvedor
class ListDevelopers(Resource):
    def get(self):
        return developers

    def post(self):
        data = json.loads(request.data)
        index = len(developers)
        data['id'] = index
        developers.append(data)
        return developers[index]

api.add_resource(Developer, '/dev/<int:id>/')
api.add_resource(ListDevelopers, '/dev/')
api.add_resource(Skills, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)