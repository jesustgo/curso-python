promedio = 0
num_ingresados = 0
i = 0

def calcular_promedio(num):
    if num != "salir" and num != None:
        num = float(num)
        global promedio 
        promedio += num
        global num_ingresados 
        num_ingresados += 1
    else:
        global i
        i = 1
        promedio = promedio/num_ingresados
        print(f"El promedio final de los numeros solicitados es: {promedio}")
    

while i != 1:
    num = input("Digita los numeros de los que quieras sacar el promedio y para salir digita 'salir': ")
    calcular_promedio(num)
    