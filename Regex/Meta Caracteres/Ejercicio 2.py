import re

files = "file1.txt file2.pdf midu-of.webp secret.txt"
pattern = r"\w{1,6}\.txt"

matches = re.finditer(pattern, files)
for match in matches:
    print(f"{match.group()}, en las posiciones({match.start()}, {match.end()})")