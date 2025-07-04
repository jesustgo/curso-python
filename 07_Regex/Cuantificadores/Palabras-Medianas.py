import re

words = "ala casa árbol león cinco murcielago"
pattern = r"\b\w{4,6}\b"

coincidences = re.findall(pattern, words)
print(coincidences)