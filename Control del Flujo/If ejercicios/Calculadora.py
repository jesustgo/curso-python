num1 = int(input("Digita el primer numero a operar: "))
num2 = int(input("Digita el segundo numero a operar: "))

operacion = input("Digita la operacion que quieras realizar: +, -, *, /: ")

if operacion == "+":
    print(f"El resultado de la suma con los numeros {num1} y {num2} es: {num1 + num2}")
elif operacion == "-":
    print(f"El resultado de la resta con los numeros {num1} y {num2} es: {num1 - num2}")
elif operacion == "*":
    print(f"El resultado de la multiplicacion con los numeros {num1} y {num2} es: {num1 * num2}")
elif operacion == "/":
    if num2 != 0:
        print(f"El resultado de la division con los numeros {num1} y {num2} es: {num1 / num2}")
    else:
        print("La division por 0 no es posible")
else:
    print("Esa no es una opcion valida por favor digite una opcion valida")