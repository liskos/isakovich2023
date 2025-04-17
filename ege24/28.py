a = open('24data/k7b-2.txt').read()

import re

pattern = r'(?:DBAC)+'
r = max([x.group() for x in re.finditer(pattern, a)])
print(len(r), r)