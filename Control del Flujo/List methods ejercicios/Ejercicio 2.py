lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]

lista_a.extend(lista_b)
lista_a.remove(1)
dato = lista_a.pop(3)
lista_b.clear()

print(f"Dato eliminado: {dato}")
print(f"Asi quedo la lista a: {lista_a}")
print(f"Asi quedo la lista b: {lista_b}")