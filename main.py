from flask import Flask , make_response, jsonify, request
from bd import Carros

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/carros', methods=['GET'])
def get_carros():
    return make_response( 
        jsonify(
            message="Lista de carros",
            carros=Carros
        ), 
        200
    )

@app.route('/carros', methods=['POST'])
def create_carro():
    novo_carro = request.json
    novo_carro['id'] = len(Carros) + 1  # Assign a new ID based on the current length of the list
    Carros.append(novo_carro)
    return make_response(
        jsonify(
            message="Carro adicionado com sucesso!",
            carro=novo_carro
        ), 
        201
    )    

app.run(debug=True, port=5000)

