def tabla_multiplicar(num_multiplicado, num_max):
    for i in range(1, num_max+1):
        multiplicacion = num_multiplicado * i
        if multiplicacion % 5 == 0:
            print(f"{num_multiplicado} * {i} = {multiplicacion}", end= " ")
            print(f"(El numero {multiplicacion} es multiplo de 5)")
        else:
            print(f"{num_multiplicado} * {i} = {multiplicacion}")

try:
    num_multiplicado = int(input("Digita el numero a multiplicar: "))
    num_max = int(input("Digita el numero hasta el que quieres multiplicar: "))
    tabla_multiplicar(num_multiplicado, num_max)
except:
    print("Eso que acabas de digitar no es un numero valido")