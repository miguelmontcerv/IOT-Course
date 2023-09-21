from flask import Flask, jsonify, request, make_response

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Datos de películas (puedes reemplazar esto con tu propia lista de películas)
peliculas = ["Spider Man", "Harry Potter", "Kunf fu panda"]

# Definir una ruta para la API que maneja las solicitudes POST y PUT
@app.route('/movies', methods=['POST', 'PUT'])
def movies():
    # Obtenemos el nombre de los parametros
    name = request.args.get('name')
    if name == "Juan":
        try:
            # Seleccionamos el body
            body = request.get_json()
            # Agregamos el campo 'movie' al array de las peliculas
            peliculas.append(body['movie'])
            # Generamos respuesta
            response = make_response(f"Se ha agregado {body['movie']} al la lista\n\n Lista: {peliculas}", 201)
        except Exception:
            # Respuesta en caso de error
            response = make_response(f'Necesito un body', 400)
    else:
            # Si no se proporciona un nombre, responder con la lista de películas completa
            response_data = f"No se quien eres, sorry"
            # Crear una respuesta HTTP personalizada con el código de estado 401
            response = make_response(response_data, 401)
    
    return response
    

# Ejecutar la aplicación en el puerto 8000
if __name__ == '__main__':
    app.run(port=8000, debug=True)