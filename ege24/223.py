a = open('24data/24-223.txt').read()

import re


pattern = r'(AB|CAC)*(CAC|AB)*'

d = max([x.group() for x in re.finditer(pattern, a)], key=len)
print(len(d))