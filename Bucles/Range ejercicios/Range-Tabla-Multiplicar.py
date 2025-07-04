try:
    num = int(input("Digita un numero entero: "))
    for i in range(1,11):
        print(f"{num} * {i} = {num * i}")
except:
    print("Eso no es un numero por favor intentalo de nuevo")