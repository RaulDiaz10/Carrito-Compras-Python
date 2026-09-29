def cuadrado(x):
    return x * x

def cubo(x):
    return x * x * x

def aplicar(funcion, valor):
    return funcion(valor)

aplicar(cuadrado, 5)  # Devuelve 25
aplicar(cubo, 5)  # Devuelve 125
    