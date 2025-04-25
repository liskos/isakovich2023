a = open('24data/24-307.txt').read()

import re


pattern = r'[1-9]+[*+]*[0-9]*(B)'

d = max([x.group() for x in re.finditer(pattern, a)], key=len)
print(len(d), d)