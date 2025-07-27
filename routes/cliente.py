from flask import Blueprint, jsonify, make_response, render_template, request
from database.cliente import Clientes  

cliente_routes = Blueprint('cliente_routes', __name__)
cliente_routes_api = Blueprint('cliente_routes_api', __name__) 

@cliente_routes.route('/lista', methods=['GET'])
def lista():
    return render_template('clientes.html', clientes=Clientes)

@cliente_routes.route('/detalhe/<int:cliente_id>', methods=['GET'])
def detalhe(cliente_id):
    return f"Detalhes do cliente com ID {cliente_id}"

@cliente_routes.route('/adicionar', methods=['POST'])
def adicionar():
    novo_cliente = request.json
    return make_response(
        jsonify(
            message="Cliente adicionado com sucesso!",
            cliente=novo_cliente
        ), 
        201
    )

@cliente_routes.route('/remover/<int:cliente_id>', methods=['DELETE'])
def remover(cliente_id):
    return make_response(
        jsonify(
            message=f"Cliente com ID {cliente_id} removido com sucesso!"
        ), 
        200
    )       

@cliente_routes.route('/atualizar/<int:cliente_id>', methods=['PUT'])
def atualizar(cliente_id):
    cliente_atualizado = request.json
    return make_response(
        jsonify(
            message=f"Cliente com ID {cliente_id} atualizado com sucesso!",
            cliente=cliente_atualizado
        ), 
        200
    )   
