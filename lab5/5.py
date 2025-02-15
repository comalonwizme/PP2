import re

with open('row.txt', 'r') as ok:
    pt = r"^a.*b$"
    for lines in ok.readlines():
        words = lines.split()
        for word in words:
            if re.fullmatch(pt, word):
                print(word)
