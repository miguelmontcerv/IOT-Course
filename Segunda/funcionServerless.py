import logging

from azure.functions import HttpRequest, HttpResponse

def main(req: HttpRequest) -> HttpResponse:
    peliculas = ["Spider Man", "Harry Potter", "Kunf fu panda"]

    # Obtenemos el nombre de los parametros
    name = req.params.get('name')
    if name == "Juan":
        try:
            # Seleccionamos el body
            body = req.get_json()
            # Agregamos el campo 'movie' al array de las peliculas
            peliculas.append(body['movie'])
            # Generamos respuesta
            return HttpResponse(f"Has agregado {body['movie']} a la lista de peliculas, ahora son: {peliculas}", status_code = 200)
        
        except Exception:
            # Respuesta en caso de error
            return HttpResponse(f'Necesito un body', status_code = 400)

        
    else:
        return HttpResponse("No se quien eres, sorry", status_code = 401)