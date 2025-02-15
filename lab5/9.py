import re

with open('row.txt', 'r') as ok:
    for lines in ok.readlines():
        pt = re.sub(r"(?=[A-ZА-Я])", ' ', lines).strip()
        print(pt)
