def calcular_velocidad(distancia, tiempo):
    velocidad = distancia / tiempo
    if velocidad > 100:
        return "Exceso de velocidad"
    else:
        return "Velocidad óptima"

while True:
    distancia = float(input("Ingresa la distancia (en kilómetros): "))
    tiempo = float(input("Ingresa el tiempo (en horas): "))
    resultado = calcular_velocidad(distancia, tiempo)
    print(resultado)

    continuar = input("¿Quieres calcular otra velocidad? (s/n): ").lower()
    
    if continuar != "s":
        print("Bye :)")
        break

