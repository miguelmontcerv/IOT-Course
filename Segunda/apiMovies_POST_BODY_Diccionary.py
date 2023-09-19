from flask import Flask, request, jsonify, make_response

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Diccionario de películas con información adicional
peliculas = {
    "Spider Man": {
        "director": "Sam Raimi",
        "año": 2002,
        "género": "Acción",
        "calificación": 7.3
    },
    "Harry Potter": {
        "director": "Chris Columbus",
        "año": 2001,
        "género": "Fantasía",
        "calificación": 7.6
    },
    "Kung Fu Panda": {
        "director": "Mark Osborne",
        "año": 2008,
        "género": "Animación",
        "calificación": 7.6
    }
}

# Definir una ruta para la API que maneja las solicitudes POST y PUT
@app.route('/movies', methods=['POST', 'PUT'])
def movies():
    # Obtener el nombre de los parámetros
    name = request.args.get('name')
    
    if name == "Juan":
        try:
            # Obtener el JSON del cuerpo de la solicitud
            body = request.get_json()
            
            if 'movie_name' in body:
                movie_name = body['movie_name']
                # Crear una copia del cuerpo del JSON sin el campo 'movie_name'
                movie_data = dict(body)
                del movie_data['movie_name']
                
                # Agregar la película al diccionario de películas
                peliculas[movie_name] = movie_data
                response_data = f"Se ha agregado {movie_name} a la lista de películas"
                # Crear una respuesta HTTP con el código de estado 201 (Created)
                response = make_response(response_data, 201)
            else:
                response_data = "El JSON debe contener un campo 'movie_name' para el nombre de la película."
                # Crear una respuesta HTTP con el código de estado 400 (Bad Request)
                response = make_response(response_data, 400)
        except Exception as e:
            response_data = f'Error: {str(e)}'
            # Crear una respuesta HTTP con el código de estado 400 (Bad Request)
            response = make_response(response_data, 400)
    else:
        response_data = "No tienes permisos para agregar películas."
        # Crear una respuesta HTTP con el código de estado 401 (Unauthorized)
        response = make_response(response_data, 401)
    
    return response
    

# Ejecutar la aplicación en el puerto 8000
if __name__ == '__main__':
    app.run(port=8000, debug=True)