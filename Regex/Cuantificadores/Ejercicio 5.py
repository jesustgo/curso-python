import re

text = "omniman fanatico man bandana"
pattern = r"\b[mfb]an\b"

coincidences = re.findall(pattern, text)
print(coincidences)