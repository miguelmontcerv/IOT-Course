from flask import Flask, jsonify, request, make_response

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Datos de películas (puedes reemplazar esto con tu propia lista de películas)
peliculas = ["Spider Man", "Harry Potter", "Kunf fu panda"]

# Definir una ruta para la API que devuelve la lista de películas
@app.route('/movies', methods=['GET'])
def get_movies():
    name = request.args.get('name')
    if name:
        # Si se proporciona un nombre en la solicitud, responder personalizado
        response_data = f"Hola, {name}. Aquí tienes la lista de películas: {peliculas}"
        # Crear una respuesta HTTP personalizada con el código de estado 202
        response = make_response(response_data, 202)
    else:
        # Si no se proporciona un nombre, responder con la lista de películas completa
        response_data = f"No se quien eres, sorry"
        # Crear una respuesta HTTP personalizada con el código de estado 401
        response = make_response(response_data, 401)
        
    response.headers['Content-Type'] = 'application/json'
    return response


# Ejecutar la aplicación en el puerto 8000
if __name__ == '__main__':
    app.run(port=8000, debug=True)
