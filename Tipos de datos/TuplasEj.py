"""
¿QUÉ ES UNA TUPLA?
Una tupla es una estructura de datos integrada en Python que permite almacenar 
una colección de elementos. Es muy similar a una lista, pero con una diferencia
crucial: NO se puede modificar una vez creada.

CARACTERÍSTICAS PRINCIPALES:
1. Inmutables: NO puedes agregar, eliminar ni cambiar elementos después de crearla.
2. Ordenadas: Los elementos mantienen el orden exacto en que fueron insertados.
3. Indexadas: Se accede a sus elementos por un índice numérico (empezando desde 0).
4. Heterogéneas: Pueden contener distintos tipos de datos a la vez.
5. Eficientes: Al ser inmutables, ocupan menos memoria y son más rápidas de 
   procesar que las listas.
6. Seguras: Se usan para proteger datos que no deben ser alterados accidentalmente.
=============================================================================
"""

print("--- PARTE 1: LOS ÚNICOS 2 MÉTODOS DE LAS TUPLAS (NO MUTAN) ---")
# Se crean usando paréntesis () en lugar de corchetes []
mi_tupla = (10, 20, 30, 20, 40)
print(f"Tupla inicial: {mi_tupla}")

# count(x) - Cuenta y devuelve cuántas veces aparece el valor 'x'.
cantidad_20 = mi_tupla.count(20)
print(f"1. count(20): El número 20 aparece {cantidad_20} veces")

# index(x) - Devuelve el índice de la primera aparición del valor 'x'.
indice_30 = mi_tupla.index(30)
print(f"2. index(30): El número 30 está en el índice {indice_30}\n")


print("--- PARTE 2: FUNCIONES INTEGRADAS (BUILT-IN) PARA TUPLAS ---")
numeros = (5, 15, 25, 10)
print(f"Tupla de números: {numeros}")

# len() - Devuelve la cantidad de elementos de la tupla.
longitud = len(numeros)
print(f"3. len(numeros): La tupla tiene {longitud} elementos")

# max() - Devuelve el valor más grande.
valor_max = max(numeros)
print(f"4. max(numeros): El valor máximo es {valor_max}")

# min() - Devuelve el valor más pequeño.
valor_min = min(numeros)
print(f"5. min(numeros): El valor mínimo es {valor_min}")

# sum() - Suma todos los elementos (solo válido para números).
total = sum(numeros)
print(f"6. sum(numeros): La suma total es {total}")

# sorted() - Devuelve una LISTA NUEVA con los elementos ordenados.
# OJO: Devuelve una lista [], porque las tuplas no se pueden modificar.
tupla_ordenada = sorted(numeros)
print(f"7. sorted(numeros): {tupla_ordenada} -> (Nota que devuelve una lista)")

# tuple() - Convierte otro iterable (como una lista o string) a tupla.
lista_temp = ["A", "B", "C"]
nueva_tupla = tuple(lista_temp)
print(f"8. tuple(lista_temp): {nueva_tupla} -> (Se convirtió de lista a tupla)\n")


print("--- PARTE 3: OPERACIONES ESPECIALES Y TRUCOS CON TUPLAS ---")

# Tupla de un solo elemento (OJO: requiere una coma al final).
# Si no pones la coma, Python lo tratará como un número entre paréntesis.
tupla_un_elemento = (50,)
print(f"9. Tupla de 1 elemento: {tupla_un_elemento} (Tipo: {type(tupla_un_elemento).__name__})")

# Empaquetado de tuplas (Tuple packing).
# Puedes crear una tupla sin usar paréntesis, solo separando por comas.
datos_usuario = "Juan", 28, "México"
print(f"10. Empaquetado: {datos_usuario}")

#  Desempaquetado de tuplas (Tuple unpacking).
# Asignar los valores de una tupla a variables individuales en una sola línea.
nombre, edad, pais = datos_usuario
print(f"11. Desempaquetado: Nombre={nombre}, Edad={edad}, País={pais}")

# Concatenación (+) - Une dos tuplas creando una NUEVA tupla.
tupla1 = (1, 2)
tupla2 = (3, 4)
tupla_unida = tupla1 + tupla2
print(f"12. Concatenación (tupla1 + tupla2): {tupla_unida}")

# Repetición (*) - Multiplica los elementos creando una NUEVA tupla.
tupla_repetida = tupla1 * 3
print(f"13. Repetición (tupla1 * 3): {tupla_repetida}")

# Rebanado (Slicing) - Extraer una porción de la tupla.
tupla_letras = ('a', 'b', 'c', 'd', 'e')
rebanada = tupla_letras[1:4] # Del índice 1 al 3 (el 4 no se incluye)
print(f"14. Rebanado (tupla_letras[1:4]): {rebanada}")