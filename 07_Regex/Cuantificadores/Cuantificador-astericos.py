import re
text = "haaaabbbbblo"
pattern = "a*b*"
matches = re.findall(pattern, text)

print(matches)

# El * sirve para saber si hay 0 o mas veces determinado caracter y si no hay va a devolver algo vacio