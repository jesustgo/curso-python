import re

text = "123456789"
pattern = r"\+?3?4?\d{9}"
coincidences = re.findall(pattern, text)

print(coincidences)

# El ? es para saber si hay 0 o mas veces determinado patron