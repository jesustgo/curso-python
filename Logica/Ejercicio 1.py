def contar_letras(alianza):
    alianza = alianza.upper()
    contar_r = alianza.count("R")
    contar_j = alianza.count("J")
    return contar_r == contar_j
    
hola = input("Ingresa la cadena a verificar para la alianza: ")
print(contar_letras(hola))