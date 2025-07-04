lista = [10, 20, 30, 40, 50]

mitad = len(lista)/2
mitad = int(mitad + 0.5 if mitad % 2 != 0 else mitad)

print(lista[mitad-1:mitad])