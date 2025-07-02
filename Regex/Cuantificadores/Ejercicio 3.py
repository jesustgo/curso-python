import re

text = "El gato está en la casa. La gata también está en la casa"
pattern = "gata?"
coincidences = re.findall(pattern, text)

print(coincidences)

# El ? es para saber si hay 1 o 0 veces determinado caracter