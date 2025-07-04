age = int(input("Digite la edad de la persona: "))

if age >= 0 and age <= 2:
    print("Es un bebe")
elif age >= 3 and age <= 12:
    print("Es un niño")
elif age >= 13 and age <= 17:
    print("Es un adolescente")
elif age >= 18 and age <= 64:
    print("Es un adulto")
elif age >= 65:
    print("Es un adulto mayor")
else:
    print("Nadie tiene edad negativa, bobo")