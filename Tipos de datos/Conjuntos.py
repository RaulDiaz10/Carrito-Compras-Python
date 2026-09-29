"""
¿QUÉ ES UN CONJUNTO?
Un conjunto (set) es una colección desordenada de elementos ÚNICOS. Se utilizan 
principalmente para pruebas de pertenencia, eliminar duplicados de otras 
secuencias y realizar operaciones matemáticas como intersecciones y uniones.

CARACTERÍSTICAS PRINCIPALES:
1. Sin orden ni índice: Los elementos no mantienen un orden específico. No 
   puedes acceder a ellos usando `mi_set[0]`.
2. Elementos Únicos: NO permiten valores duplicados. Si intentas agregar un 
   duplicado, Python simplemente lo ignora de forma silenciosa.
3. Mutables: Puedes agregar o eliminar elementos una vez creado el conjunto.
4. Solo admiten elementos inmutables: Un set puede contener números, strings 
   y tuplas, pero NO puede contener listas ni diccionarios.
"""

print("--- PARTE 1: MÉTODOS QUE MUTAN (AGREGAR Y ELIMINAR) ---")
# Se crean usando llaves {} o la función set()
mi_conjunto = {10, 20, 30}
print(f"Conjunto inicial: {mi_conjunto}")

# add(x) - Agrega un solo elemento al conjunto.
mi_conjunto.add(40)
print(f"1. add(40): {mi_conjunto}")

# Si intentas agregar un duplicado, no hace nada (no da error).
mi_conjunto.add(20)
print(f"2. add(20) [duplicado]: {mi_conjunto} -> (Se ignora)")

# update(iterable) - Agrega múltiples elementos desde otro iterable.
mi_conjunto.update([50, 60, 70])
print(f"3. update([50, 60, 70]): {mi_conjunto}")

# remove(x) - Elimina el elemento 'x'. Da ERROR (KeyError) si no existe.
mi_conjunto.remove(70)
print(f"4. remove(70): {mi_conjunto}")

# discard(x) - Elimina el elemento 'x'. NO da error si no existe.
mi_conjunto.discard(100) # El 100 no existe, pero no pasa nada
print(f"5. discard(100) [no existe]: {mi_conjunto} -> (No da error)")

# pop() - Elimina y devuelve un elemento ALEATORIO (porque no hay orden).
extraido = mi_conjunto.pop()
print(f"6. pop(): {mi_conjunto} -> (Extrajo aleatoriamente el {extraido})")

# clear() - Vacía el conjunto por completo (retorna set()).
conjunto_temporal = {1, 2, 3}
conjunto_temporal.clear()
print(f"7. clear(): {conjunto_temporal}\n")


print("--- PARTE 2: OPERACIONES MATEMÁTICAS (NO MUTAN, RETORNAN NUEVO SET) ---")
set_A = {1, 2, 3, 4}
set_B = {3, 4, 5, 6}
print(f"Set A: {set_A} | Set B: {set_B}")

# union() o el operador | - Une ambos conjuntos (sin duplicados).
union_sets = set_A.union(set_B)
print(f"8. union() o (A | B): {union_sets}")

# intersection() o el operador & - Elementos que están en AMBOS conjuntos.
interseccion = set_A.intersection(set_B)
print(f"9. intersection() o (A & B): {interseccion}")

# difference() o el operador - - Elementos que están en A, pero NO en B.
diferencia = set_A.difference(set_B)
print(f"10. difference() o (A - B): {diferencia}")

# symmetric_difference() o ^ - Elementos en A o B, pero NO en ambos.
dif_simetrica = set_A.symmetric_difference(set_B)
print(f"11. symmetric_difference() o (A ^ B): {dif_simetrica}\n")


print("--- PARTE 3: MÉTODOS DE CONSULTA Y COPIA (NO MUTAN) ---")
set_pequeno = {1, 2}
set_grande = {1, 2, 3, 4, 5}
set_distinto = {8, 9, 10}

# issubset() - ¿Están todos los elementos del set pequeño dentro del grande?
es_subconjunto = set_pequeno.issubset(set_grande)
print(f"12. issubset(): ¿{set_pequeno} está dentro de {set_grande}? -> {es_subconjunto}")

# issuperset() - ¿Contiene el set grande todos los elementos del pequeño?
es_superconjunto = set_grande.issuperset(set_pequeno)
print(f"13. issuperset(): ¿{set_grande} contiene a {set_pequeno}? -> {es_superconjunto}")

# isdisjoint() - ¿Tienen cero elementos en común? (True si no comparten nada).
son_disjuntos = set_pequeno.isdisjoint(set_distinto)
print(f"14. isdisjoint(): ¿No tienen elementos en común? -> {son_disjuntos}")

# copy() - Crea una copia independiente del conjunto.
copia_set = set_pequeno.copy()
print(f"15. copy(): Copia creada -> {copia_set}\n")


print("--- PARTE 4: FUNCIONES INTEGRADAS Y TRUCOS ---")
numeros_set = {5, 10, 15, 20}
print(f"Conjunto final: {numeros_set}")

# len(), max(), min(), sum() funcionan igual que en listas y tuplas.
print(f"16. Funciones integradas: len={len(numeros_set)}, max={max(numeros_set)}, sum={sum(numeros_set)}")

# set() vacío - OJO: Para crear un set vacío NO se usa {}, eso crea un diccionario.
set_vacio = set()
print(f"17. set() vacío: {set_vacio} (Tipo: {type(set_vacio).__name__})")

# El súper truco - Usar set() para eliminar duplicados de una lista.
lista_con_duplicados = ["rojo", "azul", "rojo", "verde", "azul"]
lista_sin_duplicados = list(set(lista_con_duplicados))
print(f"18. Truco limpiar duplicados: {lista_con_duplicados} -> {lista_sin_duplicados}")