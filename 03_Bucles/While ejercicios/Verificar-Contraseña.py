contraseña = ""

while len(contraseña) < 8:
    contraseña = input("Digita una contraseña con minimo 8 caracteres: ")
else:
    print("Contraseña valida")