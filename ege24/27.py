a = open('24data/k7b-1.txt').read()

import re

pattern = r'(?:EAB)+'
r = max([x.group() for x in re.finditer(pattern, a)])
print(len(r))