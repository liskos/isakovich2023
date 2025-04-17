a = open('24data/k7b-4.txt').read()

import re

pattern = r'(?:EBCF)+'
r = max([x.group() for x in re.finditer(pattern, a)])
print(len(r), r)