registro_compras = {
    "Miguel": {
        "Enero": [150.0, 655.99, 153.25, 74.59, 46.0],
        "Febrero": [200.0, 856.0, 75.5, 99.0, 10.62, 64.55, 49.33, 10.25, 25.64, 33.75],
        "Marzo": [69.14, 78.12, 36.99, 97.0, 66.49, 49.25, 19.99, 63.74],
        "Abril": [150.0, 655.99, 153.25, 74.59, 46.0],
        "Mayo": [200.0, 856.0, 75.5, 99.0, 10.62, 64.55, 49.33, 10.25, 25.64, 33.75],
        "Junio": [69.14, 78.12, 36.99, 97.0, 66.49, 49.25, 19.99, 63.74],
        "Julio": [150.0, 655.99, 153.25, 74.59, 46.0],
        "Agosto": [200.0, 856.0, 75.5, 99.0, 10.62, 64.55, 49.33, 10.25, 25.64, 33.75],
        "Septiembre": [69.14, 78.12, 36.99, 97.0, 66.49, 49.25, 19.99, 63.74],
        "Octubre": [150.0, 655.99, 153.25, 74.59, 46.0],
        "Noviembre": [200.0, 856.0, 75.5, 99.0, 10.62, 64.55, 49.33, 10.25, 25.64, 33.75],
        "Diciembre": [69.14, 78.12, 36.99, 97.0, 66.49, 49.25, 19.99, 63.74]
    },
    "Ana": {
        "Enero": [200.0, 856.0, 75.5, 99.0, 10.62, 64.55, 49.33, 10.25, 25.64, 33.75],
        "Febrero": [69.14, 78.12, 36.99, 97.0, 66.49, 49.25, 19.99, 63.74],
        "Marzo": [150.0, 655.99, 153.25, 74.59, 46.0],
        "Abril": [150.0, 655.99, 153.25, 74.59, 46.0],
        "Mayo": [200.0, 856.0, 75.5, 99.0, 10.62, 64.55, 49.33, 10.25, 25.64, 33.75],
        "Junio": [69.14, 78.12, 36.99, 97.0, 66.49, 49.25, 19.99, 63.74],
        "Julio": [150.0, 655.99, 153.25, 74.59, 46.0],
        "Agosto": [200.0, 856.0, 75.5, 99.0, 10.62, 64.55, 49.33, 10.25, 25.64, 33.75],
        "Septiembre": [69.14, 78.12, 36.99, 97.0, 66.49, 49.25, 19.99, 63.74],
        "Octubre": [150.0, 655.99, 153.25, 74.59, 46.0],
        "Noviembre": [200.0, 856.0, 75.5, 99.0, 10.62, 64.55, 49.33, 10.25, 25.64, 33.75],
        "Diciembre": [69.14, 78.12, 36.99, 97.0, 66.49, 49.25, 19.99, 63.74]
    },
    "Leo": {
        "Enero": [200.0, 856.0, 75.5, 99.0, 10.62, 64.55, 49.33, 10.25, 25.64, 33.75],
        "Febrero": [150.0, 655.99, 153.25, 74.59, 46.0],
        "Marzo": [150.0, 655.99, 153.25, 74.59, 46.0],
        "Abril": [200.0, 856.0, 75.5, 99.0, 10.62, 64.55, 49.33, 10.25, 25.64, 33.75],
        "Mayo": [69.14, 78.12, 36.99, 97.0, 66.49, 49.25, 19.99, 63.74],
        "Junio": [150.0, 655.99, 153.25, 74.59, 46.0],
        "Julio": [150.0, 655.99, 153.25, 74.59, 46.0],
        "Agosto": [200.0, 856.0, 75.5, 99.0, 10.62, 64.55, 49.33, 10.25, 25.64, 33.75],
        "Septiembre": [69.14, 78.12, 36.99, 97.0, 66.49, 49.25, 19.99, 63.74],
        "Octubre": [150.0, 655.99, 153.25, 74.59, 46.0],
        "Noviembre": [200.0, 856.0, 75.5, 99.0, 10.62, 64.55, 49.33, 10.25, 25.64, 33.75],
        "Diciembre": [69.14, 78.12, 36.99, 97.0, 66.49, 49.25, 19.99, 63.74]
    }
}

def calcular_gasto_acumulado(registro_compras, usuario, mes):
    try:
        # Obtener las compras del usuario para el mes especificado
        compras_mes = registro_compras[usuario][mes]

        # Calcular el gasto acumulado sumando todas las compras del mes
        gasto_acumulado = sum(compras_mes)

        return gasto_acumulado
    except KeyError:
        return None  # Manejo de excepción si el usuario o el mes no existen en el registro_compras


# Ejemplo de uso de la función
nombre_usuario = "Miguel"
mes_seleccionado = "Enero"

gasto_total = calcular_gasto_acumulado(registro_compras, nombre_usuario, mes_seleccionado)

if gasto_total is not None:
    print(f"Usuario: {nombre_usuario}")
    print(f"Mes: {mes_seleccionado}")
    print(f"Gasto acumulado: ${gasto_total:.2f}")
else:
    print("El usuario o el mes no existen en el registro.")