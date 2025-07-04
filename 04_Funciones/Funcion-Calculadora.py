def calculadora(num1, num2, operacion):
    if operacion == "+":
        return num1 + num2
    elif operacion == "-":
        return num1 - num2
    elif operacion == "*":
        return num1 * num2
    elif operacion == "/":
        return num1 / num2
    else:
        print("Lo que digitaste no es una opcion valida en la calculadora por favor vuelve a intentarlo")

try:
    num1 = int(input("Digita el primer numero a operar: "))
    num2 = int(input("Digita el segundo numero a operar: "))
    operacion = input("Digita alguna de las siguientes opciones para la operacion suma(+), resta(-), multiplicacion(*), division(/): ")
    print(f"El resultado de la operacion es {calculadora(num1, num2, operacion)}")
except:
    print("Lo que acabas de digitar no es valido por favor vuelve a intentarlo")