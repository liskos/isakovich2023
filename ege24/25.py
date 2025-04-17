a = open('24data/k7a-5.txt').read()

import re

pattern = r'[^CF]+'
r = max([len(x.group()) for x in re.finditer(pattern, a)])
print(r)