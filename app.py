from flask import Flask, jsonify, request
import json

app = Flask(__name__)

developers = [
    {
        'id': 0,
        'nome': Wellisson',
        'habilidades':['Python', 'Flask']
    },
    {
        'id': 1,
        'nome': 'Wellbugs',
        'habilidades': ['PHP', 'Laravel']
    }
]

# devolve um desenvolvedor pelo ID, também altera e deleta um desenvolvedor
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def developer(id):
    if request.method == 'GET':
        try:
            response = developers[id]
        except IndexError:
            response = {'status': 'error', 'message': 'Desenvolvedor de ID {} não existe'.format(id)}
        except Exception:
            response = {'status': 'error', 'message': 'Erro desconhecido. Procure o administrador da API'}
        return jsonify(response)

    if request.method == 'PUT':
        dados = json.loads(request.data)
        developers[id] = dados
        return jsonify(dados)

    if request.method == 'DELETE':
        developers.pop(id)
        return jsonify({'status':'sucesso', 'mensagem':'Registro excluído'})

# Lista todos os desenvolvedor e permite registrar um novo desenvolvedor
@app.route('/dev/', methods=['POST', 'GET'])
def lista_developers():
    if request.method == 'POST':
        data = json.loads(request.data)
        index = len(developers)
        data['id'] = index
        developers.append(data)
        return jsonify(developers[index])
    
    if request.method == 'GET':
        return jsonify(developers)

if __name__ == '__main__':
    app.run(debug=True)