# API Flask Carros

A simple REST API built with Flask for managing car information.

## Features

- List all cars
- Add new cars

## Endpoints

### GET /carros
Returns a list of all cars in the database.

**Response Example:**
```json
{
    "message": "Lista de carros",
    "carros": [
        {
            "id": 1,
            "marca": "Toyota",
            "modelo": "Corolla",
            "ano": 2020
        }
    ]
}
```

### POST /carros
Add a new car to the database.

**Request Body Example:**
```json
{
    "marca": "Volkswagen",
    "modelo": "Golf",
    "ano": 2022
}
```

**Response Example:**
```json
{
    "message": "Carro adicionado com sucesso!",
    "carro": {
        "id": 4,
        "marca": "Volkswagen",
        "modelo": "Golf",
        "ano": 2022
    }
}
```

## Running the Application

1. Make sure you have Flask installed:
```bash
pip install flask
```

2. Run the application:
```bash
python main.py
```

The API will be available at `http://localhost:5000/carros`.
