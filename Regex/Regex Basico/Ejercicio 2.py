import re

text = "Este es el curso de Python de midudev. ¡Suscríbete a midudev si te gusta este contenido! midu"
pattern = "midu"

matches = re.finditer(pattern, text)

for match in matches:
    print(f"Se encontro la coincidencia '{match.group()}' en las posiciones ({match.start()}, {match.end()})")
print(f"La coincidencia con el patron se encontro {len(re.findall(pattern, text))} veces")