import re

with open('row.txt', 'r') as ok:
    for lines in ok.readlines():  
        pt = re.sub(r"[ ,.]", ":", lines)
        print(pt)
