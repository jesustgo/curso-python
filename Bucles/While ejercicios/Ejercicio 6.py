try:
    num = int(input("Digita un numero entero positivo: "))
    contador = 1
    if num > 0:
        while contador <= num:
            if contador == 2 or contador == 3 or contador == 5 or (contador % 2 != 0 and contador % 3 != 0 and contador % 5 != 0 and contador != 1):
                print(contador)
                contador += 1
            else:
                contador += 1
    else:
        print(f"El numero {num} no es valido porque no es positivo")
except:
    print("No digitaste un numero por favor vuelve a intentarlo")