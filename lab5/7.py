import re

with open('row.txt', 'r') as ok:
    for line in ok.readlines():
        pt = re.sub(r"snake", "camel", line)
        print(pt)
