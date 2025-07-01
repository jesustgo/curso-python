year = int(input("Digite el año a verificar: "))

if(year % 4 == 0 and (year % 100 == 0 and year % 400 == 0)):
    print(f"El año {year} si es bisiesto")
else:
    print(f"El año {year} no es bisiesto")