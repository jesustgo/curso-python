lista = [1, 2, 3, 4, 5, 6]

mitad = len(lista)/2
mitad = int(mitad + 0.5 if mitad % 2 != 0 else mitad)

print(lista[mitad-1::-1]+lista[mitad:])