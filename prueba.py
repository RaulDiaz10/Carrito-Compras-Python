"""
# Imperativo
resultado = []
for n in range(1, 11):
    if n % 2 == 0:
        resultado.append(n * n)
print(resultado)

"""
"""
# Funcional 
resultado = list(
    map(lambda x: x * x,
        filter(lambda x: x % 2 == 0, range(1, 11)))
)
print(resultado)
"""

# POO
class Numeros:
    def __init__(self, inicio, fin):
        self.inicio = inicio
        self.fin = fin

    def obtener_cuadrados_pares(self):
        resultado = []

        for n in range(self.inicio, self.fin + 1):
            if n % 2 == 0:
                resultado.append(n * n)

        return resultado

numeros = Numeros(1, 10)
resultado = numeros.obtener_cuadrados_pares()

print(resultado)

