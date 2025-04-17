a = open('24data/k7a-2.txt').read()

import re

pattern = r'[^BEF]+'
r = max([len(x.group()) for x in re.finditer(pattern, a)])
print(r)