import re

text = "Mí número de teléfono es +34 688999999 apúntalo vale?"
found = re.search(r"\+34 \d{9}", text)

if found:
    print(f"He encontrado el numero {found.group()}")