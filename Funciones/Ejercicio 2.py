def es_primo(num):
    if num <= 1:
        print(f"El número {num} no es primo (debe ser mayor que 1).")
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"El número {num} no es primo (es divisible por {i}).")
    
    print(f"El número {num} es primo.")
try:
    num = int(input("Digita el numero a verificar: "))
    es_primo(num)
except:
    print("Lo que acabas de digitar no es un numero por favor intentalo de nuevo")