import re

files = "file1.txt file2.pdf midu-of.webp secret.txt"
pattern = r"\b\w{1,6}\.\w{1,6}\b"


matches = re.finditer(pattern, files)
for match in matches:
    print(f"{match.group()}, en las posiciones({match.start()}, {match.end()})")