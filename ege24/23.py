a = open('24data/k7a-3.txt').read()

import re

pattern = r'[^CD]+'
r = max([len(x.group()) for x in re.finditer(pattern, a)])
print(r)