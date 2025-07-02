import re

text = "dddd aaa ccc"
pattern = "ac+"

matches = re.findall(pattern, text)
print(matches)

# El + sirve para saber si hay 1 o mas veces un determinado caracter