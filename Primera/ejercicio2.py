def simpson_integral(a, b, n):
    h = (b - a) / n
    suma = 0

    for i in range(n + 1):
        x = a + i * h
        if i == 0 or i == n:
            coef = 1
        elif i % 2 == 1:
            coef = 4
        else:
            coef = 2
        suma += coef * (x ** 2)

    integral_aproximada = (h / 3) * suma
    return integral_aproximada

# Ejemplo de uso:
a = 50  # Límite inferior del intervalo
b = 120  # Límite superior del intervalo
n = 20  # Número de subintervalos (debe ser un número par)

resultado = simpson_integral(a, b, n)
print("Resultado de la integral:", resultado)
