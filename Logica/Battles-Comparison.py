lista_a = [4,4,4]
lista_b = [2,8,2]

def battle(lista_a, lista_b):
    suma_a = sum(lista_a)
    suma_b = sum(lista_b)
    diferencia = 0

    if suma_a > suma_b:
        diferencia = suma_a - suma_b
        return f"{diferencia}a"
    elif suma_b > suma_a:
        diferencia = suma_b - suma_a
        return f"{diferencia}b"
    else:
        return "x"
    
print(battle(lista_a, lista_b))