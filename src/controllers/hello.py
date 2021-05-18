from typing import DefaultDict
from src.app import application
from flask import request, escape

#define uma rota /hello e permite apenas método GET
@application.route('/hello', methods=["GET"])
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {(escape(name))}!'

#tratamento de campo vazio para a rota /teste
@application.route("/teste")
@application.route("/teste/<msg>")
def teste(msg=None):
    if msg:
        return f'Testando {msg}!'
    else:
        return 'Testando alguma coisa!'

#outra forma de tratamento de campo vazio para a rota /teste2
@application.route("/teste2", defaults={"msg":None})
@application.route("/teste2/<msg>")
def teste2(msg):
    if msg:
        return f'Testando {msg}!'
    else:
        return 'Testando alguma coisa!'

#define que o parâmetro id da rota /teste3 deve ser inteiro
@application.route('/teste3/<int:id>')
def teste3(id):
    print(type(id))
    return f'ID * 100 = {id * 100}!'