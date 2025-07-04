try:
    num = int(input("Digita un numero entero positivo: "))
    contador = 2
    if num > 1:
        while contador <= num:
            for i in range(2, int(contador**0.5) + 1):    
                if contador % i == 0 and contador != i:
                    contador += 1
                    break
            else:
                print(contador)
                contador += 1
    elif num == 1:
        print("No hay numeros primos para 1")
    else:
        print(f"El numero {num} no es valido porque no es positivo")
except ValueError:
    print("No digitaste un numero por favor vuelve a intentarlo")