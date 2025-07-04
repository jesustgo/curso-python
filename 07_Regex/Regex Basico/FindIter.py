import re

text = "Este es el curso de Python de midudev. ¡Suscribete a python si te gusta este contenido! PYTHON"
pattern = "Python"

matches = re.finditer(pattern, text, re.IGNORECASE)

for match in matches:
    print(f"Se encontro la coincidencia '{match.group()}' en las posiciones ({match.start()}, {match.end()})")