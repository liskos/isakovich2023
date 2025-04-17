a = open('24data/k7b-3.txt').read()

import re

pattern = r'(?:BAFE)+'
r = max([x.group() for x in re.finditer(pattern, a)])
print(len(r), r)