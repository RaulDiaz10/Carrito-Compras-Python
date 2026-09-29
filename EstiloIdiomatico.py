""" ESTILO IDIOMÁTICO EN PYTHON """

""" 1. TRANSFORMACIONES DE COLECCIONES DE MANERA FUNCIONAL """
# Las comprensiones de listas permiten crear y filtrar listas en una sola línea.
cuadrados = [x ** 2 for x in range(1, 6)]
cuadradosPares = [x ** 2 for x in range(1, 11) if x % 2 == 0]


""" 2. PUENTE HACIA LA CIENCIA DE DATOS """
# Flujo: Datos -> Filtrar -> Transformar -> Agregar -> Resultado
ventas = [1200, 800, 1500, 400, 2200, 950]

# Filtramos las ventas y luego aplicamos una transformación matemática
mayores = filter (lambda x: x > 1000, ventas)
actualizadas = map (lambda x: x * 1.10, mayores)

print(list(actualizadas))  # Imprime las ventas mayores a 1000 actualizadas con un incremento del 10%


""" 3. RECURSIVIDAD PARA BASES DE DATOS """

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Imprime el factorial de 5 = 120

# TIEMPO DE EJECUCIÓN DE LA FUNCIÓN RECURSIVA FACTORIAL
# exited with code=0 in 0.298 seconds
# exited with code=0 in 0.316 seconds
# exited with code=0 in 0.294 seconds
# exited with code=0 in 0.292 seconds
# exited with code=0 in 0.268 seconds
# PROMEDIO DE EJECUCIÓN: 0.2936 segundos (Mas rapido)


# Usando el ciclo for para comparar el tiempo de ejecución con la recursividad
def factorial_for(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado
print(factorial_for(5))  # Imprime 120

# TIEMPO DE EJECUCIÓN DE LA FUNCIÓN FACTORIAL CON CICLO FOR
# exited with code=0 in 0.310 seconds
# exited with code=0 in 0.294 seconds
# exited with code=0 in 0.332 seconds
# exited with code=0 in 0.265 seconds
# exited with code=0 in 0.312 seconds
# PROMEDIO DE EJECUCIÓN: 0.3026 segundos

# CONCLUSIÓN: La recursividad fue ligeramente más rápido por una diferencia de 0.009 segundos.

"""" 4. ARBOLES: ESTRUCTURAS NATURALMETE RECURSIVAS """

# Programa que permita agregar elementos a un árbol binario de búsqueda de manera que deje consultarlo 
# Usando lista strings, que permita imprimirlo en orden alfabetico usando la recursividad paraa recorrer el arbol.



