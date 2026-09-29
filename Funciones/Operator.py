""" 
La libreria operator contiene funciones que permiten 
realizar operaciones matematicas y logicas: 
"""

import operator

# Suma: equivale a 5 + 3 (Resultado: 8)
print(operator.add(5, 3))

# Multiplicación: equivale a 5 * 3 (Resultado: 15)
print(operator.mul(5, 3))

# Mayor que (Greater Than): equivale a 10 > 2 (Resultado: True)
print(operator.gt(10, 2))

# Igual a (Equal): equivale a 10 == 2 (Resultado: False)
print(operator.eq(10, 2))

# Menor o igual (Less or Equal): equivale a 10 <= 2 (Resultado: False)
print(operator.le(10, 2))

# Mayor o igual (Greater or Equal): equivale a 10 >= 2 (Resultado: True)
print(operator.ge(10, 2))

# No es igual a (Not Equal): equivale a 10 != 2 (Resultado: True)
print(operator.ne(10, 2))

# Menor que (Less Than): equivale a 10 < 2 (Resultado: False)
print(operator.lt(10, 2))

# Potencia: equivale a 2 ** 3 (Resultado: 8)
print(operator.pow(2, 3))

# Módulo (resto): equivale a 10 % 3 (Resultado: 1)
print(operator.mod(10, 3))

# División entera: equivale a 10 // 3 (Resultado: 3)
print(operator.floordiv(10, 3))

# División real flotante: equivale a 10 / 3 (Resultado: 3.333...)
print(operator.truediv(10, 3))

# Negación (cambio de signo): equivale a -5 (Resultado: -5)
print(operator.neg(5))

# Positivo (mantiene el signo original): equivale a +(-5) (Resultado: -5)
print(operator.pos(-5))

# Valor absoluto: equivale a abs(-5) (Resultado: 5)
print(operator.abs(-5))

# Inversión a nivel de bits (NOT): equivale a ~5 (Resultado: -6)
print(operator.invert(5))

# AND a nivel de bits: equivale a 5 & 3 (Resultado: 1)
print(operator.and_(5, 3))

# OR a nivel de bits: equivale a 5 | 3 (Resultado: 7)
print(operator.or_(5, 3))

# XOR a nivel de bits: equivale a 5 ^ 3 (Resultado: 6)
print(operator.xor(5, 3))

# Desplazamiento de bits a la izquierda: equivale a 5 << 3 (Resultado: 40)
print(operator.lshift(5, 3))

# Desplazamiento de bits a la derecha: equivale a 5 >> 3 (Resultado: 0)
print(operator.rshift(5, 3))

# Obtiene el ítem en el índice 1: equivale a lista[1] (Resultado: 2)
print(operator.itemgetter(1)([1, 2, 3]))

# Obtiene el atributo 'real' del objeto complejo (Resultado: 3.0)
print(operator.attrgetter('real')(3 + 4j))

# Ejecuta el método 'upper()' sobre la cadena (Resultado: 'HELLO')
print(operator.methodcaller('upper')('hello'))

# Comprueba si existe (Contiene): equivale a 2 in [1, 2, 3] (Resultado: True)
print(operator.contains([1, 2, 3], 2))

# Convierte el objeto a índice usando su método __index__ (Resultado: 5)
print(operator.index(5))

# Concatena secuencias: 'Hello, ' + 'World!' (Resultado: 'Hello, World!')
print(operator.concat('Hello, ', 'World!'))

# Identidad de objetos: equivale a 5 is 5 (Resultado: True)
print(operator.is_(5, 5))

# No identidad de objetos: equivale a 5 is not 5 (Resultado: False)
print(operator.is_not(5, 5))

# Evaluación booleana de verdad: equivale a bool(5) (Resultado: True)
print(operator.truth(5))

# Negación lógica: equivale a not 5 (Resultado: False)
print(operator.not_(5))

# Devuelve el tamaño estimado (lenght) del objeto (Resultado: 3)
print(operator.length_hint([1, 2, 3]))

# Obtiene múltiples ítems (índices 1 y 2) como tupla (Resultado: (2, 3))
print(operator.itemgetter(1, 2)([1, 2, 3]))

# Obtiene múltiples atributos del objeto como tupla (Resultado: (3.0, 4.0))
print(operator.attrgetter('real', 'imag')(3 + 4j))