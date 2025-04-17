a = open('24data/k7a-1.txt').read()

import re

pattern = r'[^DE]+'
r = max([len(x.group()) for x in re.finditer(pattern, a)])
print(r)