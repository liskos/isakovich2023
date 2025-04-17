a = open('24data/k7-44.txt').read()

t = 'C'
while t in a:
    t += 'C'
print(t)

import re

pattern = r'[C]+'
r = re.finditer(pattern, a)
d = max([len(x.group()) for x in r])
print(d)