"""
=============================================================================
GUÍA COMPLETA SOBRE DICCIONARIOS EN PYTHON (TEORÍA Y 18 EJEMPLOS)
=============================================================================

¿QUÉ ES UN DICCIONARIO?
Un diccionario (dict) es una estructura de datos que almacena elementos en 
pares de "clave: valor" (key: value). A diferencia de las listas que se 
indexan por un rango de números, los diccionarios se indexan por sus claves.

CARACTERÍSTICAS PRINCIPALES:
1. Clave-Valor: Cada elemento consta de una clave única y su valor asociado.
2. Claves únicas e inmutables: Las claves NO se pueden repetir y deben ser 
   tipos inmutables (strings, números, tuplas). Los valores pueden ser cualquier cosa.
3. Mutables: Puedes agregar, modificar o eliminar pares clave-valor después de crearlo.
4. Ordenados: Desde Python 3.7, los diccionarios mantienen el orden de 
   inserción de los elementos.
5. Eficientes: Están optimizados para recuperar valores rapidísimo si conoces la clave.
=============================================================================
"""

print("--- PARTE 1: MÉTODOS Y ACCIONES QUE MUTAN (AGREGAR, MODIFICAR, ELIMINAR) ---")
# Se crean usando llaves {} con la sintaxis clave: valor
usuario = {"nombre": "Ana", "edad": 28}
print(f"Diccionario inicial: {usuario}")

# Agregar o modificar con asignación directa (dict[clave] = valor)
usuario["pais"] = "México" # Como 'pais' no existe, lo agrega
usuario["edad"] = 29       # Como 'edad' ya existe, actualiza su valor
print(f"1. Asignación directa: {usuario}")

# update() - Actualiza el diccionario fusionándolo con otro diccionario o iterable.
usuario.update({"profesion": "Ingeniera", "edad": 30})
print(f"2. update(): {usuario}")

# setdefault() - Devuelve el valor de la clave. Si la clave NO existe, la crea con un valor por defecto.
rol = usuario.setdefault("rol", "Administradora")
print(f"3. setdefault() [agregó 'rol']: {usuario}")
usuario.setdefault("pais", "España") # No hace nada porque 'pais' ya existe

# pop(clave) - Elimina la clave y devuelve su valor. Da error si no existe (a menos que pases un valor por defecto).
profesion_eliminada = usuario.pop("profesion")
print(f"4. pop('profesion'): {usuario} -> (Extrajo: {profesion_eliminada})")

# popitem() - Elimina y devuelve el ÚLTIMO par clave-valor insertado como una tupla.
ultimo_par = usuario.popitem()
print(f"5. popitem(): {usuario} -> (Extrajo el par: {ultimo_par})")

# del dict[clave] - Usando la sentencia 'del' para borrar una clave.
del usuario["edad"]
print(f"6. del usuario['edad']: {usuario}")

# clear() - Elimina todos los elementos, dejando un diccionario vacío {}.
usuario.clear()
print(f"7. clear(): {usuario}\n")


print("--- PARTE 2: MÉTODOS DE CONSULTA Y VISTAS (NO MUTAN) ---")
inventario = {"manzanas": 10, "peras": 5, "uvas": 20}
print(f"Nuevo diccionario: {inventario}")

# get(clave) - Obtiene el valor de una clave. NO da error si no existe (devuelve None o el valor por defecto que le indiques).
manzanas = inventario.get("manzanas")
naranjas = inventario.get("naranjas", 0) # Devuelve 0 porque 'naranjas' no existe
print(f"8. get(): manzanas={manzanas}, naranjas={naranjas} (sin error)")

# keys() - Devuelve una vista con todas las CLAVES del diccionario.
claves = inventario.keys()
print(f"9. keys(): {claves}")

# values() - Devuelve una vista con todos los VALORES del diccionario.
valores = inventario.values()
print(f"10. values(): {valores}")

# items() - Devuelve una vista con todos los pares (clave, valor) guardados como tuplas.
pares = inventario.items()
print(f"11. items(): {pares}")

# Operador 'in' - Comprueba si una CLAVE (no un valor) existe en el diccionario.
existe_pera = "peras" in inventario
print(f"12. 'in': ¿Existe la clave 'peras'? -> {existe_pera}")

# copy() - Crea una copia independiente (superficial) del diccionario.
copia_inventario = inventario.copy()
print(f"13. copy(): Copia creada -> {copia_inventario}\n")


print("--- PARTE 3: FUNCIONES INTEGRADAS Y TRUCOS MODERNOS ---")
puntuaciones = {"Juan": 85, "María": 92, "Pedro": 78}
print(f"Diccionario de puntuaciones: {puntuaciones}")

# len() - Devuelve el número total de pares clave-valor.
total_pares = len(puntuaciones)
print(f"14. len(puntuaciones): Tiene {total_pares} pares")

# Función dict() - Construye un diccionario a partir de una lista de tuplas.
lista_tuplas = [("a", 1), ("b", 2), ("c", 3)]
dic_desde_lista = dict(lista_tuplas)
print(f"15. dict(lista_tuplas): {dic_desde_lista}")

# max(), min(), sorted() - OJO: Estas funciones operan sobre las CLAVES por defecto, no los valores.
mejor_alfabetico = max(puntuaciones) # "Pedro" porque la 'P' es mayor en el abecedario
claves_ordenadas = sorted(puntuaciones)
print(f"16. max() y sorted() por defecto: max={mejor_alfabetico}, sorted={claves_ordenadas}")

# Comprensión de diccionarios (Dict comprehension) - Crea diccionarios dinámicamente con bucles.
cuadrados = {numero: numero**2 for numero in range(1, 4)}
print(f"17. Comprensión de dict (número al cuadrado): {cuadrados}")

# Operador de unión (|) - Une dos diccionarios de forma limpia (Disponible desde Python 3.9+).
# Si hay claves repetidas, el valor del diccionario de la derecha (dict2) prevalece.
dict1 = {"A": 1, "B": 2}
dict2 = {"B": 99, "C": 3}
dict_unido = dict1 | dict2 
print(f"18. Operador de unión '|': {dict1} | {dict2} -> {dict_unido}")