from flask import Flask , make_response, jsonify, request
from bd import Carros
import mysql.connector

mydb = mysql.connector.connect(
    host="db",
    user="root",
    password="root",
    database="Pycodebr"
)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/carros_json', methods=['GET'])
def get_carros_json():

    return make_response( 
        jsonify(
            message="Lista de carros",
            carros=Carros
        ), 
        200
    )


@app.route('/carros_db', methods=['GET'])
def get_carros_db():
    mycarros = mydb.cursor(dictionary=True)
    mycarros.execute("SELECT * FROM carros")
    Carros = mycarros.fetchall()    
    
    return make_response( 
        jsonify(
            message="Lista de carros",
            carros=Carros
        ), 
        200
    )


def lista_carros(Carros):    
    lista = list()
    for carro in Carros:
        lista.append(
            {
                'id': carro[0],
                'marca': carro[1],
                'modelo': carro[2],
                'ano': carro[3]
            }
        )

    return lista


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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
else:
    app.run(debug=True, port=5000)

