import random

numero_aleatorio = random.randint(1,100)

def adivina_numero():
    while True:
        try:
            num = int(input("Ingresa un numero entre 1 y 100: "))
            if num <= 100 and num >= 0:    
                if num > numero_aleatorio:
                    print("El numero es menor")
                elif num < numero_aleatorio:
                    print("El numero es mayor")
                else:
                    print("Felicidades haz encontrado el numero aleatorio")
                    break
            else:
                print("El numero ingresado no esta dentro del rango que se busca")
        except:
            print("Lo digitado anteriormente no es valido porfavor vuelve a intentarlo")

adivina_numero()