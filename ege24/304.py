a = open('24data/24-304.txt').read()

import re


pattern = r'(A)[1-9]+[*+]*[0-9]*'

d = max([x.group() for x in re.finditer(pattern, a)], key=len)
print(len(d), d)