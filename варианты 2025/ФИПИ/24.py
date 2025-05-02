a = open('24.txt').read()

import re

pattern = r'[1-9A-D]+[0-9A-D]*[02468AC]+'
r = []
d = [x.group() for x in re.finditer(pattern, a)]
for x in d:
    if len(x) != 2599:
        r.append(x)
c = max(r, key=len)
print(len(c), c)