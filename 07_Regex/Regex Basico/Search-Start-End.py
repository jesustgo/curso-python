import re

text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con las Regex para ir con cuidado"
pattern = "IA"

coincidence = re.search(pattern, text)

if coincidence:
    print(f"He encontrado la coincidencia con el patron y esta empieza en la posicion {coincidence.start()} y termina en la posicion {coincidence.end()}")
else:
    print("No he podido encontrar el patron en el texto")