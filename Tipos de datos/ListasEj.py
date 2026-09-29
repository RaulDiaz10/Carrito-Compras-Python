"""
¿QUÉ ES UNA LISTA?
Una lista es una estructura de datos integrada en Python que permite almacenar 
una colección de elementos (ítems) bajo un solo nombre de variable.

CARACTERÍSTICAS PRINCIPALES:
1. Ordenadas: Los elementos mantienen el orden en el que fueron insertados.
2. Mutables: Puedes cambiar, agregar o eliminar elementos una vez creada.
3. Heterogéneas: Soportan diferentes tipos de datos a la vez (int, str, listas).
4. Dinámicas: Crecen o se reducen en memoria automáticamente.
5. Indexadas: Se accede a sus elementos mediante índices, empezando desde el 0.

MÉTODOS Y FUNCIONES:
- Métodos que mutan: Alteran la lista original (append, extend, insert, etc.).
- Métodos que NO mutan: Solo consultan o copian (index, count, copy).
- Funciones integradas (Built-ins): Operan sobre la lista (len, max, sum, etc.).
"""

# Creamos una lista inicial
mi_lista = [10, 20, 30]
print(f"--- LISTA ORIGINAL ---\nLista: {mi_lista}\n")

# =======================================================
# 1. MÉTODOS QUE MUTAN (MODIFICAN) LA LISTA
# =======================================================
print("--- A. MÉTODOS QUE MUTAN ---")

# append(x) - Agrega un elemento al final.
mi_lista.append(40)
print(f"1. append(40) -> {mi_lista}")

# extend(iterable) - Agrega múltiples elementos al final.
mi_lista.extend([50, 60])
print(f"2. extend([50, 60]) -> {mi_lista}")

# insert(i, x) - Inserta un elemento en el índice especificado.
mi_lista.insert(1, 15) # Inserta el 15 en la posición 1
print(f"3. insert(1, 15) -> {mi_lista}")

# remove(x) - Elimina la primera aparición de un valor.
mi_lista.remove(20)
print(f"4. remove(20) -> {mi_lista}")

# pop([i]) - Elimina y extrae el elemento del índice especificado.
extraido = mi_lista.pop(3) # Extrae el elemento en el índice 3
print(f"5. pop(3) -> Extrajo el {extraido}. Lista actual: {mi_lista}")

# pop() sin argumentos - Extrae el último elemento.
ultimo = mi_lista.pop()
print(f"6. pop() vacío -> Extrajo el {ultimo}. Lista actual: {mi_lista}")

# sort() - Ordena la lista (ascendente por defecto).
lista_desordenada = [8, 2, 10, 1]
lista_desordenada.sort()
print(f"7. sort() -> Ordena lista desordenada: {lista_desordenada}")

# reverse() - Invierte el orden de la lista original.
lista_desordenada.reverse()
print(f"8. reverse() -> Invierte la lista anterior: {lista_desordenada}")

# clear() - Vacía la lista por completo.
lista_desordenada.clear()
print(f"9. clear() -> Vacía la lista: {lista_desordenada}\n")


# =======================================================
# 2. MÉTODOS QUE NO MUTAN (SOLO CONSULTAN/COPIAN)
# =======================================================
print("--- B. MÉTODOS QUE NO MUTAN ---")
lista_letras = ['a', 'b', 'c', 'a', 'd']
print(f"Nueva lista de letras: {lista_letras}")

# index(x) - Devuelve el índice de la primera aparición.
indice_c = lista_letras.index('c')
print(f"10. index('c') -> La letra 'c' está en el índice: {indice_c}")

# count(x) - Cuenta cuántas veces aparece un elemento.
cantidad_a = lista_letras.count('a')
print(f"11. count('a') -> La letra 'a' aparece {cantidad_a} veces")

# copy() - Crea una copia independiente de la lista.
copia_lista = lista_letras.copy()
copia_lista.append('z') # Mutamos la copia para demostrar que son independientes
print(f"12. copy() -> Original: {lista_letras} | Copia modificada: {copia_lista}\n")


# =======================================================
# 3. FUNCIONES INTEGRADAS (BUILT-IN)
# =======================================================
print("--- C. FUNCIONES INTEGRADAS ---")
numeros = [5, 10, 15, 20]
print(f"Lista de números: {numeros}")

# len() - Devuelve la cantidad de elementos.
longitud = len(numeros)
print(f"13. len(numeros) -> La lista tiene {longitud} elementos")

# max() - Devuelve el valor máximo.
maximo = max(numeros)
print(f"14. max(numeros) -> El valor máximo es {maximo}")

# min() - Devuelve el valor mínimo.
minimo = min(numeros)
print(f"15. min(numeros) -> El valor mínimo es {minimo}")

# Sum() - Suma todos los elementos de la lista.
total = sum(numeros)
print(f"16. sum(numeros) -> La suma total es {total}\n")


# =======================================================
# 4. OPERADORES Y UTILIDADES EXTRA
# =======================================================
print("--- D. OPERACIONES EXTRA IMPORTANTES ---")

# del - Sentencia para borrar por índice (también muta).
del numeros[1] # Borra el elemento en el índice 1 (el 10)
print(f"17. del numeros[1] -> Elimina el índice 1: {numeros}")

# in - Operador para comprobar si un elemento existe.
existe_20 = 20 in numeros
print(f"18. 'in' -> ¿Está el 20 en la lista? {existe_20}")