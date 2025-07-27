from flask import Flask 
from routes.carros import carros_routes
from routes.cliente import cliente_routes, cliente_routes_api

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

app.register_blueprint(carros_routes, url_prefix='/carros')
app.register_blueprint(cliente_routes, url_prefix='/clientes')
app.register_blueprint(cliente_routes_api, url_prefix='/clientes/api')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
else:
    app.run(debug=True, port=5000)

