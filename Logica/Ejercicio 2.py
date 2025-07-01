def contar_huevos(huevos):
    suma = 0
    for i in huevos:
        if i % 2 == 0:
            suma += i
    return suma

print(contar_huevos([1,2,3,4,5,6,7,8,9,10]))