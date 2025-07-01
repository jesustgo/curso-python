try:
    num = int(input("Digita un numero entero positivo: "))
    producto = 1
    if num >= 0:
        while num > 0:
            producto *= num
            num -= 1
        print(f"El factorial es: {producto}")
    else:
        print(f"El numero {num} no es valido tiene que ser entero positivo")
except:
    print("Lo que digitaste no es un numero por favor intentalo de nuevo")