from flask import Blueprint, make_response, jsonify, render_template, request
from database.bd import Carros
import mysql.connector

mydb = mysql.connector.connect(
    host="db",
    user="root",
    password="root",
    database="Pycodebr"
)
mydb.commit()

carros_routes = Blueprint('carros_routes', __name__)

@carros_routes.route('/', methods=['GET'])
def index():
    return "Carros API is running!"

@carros_routes.route('/json', methods=['GET'])
def get_carros_json():

    return make_response( 
        jsonify(
            message="Lista de carros",
            carros=Carros
        ), 
        200
    )

@carros_routes.route('/db', methods=['GET'])
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

@carros_routes.route('/add_json', methods=['POST'])
def create_carro_json():
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

@carros_routes.route('/add_db', methods=['POST'])
def create_carro_db():
    mycarros = mydb.cursor()
    sql = "INSERT INTO carros (marca, modelo, ano) VALUES (%s, %s, %s)"
    val = (request.json['marca'], request.json['modelo'], request.json['ano'])
    mycarros.execute(sql, val)
    mydb.commit()
    
    return make_response(
        jsonify(
            message="Carro adicionado com sucesso!",
            carro=request.json
        ), 
        201
    )

@carros_routes.route('/list', methods=['GET'])
def list():
    mycarros = mydb.cursor(dictionary=True)
    mycarros.execute("SELECT * FROM carros")
    Carros = mycarros.fetchall()  

    return render_template('index.html', carros=Carros)