lista = [1, 2, 3]
tupla = (4, 5, 6)
conjunto1 = {"a", "b","c","d"}
conjunto2 = {1, 2, 3, 4, 5, tupla}
print(conjunto1)
print(conjunto2)

conjunto1.add("a")
print(conjunto1)

print(sorted(conjunto1))
print(conjunto1)

print(len(conjunto1))

conjunto3 = {1, 2, 3, 4, 5}
conjunto4 = {4, 5, 6, 7, 8}
print("unión")
print(conjunto3.union(conjunto4))
print(conjunto3 | conjunto4)
print(conjunto3.intersection(conjunto4))
print(conjunto3 & conjunto4)
print(conjunto4.difference(conjunto3))
print(conjunto4 - conjunto3)
print(conjunto3.symmetric_difference(conjunto4))
print(conjunto3 ^ conjunto4)

print(sum(conjunto3))
print(max(conjunto3))
print(min(conjunto3))

conjunto3.remove(3)
print(conjunto3)

conjunto3.pop()
print(conjunto3)
conjunto3.discard(10)
print(conjunto3)

lista = list(conjunto3)
print(lista)

tupla = tuple(conjunto3)
print(tupla)

conjunto3.update([10, 11, 12], {13, 14, 15}, (16, 17, 18))
print(conjunto3)

var1 = {1, 2}
var2 = {1, 2, 5}

print(var1.issubset(var2))
print(var1.issuperset(var2))
print(var1.isdisjoint(var2))

var3 = frozenset({1, 2, 3})
print(var3)

var3.add(4)  # This will raise an AttributeError since frozensets are immutable



