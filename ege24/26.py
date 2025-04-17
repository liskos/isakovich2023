a = open('24data/k7a-6.txt').read()

import re

pattern = r'[^AE]+'
r = max([len(x.group()) for x in re.finditer(pattern, a)])
print(r)