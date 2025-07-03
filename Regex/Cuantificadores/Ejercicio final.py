import re

text = input("Digita el correo: ")
pattern = r"""
    ^([a-zA-Z0-9]) # Inicio del nombre
    ([\w\.\+-_@]+)? # Mediados del nombre
    ([a-zA-Z0-9])? # Finales del nombre
    @[a-zA-Z0-9] # Inicio del Dominio
    [a-zA-Z0-9-]+ # Fin del Dominio
    \.([a-zA-Z0-9-]){1,63} # Primera Extension
    ((\.[a-zA-Z0-9-]{1,63})?)$""" # Segunda Extension

pattern_verbose = re.compile(pattern, re.VERBOSE)
valid = pattern_verbose.search(text)
if valid:
    print(f"El correo ({valid.group()}) es valido")
else:
    print("El correo no es valido")