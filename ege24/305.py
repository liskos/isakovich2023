a = open('24data/24-305.txt').read()

import re


pattern = r'(AF)[1-9]+[*+]*[0-9]*'

d = max([x.group() for x in re.finditer(pattern, a)], key=len)
print(len(d), d)