a = open('24data/24-298.txt').read()

import re


pattern = r'[1-9]+[+*]?[1-9]+'

d = [x.group() for x in re.finditer(pattern, a)]
print(len(d), d)