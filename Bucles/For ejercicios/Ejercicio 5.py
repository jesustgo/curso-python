palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]

letra = input("Digita la letra a buscar: ").lower()
contador = 0
for i in palabras:
    if letra == i[0]:
        contador += 1

print(f"La letra {letra.upper()} empieza en {contador} palabras")