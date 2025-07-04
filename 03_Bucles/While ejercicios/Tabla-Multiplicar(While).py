try:
    contador = 1
    num = int(input("Digita el numero del que quieres saber las tablas de multiplicar: "))
    while contador <= 10:
        print(f"{num} * {contador} = {num*contador}")
        contador += 1
except:
    print("Eso no es un numero por favor intentalo de nuevo")