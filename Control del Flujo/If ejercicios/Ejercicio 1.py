num1= int(input("Digita el primer numero a comparar: "))
num2= int(input("Digita el segundo numero a comparar: "))

if num1 > num2:
    print(f"El numero {num1} es mayor que el {num2}")
elif num2 > num1:
    print(f"El numero {num2} es mayor que el {num1}")
else:
    print("Los 2 numeros son iguales")