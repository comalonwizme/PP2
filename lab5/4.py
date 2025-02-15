import re

with open('row.txt', 'r') as ok:
    pt = r"^[A-Z][a-z]+$"
    for lines in ok:
        words = lines.split()
        for word in words:
            if re.fullmatch(pt, word):
                print(word)
