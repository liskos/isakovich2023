a = open('24data/24-264.txt').read()

import re


pattern = r'[0-9]?([A-Z][0-9])*[A-Z]?'

d = [x.group() for x in re.finditer(pattern, a)]
print(d)
m = max(d, key=len)
print(len(m), m)