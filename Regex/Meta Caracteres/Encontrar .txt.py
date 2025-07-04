import re

files = "file1.txt file2.pdf midu-of.webp secret.txt file-of.txt"
pattern = r"\b([\w-]+)\.txt\b"


matches = re.finditer(pattern, files)
for match in matches:
    print(f"{match.group()} en las posiciones({match.start()}, {match.end()})")