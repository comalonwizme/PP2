import re

with open('row.txt', 'r') as ok:
    pt = r"^ab{2,3}"

    for lines in ok:
        words = lines.split()
        for word in words:
            if re.fullmatch(pt, word):
                print(word)
