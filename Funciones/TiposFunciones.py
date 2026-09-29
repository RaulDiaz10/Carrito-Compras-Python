"""
TIPOS DE FUNCIONES:
- Funciones puras (Normales)
- Funciones de orden superior
- Funciones lambda 
- Funciones predicadas
"""

# Ejemplo de funcion normal
numeros = [1, 2, 3, 4, 5]

def cuadrado(numeros):
    return numeros ** 2

resultado = map(cuadrado, numeros)
print(list(resultado)) # Salida: [1, 4, 9, 16, 25] 


# Ejemplo de funcion lambda
""" Lambda es una funcion anonima que se puede definir en una sola linea de codigo, 
es decir no necesita un nombre para ser definida, se puede usar en el momento que se necesite. """

numeros = [1, 2, 3, 4, 5]
resultado = map(lambda x: x ** 2, numeros)
print(list(resultado))  # Salida: [1, 4, 9, 16, 25]     

# Ejemplo de funcion lambda con range
""" range es una funcion que genera una secuencia de numeros, 
se puede usar para iterar sobre una secuencia de numeros."""
resultado = map(lambda x: x ** 2, range(1, 11))
print(list(resultado))  # Salida: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Ejemplo de funcion predicada, funciones para decidir si un elemento cumple con una condicion


