""" Imperativo / Procedural (Paso a paso) """

numeros = [1, 2, 3, 4, 5, 6]
pares = []

# Le decimos a la máquina los pasos exactos
for n in numeros:
    if n % 2 == 0:
        pares.append(n)

print(pares) # Resultado: [2, 4, 6]


""" Orientado a Objetos - POO """

class ProcesadorDeLista:
    def __init__(self, datos):
        self.datos = datos  # El objeto guarda su propia información

    def obtener_pares(self):
        # El objeto tiene la "habilidad" de procesar sus propios datos
        return [n for n in self.datos if n % 2 == 0]

# Creamos el objeto y le pedimos que actúe
mi_procesador = ProcesadorDeLista([1, 2, 3, 4, 5, 6])
print(mi_procesador.obtener_pares()) # Resultado: [2, 4, 6]


""" Funcional / Declarativo """

numeros = [1, 2, 3, 4, 5, 6]

# Declaramos la regla (lambda) y filtramos la lista original
pares = list(filter(lambda x: x % 2 == 0, numeros))

print(pares) # Resultado: [2, 4, 6]