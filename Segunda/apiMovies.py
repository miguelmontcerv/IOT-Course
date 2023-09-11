from flask import Flask, jsonify

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Datos de películas (puedes reemplazar festo con tu propia lista de películas)
peliculas = ["Spider Man", "Harry Potter", "Kunf fu panda"]

# Definir una ruta para la API que devuelve la lista de películas
@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify(peliculas)

# Ejecutar la aplicación en el puerto 8000
if __name__ == '__main__':
    app.run(port=8000, debug=True)
