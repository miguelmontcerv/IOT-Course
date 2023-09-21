import mysql.connector
import json
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Obtener los datos del cuerpo de la solicitud HTTP en formato JSON
        datos = req.get_json()

        # Validar que todos los campos requeridos estén presentes en el JSON
        campos_requeridos = ['alumno', 'opinion', 'calificacion']

        for campo in campos_requeridos:
            if campo not in datos:
                return func.HttpResponse('Error: El campo {} es requerido.'.format(campo), status_code=400)

        # Conexión a la base de datos
        cnx = mysql.connector.connect(
            user="tu_usuario",
            password="tu_contraseña",
            host="tu_host.mysql.database.azure.com",
            port=3306,
            database="curso_iot",
            ssl_disabled=False
        )

        cursor = cnx.cursor()

        # Consulta SQL para insertar los datos en la tabla 'opiniones'
        insert_query = "INSERT INTO opiniones (alumno, opinion, calificacion) VALUES (%s, %s, %s)"
        data_to_insert = (datos['alumno'], datos['opinion'], datos['calificacion'])

        cursor.execute(insert_query, data_to_insert)
        cnx.commit()

        cursor.close()
        cnx.close()

        return func.HttpResponse('Datos insertados correctamente en la tabla opiniones.', status_code=201)
    
    except Exception as e:
        return func.HttpResponse('Error: {}'.format(str(e)), status_code=500)
